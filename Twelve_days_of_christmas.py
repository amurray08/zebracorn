from graphics import *
win = GraphWin("Karaoke",600,500)
win.setBackground("white")

aRectangle = Rectangle(Point(590,490), Point(10, 10))
aRectangle.setFill("Red")
aRectangle.draw(win)

w = Circle(Point(115, 115), 75)
w.setFill("Green")
w.draw(win)

w = Circle(Point(115, 115), 40)
w.setFill("Red")
w.draw(win)

w = Circle(Point(140, 170), 15)
w.setFill("Purple")
w.draw(win)

w = Circle(Point(80, 70), 15)
w.setFill("Purple")
w.draw(win)

w = Circle(Point(164, 80), 15)
w.setFill("Yellow")
w.draw(win)

w = Circle(Point(77, 163), 15)
w.setFill("Yellow")
w.draw(win)




c = Circle(Point(525, 450), 40)
c.setFill("white")
c.draw(win)

c = Circle(Point(525, 390), 35)
c.setFill("white")
c.draw(win)

c = Circle(Point(525, 330), 30)
c.setFill("white")
c.draw(win)

c = Circle(Point(515, 320), 3)
c.setFill("black")
c.draw(win)

c = Circle(Point(535, 320), 3)
c.setFill("black")
c.draw(win)

c = Circle(Point(525, 345), 3)
c.setFill("black")
c.draw(win)

c = Circle(Point(515, 340), 3)
c.setFill("black")
c.draw(win)

c = Circle(Point(535, 340), 3)
c.setFill("black")
c.draw(win)

c = Circle(Point(525, 370), 3)
c.setFill("black")
c.draw(win)

c = Circle(Point(525, 390), 3)
c.setFill("black")
c.draw(win)

c = Circle(Point(525, 410), 3)
c.setFill("black")
c.draw(win)



def name():
    aText = Text(Point(300,250), m)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
a = "Twelve drummers drumming"
b = "Eleven pipers piping"
c = "Ten lords a-leaping"
d = "Nine ladies dancing"
e = "Eight maids a-milking"
f = "Seven swans a-swimming"
g = "Six geese a-laying"
h = "Five golden rings"
i = "Four calling birds"
j = "Three french hens"
k = "Two turtle doves and"
l = "A partridge in a pear tree"
m = "The Twelve Days of Christmas"
def first():
    aText = Text(Point(300,250), l)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
def second():
    aText = Text(Point(300,250), k)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    first()
def third():
    aText = Text(Point(300,250), j)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    second()
def fourth():
    aText = Text(Point(300,250), i)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    third()
def fifth():
    aText = Text(Point(300,250), h)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    fourth()
def sixth():
    aText = Text(Point(300,250), g)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    fifth()
def seventh():
    aText = Text(Point(300,250), f)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    sixth()
def eigth():
    aText = Text(Point(300,250), e)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    seventh()
def ninth():
    aText = Text(Point(300,250), d)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    eigth()
def tenth():
    aText = Text(Point(300,250), c)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    ninth()
def eleventh():
    aText = Text(Point(300,250), b)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    tenth()
def twelfth():
    aText = Text(Point(300,250), a)
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
    eleventh()
def new_verse(verse: str):
    aText = Text(Point(300,250), "On the " + verse + " day of christmas \n my true love sent to me")
    aText.setSize(36)
    aText.draw(win)
    win.getMouse()
    aText.undraw()
def end():
    aText = Text(Point(300,250), "Happy Holidays")
    aText.setSize(36)
    aText.draw(win)

def main():
    name()
    new_verse("first")
    first()
    new_verse("second")
    second()
    new_verse("third")
    third()
    new_verse("fourth")
    fourth()
    new_verse("fifth")
    fifth()
    new_verse("sixth")
    sixth()
    new_verse("seventh")
    seventh()
    new_verse("eigth")
    eigth()
    new_verse("ninth")
    ninth()
    new_verse("tenth")
    tenth()
    new_verse("eleventh")
    eleventh()
    new_verse("twelfth")
    twelfth()
    end()
main()


    