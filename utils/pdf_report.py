from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import tempfile

def generate_pdf(score, style, security, complexity):
    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(temp_pdf.name)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("CodeInsight AI - Code Review Report", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(f"Health Score: {score}/100", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph("Style Issues:", styles["Heading2"]))
    elements.append(Paragraph(style or "None", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Security Issues:", styles["Heading2"]))
    elements.append(Paragraph(security or "None", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Complexity Report:", styles["Heading2"]))
    elements.append(Paragraph(complexity or "None", styles["Normal"]))

    doc.build(elements)
    return temp_pdf.name
