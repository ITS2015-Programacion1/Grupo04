# coding: utf-8
import pilasengine
#import escena_de_juego
	
pilas = pilasengine.iniciar()


pilas.fondos.Selva()    

def personajes():

    pilas.fondos.Pasto()
    titulo=pilas.actores.Texto("Enemigos Basicos")
    titulo.y = 200 
    
    class enemigo1(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo1.png"
            self.escala = 0.3 
            self.x = -210
            self.y = 130 

    pilas.actores.vincular(enemigo1)
    enemigo1 = pilas.actores.enemigo1()

    class enemigo2(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo2.png"
            self.escala = 0.3 
            self.x = -70
            self.y = 130 

    pilas.actores.vincular(enemigo2)
    enemigo2 = pilas.actores.enemigo2()

    class enemigo3(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo3.png"
            self.escala = 0.3 
            self.x = 60
            self.y = 130 

    pilas.actores.vincular(enemigo3)
    enemigo3 = pilas.actores.enemigo3()

    class enemigo4(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo4.png"
            self.escala = 0.3 
            self.x = 210
            self.y = 130 

    pilas.actores.vincular(enemigo4)
    enemigo4 = pilas.actores.enemigo4()
 
    titulo2=pilas.actores.Texto("Heroe")
    titulo2.y = 50

    class Soldado(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "soldado.png"
            self.x = 0
            self.y =-8
            self.escala = 0.3    

    pilas.actores.vincular(Soldado)
    soldado = pilas.actores.Soldado()

    titulo3=pilas.actores.Texto("Enemigo Final")
    titulo3.y=-75

    class robot(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "robot.png"
            self.escala = 0.6 
            self.x = 0
            self.y = -165 
            

    pilas.actores.vincular(robot)
    robot = pilas.actores.robot()
        
    menu.eliminar() 

def opciones():

    boton = pilas.interfaz.Boton("Regresar")
    def cuando_hacen_click():
        boton.conectar(menu	)    
        boton.y = 50
        boton.x = -200    
        
    
    pilas.fondos.Pasto()

    sonido =pilas.actores.Sonido()
    sonido.y = 0
    sonido.x = 200 
    pilas.avisar("Boton de sonido activo")
      
    menu.eliminar()

def como_jugar():

    pilas.fondos.Noche()
	
    text=pilas.actores.Texto("CONTROLES DE MOVIMIENTO")
    text.y = 200    
    text.escala = 1 
    text.definir_color(pilas.colores.rojo)
    texto=pilas.actores.Texto("Utiliza las teclas arriba abajo para mover al personaje y barra espaciadora para disparar")
    texto.y = 100
    texto.escala= 0.6
    texto2=pilas.actores.Texto("OBJETIVO")
    texto2.definir_color(pilas.colores.rojo)	
    texto3=pilas.actores.Texto("Evita que los enemigos lleguen hasta tu base")
    texto3.y = -60
    texto3.escala= 0.6
    texto4=pilas.actores.Texto("IMPORTANTE")
    texto4.y = -130
    texto4.definir_color(pilas.colores.rojo)
    texto5=pilas.actores.Texto("No utilises el mouse debido a un bug que ocurre, que cambia la ecena de juego por una del menu")    
    texto5.escala = 0.5 
    texto5.y = -160    


    menu.eliminar() 



def salir_del_juego():
    	pilas.terminar()


def iniciar_juego():

    menu.eliminar()

    pilas.fondos.Galaxia()

    class Soldado(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "soldado.png"
            self.x = -275
            self.escala = 0.3    

        def actualizar(self):
            if pilas.escena_actual().control.arriba:
                self.y += 5
            elif pilas.escena_actual().control.abajo:
           		self.y -= 5

    class enemigo1(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo1.png"
            self.escala = 0.3 
            self.x = -210
            self.y = 130 

    pilas.actores.vincular(enemigo1)
    enemigo1 = pilas.actores.enemigo1()

    class enemigo2(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo2.png"
            self.escala = 0.3 
            self.x = -70
            self.y = 130 

    pilas.actores.vincular(enemigo2)
    enemigo2 = pilas.actores.enemigo2()

    class enemigo3(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo3.png"
            self.escala = 0.3 
            self.x = 60
            self.y = 130 

    pilas.actores.vincular(enemigo3)
    enemigo3 = pilas.actores.enemigo3()

    class enemigo4(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "enemigo4.png"
            self.escala = 0.3 
            self.x = 210
            self.y = 130 

    pilas.actores.vincular(enemigo4)
    enemigo4 = pilas.actores.enemigo4()
 
    titulo2=pilas.actores.Texto("Heroe")
    titulo2.y = 50


    menu.eliminar()


    class robot(pilasengine.actores.Actor):   

        def iniciar(self):
            self.imagen = "robot.png"
            self.escala = 0.8 
            self.x = 0
            self.y = 0 

    pilas.actores.vincular(robot)
    robot = pilas.actores.robot()   

    class MiMunicion(pilasengine.actores.Actor):             
        def iniciar(self):            
            self.imagen = "disparos/bola_amarilla.png"
            self.escala_y = 0.25
            self.escala_x = 0.25
            self.y = 90

            def actualizar(self):
                self.escala_y += 10
                self.rotacion += 10

    pilas.actores.vincular(Soldado)
    pilas.actores.vincular(MiMunicion)
    
    bala = pilas.actores.MiMunicion()
    
    soldado = pilas.actores.Soldado()
    soldado.aprender('disparar', municion='MiMunicion')
    soldado.aprender(pilas.habilidades.LimitadoABordesDePantalla)

    def matar(bala, enemigo1):
        enemigo1.eliminar()
        bala.eliminar()

    pilas.colisiones.agregar(bala, enemigo1, matar)

def crear_enemigo():
    enemigo = pilas.actores.Actor()
    enemigo.aprender(pilas.habilidades.PuedeExplotar)

menu = pilas.actores.Menu(
    texto_personalizado = pilas.actores.Texto("Call of Duty", magnitud=10, fuente="visitor1.ttf", y=100)


        [

            ('Iniciar juego', iniciar_juego),
			('Como Jugar', como_jugar),            
            ("Personajes", personajes),			
            ('Opciones', opciones),			
            ('Salir', 	salir_del_juego),
        ])

pilas.ejecutar()
