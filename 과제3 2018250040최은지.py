from BMP_Packages.BMEgraphics import *

canvas = Canvas(600, 600)
canvas.setBackgroundColor("light blue")

machine = Layer()
tire1 = Rectangle(150, 250, Point(80,60))
tire1.setFillColor('skyblue')
machine.add(tire1)
tire2 = Rectangle(200, 60, Point(100,260))
tire2.setFillColor('black')
machine.add(tire2)
body = Rectangle(210, 400, Point(100, 100))
body.setFillColor('red')
body.setDepth(60)
machine.add(body)
line1 = Rectangle(140, 10, Point(80, 60))
line1.setFillColor('red')
machine.add(line1)
line2 = Rectangle(140, 10, Point(80, 0))
line2.setFillColor('red')
machine.add(line2)
line3 = Rectangle(140, 10, Point(80, 165))
line3.setFillColor('red')
machine.add(line3)
line4 = Rectangle(40, 10, Point(180, 70))
line4.setFillColor('red')
machine.add(line4)
coinin = Rectangle(40, 40, Point(180,100))
coinin.setFillColor('black')
machine.add(coinin)

machine2 = Layer()
body2 = Rectangle(150, 43, Point(130,357))
body2.setFillColor('red')
machine2.add(body2)


class Coin(object):
    def __init__(self, coin1=None, coin2 = None):
        layer = Layer()
        self.layer = layer
        self.coin1 = coin1
        self.coin2 = coin2

def make_coin():
    layer = Layer()
    coin1 = Circle(18)
    coin1.setFillColor('yellow')
    layer.add(coin1)
    coin2 = Circle(16)
    coin2.setFillColor('yellow')
    layer.add(coin2)

    co = Coin()
    co.layer = layer
    co.coin1 = coin1
    co.coin2 = coin2
    return co

def move(self, dx, dy):
    self.layer.move(dx, dy)

class Drink(object):

    def __init__(self, body=None, bottom = None, top = None, cap = None, extra = None):
        layer = Layer()
        self.layer = layer
        self.body = body
        self.bottom = bottom
        self.top = top
        self.cap = cap
        self.extra = extra



def make_drink(bottle = False):
    layer = Layer()
    if bottle:
        body = Rectangle(30,50)
        body.setFillColor('blue')
        label = Rectangle(10,40)
        label.setFillColor('white')
        label.move(-5,5)
        top = Ellipse(30,10)
        top.setFillColor('blue')
        top.move(0,-25)
        bottom = Ellipse(30,10)
        bottom.setFillColor('blue')
        bottom.setDepth(60)
        bottom.move(0,25)
        extra = Rectangle(10,35)
        extra.setFillColor('blue')
        extra.move(0,-42)
        cap = Ellipse(12,8)
        cap.setFillColor('white')
        cap.move(0,-57)
    else:
        body = Rectangle(30,50)
        body.setFillColor('green')
        label = Rectangle(10,40)
        label.setFillColor('white')
        label.move(-5,5)
        extra = Rectangle(5,20)
        extra.setFillColor('gray')
        extra.move(-5,5)
        top = Ellipse(30,10)
        top.setFillColor('gray')
        top.move(0,-25)
        bottom = Ellipse(30,10)
        bottom.setFillColor('green')
        bottom.move(0,25)
        cap = Ellipse(10,5)
        cap.setFillColor('gray')
        cap.move(-2,-25)
    layer.add(body)
    layer.add(label)
    layer.add(top)
    layer.add(bottom)
    layer.add(extra)
    layer.add(cap)

    dr = Drink()
    dr.layer = layer
    dr.body = body
    dr.label = label
    dr.top = top
    dr.bottom = bottom
    dr.extra = extra
    dr.cap = cap
    return dr


foot = Layer()
leg = Rectangle(30,80, Point(350, 370))
leg.setFillColor('yellow')
foot.add(leg)
foot1 = Ellipse(70,30, Point(330,410))
foot1.setFillColor('yellow')
foot.add(foot1)
foot2 = Rectangle(70,20,Point(330, 423))
foot2.setFillColor('black')
foot.add(foot2)
foot3 = Rectangle(10,20, Point(310, 405))
foot3.setFillColor('black')
foot.add(foot3)



bottle1 = make_drink(True)
bottle2 = make_drink(True)
bottle3 = make_drink(True)
can0 = make_drink()
can1 = make_drink()
can2 = make_drink()
can3 = make_drink()
can4 = make_drink()
can5 = make_drink()
bottle2.layer.move(50,0)
bottle3.layer.move(100,0)
can0.layer.move(80,115)
can1.layer.move(0,-100)
can2.layer.move(50,-100)
can3.layer.move(100,-100)
can4.layer.move(50,-165)
can5.layer.move(100,-165)

vending1= Layer()
vending2 = Layer()
vending3= Layer()
vending2.add(can1.layer)
vending2.add(can2.layer)
vending2.add(can3.layer)
vending1.add(can4.layer)
vending1.add(can5.layer)
vending3.add(bottle1.layer)
vending3.add(bottle2.layer)
vending3.add(bottle3.layer)
vending1.move(80,280)
vending2.move(80,280)
vending3.move(80,280)
#coin = Layer()
coin11 = make_coin()
coin11.layer.move(300,250)
#coin.add(coin11.layer)
machine.move(50, 150)




canvas.add(machine)
canvas.add(can0.layer)
canvas.add(vending1)
canvas.add(vending2)
canvas.add(vending3)
canvas.add(coin11.layer)
canvas.add(foot)
canvas.add(machine2)

button1 = Layer()
button11 = Rectangle(200, 100)
button12 = Text("마우스로 클릭하여 동전을 넣어주세요", 15)
button1.add(button11)
button1.add(button12)
button1.move(450, 100)

canvas.add(button1)

button2 = Layer()
button21 = Rectangle(200, 100)
button22 = Text("동전이 없을 시 'q'를 눌러 발로 차주세요", 14)
button2.add(button21)
button2.add(button22)
button2.move(450, 200)

canvas.add(button2)

def click():
    e = canvas.wait()
    d = e.getDescription()
    if d == 'mouse click':
        for i in range(35):
            coin11.layer.move(-2, 0)
        for i in range(100):
            can0.layer.move(0, 3)


def keyboard_input():
    P = input("q를 눌러 발로 자판기를 차주세요")
    if P == 'q':
        for i in range(20):
            foot.move(-2, -1)
            foot.rotate(0.5)
        for i in range(20):
            foot.move(2, 1)
        foot.rotate(-0.5)
        for i in range(20):
            foot.move(-2, -1)
            foot.rotate(0.5)
        for i in range(20):
            foot.move(2, 1)
            foot.rotate(-0.5)

        for i in range(6):
            vending1.move(0, 48)
            vending1.move(0.8, 0)
            vending2.move(0, 40)
            vending2.move(1, 0)
            vending3.move(0, 28)
            vending3.move(1.6, 0)


click()
keyboard_input()