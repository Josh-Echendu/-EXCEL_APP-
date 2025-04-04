import pandas as pd
import glob #this is a library used to create a list of files
from fpdf import FPDF
from pathlib import Path

file_paths = glob.glob("invoice/*.xlsx")

# Add Header
for file_path in file_paths:
    
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()
    file_name = Path(file_path).stem # convert the file path to an intelligent string which we can work on

    invoice_nr, date = file_name.split("-")

    pdf.set_font(family="Times", style="B", size=8)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", align="L", ln=1)

    pdf.set_font(family="Times", style= "B", size=8)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", align= "L", ln=1)


    df = pd.read_excel(file_path, sheet_name= "Sheet 1")
    
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", style="B", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Rows to the table   
    for index, row in df.iterrows():
        pdf.cell(w=30, h=8, txt= str(row["product_id"]), align="L", border=1)
        pdf.cell(w=70, h=8, txt= str(row["product_name"]), align="L", border=1)
        pdf.cell(w=30, h=8, txt= str(row["amount_purchased"]), align="L", border=1)
        pdf.cell(w=30, h=8, txt= str(row["price_per_unit"]), align="L", border=1)
        pdf.cell(w=30, h=8, txt= str(row["total_price"]), align="L", border=1, ln=1)
        
    pdf.output(f"PDFs/{file_name}.pdf")

# Add the Table