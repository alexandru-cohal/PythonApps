import pandas as pd
import glob
from fpdf import  FPDF
from pathlib import Path

XLSX_INVOICES_PATH = "invoices"
PDF_INVOICES_PATH = "PDFs"

invoices_paths = glob.glob(XLSX_INVOICES_PATH + "/*.xlsx")
for invoice_path in invoices_paths:
    filename = Path(invoice_path).stem
    invoice_nr, invoice_date = filename.split("-")

    pdf_document = FPDF(orientation="P", unit="mm", format="A4")
    pdf_document.add_page()
    pdf_document.set_font(family="Times", style="B", size=16)
    pdf_document.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf_document.cell(w=50, h=8, txt=f"Date: {invoice_date}", ln=1)

    pdf_document.ln(20)

    invoice_content = pd.read_excel(invoice_path, sheet_name="Sheet 1")

    table_header = [column.replace("_", " ").title() for column in invoice_content.columns]

    pdf_document.set_font(family="Times", size=10, style="B")
    pdf_document.set_text_color(80, 80, 80)
    pdf_document.cell(w=30, h=8, txt=table_header[0], border=1)
    pdf_document.cell(w=60, h=8, txt=table_header[1], border=1)
    pdf_document.cell(w=40, h=8, txt=table_header[2], border=1)
    pdf_document.cell(w=30, h=8, txt=table_header[3], border=1)
    pdf_document.cell(w=30, h=8, txt=table_header[4], border=1, ln=1)

    for index, row in invoice_content.iterrows():
        pdf_document.set_font(family="Times", size = 10)
        pdf_document.set_text_color(80, 80, 80)
        pdf_document.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf_document.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf_document.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf_document.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf_document.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)


    total_sum = invoice_content["total_price"].sum()
    pdf_document.set_font(family="Times", size=10, style="B")
    pdf_document.set_text_color(80, 80, 80)
    pdf_document.cell(w=30, h=8, txt="", border=1)
    pdf_document.cell(w=60, h=8, txt="", border=1)
    pdf_document.cell(w=40, h=8, txt="", border=1)
    pdf_document.cell(w=30, h=8, txt="", border=1)
    pdf_document.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf_document.ln(20)

    pdf_document.set_font(family="Times", size=15, style="B")
    pdf_document.cell(w=60, h=8, txt=f"The total price is {total_sum}", ln=1)

    pdf_document.ln(20)
    pdf_document.cell(w=45, h=10, txt=f"Alexandru Cohal")
    pdf_document.image("logo.jpg", w=10)


    pdf_document.output(f"{PDF_INVOICES_PATH}/{invoice_nr}.pdf")


