# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

#crear la escena que contendra al juego
    class Juegoactivo(pilasengine.escenas.Escena):
        def iniciar(self):

            pilas.escenas.juegoactivo(inicio)
            pilas.escenas.juegoactivo()

menu = pilasengine.actores.Menu(
    
        [	
            ('Iniciar juego', iniciar_juego),
            ('Como Jugar', como_jugar),                      
            ('Salir', salir_del_juego),
        ])

pilas.ejecutar()

