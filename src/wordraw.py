import turtle



def main():
    code_map = {'A':'r 34','B':'c 48','C':'f 32','D':'f 126','E':'r 123','F':'c 52','G':'d 30','H':'b 68','I':'d 66','J':'d 57','K':'d 33','L':'f 79','M':'d 87','N':'l 95','O':'c 145','P':'b 117','Q':'r 106','R':'f 110','S':'f 146','T':'f 43','U':'l 105','V':'r 66','W':'b 52','X':'l 115','Y':'c 97','Z':'c 101','a':'b 47','b':'r 26','c':'c 63','d':'f 108','e':'d 53','f':'d 75','g':'c 71','h':'f 46','i':'f 82','j':'b 112','k':'l 60','l':'d 127','m':'c 145','n':'b 46','o':'r 108','p':'b 97','q':'l 70','r':'c 80','s':'f 105','t':'c 100','u':'r 66','v':'f 69','w':'r 126','x':'c 66','y':'b 32','z':'c 131', '0': 'b 131', '1': 'f 147', '2': 'r 19', '3': 'd 90', '4': 'c 89', '5': 'l 27', '6': 'r 45', '7': 'r 109', '8': 'b 65', '9': 'd 121', ' ': 'd 25'}
    screen = turtle.Screen()
    screen.bgcolor('white')
    pen = turtle.Turtle()
    pen.speed(5)
    message = input("Message: ")
    if message == 'cat':
        cat(pen)
    elif message == 'star':
        star(pen)
    elif message == 'flower':
        flower(pen)
    else:
        last_char_space = True
        for character in message:
            if(last_char_space):
                format(character, pen)
            last_char_space = False
            if character == ' ':
                last_char_space = True
            clist = code_map[character].split(' ')
            
            if clist[0] == 'f':
                pen.forward(int(clist[1]))
            elif clist[0] == 'l':
                pen.left(int(clist[1]))
            elif clist[0] == 'c':
                pen.circle(int(clist[1]))
            elif clist[0] == 'd':
                pen.dot(int(clist[1]))
            elif clist[0] == 'b':
                pen.backward(int(clist[1]))
            elif clist[0] == 'r':
                pen.right(int(clist[1]))
            
    turtle.mainloop()
def format(character, pen):
    format_map = {'A':'skyblue 4','B':'navy 2','C':'skyblue 4','D':'cyan 12','E':'red 3','F':'orange 7','G':'blue 8','H':'gold 9','I':'purple 11','J':'yellow 6','K':'gray 2','L':'yellow 8','M':'skyblue 10','N':'gray 3','O':'turquoise 15','P':'orange 7','Q':'cyan 2','R':'magenta 9','S':'magenta 10','T':'cyan 5','U':'blue 1','V':'magenta 2','W':'cyan 3','X':'gray 9','Y':'purple 10','Z':'lightgreen 6','a':'magenta 10','b':'gray 1','c':'blue 7','d':'chocolate 7','e':'skyblue 8','f':'lightgreen 5','g':'red 2','h':'black 1','i':'turquoise 8','j':'turquoise 1','k':'green 3','l':'magenta 7','m':'orange 15','n':'orange 8','o':'chocolate 6','p':'lightgreen 3','q':'red 9','r':'green 2','s':'white 14','t':'darkgreen 1','u':'black 2','v':'red 7','w':'orange 3','x':'darkgreen 1','y':'magenta 2','z':'red 7','0':'turquoise 6','1':'purple 1','2':'orange 1','3':'brown 7','4':'white 6','5':'lightgreen 4','6':'gold 4','7':'darkgreen 8','8':'orange 3','9':'cyan 2'}
    flist = format_map[character].split(' ')
    pen.pencolor(flist[0])
    pen.width(int(flist[1]))

def cat(pen):
    pen.pencolor('orange')
    pen.width(25)
    pen.dot(300)
    pen.up()
    pen.goto(100,100)
    pen.down()
    pen.left(108)
    pen.forward(100)
    pen.left(148)
    pen.forward(100)
    pen.right(80)
    pen.forward(130)
    pen.right(108)
    pen.forward(100)
    pen.right(148)
    pen.forward(100)
    pen.home()
    pen.pencolor('yellow')
    pen.dot(100)
    pen.left(90)
    pen.forward(30)
    pen.pencolor('violet')
    pen.dot(50)
    pen.up()
    pen.pencolor('white')
    pen.forward(30)
    pen.right(90)
    pen.forward(30)
    pen.down()
    pen.dot(70)
    pen.pencolor('blue')
    pen.dot(50)
    pen.up()
    pen.backward(60)
    pen.pencolor('white')
    pen.down()
    pen.dot(70)
    pen.pencolor('blue')
    pen.dot(50)
    pen.up()
    pen.goto(-10, -10)
    pen.width(5)
    pen.down()
    pen.forward(10)
    pen.circle(30, 40)
    pen.right(40)
    pen.up()
    pen.goto(100, 0)
    pen.down()
    pen.forward(100)
    pen.up()
    pen.goto(100, -20)
    pen.down()
    pen.forward(100)
    pen.up()
    pen.goto(-100, 0)
    pen.down()
    pen.left(180)
    pen.forward(100)
    pen.up()
    pen.goto(-100, -20)
    pen.down()
    pen.forward(100)   

def star(pen):
    pen.width(3)
    pen.color('gold')
    pen.begin_fill()

    for steps in range(36):
        pen.forward(200)
        pen.left(170)

    pen.end_fill()        

def flower(pen):
    pen.width(5)
    pen.color('violet')
    pen.begin_fill()
    for steps in range(9):
        pen.circle(30)
        pen.forward(150)
        pen.left(160)
    pen.end_fill()


if __name__ == "__main__":
    main()