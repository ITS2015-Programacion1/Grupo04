# coding: utf-8
import pilasengine

def iniciar_juego():
    
    class juegoactivo(pilasengine.escenas.Escena):
        def iniciar(self):

            pilas.escenas.juegoactivo(inicio)
            pilas.escenas.juegoactivo()
    
            def cuando_elimina_enemigo(bala, enemigo):
                bala.eliminar()
                enemigo.eliminar()

            def cuando_toca(enemigos, pizarra):
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
         
        cambio_de_radio_de_colision = pilas.actores.Pizarra(x=0)
        rectangulo = pilas.fisica.Rectangulo(0, 0, 1, 10000, sensor=True, dinamica=False)
        cambio_de_radio_de_colision.figura_de_colision = rectangulo



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

