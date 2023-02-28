from tablero import Tablero
class Jugador():
    def init(self):
        self.jugador=Jugador
        self.tablero=Tablero
        self.simbolo='x'
    def marcar(self,tablero):
        x=input(int("ingrese posicion 1:"))
        y=input(int("ingrese posicion 2:"))
        if tablero[x][y] == '':
            tablero[x][y]=self.simbolo
        else:
            print('jugada no valida')
            Jugador.marcar(self,tablero)