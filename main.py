# pgzero
WIDTH = 400
HEIGHT = 240
FPS = 30

background = Actor("mundomario1")
ma = Actor("m", (50, 195))
coopa = Actor("coopa", (400,200))
coopa_estado = "normal"
tiempo_coopa = 0
cubo = Actor("cubo", (265,153))
cubo2 =Actor("cubo",(345,153))
cubo3 =Actor("cubo",(375,153))
cubo4 =Actor("cubo",(360,88))
hongo =Actor("hongo")
moneda = Actor("moneda")
moneda2 =Actor("moneda")
moneda3 =Actor("moneda")
moneda4 =Actor("moneda")
moneda.pos = cubo.pos
moneda2.pos = cubo2.pos
moneda3.pos = cubo4.pos
hongo.pos = cubo3.pos
camera_x =0
posicion_camara = WIDTH / 2
cubos = [cubo, cubo2, cubo3, cubo4]
golpes_cubo = [
    {"actor": cubo, "posicion": cubo.y, "velocidad": 0, "activo": False}
    for cubo in cubos
]
suelo_ma = 195
velocidad_salto = -320
gravedad = 900
velocidad_ma_y = 0


contador = 0
mode = "game"

def draw():
    if mode == "game":
        background.draw()
        ma.draw()
        coopa.draw()
        moneda.draw()
        moneda2.draw()
        moneda3.draw()
        moneda4.draw()
        cubo.draw()
        cubo2.draw()
        hongo.draw()
        cubo3.draw()
        cubo4.draw()

    elif mode == "end":
       screen.fill ("black")
       screen.draw.text("GAME OVER",pos=(100,100),color="white",fontsize=30)


def update(dt):
    global contador,mode,velocidad_ma_y,camera_x,posicion_camara
    global coopa_estado,tiempo_coopa

    parte_superior_anterior = ma.top
    parte_inferior_anterior = ma.bottom

    if (keyboard.space or keyboard.up) and ma.y >= suelo_ma:
        velocidad_ma_y = velocidad_salto

    velocidad_ma_y += gravedad * dt
    ma.y += velocidad_ma_y * dt

    if ma.y >= suelo_ma:
        ma.y = suelo_ma
        velocidad_ma_y = 0

    for golpe in golpes_cubo:
        if golpe["activo"]:
            golpe["velocidad"] += gravedad * dt
            golpe["actor"].y += golpe["velocidad"] * dt
            if golpe["actor"].y >= golpe["posicion"]:
                golpe["actor"].y = golpe["posicion"]
                golpe["velocidad"] = 0
                golpe["activo"] = False


    if coopa_estado == "normal":
        if coopa.x <=0:
            coopa.x =400
        else:
            coopa.x -=1
    else:
        tiempo_coopa -= dt
        if coopa_estado == "aplastado" and tiempo_coopa <= 0:
            coopa.x = -1000
            coopa_estado = "esperando"
            tiempo_coopa = 1
        elif coopa_estado == "esperando" and tiempo_coopa <= 0:
            coopa.image = "coopa"
            coopa.x = 400
            coopa_estado = "normal"


    if keyboard.right:
        ma.x += 3
        limite_camara = background.width - WIDTH
        if ma.x > posicion_camara and camera_x < limite_camara:
            desplazamiento = min(ma.x - posicion_camara, limite_camara - camera_x)
            ma.x -= desplazamiento
            camera_x += desplazamiento
            background.x -= desplazamiento
            coopa.x -= desplazamiento
            moneda.x -=desplazamiento
            hongo.x -=desplazamiento
            moneda2.x -=desplazamiento
            moneda3.x -=desplazamiento
            for cubo in cubos:
                cubo.x -= desplazamiento

        if camera_x >= limite_camara:
            ma.x = min(ma.x, WIDTH - ma.width / 2)

        contador += 1

        if contador >= 5:
            contador = 0

            if ma.image == "mario1":
                ma.image = "mario2"
            else:
                ma.image = "mario1"
    elif keyboard.left:
        ma.x -= 3
        if ma.x < posicion_camara and camera_x > 0:
            desplazamiento = min(posicion_camara - ma.x, camera_x)
            ma.x += desplazamiento
            camera_x -= desplazamiento
            background.x += desplazamiento
            coopa.x += desplazamiento
            moneda.x +=desplazamiento
            hongo.x +=desplazamiento
            moneda2.x +=desplazamiento
            moneda3.x +=desplazamiento
            for cubo in cubos:
                cubo.x += desplazamiento

        if camera_x <= 0:
            ma.x = max(ma.x, ma.width / 2)
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

    if velocidad_ma_y < 0:
        for golpe in golpes_cubo:
            actor_cubo = golpe["actor"]
            if (parte_superior_anterior >= actor_cubo.bottom
                    and ma.top <= actor_cubo.bottom
                    and ma.colliderect(actor_cubo)):
                ma.y = actor_cubo.bottom + ma.height / 2
                velocidad_ma_y = 0
                golpe["velocidad"] = -190
                golpe["activo"] = True
                break

    if coopa_estado == "normal" and ma.colliderect(coopa):
        if (velocidad_ma_y > 0
                and parte_inferior_anterior <= coopa.top
                and ma.bottom >= coopa.top):
            ma.bottom = coopa.top
            velocidad_ma_y = velocidad_salto
            coopa.image = "coopaes"
            coopa_estado = "aplastado"
            tiempo_coopa = 0.35
        else:
            mode = "end"
