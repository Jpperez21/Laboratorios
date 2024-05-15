#PROYECTO
#JUAN PABLO 

#Se importa turtle
import turtle
#Se define el cuadro, la narrativa y los dibujos 
def Cuadro():
    #Elaboración del recuadro para el cuento
    turtle.clearscreen()
    cuadro=turtle.Turtle()
    cuadro.teleport (-350,-300)
    cuadro.speed(0)
    cuadro.forward (700)
    cuadro.left(90)
    cuadro.forward (600)
    cuadro.left(90)
    cuadro.forward(700)
    cuadro.left(90)
    cuadro.forward(600)
    cuadro.back(200)
    cuadro.left(90)
    cuadro.forward(700)
    cuadro.left(90)
    cuadro.forward(350)
    cuadro.left(90)
    cuadro.forward(700)
    cuadro.hideturtle()

    cuadro_color=turtle.Turtle()
    cuadro_color.speed(0)

    cuadro_color.teleport(-350,250)
    cuadro_color.color("black",color1)
    cuadro_color.begin_fill()
    cuadro_color.forward(700) 
    cuadro_color.right(90)
    cuadro_color.forward(350) 
    cuadro_color.right(90)
    cuadro_color.forward(700) 
    cuadro_color.right(90)
    cuadro_color.forward(350) 
    cuadro_color.right(90)
    cuadro_color.end_fill()
    cuadro_color.hideturtle()

def Camara():
    camara = turtle.Turtle()
    camara.speed(0)

    #Cuerpo de la cámara
    camara.color("CadetBlue","CadetBlue")
    camara.begin_fill()
    camara.teleport(-150,160)
    camara.forward(300) 
    camara.right(90)
    camara.forward(200) 
    camara.right(90)
    camara.forward(300) 
    camara.right(90)
    camara.forward(200) 
    camara.right(90)
    camara.end_fill()

    camara.color("FireBrick","FireBrick")
    camara.begin_fill()

    camara.teleport(-150,160)
    camara.forward(300) 
    camara.right(90)
    camara.forward(50) 
    camara.right(90)
    camara.forward(300) 
    camara.right(90)
    camara.forward(50) 
    camara.right(90)
    camara.end_fill()

    camara.color("lightgray","lightgray")
    camara.begin_fill()
    camara.teleport(10,110)
    for i in range(8):
        camara.forward(50)
        camara.right(360/8)
    camara.end_fill()

    camara.teleport(35,10)
    camara.color("black","black")
    camara.begin_fill()
    camara.circle(40)
    camara.end_fill()

    camara.teleport(110,120)
    camara.color("SlateGray","SlateGray")
    camara.begin_fill()
    camara.circle(17)
    camara.end_fill()

    camara.teleport(-130,160)
    camara.color("CadetBlue","CadetBlue")
    camara.begin_fill()
    for i in range(4):
        camara.forward(30) 
        camara.left(90)
    camara.end_fill()

    camara.color("Khaki","Khaki")
    camara.begin_fill()
    camara.teleport(-120,145)
    for i in range(3):
        camara.forward(30)
        camara.right(120)
    camara.teleport(-80,145)
    for i in range(3):
        camara.forward(30)
        camara.right(120)
    camara.end_fill()

    camara.hideturtle()

