from fpdf import FPDF

class Shirt(FPDF):
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        super().__init__(orientation="P", unit="mm", format="A4")
        self._name = name

    def header(self):
        self.image("shirtificate.png", x=10, y=65, w=190, h=190)
        self.set_font("helvetica", style="B", size=32)
        self.set_text_color(0, 0, 0)
        self.text(90, 90, "CS50 Shirtificate")

    def footer(self):
        self.set_font("helvetica", style="B", size=16)
        self.set_text_color(255, 255, 255)
        self.cell(70, 140, f"{self._name} took CS50", align="C")


if __name__ == "__main__":

    name = input("Name: ")

    pdf = Shirt(name)
    pdf.add_page()
    pdf.output("shirtificate.pdf")

