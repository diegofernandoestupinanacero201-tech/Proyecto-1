# pgzero
WIDTH = 400
HEIGHT = 240
FPS = 30

background = Actor("mundomario1")
ma = Actor("m", (50, 190))
coopa = Actor("coopa", (400,200))



# Contador para la animación
contador = 0


def draw():
    background.draw()
    ma.draw()
    coopa.draw()


def update(dt):
    global contador


    if coopa.x <=0:
        coopa.x =230
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
    else:
        # Cuando no se mueve, vuelve al sprite quieto
        ma.image = "m"
        contador = 0
