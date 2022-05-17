import time
import os
import pprint
import tkinter

def redraw(window_size, size, canvas, colors, board):
    s = window_size / size
    canvas.delete("all")
    for y, row in enumerate(board):
        for x, field in enumerate(row):
            if field == "Cz":
                color = colors
                canvas.create_rectangle(
                    s * x, s * y, s + (s * x), s + (s * y), fill=color, outline=color
                )
    canvas.update()

plansza = []
rozmiar = 300
for i in range(rozmiar):
    y = []
    for j in range(rozmiar):
        y.append("B")
    plansza.append(y)

root = tkinter.Tk()
rozmiar_okna = 200
canvas = tkinter.Canvas(root, width=rozmiar_okna, height=rozmiar_okna,bg = "black")
canvas.pack()




mrówka = {
    'x': 25,
    'y': 25,
    'kierunek': 3   # 1 Góra, 2 Prawo, 3 Dół, 4 Góra
}

f = 0


while f > -1:


    if plansza[mrówka['y']][mrówka['x']] == "B":
        mrówka['kierunek'] -= 1
        if mrówka['kierunek'] == 0:
            mrówka['kierunek'] += 4
        plansza[mrówka['y']][mrówka['x']] = "Cz"
        if mrówka['kierunek'] == 1:
            mrówka['y'] += 1
        elif mrówka['kierunek'] == 2:
            mrówka['x'] += 1
        elif mrówka['kierunek'] == 3:
            mrówka['y'] -= 1
        elif mrówka['kierunek'] == 4:
            mrówka['x'] -= 1
    elif plansza[mrówka['y']][mrówka['x']] == "Cz":
        mrówka['kierunek'] += 1
        if mrówka['kierunek'] == 5:
            mrówka['kierunek'] -= 4
        plansza[mrówka['y']][mrówka['x']] = "B"
        if mrówka['kierunek'] == 1:
            mrówka['y'] += 1
        elif mrówka['kierunek'] == 2:
            mrówka['x'] += 1
        elif mrówka['kierunek'] == 3:
            mrówka['y'] -= 1
        elif mrówka['kierunek'] == 4:
            mrówka['x'] -= 1
    if mrówka['x'] == rozmiar:
        mrówka['x'] = 0
    elif mrówka['y'] == rozmiar:
        mrówka['y'] = 0
    elif mrówka['x'] == -1:
        mrówka['x'] = rozmiar-1
    elif mrówka['y'] == -1:
        mrówka['y'] = rozmiar -1

    redraw(rozmiar_okna,rozmiar,canvas,"Red",plansza)


