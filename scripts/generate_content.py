from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = Path("/Users/miraz/Downloads/Published Articles by Miraz.xlsx")


def clean_text(value) -> str:
    if pd.isna(value):
        return ""
    return " ".join(str(value).replace("\n", " ").split()).strip()


def iso_date(value) -> str:
    if pd.isna(value) or value == "":
        return ""
    dt = pd.to_datetime(value, errors="coerce")
    if pd.isna(dt):
        return ""
    return dt.strftime("%Y-%m-%d")


def records_from_sheet(sheet_name: str, outlet: str) -> list[dict[str, str]]:
    df = pd.read_excel(WORKBOOK, sheet_name=sheet_name, header=1)
    out = []
    for _, row in df.iterrows():
        title = clean_text(row.get("Title"))
        link = clean_text(row.get("Link"))
        if not title or not link:
            continue
        out.append(
            {
                "title": title,
                "date": iso_date(row.get("Date")),
                "link": link,
                "outlet": outlet,
            }
        )
    return out


articles = records_from_sheet("Sheet1", "The Business Standard")
articles.extend(records_from_sheet("Sheet3", "Netra News"))

selected_writing = [
    {
        "title": "Cops, camera, cannabis",
        "outlet": "Netra News",
        "date": "2026-05-08",
        "category": "Criminal justice",
        "link": "https://netra.news/2026/cannabis-war-bangladesh/",
        "blurb": "A reported investigation into Bangladesh's cannabis enforcement machinery, showing how policing, spectacle, and public policy collide around ordinary citizens.",
        "image": "",
    },
    {
        "title": "The job \"verification\" trap",
        "outlet": "Netra News",
        "date": "2025-10-23",
        "category": "OSINT investigation",
        "link": "https://netra.news/2025/the-job-verification-trap/",
        "blurb": "An investigation into informal verification rackets and the way jobseekers are made vulnerable by opaque employment-screening systems.",
        "image": "",
    },
    {
        "title": "Bangladesh is building a digital economy on a floor that is giving way",
        "outlet": "The Business Standard",
        "date": "2026-05-07",
        "category": "Digital governance",
        "link": "https://www.tbsnews.net/thoughts/bangladesh-building-digital-economy-floor-giving-way-1431946",
        "blurb": "A policy-facing essay connecting AI ambition, infrastructure fragility, and the hidden exclusions beneath Bangladesh's digital-economy narrative.",
        "image": "",
    },
    {
        "title": "How Bangladesh's local NGOs are surviving the foreign aid collapse",
        "outlet": "The Business Standard",
        "date": "2026-05-11",
        "category": "Development sector",
        "link": "https://www.tbsnews.net/features/panorama/how-bangladeshs-local-ngos-are-surviving-foreign-aid-collapse-1435376",
        "blurb": "Field-sensitive reporting on institutional survival, shrinking aid, and the pressure local NGOs face while serving communities after donor retreat.",
        "image": "",
    },
    {
        "title": "Arrests over social media posts: Who decides what speech is acceptable?",
        "outlet": "The Business Standard",
        "date": "2026-04-21",
        "category": "Free speech",
        "link": "https://www.tbsnews.net/features/panorama/arrests-over-social-media-posts-who-decides-what-speech-acceptable-1418011",
        "blurb": "A sharp public-rights piece on social media policing, legal ambiguity, and the uneven power to define acceptable speech online.",
        "image": "",
    },
    {
        "title": "Chalaiden: Misinformation war grips social media",
        "outlet": "The Business Standard",
        "date": "2024-08-05",
        "category": "Misinformation",
        "link": "https://www.tbsnews.net/bangladesh/chalaiden-misinformation-war-grips-social-media-909926",
        "blurb": "A timely account of how rumour, coded language, and platform dynamics moved through Bangladesh's information space during national crisis.",
        "image": "",
    },
    {
        "title": "Not so 'digital' Bangladesh",
        "outlet": "The Business Standard",
        "date": "2024-10-27",
        "category": "Technology policy",
        "link": "https://www.tbsnews.net/features/panorama/not-so-digital-bangladesh-977551",
        "blurb": "A systems critique of digital public-service promises, showing where infrastructure, access, and governance fail the people they claim to serve.",
        "image": "",
    },
    {
        "title": "Jatiya Nagorik Committee: A New Dawn in Bangladesh's Politics?",
        "outlet": "Netra News",
        "date": "2025-01-19",
        "category": "Politics",
        "link": "https://netra.news/2025/jatiya-nagorik-committee-a-new-dawn-bangladesh/",
        "blurb": "Long-form political reporting on a new civic formation and the uncertain shape of Bangladesh's post-authoritarian transition.",
        "image": "",
    },
    {
        "title": "Campus cold war: Chhatra Dal vs. Shibir",
        "outlet": "Netra News",
        "date": "2024-12-30",
        "category": "Campus politics",
        "link": "https://netra.news/2024/campus-cold-war-chhatra-dal-vs-shibir-en/",
        "blurb": "Ground-level reporting on ideological competition inside universities and what campus politics reveals about the national moment.",
        "image": "",
    },
    {
        "title": "The politics of election affidavits: Why asset declarations no longer reveal the truth",
        "outlet": "The Business Standard",
        "date": "2026-01-11",
        "category": "Accountability",
        "link": "https://www.tbsnews.net/features/panorama/politics-election-affidavits-why-asset-declarations-no-longer-reveal-truth-1330986",
        "blurb": "A governance piece tracing how transparency instruments can become ritual paperwork when political incentives reward opacity.",
        "image": "",
    },
]

