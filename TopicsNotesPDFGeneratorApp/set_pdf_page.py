from fpdf import FPDF


def set_header(pdf_document, topic):
    """ Set the header of a topic notes PDF page """
    pdf_document.set_font(family="Times", style="B", size=24)
    pdf_document.set_text_color(100, 100, 100) #Dark gray
    pdf_document.cell(w=0, h=12, txt=topic, align="L", ln=1)


def set_grid(pdf_document):
    """ Set the grid of a topic notes PDF page """
    for y in range(40, 280, 10):
        pdf_document.line(10, y, 200, y)


def set_footer(pdf_document, distance_to_last_cell, topic, current_page, total_page):
    """ Set the footer of a topic notes PDF page """
    pdf_document.ln(distance_to_last_cell)
    pdf_document.set_font(family="Times", style="I", size=8)
    pdf_document.set_text_color(180, 180, 180) #Light gray
    pdf_document.cell(w=0, h=10, txt=f"{topic} - {current_page} / {total_page}", align="R", ln=1)