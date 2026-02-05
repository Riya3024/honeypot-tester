from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_fir_pdf(fir, filename="FIR_Report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Cyber Crime FIR Report</b>", styles["Title"]))
    for k, v in fir.items():
        story.append(Paragraph(f"<b>{k}:</b> {v}", styles["Normal"]))

    doc.build(story)
    return filename