def Leon():
    leon = turtle.Turtle()
    leon.speed(0)
    #Cola
    leon.pencolor("goldenrod")
    leon.pensize(6)
    leon.teleport(30,-5)
    leon.left(45)
    leon.forward(55)

    leon.pencolor("black")
    leon.pensize(0)
    leon.right(45)

    leon.teleport(70,60)
    leon.color("sienna","sienna")
    leon.begin_fill()
    for i in range(7):
        leon.forward(15)
        leon.right(360/7)
    leon.end_fill()

    #Cuerpo
    leon.teleport(-75,-40)
    leon.color("goldenrod","goldenrod")
    leon.begin_fill()
    for i in range(3):
        leon.forward(150)
        leon.left(120)
    leon.end_fill()

    #Dibujo melena
    leon.teleport(0,50)
    leon.color("sienna","sienna")
    leon.begin_fill()
    leon.circle(75) 
    leon.end_fill()

    #Dibujo cabaeza y orejas
    leon.color("goldenrod","goldenrod")
    leon.teleport(0,80)
    leon.begin_fill()
    leon.circle(45)
    leon.teleport(30,150)
    leon.circle(15) 
    leon.teleport(-30,150)
    leon.circle(15) 
    leon.end_fill()

    #Dibujo Nariz y ojos
    leon.teleport(-7.5,120)
    leon.color("black","black")
    leon.begin_fill()
    for i in range(3):
        leon.forward(15)
        leon.right(120)

    leon.teleport(15,130)
    leon.circle(7) 
    leon.teleport(-15,130)
    leon.circle(7)
    leon.end_fill()

    #Pasos para las patas
    leon.color("sienna","sienna")
    leon.teleport(20,-40)
    leon.begin_fill()
    for i in range(4):
        leon.forward(25) 
        leon.left(90)
    leon.teleport(-40,-40)
    for i in range(4):
        leon.forward(25) 
        leon.left(90)
    leon.end_fill()

    leon.hideturtle()

def Mono():
    mono = turtle.Turtle()
    mono.speed(0)

    #Dibujo cabeza
    mono.color("SaddleBrown","SaddleBrown")
    mono.begin_fill()
    mono.teleport(-45,120)
    for i in range(4):
        mono.forward(90) 
        mono.left(90)

    #Orejas
    mono.teleport(50,150)
    mono.circle(20)
    mono.teleport(-50,150)
    mono.circle(20)

    #Cuerpo mono
    mono.teleport(-45,0)
    for i in range(4):
        mono.forward(90) 
        mono.left(90)

    #cuello
    mono.teleport(-10,100)
    for i in range(4):
        mono.forward(20) 
        mono.left(90)

    #brazos
    mono.teleport(-125,100)
    mono.forward(250) 
    mono.right(90)
    mono.forward(25) 
    mono.right(90)
    mono.forward(250) 
    mono.right(90)
    mono.forward(25) 
    mono.right(90)

    #Pierna Izquierda
    mono.teleport(-45,10)
    mono.forward(25) 
    mono.right(90)
    mono.forward(80) 
    mono.right(90)
    mono.forward(25) 
    mono.right(90)
    mono.forward(80) 
    mono.right(90)

    #Pierna derecha
    mono.teleport(20,10)
    mono.forward(25) 
    mono.right(90)
    mono.forward(80) 
    mono.right(90)
    mono.forward(25) 
    mono.right(90)
    mono.forward(80) 
    mono.right(90)
    mono.end_fill()

    mono.color("BurlyWood","Bisque")
    mono.begin_fill()
    mono.teleport(-125,75)
    for i in range(4):
        mono.forward(25) 
        mono.left(90)
    mono.teleport(100,75)
    for i in range(4):
        mono.forward(25) 
        mono.left(90)
    mono.teleport(-45,-70)
    for i in range(4):
        mono.forward(25) 
        mono.left(90)
    mono.teleport(20,-70)
    for i in range(4):
        mono.forward(25) 
        mono.left(90)

    mono.teleport(-45,160)
    mono.forward(90) 
    mono.right(90)
    mono.forward(45) 
    mono.right(90)
    mono.forward(90) 
    mono.right(90)
    mono.forward(45) 
    mono.right(90)

    mono.teleport(-15,85)
    for i in range(8):
        mono.forward(30)
        mono.right(360/8)
    mono.end_fill()

    #Ojos
    mono.color("black","black")
    mono.begin_fill()
    mono.teleport(-15,175)
    mono.circle(6)
    mono.teleport(15,175)
    mono.circle(6)


    #nariz
    mono.teleport(6,150)
    mono.circle(2)
    mono.teleport(-6,150)
    mono.circle(2)
    mono.end_fill()

    mono.hideturtle()

