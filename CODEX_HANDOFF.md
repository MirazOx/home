# Miraz Portfolio Site Handoff

Use this file as the first message/context in a new Codex chat to continue editing the site without carrying the full old conversation.

## Project Location

Main working folder:

`/Users/miraz/Documents/Claude/Projects/Shamsad Mortuza Portfolio/latest-site/MirazOx.github.io-main`

Local preview server usually runs at:

`http://127.0.0.1:8012/`

Important: this is Miraz Hossain's personal portfolio, not Shamsad Mortuza's website. Keep the two completely separate.

## Site Identity

Owner: Md. Miraz Hossain.

Positioning:

Dhaka-based journalist and researcher. His work sits at the intersection of journalism, education, social science, and technology, with a focus on how algorithmic media systems shape truth and public knowledge in South Asia.

Core roles:

- Researcher
- Journalist
- Educator

Preferred tone:

- Serious but literary.
- Strong Oxford/Harvard application energy.
- Avoid clutter and long explanatory text.
- Keep homepage selective and high-signal.
- Let archive/detail pages carry depth.

## Design Direction

General visual direction:

- Dark theme should be the default.
- Light theme is optional via toggle.
- Navigation should remain accessible while scrolling.
- Avoid overly text-heavy homepage sections.
- Use restrained editorial design, not a generic portfolio template.
- Use strong typography, large negative space only when intentional, and visual hierarchy that feels mature.

User dislikes:

- Novice-looking file/page structure.
- Too much intro text.
- Repetition.
- Cards taking too much space for minor recognition.
- Hidden/unclear interactive states.
- Photos cropping heads.
- Tags/filter pills laid bare under search bars when it looks messy.

User likes:

- Literary about page.
- Secret/hidden "Beyond the work" page linked subtly inside the about narrative.
- Dean's List card that shows one cover first, then spreads the four cards on click.
- Selected work pages with strong images.
- Black and white images that become color on hover for article showcases.
- Homepage with strong, coherent hero and quick links to major work.

## Current Main Navigation

Current main pages are intended to be:

- Home: `/`
- Research: `/research/`
- Academic: `/academic/`
- Reportage/Writing: `/writing/`
- Interventions: `/interventions/`
- About: `/about/`

Services and Credentials should be accessible from About, but their own pages can remain.

Projects were moved into Interventions.

Quickblog should be removed/hidden entirely.

## Homepage Notes

Hero:

- Name should be slim, elegant, large.
- Three role words after the name should be hyperlinked:
  - Researcher -> Research page
  - Journalist -> Reportage/Writing page
  - Educator -> Academic or Interventions page
- Moving "I work on" text should be slower and should sit below the primary CTA row if requested.
- Hero intro line should be contained and not wander too wide on desktop.
- User considered a large background-photo landing hero, but current implementation uses portrait/hero layout.

Recognition:

- Dean's List Scholarship should use one clean cover photo first.
- No text overlays on Dean's cover image.
- Only one "Click to spread" line below the image.
- When spread/opened, line should turn red and clearly say something like "Click to collapse."
- Dean's card title should not say "x4"; instead use a golden "4" inside the supporting line: "4 consecutive semesters..."
- Dean's List should spread to four cards on click, and individual cards can enlarge.
- ULAB Representation is a small recognition, date: 9 Oct 2025.
- ULAB Representation should remain visually smaller than major recognitions unless clicked/enlarged.
- Journalist under attack/CPJ item should be a recognition column, but remove duplicate text from the long list.
- "Also recognised" list should be hidden behind a "See more" drawer/button to reduce homepage text weight.
- July Mass Uprising Memorial Museum should hyperlink to its website when mentioned.

Education/status cards:

- Only current ULAB education should be visible on homepage.
- Keep old education code/data hidden/commented or present in code for later reactivation.
- "Currently doing" should be less prominent:
  - Text: `BSS in Media Studies and Journalism — 9th Semester`