services = {
    "hero": {
        "eyebrow": "Freelance - Dhaka",
        "title": "Work that gets you taken seriously.",
        "intro": "Portfolio websites, sharp English writing, and research support. Done properly, delivered on time.",
        "availability": "Taking new work",
        "rotating": [
            "Portfolio Websites",
            "SOP Writing",
            "CV Editing",
            "Research Proposals",
            "Literature Reviews",
            "English Copywriting",
            "Annual Reports",
            "Content Analysis",
        ],
    },
    "sections": [
        {
            "id": "websites",
            "number": "01",
            "title": "Portfolio Websites",
            "columns": ["Package", "What's included", "Price"],
            "rows": [
                {
                    "name": "Basic",
                    "sub": "3 revisions included",
                    "detail": "Single page - 3 sections - clean layout, mobile-ready",
                    "price": "৳3,500",
                },
                {
                    "name": "Standard",
                    "sub": "3 revisions included",
                    "detail": "Multi-page - CV + Projects + Contact - most popular",
                    "price": "৳6,000",
                    "highlight": "Most popular",
                },
                {
                    "name": "Premium",
                    "sub": "3 revisions included",
                    "detail": "Custom design - Blog - LinkedIn integration - for those who want to stand out",
                    "price": "৳9,000",
                },
            ],
            "addons": [
                {"price": "৳500", "label": "Per extra revision or content update after delivery"},
                {"price": "৳800 / month", "label": "Monthly maintenance - edits, updates, uptime"},
                {"price": "৳1,500 / year", "label": "Domain + hosting support, annually"},
            ],
        },
        {
            "id": "writing",
            "number": "02",
            "title": "Writing & Editing",
            "columns": ["Service", "Details", "Price"],
            "rows": [
                {
                    "name": "Statement of Purpose",
                    "sub": "Full draft from scratch",
                    "detail": "Written around your background and target programme",
                    "price": "৳3,000",
                },
                {
                    "name": "SOP Editing",
                    "sub": "Your draft, sharpened",
                    "detail": "Argument, clarity, and flow improved",
                    "price": "৳1,500",
                },
                {
                    "name": "CV - Full Draft",
                    "sub": "Written from scratch",
                    "detail": "Structured, formatted, ready to send",
                    "price": "৳1,200",
                },
                {
                    "name": "CV Editing",
                    "sub": "Cleanup + restructure",
                    "detail": "Formatting, language, and layout fixed",
                    "price": "৳600",
                },
                {
                    "name": "English Copywriting",
                    "sub": "Per 500 words",
                    "detail": "Web copy, reports, social media posts",
                    "price": "৳1,000",
                },
                {
                    "name": "Annual Report / NGO Content",
                    "sub": "Per page",
                    "detail": "Written and proofed to publication standard",
                    "price": "৳800",
                },
            ],
        },
        {
            "id": "research",
            "number": "03",
            "title": "Research Support",
            "columns": ["Service", "Details", "Price"],
            "rows": [
                {
                    "name": "Literature Review",
                    "sub": "20-30 sources",
                    "detail": "Synthesised, cited, and properly formatted",
                    "price": "৳5,000",
                },
                {
                    "name": "Research Proposal",
                    "sub": "Full draft",
                    "detail": "Rationale, research questions, and methodology",
                    "price": "৳6,000",
                },
                {
                    "name": "Data Journalism",
                    "sub": "Content analysis",
                    "detail": "Framing, coding framework, and basic visualisation",
                    "price": "৳4,000",
                },
            ],
        },
    ],
    "process": [
        {
            "title": "Brief",
            "body": "A quick message or 15-minute call. Tell me what you need and when.",
        },
        {
            "title": "Advance",
            "body": "50% upfront. Work begins the same day or next morning.",
        },
        {
            "title": "Deliver",
            "body": "3-5 days for writing. 7-14 days for websites. 3 revisions included.",
        },
        {
            "title": "Done",
            "body": "Final payment on delivery. Ongoing retainer available if needed.",
        },
    ],
    "contact": {
        "email": "miraz8395@gmail.com",
        "phone": "+880 1969 500739",
        "location": "Dhaka, Bangladesh",
    },
    "finePrint": [
        {"label": "Turnaround", "value": "Writing: 3-5 days\nWebsites: 7-14 days"},
        {"label": "Payment", "value": "50% advance\n50% on delivery"},
        {"label": "Revisions", "value": "3 included\n৳500 per extra"},
        {"label": "Language", "value": "English - Bengali\non request"},
    ],
}

