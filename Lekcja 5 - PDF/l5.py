from fpdf import FPDF

A4W = 210
A4H = 297

pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font("DejaVu", size=32)
pdf.set_text_color(255,0,0)
pdf.text(x=40, y=20, text="Oferta biura Huricane Tave's")

pdf.image("logo.png", x= A4W * 0.25, y = A4W * 0.25, w = A4W * 0.5, h= A4W * 0.5)

pdf.set_text_color(0,0,0)
pdf.set_font("DejaVu", size=24) # tu byl blad
pdf.text(x=40, y = A4W * 0.75+20, text ="Oferta wycieczki - Slońce Pustyni")

pdf.set_font("DejaVu", size =8) # i tu
pdf.text(x=10, y = A4H - 20, text ="Oferta powstala za pomoca Pythona i AI")

pdf.output("Oferta_biura_podrozy.pdf")

