# pgzero
WIDTH = 400
HEIGHT = 240
FPS = 30

background = Actor("mundomario1")
ma = Actor("m", (50, 195))
coopa = Actor("coopa", (400,200))
cubo = Actor("cubo", (265,153))
cubo2 =Actor("cubo",(345,153))
cubo3 =Actor("cubo",(375,153))
cubo4 =Actor("cubo",(360,88))


contador = 0
mode = "game"

def draw():
    if mode == "game":
        background.draw()
        ma.draw()
        coopa.draw()
        cubo.draw()
        cubo2.draw()
        cubo3.draw()
        cubo4.draw()
    elif mode == "end":
       screen.fill ("black")
       screen.draw.text("GAME OVER",pos=(100,100),color="white",fontsize=30)


def update(dt):
    global contador,mode


    if coopa.x <=0:
        coopa.x =400
    else:
        coopa.x -=1


    if keyboard.right:
        ma.x += 5

        contador += 1

        if contador >= 5:
            contador = 0

            if ma.image == "mario1":
                ma.image = "mario2"
            else:
                ma.image = "mario1"
    elif keyboard.left:
        ma.x -= 5
        contador += 1

        if contador >= 5:
            contador = 0

            if ma.image == "mario1left":
                ma.image = "mario2left"
            else:
                ma.image = "mario1left"
    else:
        # Cuando no se mueve, vuelve al sprite quieto
        ma.image = "m"
        contador = 0

    if ma.colliderect(coopa):
        mode = "end"
