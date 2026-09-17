import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, KeepTogether, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def build_pdf():
    pdf_path = os.path.join("output", "Week1_Project_Planning_and_Wireframing.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor("#1E3A8A"), spaceAfter=10)
    subtitle_style = ParagraphStyle('DocSubTitle', parent=styles['Normal'], fontSize=12, leading=16, textColor=colors.HexColor("#4B5563"), spaceAfter=20)
    h1_style = ParagraphStyle('SectionH1', parent=styles['Heading2'], fontSize=16, leading=20, textColor=colors.HexColor("#1E40AF"), spaceBefore=15, spaceAfter=8)
    h2_style = ParagraphStyle('SectionH2', parent=styles['Heading3'], fontSize=12, leading=16, textColor=colors.HexColor("#1F2937"), spaceBefore=10, spaceAfter=5)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#374151"), spaceAfter=8)
    caption_style = ParagraphStyle('Caption', parent=styles['Italic'], fontSize=9, leading=12, textColor=colors.HexColor("#6B7280"), alignment=1, spaceBefore=4, spaceAfter=15)
    
    story = []
    
    # Title Header
    story.append(Paragraph("FitPulse — Week 1 Task Submission", title_style))
    story.append(Paragraph("Project Planning, Mobile App Architecture & UX Wireframes | Internship Deliverable", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceAfter=15))
    
    # helper function to read markdown text cleanly
    def read_doc(path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.readlines()
        return []

    # Section 1: Project Plan
    plan_lines = read_doc(os.path.join("docs", "01_project_plan.md"))
    for line in plan_lines:
        line = line.strip()
        if line.startswith("# "):
            story.append(Paragraph(line.replace("# ", ""), h1_style))
        elif line.startswith("## "):
            story.append(Paragraph(line.replace("## ", ""), h2_style))
        elif line.startswith("* "):
            story.append(Paragraph(f"• {line[2:]}", body_style))
        elif line:
            story.append(Paragraph(line, body_style))
            
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E2E8F0"), spaceBefore=10, spaceAfter=15))

    # Section 2: User Flow
    flow_lines = read_doc(os.path.join("docs", "02_user_flow.md"))
    for line in flow_lines:
        line = line.strip()
        if line.startswith("# "):
            story.append(Paragraph(line.replace("# ", ""), h1_style))
        elif line.startswith("## ") or line.startswith("### "):
            story.append(Paragraph(line.replace("### ", "").replace("## ", ""), h2_style))
        elif line.startswith("* "):
            story.append(Paragraph(f"• {line[2:]}", body_style))
        elif line and not line.startswith("```"):
            story.append(Paragraph(line, body_style))

    story.append(PageBreak())

    # Section 3: Wireframes Showcase
    story.append(Paragraph("Wireframe UI Designs", h1_style))
    story.append(Paragraph("Below are the 5 core screen wireframe designs created for the FitPulse architecture.", body_style))
    story.append(Spacer(1, 10))

    wireframe_files = [
        ("01_dashboard.png", "Screen 1: Dashboard / Home View"),
        ("02_workout_tracker.png", "Screen 2: Active Workout Tracker"),
        ("03_habit_log.png", "Screen 3: Daily Habit Logging View"),
        ("04_analytics.png", "Screen 4: Analytics & Progress View"),
        ("05_profile.png", "Screen 5: User Profile & Preferences")
    ]

    for filename, caption in wireframe_files:
        img_path = os.path.join("assets", "wireframes", filename)
        if os.path.exists(img_path):
            img = Image(img_path, width=180, height=390)
            element_group = KeepTogether([
                img,
                Paragraph(caption, caption_style),
                Spacer(1, 10)
            ])
            story.append(element_group)

    story.append(PageBreak())

    # Section 4: UX Rationale
    ux_lines = read_doc(os.path.join("docs", "03_ux_rationale.md"))
    for line in ux_lines:
        line = line.strip()
        if line.startswith("# "):
            story.append(Paragraph(line.replace("# ", ""), h1_style))
        elif line.startswith("## ") or line.startswith("### "):
            story.append(Paragraph(line.replace("### ", "").replace("## ", ""), h2_style))
        elif line.startswith("* "):
            story.append(Paragraph(f"• {line[2:]}", body_style))
        elif line:
            story.append(Paragraph(line, body_style))

    doc.build(story)
    print("Successfully built final PDF at: output/Week1_Project_Planning_and_Wireframing.pdf")

if __name__ == "__main__":
    build_pdf()