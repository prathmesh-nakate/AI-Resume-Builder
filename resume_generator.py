from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


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

    content.append(
        Paragraph(f"<b>{name}</b>", styles["Title"])
    )

    content.append(
        Paragraph(email, styles["Normal"])
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph("Professional Summary",
                  styles["Heading2"])
    )

    content.append(
        Paragraph(summary, styles["Normal"])
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph("Education",
                  styles["Heading2"])
    )

    content.append(
        Paragraph(education,
                  styles["Normal"])
    )

    content.append(
        Paragraph("Skills",
                  styles["Heading2"])
    )

    content.append(
        Paragraph(skills,
                  styles["Normal"])
    )

    content.append(
        Paragraph("Projects",
                  styles["Heading2"])
    )

    content.append(
        Paragraph(projects,
                  styles["Normal"])
    )

    pdf.build(content)