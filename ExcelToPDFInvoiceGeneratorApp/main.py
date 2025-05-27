import pandas as pd
import glob
from fpdf import  FPDF
from pathlib import Path

ORDERS_PATH = "orders"
INVOICES_PATH = "invoices"

# Iterate over the XLSX orders
orders_paths = glob.glob(ORDERS_PATH + "/*.xlsx")

for order_path in orders_paths:
    # Set the PDF invoice
    pdf_invoice = FPDF(orientation="P", unit="mm", format="A4")
    pdf_invoice.add_page()

    # Add the invoice number and date
    order_filename = Path(order_path).stem
    invoice_nr, invoice_date = order_filename.split("-")

    pdf_invoice.set_font(family="Times", style="B", size=16)
    pdf_invoice.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf_invoice.cell(w=50, h=8, txt=f"Date: {invoice_date}", ln=1)

    pdf_invoice.ln(20)

    # Add the table with the ordered items
    # Table header
    invoice_content = pd.read_excel(order_path, sheet_name="Sheet 1")
    table_header = [column.replace("_", " ").title() for column in invoice_content.columns]

    pdf_invoice.set_font(family="Times", size=10, style="B")
    pdf_invoice.set_text_color(80, 80, 80)
    pdf_invoice.cell(w=30, h=8, txt=table_header[0], border=1)
    pdf_invoice.cell(w=60, h=8, txt=table_header[1], border=1)
    pdf_invoice.cell(w=40, h=8, txt=table_header[2], border=1)
    pdf_invoice.cell(w=30, h=8, txt=table_header[3], border=1)
    pdf_invoice.cell(w=30, h=8, txt=table_header[4], border=1, ln=1)

    # Table body
    for index, row in invoice_content.iterrows():
        pdf_invoice.set_font(family="Times", size = 10)
        pdf_invoice.set_text_color(80, 80, 80)
        pdf_invoice.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf_invoice.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf_invoice.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf_invoice.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf_invoice.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Add the total amount to the table
    total_sum = invoice_content["total_price"].sum()
    pdf_invoice.set_font(family="Times", size=10, style="B")
    pdf_invoice.set_text_color(80, 80, 80)
    pdf_invoice.cell(w=30, h=8, txt="", border=1)
    pdf_invoice.cell(w=60, h=8, txt="", border=1)
    pdf_invoice.cell(w=40, h=8, txt="", border=1)
    pdf_invoice.cell(w=30, h=8, txt="", border=1)
    pdf_invoice.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf_invoice.ln(20)

    # Add the total amount
    pdf_invoice.set_font(family="Times", size=15, style="B")
    pdf_invoice.cell(w=60, h=8, txt=f"The total price is {total_sum}", ln=1)

    pdf_invoice.ln(20)

    # Add the generator's name and logo
    pdf_invoice.cell(w=45, h=10, txt=f"Alexandru Cohal")
    pdf_invoice.image("logo.jpg", w=10)

    # Output the PDF invoice
    pdf_invoice.output(f"{INVOICES_PATH}/{invoice_nr}.pdf")