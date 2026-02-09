from fpdf import FPDF
import uuid

# Initialize PDF
pdf = FPDF()
pdf.add_page()

pdf.add_font("NotoSansBengali", "", "NotoSansBengali-Regular.ttf")
pdf.set_font("NotoSansBengali", size=15)


with open("f72f533f-e5c6-4d95-8818-d0d87ee06229.txt", "r", encoding="utf-8") as f:
    for line in f:
        clean_line = line.strip()
        if clean_line:
            pdf.cell(200, 10, text=clean_line, new_x="LMARGIN", new_y="NEXT", align="C")

filename = f"{uuid.uuid4()}.pdf"
pdf.output(filename)
print(f"PDF saved as: {filename}")