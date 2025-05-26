from fpdf import FPDF
import pandas as pd

pdf_document = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf_document.add_page()
    pdf_document.set_font(family="Times", style="B", size=24)
    pdf_document.set_text_color(100, 100, 100)
    pdf_document.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf_document.line(10, 22, 200, 22)

    for index_page in range(row["Pages"] - 1):
        pdf_document.add_page()

pdf_document.output("output.pdf")

print(type(pdf_document))