def Elefante():
    #Cuerpo
    elefante = turtle.Turtle()
    elefante.speed(0)
    elefante.teleport(30,0)
    elefante.color("Dimgray","silver")
    elefante.begin_fill()
    for i in range(4):
        elefante.forward(150) 
        elefante.left(90)

    #Pasos patas
    elefante.teleport(30,0)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)

    elefante.teleport(55,0)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)

    elefante.teleport(155,0)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)

    elefante.teleport(130,0)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)
    elefante.forward(25) 
    elefante.right(90)
    elefante.forward(60) 
    elefante.right(90)

    #Pasos cabeza y trompa
    elefante.teleport(-20,60)
    elefante.circle(50) 
    elefante.teleport(-55,30)
    elefante.circle(20) 
    elefante.teleport(-30,10)
    elefante.circle(15)
    elefante.teleport(-40,-10)
    elefante.circle(10)
    elefante.teleport(-55,-15)
    elefante.circle(8)
    elefante.teleport(-70,-10)
    elefante.circle(7)
    elefante.teleport(-83,-5)
    elefante.circle(6)

    #Pasos cola
    elefante.teleport(180,150)
    elefante.left(30) 
    elefante.forward(50) 
    elefante.right(120) 
    elefante.forward(50)
    elefante.right(120) 
    elefante.forward(50) 

    #Pasos oreja
    elefante.teleport(-5,95)
    elefante.color("Dimgray","Dimgray")
    elefante.begin_fill()
    for i in range(5):
        
        elefante.color()
        elefante.forward(30)
        elefante.right(360/5)
    elefante.end_fill()

    #Pasos Ojo
    elefante.teleport(-40,100)
    elefante.color("black","black")
    elefante.begin_fill()
    elefante.circle(6)
    elefante.end_fill()

    elefante.hideturtle()
    
def Jirafa():
    jirafa = turtle.Turtle()
    jirafa.speed(0)

    #Cuerpo
    jirafa.color("goldenrod","goldenrod")
    jirafa.begin_fill()

    jirafa.teleport(-50,70)
    jirafa.forward(100) 
    jirafa.right(90)
    jirafa.forward(60) 
    jirafa.right(90)
    jirafa.forward(100) 
    jirafa.right(90)
    jirafa.forward(60) 
    jirafa.right(90)

    #Dibujo patas
    jirafa.teleport(-50,10)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(60) 
    jirafa.right(90)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(60) 
    jirafa.right(90)

    jirafa.teleport(30,10)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(60) 
    jirafa.right(90)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(60) 
    jirafa.right(90)

    #Dibujo para dibujar el cuello
    jirafa.teleport(-50,180)
    jirafa.forward(30) 
    jirafa.right(90)
    jirafa.forward(110) 
    jirafa.right(90)
    jirafa.forward(30) 
    jirafa.right(90)
    jirafa.forward(110) 
    jirafa.right(90)

    #Pasos para dibujar los cuernos
    jirafa.teleport(-45,205)
    jirafa.forward(5) 
    jirafa.right(90)
    jirafa.forward(25) 
    jirafa.right(90)
    jirafa.forward(5) 
    jirafa.right(90)
    jirafa.forward(25) 
    jirafa.right(90)

    jirafa.teleport(-30,205)
    jirafa.forward(5) 
    jirafa.right(90)
    jirafa.forward(25) 
    jirafa.right(90)
    jirafa.forward(5) 
    jirafa.right(90)
    jirafa.forward(25) 
    jirafa.right(90)


    #Pasos para rezalir la cabeza
    jirafa.teleport(-93,155)
    jirafa.left(30) 
    jirafa.forward(50) 
    jirafa.right(120) 
    jirafa.forward(50)
    jirafa.right(120) 
    jirafa.forward(50) 
    jirafa.end_fill()

    #Dibujo cola
    jirafa.pencolor("goldenrod")
    jirafa.pensize(10)
    jirafa.teleport(80,10)
    jirafa.right(30)
    jirafa.forward(60)
    jirafa.pensize(0)
    jirafa.left(30)
    jirafa.left(30)

    #Pasos dibujar las Manchas y pezuñas
    jirafa.color("saddleBrown","saddleBrown")
    jirafa.begin_fill()

    jirafa.teleport(-30,-50)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(10) 
    jirafa.right(90)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(10) 
    jirafa.right(90)

    jirafa.teleport(50,-50)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(10) 
    jirafa.right(90)
    jirafa.forward(20) 
    jirafa.right(90)
    jirafa.forward(10) 
    jirafa.right(90)

    jirafa.left(-30)
    jirafa.teleport(-25,25)
    for i in range(5):
        jirafa.forward(15)
        jirafa.right(360/5)
    jirafa.teleport(-40,160)
    for i in range(5):
        jirafa.forward(10)
        jirafa.right(360/5)
    jirafa.teleport(40,10)
    for i in range(5):
        jirafa.forward(10)
        jirafa.right(360/5)
    jirafa.teleport(-30,100)
    for i in range(5):
        jirafa.forward(8)
        jirafa.right(360/5)
    jirafa.teleport(-40,-35)
    for i in range(5):
        jirafa.forward(8)
        jirafa.right(360/5)
    jirafa.teleport(40,-25)
    for i in range(5):
        jirafa.forward(8)
        jirafa.right(360/5)
    jirafa.teleport(15,35)
    for i in range(5):
        jirafa.forward(20)
        jirafa.right(360/5)
    #Cola
    jirafa.teleport(80,0)
    for i in range(5):
        jirafa.forward(12)
        jirafa.right(360/5)

    #Orejas
    jirafa.teleport(-40,210)
    jirafa.circle(7)
    jirafa.teleport(-25,210)
    jirafa.circle(7)
    jirafa.end_fill()

    #Pasos Ojo
    jirafa.teleport(-60,160)
    jirafa.color("black","black")
    jirafa.begin_fill()
    jirafa.circle(4)
    jirafa.end_fill()

    jirafa.hideturtle()  
    
