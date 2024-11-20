import tempfile
from qrbill import QRBill
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderSVG

my_bill = QRBill(
       account='CH39 0870 4016 0754 7300 7',
       creditor={
        'name': 'Envis AG',
        'street': 'Im alten Riet 153', 
        'house_num': '153', 
        'pcode': '9494', 
        'city': 'Schaan', 
        'country': 'LI'
       },
       amount='19.43',
       debtor={
           'name': 'Bea Beispiel',
           'street': 'Bangarten',
           'house_num': '10',
           'pcode': '9490',
           'city': 'Vaduz',
           'country': 'LI'
       },
       reference_number="RF14 111",
       additional_information='Stromkostenabrechnung 01.01.2024 - 30.06.2024',
       language='de'
   )

with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
    my_bill.as_svg(temp)
    temp.seek(0)
    drawing = svg2rlg(temp)

print(renderSVG.drawToString(drawing))
renderSVG.drawToFile(drawing, "qrbill.svg")
renderPDF.drawToFile(drawing, "qrbill.pdf")