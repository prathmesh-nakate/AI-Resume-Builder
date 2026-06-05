from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def create_resume(
        filename,
        name,
        email,
        github,
        linkedin,
        education,
        skills,
        projects,
        summary):

    pdf = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    content = []

    title_style = styles["Title"]
    title_style.textColor = colors.HexColor("#1E3A8A")

    heading_style = styles["Heading2"]
    heading_style.textColor = colors.HexColor("#2563EB")

    content.append(
        Paragraph(name.upper(), title_style)
    )

    content.append(
        Paragraph(f"<b>Email:</b> {email}", styles["Normal"])
    )

    content.append(
        Paragraph(f"<b>GitHub:</b> {github}", styles["Normal"])
    )

    content.append(
        Paragraph(f"<b>LinkedIn:</b> {linkedin}", styles["Normal"])
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph("PROFESSIONAL SUMMARY", heading_style)
    )

    content.append(HRFlowable())

    content.append(
        Paragraph(summary, styles["Normal"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("SKILLS", heading_style)
    )

    content.append(HRFlowable())

    for skill in skills.split(","):
        content.append(
            Paragraph(f"• {skill.strip()}",
                      styles["Normal"])
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("PROJECTS", heading_style)
    )

    content.append(HRFlowable())

    for project in projects.split(","):
        content.append(
            Paragraph(f"• {project.strip()}",
                      styles["Normal"])
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("EDUCATION", heading_style)
    )

    content.append(HRFlowable())

    content.append(
        Paragraph(education, styles["Normal"])
    )

    content.append(Spacer(1, 12))

    score = 0

    if skills.strip():
        score += 25

    if projects.strip():
        score += 25

    if education.strip():
        score += 25

    if github.strip() and linkedin.strip():
        score += 25

    content.append(
        Paragraph("ATS SCORE", heading_style)
    )

    content.append(HRFlowable())

    content.append(
        Paragraph(f"{score}/100", styles["Normal"])
    )

    pdf.build(content)