import csv

class Libro:
    def __init__(self, id: int, titulo: str, genero: str, ISBN: str, editorial: str, autores: list[str]) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__autores = autores

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    def get_titulo(self) -> str:
        return self.__titulo

    def set_titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    def get_genero(self) -> str:
        return self.__genero

    def set_genero(self, genero: str) -> None:
        self.__genero = genero

    def get_ISBN(self) -> str:
        return self.__ISBN

    def set_ISBN(self, ISBN) -> None:
        self.__ISBN = ISBN

    def get_editorial(self) -> str:
        return self.__editorial

    def set_editorial(self, editorial) -> None:
        self.__editorial = editorial

    def get_autores(self) -> list:
        return self.__autores

    def set_autores(self, autores) -> None:
        self.__autores = autores

    def __del__(self) -> None:
        return None


#función para validar que la entrada del usuario no sea vacio

def validar_respuesta(entrada: str) -> str:

    while True:
        variable = input(entrada)
        if variable != "":
            return variable.strip()
        print("El valor a ingresar no debe ser vacio")

#funcion para validar que el dato ingresado  sea del tipo int

def validarInt(mensaje: str) -> int:
    
    while True:
        variable = input(mensaje)
        if variable.isnumeric():
            variable = int(variable)
            return variable
        print("El valor a ingresar debe ser un número")

def validarNroAutores() -> int:
    while True:
        nroAutores = validarInt(" Nro de autores:")
        if nroAutores > 0:
            return nroAutores
        print("El libro debe tener al menos 1 autor")

def crearIndice(lenLibros: int) -> int:
    return lenLibros

def leerArrayString(mensaje: str, longitud: int) -> list[str]:
    lista = []
    for i in range(1, longitud + 1):
        variable = leerArrayString(mensaje + str(i) + ":")
        lista.append(variable)
    return lista

#función de la opción 2

def listar_libros(lista_libros: list) -> None:
    datos_libro = []
    
    for libro in lista_libros:
        autores = "\n".join(libro.get_autores())
        datos_libro.append(
            [   
                libro.get_id(),
                libro.get_titulo(),
                libro.get_genero(),
                libro.get_ISBN(),
                libro.get_editorial(),
                autores,
            ]
        )

    print(datos_libro)

#función de la opción 3

def crear_libro(lista_libros: list[Libro]) -> Libro:
    id = crearIndice(len(lista_libros))
    print("Ingrese los datos del libro:")
    titulo = validar_respuesta("Título:")
    genero = validar_respuesta("Género: ")
    isbn = validar_respuesta("ISBN: ")
    editorial = validar_respuesta("Editorial: ")
    nroAutores = validarNroAutores()
    autores = leerArrayString("Autor :", nroAutores)
    libroNuevo = Libro(id, titulo, genero, isbn, editorial, autores)
    return libroNuevo

#función de la opción 4

def eliminar_libro(id: int, lista_libros: list[Libro]) -> None:
    borrado = 0
    for libro in lista_libros:

        if libro.get_id() == id:
            lista_libros.pop(lista_libros.index(libro))
            print("El libro ha sido eliminado con exito")
            borrado += 1
    if borrado == 0:
        print("El id no está en la lista")
