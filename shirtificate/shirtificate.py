from fpdf import FPDF


name = input("Name: ")


class Shirt():
    def __init__(self, name):

        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 40)
        self._pdf.cell(0, 80, "CS50 shirtificate", align ="C")
        self._pdf.image("shirtificate.png")
        self._pdf.set_font_size(40)
        self._pdf.set_text_color(255,255,255)
        self._pdf.cell(40,150,txt=f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)



shirt = Shirt(name)
shirt.save("shirtificate.pdf")