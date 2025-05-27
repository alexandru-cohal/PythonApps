import pandas as pd
import glob
from fpdf import  FPDF
from pathlib import Path

XLSX_INVOICES_PATH = "invoices"
PDF_INVOICES_PATH = "PDFs"

invoices_paths = glob.glob(XLSX_INVOICES_PATH + "/*.xlsx")
for invoice_path in invoices_paths:
    invoice_content = pd.read_excel(invoice_path, sheet_name="Sheet 1")

    filename = Path(invoice_path).stem
    invoice_nr = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf_document = FPDF(orientation="P", unit="mm", format="A4")
    pdf_document.add_page()
    pdf_document.set_font(family="Times", style="B", size=16)
    pdf_document.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}")
    pdf_document.output(f"{PDF_INVOICES_PATH}/{invoice_nr}.pdf")