- "Currently learning":
  - Text: `Python & NetworkX`
- Avoid huge empty spaces in the stats/status section.
- CGPA should be `3.99`.

Workplace logos:

- Workplace logos should follow the same visual structure as education logos.
- Black/white treatment should adapt to dark/light backgrounds.
- Workplaces/assets include:
  - The Business Standard
  - Netra News
  - FactWatch
  - ForensIQ
  - ULAB

Useful links:

- ForensIQ: `https://www.facebook.com/forensiqulab`
- Netra News author page: `https://netra.news/authors/miraz/`
- FactWatch: `https://www.fact-watch.org/`

## About Page Notes

The About page should be redesigned around:

- Photo as the centerpiece on one side.
- Literary narrative on the other side.
- Visible links/cards only for:
  - Services
  - Credentials
- End with a small CV and Get in Touch segment.

Preferred narrative style from screenshot:

Title:

`A short introduction, because the long one is the rest of the site.`

Keep this story style, with the photo on the other side.

Must include a subtle "Beyond the work" secret door link inside a sentence like:

`I believe a person's academic scholarship can only be fully understood beyond the work.`

Only the phrase "beyond the work" should be hyperlinked.

Do not show "Beyond the work" as an obvious nav/card/button.

Remove generic sections like:

- "How I move"
- "Hidden room"
- Long services/credentials explanatory blocks on the about page

About photo preference:

- Use the black jacket, white polo, broad smile brick-wall photo where appropriate.

About contact:

- Keep only: `I read everything that lands in the inbox.`
- Contact methods: email, LinkedIn, Signal, X.
- Do not use TBS byline as contact.

CV:

- Keep two PDFs:
  - Full/long CV
  - One-page essential CV
- Use a short label/copy, not a long explanation.

## Beyond The Work

This should be a hidden/secret page, accessible only through the subtle phrase in About.

The Beyond section previously included:

- Running
- Coffee
- Reading
- Photography
- Film aesthetics
- Learning/newness
- Travel/slow observation

Image positioning must be customizable because photos often crop heads. Add comments or data fields so Miraz can adjust `object-position`.

## Research Page

Research page should be less text-heavy and less boring. Use images and clearer hierarchy.

Title correction:

- Research title should include `Algorithm and Education`.

Current research proposals should be updated with the two latest proposal PDFs:

- `Algorithmic News Feeds and Misinformation Susceptibility _v10.docx.pdf`
- `Writing_Without_Writing (v6).docx.pdf`

Remove planned/old proposal placeholders if they are outdated.

Remove the "Interested in collaborating" box.

Add/keep a section named something like:

`Mini Research & Essays`

This section is for quick research, interview-based pieces, small-sample survey work, and analytical essays.

Essay added:

Title/topic:

`Bangladesh’s anti-LGBTQ frenzy is an education problem`

Placement:

- Under Research -> Mini Research & Essays
- Do not upload/embed PDF.
- Use text, hyperlinks, and the supplied image only.

Essay page styling:

- Remove two-column body layout.
- Tags should appear horizontally at the beginning.
- Writing should start centered on the page.
- Text should be justified.
- First letter of article body should be large/drop-cap style.

## Academic Page

Academic page path:

`/academic/`

Data file:

`content/academic.json`

Renderer:

`academic/index.html`

Styles:

`assets/css/style.css`

Course data is generated from ULAB transcript/result PDF.

Semester mapping:

- `233` = Fall 2023
- `241` = Spring 2024
- `242` = Summer 2024
- `243` = Fall 2024
- `251` = Spring 2025
- `252` = Summer 2025
- `253` = Fall 2025
- `261` = Spring 2026
- `262` = Summer 2026

Current known course status from transcript/advising:

Completed:

