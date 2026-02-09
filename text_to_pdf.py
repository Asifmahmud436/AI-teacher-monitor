from fpdf import FPDF
import uuid

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=15)
f = open("response.txt", "r")

for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align="C")

name = uuid.uuid4()
pdf.output(f"{name}.pdf")