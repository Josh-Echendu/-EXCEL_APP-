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

    invoice_nr, date = file_name.split("-")

    pdf.set_font(family="Times", style="B", size=8)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", align="L", ln=1)

    pdf.set_font(family="Times", style= "B", size=8)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", align= "L")
    pdf.output(f"PDFs/{file_name}.pdf")


# Add invoice date    