- Fall 2023: GEF1101 A, MSJ1101 A+, UCC1101 A-
- Spring 2024: GEF1201 A, MSJ1201 A, UCC1201 A-
- Summer 2024: GEF1202 A, MSJ2101 Communication and Technology A, UCC1202 Ethics A
- Fall 2024: HUM2112 A, HUM2204 A, SSC2149 A+, SSC3150 A+
- Spring 2025: MSJ2102 A+, MSJ2201 A, MSJ4101 Media and Law A+, NSC2283 A+
- Summer 2025: MSJ2202 A, NSC2282 A+, SSC2252 A
- Fall 2025: HUM2111 A, HUM3101 A+, MSJ3253 Data Journalism A
- Spring 2026: GEF2101 A, MSJ2252 Digital Audience A, MSJ3151 News Sourcing and Gathering A+, SSC4142 Methods of Social Research A

Registered/current Summer 2026:

- MSJ2251 Journalism and Society
- MSJ4152 Investigative Journalism-II
- NSC3282 Public Health and Epidemiology
- NSC4182 Mathematics

Withdrawn/not completed:

- CSE1201/CSE1202 related programming course was marked W and should be treated as not taken yet unless later corrected.

Course code corrections:

- HUM, not HUV
- SSC, not SSO
- NSC, not NSM

Recent academic card requests already implemented:

- Bottom metadata chips should start with semester/session first, then type, then link.
- Use `Not taken yet`, not `N/A`.
- Course title should use a distinct font/color not used elsewhere. Current implementation uses `Newsreader` in `academic/index.html` and `.course-slot h4` in CSS.
- `academic/index.html` fetch cache was bumped to `/content/academic.json?v=8`.

User does not want category labels repeated on every course card, but categories should still function internally for filtering/search.

Filtering:

- User disliked category filter pills laid bare under the search bar.
- Prefer a single filter button/dropdown, defaulting to All.

A+:

- Highlight A+ visually.

Academic intro:

- Remove line: `Papers, videos, dossiers, and experiments that escaped the classroom.`

## Reportage / Writing

Page name in nav should be:

`Reportage`

Section title:

`Selected works`

Remove:

- Bottom byline segment from selected works; archive already has details.

Archive:

- Dates should align cleanly.
- Articles should have themes and searchable theme filters.
- Include `July Movement` as a theme.
- All pieces during/after/on the July 2024 movement should be accessible under July Movement.
- Somewhere in July theme/site mention that Miraz covered the July 2024 movement that led to the fall of Sheikh Hasina.

New/important pieces added or requested:

- Netra interactive:
  - Title: `শেখ হাসিনার নিজ জবানীতে`
  - Date: 5 September
  - URL: `https://interactive.netra.news/sheikh-hasina-call-recordings-bn/`
  - Use uploaded `Sheik Hasina accounts.jpg` as selected work image.
- TBS drug story:
  - URL: `https://www.tbsnews.net/features/panorama/quiet-rise-new-drugs-bangladesh-1436601`
  - Use uploaded `the quiet rise of new drugs.webp`.
- Timeline:
  - Title: `One Month of Freedom`
  - Description: One month after Sheikh Hasina fled Bangladesh, Miraz and Mahatab Rashid created a visual timeline of her fall with artworks, cartoons, and a day-by-day record of the uprising.
  - Add under Projects and journalism archive.
  - Theme: July Movement.
  - Use `timeline output.jpg`.
  - Display initially cropped/previewed, with draggable/reveal interaction to show full poster.

Selected article images:

- User uploaded many story images. Use them instead of placeholders where matching.
- Top/selected works images may start black-and-white and become color on hover.

## Interventions Page

Current conceptual title:

`Training, workshops & other community work`

Keep short, creative, bigger-font intro.

Three core interventions:

1. ForensIQ trainings
   - Use ForensIQ training photo.
   - Use link: `https://www.facebook.com/forensiqulab`
   - Description should represent trainings as Head/Chief Executive of ForensIQ, not a single HPL workshop.

2. HPL workshop
   - Use HPL workshop banner and Zoom screenshot.
   - Hyperlink text `learning systems` to the HPL workshop.