def Texto1():
    #Texto 1
    texto1=turtle.Turtle()
    texto1.speed(0)
    style = ('Arial', 14)

    texto1.teleport(0,275)
    texto1.write("El Zoológico",False,"center",("Arial",14,"bold"))
    texto1.teleport(0,250)
    texto1.write("Visita al Zoológico",False,"center",style)
    texto1.teleport(0,-170)
    texto1.write(f"Un día {name} de {edad} años se emocionó por la noticia de que iba ir",False,"center",style) 
    texto1.teleport(0,-195)
    texto1.write("zoológico. Con una sonrisa en el rostro llenó su mochila con golosinas y alistó",False,"center",style)
    texto1.teleport(0,-220)
    texto1.write("su cámara para tomar varias fotografías de sus aventuras.",False,"center",style)
    texto1.hideturtle()
    
def Texto2():
    #Texto 2
    texto2=turtle.Turtle()
    texto2.speed(0)
    style = ('Arial', 14)

    texto2.teleport(0,275)
    texto2.write("El Zoológico",False,"center",("Arial",14,"bold"))
    texto2.teleport(0,250)
    texto2.write("El León",False,"center",style)
    texto2.teleport(0,-170)
    texto2.write(f"Al llegar, lo primero que {name} encontró fue un león majestuoso descansando",False,"center",style) 
    texto2.teleport(0,-195)
    texto2.write("bajo el sol. Quedó hipnotizado por su melena dorada y su mirada feroz. Tomó ",False,"center",style)
    texto2.teleport(0,-220)
    texto2.write("varias fotos antes de continuar su exploración.",False,"center",style)
    
    texto2.hideturtle()

