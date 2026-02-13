from fpdf import FPDF
import uuid

def pdfier(text_file):
    pdf = FPDF()
    pdf.add_page()
    
    with open(text_file, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                pdf.cell(200, 10, text=clean_line, new_x="LMARGIN", new_y="NEXT", align="C")

        filename = f"{uuid.uuid4()}.pdf"
        pdf.output(filename)
        print(f"PDF saved as: {filename}")

    return pdf

# Initialize PDF
# from fpdf import FPDF
# import uuid

# # ফন্ট ফাইলটি যেন আপনার প্রজেক্ট ডিরেক্টরিতেই থাকে
# font_path = "NotoSansBengali-Regular.ttf"

# pdf = FPDF()
# pdf.add_page()

# # fpdf2-এ add_font সরাসরি কাজ করে
# pdf.add_font("NotoSansBengali", "", font_path)
# pdf.set_font("NotoSansBengali", size=12)

# with open("1b7bc22e-54ec-4c20-bffe-be1c117d44a9.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         clean_line = line.strip()
#         if clean_line:
#             # fpdf2 তে text আর্গুমেন্ট ব্যবহার করা যায়
#             pdf.multi_cell(0, 10, text=clean_line, align="L") 

# filename = f"{uuid.uuid4()}.pdf"
# pdf.output(filename)
# print(f"PDF saved as: {filename}")
