from turtle import *
from datetime import *

#写星期几
def Week(t): week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
return week[t.weekday()]
#写日期
def Date(t):
        y = t.year
        m = t.month
        d = t.day
        return "%s %d %d" % (y, m, d) #抬起画笔，向前运动一段距离放下
def Skip(step):
        penup()
        forward(step)
        pendown()

#注册turtle的形状，建立表针turtle
def mkHand(name,length):
        reset()
        Skip(-length*0.1)
        #运动
        begin_poly()#开始记录多边形的顶点 )。#返回记录的多边形
        # 前进
        forward(length*1.1)
        # 结束记录多边形的顶点 且将一第一个顶点相连
        end_poly()

        handForm = get_poly()

        register_shape(name, handForm)

def Init():
        global secHand,minHand,hurHand,printer #秒，分，时,打印#模型，设置为向上，向北，顺时针方向模式
        mode("logo")
        mkHand("secHand", 135)
        mkHand("minHand", 120)
        mkHand("hurHand", 85)
        secHand = Turtle()  # 画秒的
        secHand.shape("secHand")
        minHand = Turtle()
        #画分的
        minHand.shape("minHand")
        hurHand = Turtle()
        hurHand.shape("hurHand")
        for hand in secHand,minHand,hurHand:
                hand.shapesize(1,1,3)
                hand.speed(0)
                #建立输出文字的
                Tutle printer = Turtle()
                printer.hideturtle()
                printer.penup()
def SetupClock(radius): #建立表的外框
        reset()
        pensize(7)
        for i in range(60):
                Skip(radius)
        if i % 5 == 0:
               forward(20)
        Skip(-radius - 20)
        Skip(radius + 20)
        if i == 0:
        write(int(12), align="center", font=("Courier", 14, "bold"))
        elif i == 30:
        Skip(25)
        write(int(i / 5), align="center", font=("Courier", 14, "bold"))
        Skip(-25) elif (i == 25 or i == 35): Skip(20)
        write(int(i / 5), align="center", font=("Courier", 14, "bold"))
        Skip(-20) else: write(int(i / 5), align="center", font=("Courier", 14, "bold"))
        Skip(-radius - 20)
        else: dot(5)
        Skip(-radius)
        right(6)

#Tick()绘制日期的动态显示
def Tick():
        t = datetime.today()
        second = t.second + t.microsecond * 0.000001
        minute = t.minute + second / 60.0
        hour = t.hour + minute / 60.0
        secHand.setheading(6 * second)
        minHand.setheading(6 * minute)
        hurHand.setheading(30 * hour)
        tracer(False)
        printer.forward(65)
        printer.write(Week(t), align="center",font=("Courier", 14, "bold"))
        printer.back(130)
        printer.write(Date(t), align="center",font=("Courier", 14, "bold"))
        printer.home()
        tracer(True) # 100ms后继续调用
        tick ontimer(Tick, 100)

def main():

tracer(False)# 打开/关闭龟动画，并为更新图纸设置延迟。
Init()#初始化
SetupClock(160)
tracer(True)
Tick()

if __name__=="__main__":

main()
mainloop()#启动事件循环不然画完就关闭了