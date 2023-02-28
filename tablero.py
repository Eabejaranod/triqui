class Tablero():
    def init(self):
        self.tablero=[['','',''],['','',''],['','','']]
    def mostrar_tablero(self,tablero):
        for i in tablero:
            print(i)

def cambiodeturno(turno):
    if (turno == 'X'):
        turno = 'O'
    else:
        turno = 'X'
    return turno
