class Menu:
    '''Muestra un menu y responde a elecciones cuando se ejecuta.'''
    def __init__(self):
        self.categorias = Cuaderno()
        self.elecciones = {
                "1" : self.mostrar_notas,
                "2" : self.search_notas,
                "3" : self.add_nota,
                "4" : self.modificar_nota,
                "5" : self.quit
                }
 
    def mostrar_menu(self):
        print("""
Menu Cuaderno
 
1 Mostrar todas las Notas
2 Buscar Notas
3 Añadir Nota
4 Modificar Nota
5 Salir
""")
 
    def run(self):
        '''Muestra el menú y responde a las elecciones.'''
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es una elección válida".format(eleccion))