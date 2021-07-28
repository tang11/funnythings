from turtle import *


def draw_begin():
        n = 5


for i in range(1, 10):
        for j in [90, 180, -90, 0]:
                seth(j)
        fd(n)
        n += 5

        if __name__ == "__main__":
                draw_begin()
        hideturtle()
        done()
