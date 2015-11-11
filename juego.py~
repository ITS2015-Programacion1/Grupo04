# coding: utf-8
import pilasengine
from clases_actores import Arma_Ak47, Soldado, MiMunicion, Enemigo
import random


    
pilas = pilasengine.iniciar()

pilas.actores.vincular(Arma_Ak47)
pilas.actores.vincular(Soldado)
pilas.actores.vincular(MiMunicion)
pilas.actores.vincular(Enemigo)


pilas.fondos.Selva()    

def como_jugar():

    boton3 = pilas.interfaz.Boton("regresar")
    boton3.y = 210
    boton3.x =-265 

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
    
    def cuando_elimina_enemigo(bala, enemigo):
        bala.eliminar()
        enemigo.eliminar()

    def cuando_colisiona(enemigos, pizarra):
        soldado.eliminar()
        ak.eliminar()
        enemigos.eliminar
        pilas.avisar("has perdido")

    enemigo1 = pilas.actores.Enemigo(img_enemigo='enemigo1.png', y=200)
    enemigo2 = pilas.actores.Enemigo(img_enemigo='enemigo2.png', y=100)
    enemigo3 = pilas.actores.Enemigo(img_enemigo='enemigo3.png', y=-100)
    enemigo4 = pilas.actores.Enemigo(img_enemigo='enemigo4.png', y=-200)

    enemigos = [enemigo1, enemigo2, enemigo3, enemigo4]

    ak = pilas.actores.Arma_Ak47(pilas, x=0)
    soldado = pilas.actores.Soldado(pilas, x=0)
    soldado.aprender('disparar', grupo_enemigos=enemigos, cuando_elimina_enemigo=cuando_elimina_enemigo)
    soldado.aprender(pilas.habilidades.LimitadoABordesDePantalla)
    ak.aprender(pilas.habilidades.LimitadoABordesDePantalla)
  
pizarra = pilas.actores.Pizarra()

pizarra.linea(0, -300, 1, 10000)
   


pilas.fondos.Fondo("mapaoficial.png")       

class alazar(pilasengine.actores.Actor):

    def iniciar(self):    
        self.imagen = "enemigo{}.png".format(random.randint(1,3))
        self.x = 300
        self.escala= 0.3
        self.y = self.pilas.azar(-200, 200)  
    
    def actualizar(self):
        if self.x>-400:
            self.x = self.x -2      
    
def crear_actor_al_azar():
    pilas.actores.alazar()

pilas.actores.vincular(alazar)
pilas.tareas.siempre(1.5, crear_actor_al_azar)  

puntos = pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.blanco)
puntos.magnitud = 40


menu = pilas.actores.Menu(
    
        [

            ('Iniciar juego', iniciar_juego),
            ('Como Jugar', como_jugar),                      
            ('Salir', salir_del_juego),
        ])

pilas.ejecutar()

