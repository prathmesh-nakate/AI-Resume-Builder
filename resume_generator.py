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
        education,
        skills,
        projects,
        summary):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    title_style = styles["Title"]
    title_style.textColor = colors.darkblue

    heading_style = styles["Heading2"]
    heading_style.textColor = colors.darkblue

    # Name
    content.append(
        Paragraph(name.upper(), title_style)
    )

    content.append(
        Paragraph(email, styles["Normal"])
    )

    content.append(Spacer(1, 15))

    # Summary
    content.append(
        Paragraph("PROFESSIONAL SUMMARY",
                  heading_style)
    )

    content.append(HRFlowable())

    content.append(
        Paragraph(summary, styles["Normal"])
    )

    content.append(Spacer(1, 10))

    # Skills
    content.append(
        Paragraph("SKILLS",
                  heading_style)
    )

    content.append(HRFlowable())

    skill_list = skills.split(",")

    for skill in skill_list:
        content.append(
            Paragraph(f"• {skill.strip()}",
                      styles["Normal"])
        )

    content.append(Spacer(1, 10))

    # Projects
    content.append(
        Paragraph("PROJECTS",
                  heading_style)
    )

    content.append(HRFlowable())

    content.append(
        Paragraph(projects,
                  styles["Normal"])
    )

    content.append(Spacer(1, 10))

    # Education
    content.append(
        Paragraph("EDUCATION",
                  heading_style)
    )

    content.append(HRFlowable())

    content.append(
        Paragraph(education,
                  styles["Normal"])
    )

    pdf.build(content)