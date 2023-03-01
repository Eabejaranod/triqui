from jugador import Jugador
from tablero import Tablero

class juego():
    def init(self):
        self.jugador=Jugador
        self.tablero=Tablero
        self.turno='x'
    def iniciar_juego():
        pass
    def cambiodeturno(self,):
        if (self.turno == 'X'):
            self.turno = 'O'
        else:
            self.turno = 'X'
        return self.turno
