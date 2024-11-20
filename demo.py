import tempfile
from qrbill import QRBill
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderSVG

my_bill = QRBill(
       account='CH5800791123000889012',
       creditor={
        'name': 'Co4 Aktiengesellschaft',
        'street': 'Gewerbeweg', 
        'house_num': '15', 
        'pcode': '9490', 
        'city': 'Vaduz', 
        'country': 'LI'
       },
       amount='22.45',
       debtor={
           'name': 'Hans Muster',
           'street': 'Musterweg',
           'house_num': '10',
           'pcode': '9470',
           'city': 'Buchs',
           'country': 'CH'
       },
       language='de'
   )
with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
    my_bill.as_svg(temp)
    temp.seek(0)
    drawing = svg2rlg(temp)

renderSVG.drawToFile(drawing, "qrbill.svg")
renderPDF.drawToFile(drawing, "qrbill.pdf")