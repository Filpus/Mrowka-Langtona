import tkinter
import sys
class Ant():
    def __init__(self, color,name, x,y):
        self.color = color
        self.name = name
        self.x = x
        self.y = y
        self.direction = 3 # 1 North, 2 East, 3 South, 0 West
    def move(self,board,size):
        if board[self.y][self.x] == 0:
            board[self.y][self.x] = self.color
            self.direction = (self.direction + 3) % 4
        else:
            board[self.y][self.x] = 0
            self.direction = (self.direction + 1) % 4

        if self.direction == 1:
            self.y -= 1
        elif self.direction == 2:
            self.x += 1
        elif self.direction == 3:
            self.y += 1
        else:
            self.x -= 1

        if self.x == -1:
            self.x = size - 1
        if self.x == size:
            self.x = 0

        if self.y == -1:
            self.y = size - 1
        if self.y == size:
            self.y = 0

def redraw(window_size, size, canvas, board):
    s = window_size / size
    canvas.delete("all")
    for y, row in enumerate(board):
        for x, field in enumerate(row):
            if field != 0:
                color = field
                canvas.create_rectangle(
                    s * x, s * y, s + (s * x), s + (s * y), fill=color, outline=color
                )
    canvas.update()




15





def main():
    window_size = int(input("Entet the size of the window: "))
    size = int(input("Enter the size of the board: "))
    board = []
    for i in range(size):
        y = []
        for j in range(size):
            y.append(0)
        board.append(y)
    background = input("Enter the background of the board: ")
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=window_size, height=window_size, bg=background)
    canvas.pack()
    a = int(input("How many ant do you want creat? "))
    anthill = []
    for i in range(a):
        name = input("Enter the ant name: ")
        color = input("Enter the ant color: ")
        x = int(input("Enter the starting x: "))
        y = int(input("Enter the starting y: "))
        test = Ant(color,name,x,y)
        anthill.append(test)
    print(anthill)
    f = -1
    while f <0:
        for i in range(a):
            anthill[i].move(board,size)
        redraw(window_size,size,canvas,board)

main()
