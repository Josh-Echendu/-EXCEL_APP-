import glob
from fpdf import FPDF
from pathlib import Path
import pandas as pd 

pdf = FPDF(orientation="P", unit= "mm", format="A4")
file_paths = glob.glob("text_file/*.txt")
print(file_paths)

for file_path in file_paths:
    pdf.add_page()

    file_name = Path(file_path).stem
    name = file_name.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt= name, align= 'L', ln=1)
    
    #Get the content of each text file
    with open(file_path, 'r') as file:
        content = file.read()

    # Add the text of each text file
    pdf.set_font(family="Times", style="B", size=10)
    pdf.multi_cell(w=0, h= 8, align="L", txt= content) # we used a multicell because we are dealing with a multiple line of text
    
pdf.output("output.pdf")

