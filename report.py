# https://recursospython.com/guias-y-manuales/crear-documentos-pdf-en-python-con-reportlab/

import time
import itertools
from random import randint
from statistics import mean

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


def export_to_pdf(data):
    c = canvas.Canvas("reporte.pdf", pagesize=A4)
    w, h = A4
    c.drawString(475, 780, time.strftime("%d/%m/%y"))

    #c.showPage()
    max_rows_per_page = 45
    # Margin.
    x_offset = 75
    y_offset = 100
    # Space between rows.
    padding = 15


    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    cont_pag = 0
    for rows in grouper(data, max_rows_per_page):
        cont_pag += 1
        c.drawImage("logo.jpg", 5, 750, width=300, height=75)
        rows = tuple(filter(bool, rows))
        #c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            #c.setFillColorRGB(0, 0, 1)
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
            c.line(30, 40, 550, 40)
        c.drawString(475, 20, "Pagina " + str(cont_pag))
        c.showPage()
    c.save()


data = [("NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROM.", "ESTADO")]
for i in range(1, 101):
    exams = [randint(0, 10) for _ in range(3)]
    avg = round(mean(exams), 2)
    state = "Aprobado" if avg >= 4 else "Desaprobado"
    data.append(("Alumno "+str(i), *exams, avg, state))
export_to_pdf(data)