3. Media literacy panel discussion
   - German Embassy Dhaka, 29 Oct 2024.
   - Mention algorithmic media literacy / media literacy in the age of algorithms.
   - Write in a way suitable for Oxford/Harvard applications and self-presentation.

Additional intervention:

- English Olympiad / language facilitation:
  - Over the years, from campus ambassador to adjudicator for national olympiad and medal for excellence, Miraz inspired/facilitated hundreds of students with language.
  - Date/photo context: 27 Jan 2023.

Important:

- Cure with Facts should not be removed.

Projects now live inside Interventions.

Project intro copy should be:

`Some projects I do out of passion, curiosity and to contribute for those who need it. They have no direct connection with my study or work but somehow they fulfill me and complement my work too.`

Project item:

- Easeparenting essay/project should be positioned as Digital Audience project.
- Use uploaded easeparenting images.
- Make it more visual and interactive.

## Services Page

Keep service page content/style from the external provided HTML as much as possible, but make it feel native to Miraz site.

Remove from left sidebar:

- Journalist · Researcher
- Dhaka, Bangladesh
- miraz8395@gmail.com
- +880 1969 500739

Freelance Translator & Education Consultant in homepage experience should link directly to Services page.

## Credentials Page

Credentials should have:

- Theme-based search/filter.
- Year-based search/filter.
- Newest first / oldest first sorting.

Move/keep "Need proof of certificate?" box at end of page, using style from the shared `index.html` reference.

Short intro idea:

Learning/exploring new things and connecting branches of knowledge is a stimulant.

Keep clean and short.

Homepage credential button should link directly to credentials page, not an about hash.

Credential button/card on homepage should have a subtle glimmering/ray-of-light attention effect.

## Assets / Files

User has uploaded many images. Use relevant assets, place inside proper assets folders, and avoid dumping files at root.

Structure should be clean, not novice. Keep pages/assets organized.

Workplace logos uploaded:

- `cropped-FactWatch_Logo1.png`
- `tbs-logo_0.webp`
- `unnamed (2).jpg`
- `banner.png`
- `netra news cover.jpg`
- `netra news dp.jpg`
- `ForensIQ.jpg`
- `ulab_15 (1).jpg`

Important personal/photos:

- Black jacket, white polo, broad smile brick-wall photo should be used for about.
- Kosovo ambassador photo for recognition.
- ForensIQ training photo for interventions.
- Dean's List cover image: `assets/awards/deans-list.jpg`

## Deployment / HTTPS

User manually uploads to GitHub Pages by dragging files.

Issue encountered:

- `.htaccess` does not upload because dotfiles are hidden and GitHub Pages does not use Apache `.htaccess` anyway.
- GitHub Pages HTTPS must be handled through GitHub Pages settings/custom domain, not `.htaccess`.

When giving upload lists, list exact files changed.

## Coding Notes

Use:

- `rg` for search.
- `apply_patch` for manual edits.
- Do not revert user changes.
- Preserve existing site style.
- If adding cache-busted data/CSS/JS, increment query strings.

Current recent edit files from latest academic request:

- `academic/index.html`
- `assets/css/style.css`

Recent academic edit details:

- Added `Newsreader` font import only to academic page.
- Reordered academic course metadata chips to session first.
- Course title styling in CSS:
  - `.course-slot h4`
  - font-family: `Newsreader`
  - dark color: `#8fd7ff`
  - light color: `#17647a`
- `content/academic.json` already uses `Not taken yet`.

## If Continuing Immediately

Most likely next checks:

1. Open `/academic/` and verify course cards:
   - Semester/session chip appears first at bottom.
   - No `N/A`.
   - Course title has distinct font/color.

2. If user asks for upload list after latest academic changes, upload:
   - `academic/index.html`
   - `assets/css/style.css`

3. If cache does not update on live site, hard refresh or increment:
   - CSS version in the page link.
   - JSON fetch query version.

