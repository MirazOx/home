const SHEET_ID = '1kBuagBfHdbYlTU7mLFrWSQMJHqrELaYIpVLQ37qOGx0';
const ATTEMPTS_SHEET = 'Attempts';
const ANSWERS_SHEET = 'Answers';

function doPost(e) {
  try {
    const payload = parseRequest_(e);
    validatePayload_(payload);

    const spreadsheet = SpreadsheetApp.openById(SHEET_ID);
    const attemptsSheet = getOrCreateSheet_(spreadsheet, ATTEMPTS_SHEET, [
      'attempt_id',
      'submitted_at_iso',
      'submitted_at_local',
      'project',
      'quiz_version',
      'provider',
      'session_code',
      'student_name',
      'student_id',
      'student_email',
      'overall_score',
      'total_correct',
      'total_questions',
      'overall_percent',
      'sections_complete',
      'total_sections',
      'responses_logged',
      'chapter_scores_text',
      'visitor_note',
      'source_page',
      'user_agent'
    ]);
    const answersSheet = getOrCreateSheet_(spreadsheet, ANSWERS_SHEET, [
      'attempt_id',
      'session_code',
      'student_name',
      'student_id',
      'chapter',
      'chapter_title',
      'question_number',
      'question',
      'chosen_answer',
      'correct_answer',
      'result',
      'timestamp_local'
    ]);

    attemptsSheet.appendRow([
      payload.attemptId,
      payload.submittedAt,
      payload.submittedAtLocal,
      payload.project,
      payload.quizVersion,
      payload.provider,
      payload.sessionCode,
      payload.visitorName,
      payload.visitorId,
      payload.visitorEmail || '',
      payload.overallScore,
      payload.totalCorrect,
      payload.totalQuestions,
      payload.overallPercent,
      payload.sectionsComplete,
      payload.totalSections,
      payload.responsesLogged,
      payload.chapterScoresText,
      payload.visitorNote || '',
      payload.sourcePage || '',
      payload.userAgent || ''
    ]);

    const rows = (payload.responses || []).map(function(response) {
      return [
        payload.attemptId,
        payload.sessionCode,
        payload.visitorName,
        payload.visitorId,
        response.chapter,
        response.chapterTitle,
        response.qIndex,
        response.question,
        response.chosen,
        response.answer,
        response.correct ? 'CORRECT' : 'WRONG',
        response.ts
      ];
    });

    if (rows.length) {
      answersSheet.getRange(answersSheet.getLastRow() + 1, 1, rows.length, rows[0].length).setValues(rows);
    }

    return jsonResponse_({ ok: true, attemptId: payload.attemptId });
  } catch (error) {
    return jsonResponse_({ ok: false, message: error.message || String(error) });
  }
}

function parseRequest_(e) {
  if (!e || !e.postData || !e.postData.contents) {
    throw new Error('No submission payload received.');
  }
  return JSON.parse(e.postData.contents);
}

function validatePayload_(payload) {
  if (!SHEET_ID || SHEET_ID === 'PASTE_YOUR_GOOGLE_SHEET_ID_HERE') {
    throw new Error('Set SHEET_ID in the Apps Script file before deploying.');
  }
  ['attemptId', 'visitorName', 'visitorId', 'sessionCode', 'overallScore'].forEach(function(field) {
    if (!payload[field]) {
      throw new Error('Missing required field: ' + field);
    }
  });
}

function getOrCreateSheet_(spreadsheet, name, headers) {
  var sheet = spreadsheet.getSheetByName(name);
  if (!sheet) {
    sheet = spreadsheet.insertSheet(name);
  }
  if (sheet.getLastRow() === 0) {
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function jsonResponse_(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
