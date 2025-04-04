import pandas as pd
import glob #this is a library used to create a list of files
from fpdf import FPDF
from pathlib import Path

file_paths = glob.glob("invoice/*.xlsx")

for file_path in file_paths:
    df = pd.read_excel(file_path, sheet_name= "Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    file_name = Path(file_path).stem # convert the file path to an intelligent string which we can work on
    print(file_name)
    invoice_nr = file_name.split("-")[0]
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt="Invoice nr." + invoice_nr, align="L")
    pdf.output(f"PDFs/{file_name}.pdf")


# Create a minimal PDF for each Excel file


# from pathlib import Path
# file_path = r"invoice/10001-2023.1.18.xlsx"
# file_path
#file_name = Path(file_path).stem
#file_name
# invoice_nr = file_name.split("-")
# invoice_nr
# invoice_nr = file_name.split("-")[0]
# invoice_nr
# f"pdfs/{file_name}.pdf" 



