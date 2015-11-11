# coding: utf-8
import pilasengine


class Arma_Ak47(pilasengine.actores.Actor):

    def iniciar(self, pilas, x=0, y=0):
        self.imagen = "ak.png"
        self.x = -250
        self.y = 0
        self.escala = 0.3    
        self.pilasobject = pilas

    def actualizar(self):
        if  self.pilasobject.escena_actual().control.arriba:
            self.y += 5
        elif self.pilasobject.escena_actual().control.abajo:
       		self.y -= 5   


class Soldado(pilasengine.actores.Actor):   

    def iniciar(self, pilas, x=0, y=0):
        self.imagen = "soldado.png"
        self.x = -275
        self.y = 0
        self.escala = 0.3 
        self.pilasobject = pilas   

    def actualizar(self):
        if  self.pilasobject.escena_actual().control.arriba:
            self.y += 5
        elif  self.pilasobject.escena_actual().control.abajo:
       		self.y -= 5

	self.radio_de_colision = 35


class Enemigo(pilasengine.actores.Actor):   

    def iniciar(self, img_enemigo='enemigo1.png', y=0):                                                       
        self.imagen = img_enemigo
        self.x = 0
        self.y =y
        self.escala = 0.3

    
	self.radio_de_colision = 37


class enemigo2(pilasengine.actores.Actor):   

    def iniciar(self):                                                       
        self.imagen = "enemigo2.png"
        self.x = 0
        self.y =-10
        self.escala = 0.3    


class enemigo3(pilasengine.actores.Actor):   

    def iniciar(self):                                                       
        self.imagen = "enemigo3.png"
        self.x = 0
        self.y = 10
        self.escala = 0.3    


class enemigo4(pilasengine.actores.Actor):   

    def iniciar(self):                                                       
        self.imagen = "enemigo4.png"
        self.x = 0
        self.y = 30
        self.escala = 0.3    



class MiMunicion(pilasengine.actores.Actor):             
    def iniciar(self):            
	    self.imagen = "disparos/bola_amarilla.png"
	    self.escala_y = 0.25
	    self.escala_x = 0.25
	    self.y = 90

    def actualizar(self):
	    self.escala_y += 10
	    self.rotacion += 10




