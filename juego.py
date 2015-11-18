# coding: utf-8
#importar todos los archivos del juego para ejecutarlos en uno solo
import pilasengine
from clases_actores import Arma_Ak47, Soldado, MiMunicion, Enemigo
import random
from iniciar_juego import Alazar

    
pilas = pilasengine.iniciar()

#vincular los actores que estan en otro archivo
pilas.actores.vincular(Arma_Ak47)
pilas.actores.vincular(Soldado)
pilas.actores.vincular(MiMunicion)
pilas.actores.vincular(Enemigo)

#crear la primera escena
class inicio(pilasengine.escenas.Escena):
    
    def inciar(self):
        self.fondo = self.pilas.fondos.Fondo("ghost.jpg") 
        pass


pilas.escenas.vincular(inicio)
pilas.escenas.inicio()


def Como_jugar():

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


