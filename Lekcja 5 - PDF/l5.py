from fpdf import FPDF
from fpdf.enums import XPos, YPos
import glob
import os

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

pdf.set_font("DejaVu", size=8) # i tu
pdf.text(x=10, y = A4H - 20, text ="Oferta powstala za pomoca Pythona i AI")



list_of_attractions = ["Atrakcja"]

for image_path in glob.glob("atrakcje_grafiki/*"):
    attraction = os.path.basename(image_path[:-4])
    text_path = os.path.join("atrakcje_opisy", f"{attraction}.txt")
    formattedAttraction = attraction.replace('_', ' ').capitalize()
    list_of_attractions.append(formattedAttraction)  ## .append

    pdf.add_page()
    # ustawienie tytulu strony z atrakcja
    pdf.set_font('DejaVu', size= 24)
    pdf.cell(200,20, text=f"Nazwa atrakcji: {formattedAttraction}", new_x= XPos.LEFT, new_y = YPos.NEXT, align="C")

    # ustawienie obrazka atrakcji
    pdf.cell(200,10, link=pdf.image(f"{image_path}", w=190, h=120), new_x = XPos.LEFT, new_y = YPos.NEXT, align="L")
    # brak nawiasu po h=120
    # ustawienie opisu atrakcji, usuniecie nawiasu na koncu
    pdf.set_font('DejaVu', size=12)

    with open(text_path, "r", encoding="utf-8") as file:
        description = file.read()
        pdf.multi_cell(200,10, text=f"Opis atrakcji: {description}", new_x= XPos.LEFT, new_y = YPos.NEXT, align="L")
        

list_of_times = ["Czas", "16h", "8h", "12h", "14h", "4h"]
list_of_costs = ["Cena", "1500PLN", "700PLN", "1000 PLN", "1200PLN", "400PLN"]

pdf.add_page()
pdf.set_font('DejaVu', size=24)
pdf.cell(200,20, text="Ceny atrakcji", new_x=XPos.LEFT, new_y=YPos.NEXT, align="C")
pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
#dodawanie w petli kolejnych wierszy tabeli 
pdf.set_font("DejaVu", size=12)
with pdf.table(line_height=pdf.font_size, padding=2) as table:
    for atr,cost,time in zip(list_of_attractions, list_of_costs, list_of_times):
        rows = table.row()
        for element in(atr,cost,time):
            rows.cell(element)

pdf.output("Oferta_biura_podrozy.pdf")