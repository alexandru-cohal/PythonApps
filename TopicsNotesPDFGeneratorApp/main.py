import set_pdf_page as spp
from fpdf import FPDF
import pandas as pd

INPUT_FILEPATH = "topics.csv"
OUTPUT_FILEPATH = "output.pdf"

pdf_document = FPDF(orientation="P", unit="mm", format="A4")
pdf_document.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv(INPUT_FILEPATH)

# Iterate over topics
for index, row in df.iterrows():
    pdf_document.add_page()

    spp.set_header(pdf_document, row["Topic"])
    spp.set_grid(pdf_document)
    spp.set_footer(pdf_document, 260, row["Topic"], 1, row["Pages"])

    for index_page in range(2, row["Pages"]+1):
        pdf_document.add_page()

        spp.set_grid(pdf_document)
        spp.set_footer(pdf_document, 270, row["Topic"], index_page, row["Pages"])

pdf_document.output(OUTPUT_FILEPATH)