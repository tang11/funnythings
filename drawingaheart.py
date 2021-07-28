from turtle import *


def curvemove():  # 这个函数是为了绘制爱心上方的曲线
        for i in range(200):
                right(1)
                fd(1)


pensize(2)  # 调整画笔粗细
speed(100)  # 调节画笔速度
color('red', 'pink')  # 画笔颜色及填充颜色
begin_fill()  # 开始填充
left(140)
fd(111.65)
curvemove()  # 调用函数
left(120)
curvemove()  # 调用函数
fd(111.65)
end_fill()  # 结束填充
hideturtle()  # 隐藏画笔
done()
