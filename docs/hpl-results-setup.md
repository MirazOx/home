# HPL Results Setup

This page can now send quiz results to a Google Sheet through Google Apps Script.

## Files

- `projects/high-performance-learning/index.html`
- `assets/js/hpl-results-config.js`
- `scripts/hpl-results-google-apps-script.gs`

## What students see

Students can:
- take quizzes
- see their own score on the page
- retake quizzes before submitting
- submit with name, student ID, and session code

Students do **not** see the local clear/reset button.

## What you receive

If Google Apps Script is configured, each submission is written into a Google Sheet:
- `Attempts` sheet: one row per student attempt
- `Answers` sheet: one row per answered question

This gives you a proper class record instead of only email summaries.

## Deploy Google Sheets backend

1. Create a new Google Sheet.
2. Copy the Sheet ID from its URL.
3. Open [script.google.com](https://script.google.com/) and create a new Apps Script project.
4. Paste the contents of `scripts/hpl-results-google-apps-script.gs` into `Code.gs`.
5. Replace `PASTE_YOUR_GOOGLE_SHEET_ID_HERE` with your real Sheet ID.
6. Click `Deploy` -> `New deployment`.
7. Choose `Web app`.
8. Set:
   - Execute as: `Me`
   - Who has access: `Anyone`
9. Deploy and copy the web app URL.
10. Open `assets/js/hpl-results-config.js`.
11. Paste the web app URL into `appsScriptUrl`.
12. Reupload the folder/site.

## Email fallback

If `appsScriptUrl` is left empty, the page falls back to the email endpoint in `emailEndpoint`.

## Teacher mode

Open the page with:

- `?admin=1`

Example:

- `/projects/high-performance-learning/?admin=1`

That shows:
- local export button
- local device clear button
- full response log table

## Session presets

You can preset a session in either of two ways:

1. In the URL:
   - `?session=CLS-May-05-AM`
2. In `assets/js/hpl-results-config.js`:
   - `defaultSessionCode: 'CLS-May-05-AM'`

## Important note

The on-page dashboard is for the current browser/device only.
Your real master record should be the Google Sheet.
