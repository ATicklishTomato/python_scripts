from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter


def make_watermark():
    text = input("Enter the watermark text here:").replace("\\n", "\n")
    pdf = canvas.Canvas("watermark.pdf", pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.white, alpha=0.6)
    pdf.setFont("Helvetica", 60)
    pdf.rotate(45)
    t = pdf.beginText()
    t.setTextOrigin(100, 100)
    t.textLines(text)
    pdf.drawText(t)
    pdf.showPage()
    pdf.save()


def make_pdf():
    pdf_file = input("PDF file: ")
    watermark = 'watermark.pdf'
    merged = input("Filename for new file: ")

    with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]
        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)
            output.add_page(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)


if __name__ == '__main__':
    make_watermark()
    make_pdf()