def Texto3():
    #Texto 3
    texto3=turtle.Turtle()
    texto3.speed(0)
    style = ('Arial', 14)

    texto3.teleport(0,275)
    texto3.write("El Zoológico",False,"center",("Arial",14,"bold"))
    texto3.teleport(0,250)
    texto3.write("Los monos",False,"center",style)
    texto3.teleport(0,-160)
    texto3.write(f"Después de caminar un poco más, {name} se topó con una familia de ",False,"center",style) 
    texto3.teleport(0,-185)
    texto3.write("simpáticos monos. Se divirtió viéndolos saltar de rama en rama y hacer",False,"center",style)
    texto3.teleport(0,-210)
    texto3.write("payasadas. Incluso le lanzaron algunas miradas curiosas antes de ",False,"center",style)
    texto3.teleport(0,-235)
    texto3.write("desaparecer entre la vegetación.",False,"center",style)

    texto3.hideturtle()

def Texto4():
    #Texto 4
    texto4=turtle.Turtle()
    texto4.speed(0)
    style = ('Arial', 14)

    texto4.teleport(0,275)
    texto4.write("El Zoológico",False,"center",("Arial",14,"bold"))
    texto4.teleport(0,250)
    texto4.write("El Elefante",False,"center",style)
    texto4.teleport(0,-170)
    texto4.write(f"En otra área del zoológico, {name} se maravilló al ver a un elefante gigante que se ",False,"center",style) 
    texto4.teleport(0,-195)
    texto4.write("bañaba en una piscina. Observó cómo el elefante usaba su trompa para",False,"center",style)
    texto4.teleport(0,-220)
    texto4.write("rociarse agua y cómo se movía con gracia a pesar de su tamaño imponente.",False,"center",style)

    texto4.hideturtle()

def Texto5():
    #Texto 5
    texto5=turtle.Turtle()
    texto5.speed(0)
    style = ('Arial', 14)

    texto5.teleport(0,275)
    texto5.write("El Zoológico",False,"center",("Arial",14,"bold"))
    texto5.teleport(0,250)
    texto5.write("La Jirafa",False,"center",style)
    texto5.teleport(0,-160)
    texto5.write(f"Antes de irse, {name} hizo una última parada en el hábitat de las jirafas. Quedó",False,"center",style) 
    texto5.teleport(0,-185)
    texto5.write("impresionado por su cuello largo y elegante, y cómo se alimentaban de las ",False,"center",style)
    texto5.teleport(0,-210)
    texto5.write("hojas más altas de los árboles. Sacó su cámara una vez más para capturar",False,"center",style)
    texto5.teleport(0,-235)
    texto5.write("este último recuerdo de su día en el zoológico.",False,"center",style)
    texto5.hideturtle()

#Nombre del cuento
print("Cuento: El Zoológico")
print("")
#Entrada de datos
name=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")
print("")
print("Elija un color:")
print("1. Azul")
print("2. Rojo")
print("3. Verde")
print("4. Anaranjado")
print("5. Morado")
color=int(input("Ingrese el valor de su opción: "))
print("")

if color<1 or color>5:
    print("Error: Ingrese una opción dentro de 1 y 5")
#Empieza ciclo     
while True:
    print("Elija una escena:")
    print("1. Visita al Zoológico")
    print("2. El León")
    print("3. Los Monos")
    print("4. El Elefante")
    print("5. La Jirafa")
    print("6. SALIR")
    escena=int(input("Ingrese el número de su opción: "))
    print("")
    if escena == 6:
        print("Fin del Cuento")
        break #Para salir del ciclo y terminar el programa

    if escena<1 or escena>6:
        print("Error: Ingrese una opción dentro de 1 y 6 ")
        continue  # olver al inicio del ciclo 
    else:
        color1 = ""
        match color:
            case 1:
                color1 = "PaleTurquoise"
            case 2:
                color1 = "lightCoral"
            case 3:
                color1 = "PaleGreen"
            case 4:
                color1 = "SandyBrown"
            case 5:
                color1 = "Plum"
        Cuadro()
        match escena:
            case 1:
                Texto1()
                Camara()
                
            case 2:
                Texto2()
                Leon()
            case 3:
                Texto3()
                Mono()
                
            case 4:
                Texto4()
                Elefante()
                
            case 5:
                Texto5()
                Jirafa()
#Salir del programa
turtle.done()