academic = {
    "stats": [
        {"label": "CGPA", "value": "3.99"},
        {"label": "Credits completed", "value": "81"},
        {"label": "Completed courses", "value": "27"},
        {"label": "Dean's List", "value": "4x"},
    ],
    "showcase": [
        {
            "title": "Algorithmic News Feeds and Misinformation Susceptibility",
            "type": "Research proposal",
            "course": "SSC4142 - Methods of Social Research",
            "session": "Spring 2026",
            "grade": "A",
            "desc": "Sequential explanatory mixed-methods proposal on algorithmic exposure, trust, and misinformation vulnerability among Dhaka university students.",
            "file": "pdfs/midterm-project.pdf",
            "fileLabel": "Read proposal",
            "media": "image",
        },
        {
            "title": "Platform Studies and Epistemic Equity",
            "type": "Literature review",
            "course": "MSJ1201 - Communication Research",
            "session": "Spring 2024",
            "grade": "A",
            "desc": "A literature-review project connecting platform power, information inequality, and Global South knowledge production.",
            "file": "pdfs/comm-research-paper.docx",
            "fileLabel": "Read paper",
            "media": "image",
        },
        {
            "title": "Team Data Decoder",
            "type": "Data journalism project",
            "course": "MSJ3253 - Data Journalism",
            "session": "Fall 2025",
            "grade": "A",
            "desc": "Collaborative data-journalism capstone with a reproducible evidence trail and publishable public-interest narrative.",
            "file": "pdfs/team-data-decoder.pdf",
            "fileLabel": "Read project",
            "media": "image",
        },
        {
            "title": "Convergence Communication I - Video Project",
            "type": "Video project",
            "course": "MSJ2102 - Convergence Communication I",
            "session": "Spring 2025",
            "grade": "A+",
            "desc": "A video-first coursework project exploring how reporting, scripting, shooting, and editing converge into a single story package.",
            "file": "",
            "fileLabel": "Video placeholder",
            "media": "video",
        },
        {
            "title": "Convergence Communication II - Video Project",
            "type": "Video project",
            "course": "MSJ2202 - Convergence Communication II",
            "session": "Summer 2025",
            "grade": "A",
            "desc": "Second convergence video project, extending the workflow into tighter production planning, post-production, and audience-facing packaging.",
            "file": "",
            "fileLabel": "Video placeholder",
            "media": "video",
        },
        {
            "title": "Digital Audience Mapping Portfolio",
            "type": "Audience analysis",
            "course": "MSJ2252 - Digital Audience",
            "session": "Spring 2026",
            "grade": "A",
            "desc": "Audience-behaviour coursework focused on digital attention, engagement signals, and how platform metrics shape editorial choices.",
            "file": "",
            "fileLabel": "Details coming soon",
            "media": "image",
        },
        {
            "title": "Media Law Case Briefs",
            "type": "Legal analysis",
            "course": "MSJ4101 - Media and the Law",
            "session": "Spring 2025",
            "grade": "A+",
            "desc": "Case-led portfolio on media regulation, rights, and legal constraints around journalism practice in Bangladesh.",
            "file": "",
            "fileLabel": "Details coming soon",
            "media": "image",
        },
        {
            "title": "Communication and Technology Essay",
            "type": "Theory essay",
            "course": "MSJ2101 - Communication and Technology",
            "session": "Summer 2024",
            "grade": "A",
            "desc": "Analytical coursework on the social consequences of communication technologies and the politics embedded in technical systems.",
            "file": "",
            "fileLabel": "Details coming soon",
            "media": "image",
        },
        {
            "title": "Grassroots Economic Development Field Notes",
            "type": "Field essay",
            "course": "SSC3150 - Seminar on Grassroots Economic Development",
            "session": "Fall 2024",
            "grade": "A+",
            "desc": "Social-science coursework on community economies, development practice, and how local institutions negotiate scarcity.",
            "file": "",
            "fileLabel": "Details coming soon",
            "media": "image",
        },
        {
            "title": "Investigative Journalism II Dossier",
            "type": "Reporting dossier",
            "course": "MSJ4152 - Investigative Journalism-II",
            "session": "Summer 2026",
            "grade": "Registered",
            "desc": "Reserved showcase slot for the advanced investigation portfolio currently in progress.",
            "file": "",
            "fileLabel": "In progress",
            "media": "image",
        },
    ],
    "more": [
        {
            "title": "The Listening City",
            "course": "MSJ3151 - News Sourcing and Gathering",
            "session": "Spring 2026",
        },
        {
            "title": "Public Memory After the Uprising",
            "course": "HUM2204 - History of Modern South Asia",
            "session": "Fall 2024",
        },
        {
            "title": "Ethics of Seeing",
            "course": "HUM2112 - Introduction to Photography",
            "session": "Fall 2024",
        },
        {
            "title": "Conflict, Rumour, and Everyday Survival",
            "course": "SSC2252 - Living with Conflict",
            "session": "Summer 2025",
        },
        {
            "title": "Film Form and Public Feeling",
            "course": "HUM3101 - Aesthetic of Film",
            "session": "Fall 2025",
        },
        {
            "title": "Statistics for Newsroom Decisions",
            "course": "GEF2101 - Introduction to Data and Statistics",
            "session": "Spring 2026",
        },
        {
            "title": "Mass Communication Theory Notebook",
            "course": "MSJ2201 - Mass Communication",
            "session": "Spring 2025",
        },
        {
            "title": "Biodiversity, Risk, and Public Communication",
            "course": "NSC2282 - Biodiversity and Nature Conservation",
            "session": "Summer 2025",
        },
        {
            "title": "Public Health Explainers",
            "course": "NSC3282 - Public Health and Epidemiology",
            "session": "Summer 2026",
        },
        {
            "title": "Advanced Bangla Writing Portfolio",
            "course": "GEF1203 - Advanced Bangla Writing Skills",
            "session": "Summer 2026",
        },
    ],
}


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


save_json(ROOT / "content/articles.json", articles)
save_json(ROOT / "content/writing-selected.json", selected_writing)
save_json(ROOT / "content/services.json", services)
save_json(ROOT / "content/academic.json", academic)

print(f"articles={len(articles)} selected={len(selected_writing)}")
