import csv
import sys


class Libro:
    def __init__(
        self,
        id: int,
        titulo: str,
        genero: str,
        ISBN: str,
        editorial: str,
        autores: list[str],
    ) -> None:
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


# función para validar que la entrada del usuario no sea vacio


def validar_respuesta(entrada: str) -> str:

    while True:
        variable = input(entrada)
        if variable != "":
            return variable.strip()
        print("El valor a ingresar no debe ser vacio")


# funcion para validar que el dato ingresado  sea del tipo int


def validarInt(mensaje: str) -> int:

    while True:
        variable = input(mensaje)
        if variable.isnumeric():
            variable = int(variable)
            return variable
        print("El valor a ingresar debe ser un número")


ASCII_TITULO = """
 __       __  .______   .______       _______ .______       __       ___      
|  |     |  | |   _  \  |   _  \     |   ____||   _  \     |  |     /   \     
|  |     |  | |  |_)  | |  |_)  |    |  |__   |  |_)  |    |  |    /  ^  \    
|  |     |  | |   _  <  |      /     |   __|  |      /     |  |   /  /_\  \   
|  `----.|  | |  |_)  | |  |\  \----.|  |____ |  |\  \----.|  |  /  _____  \  
|_______||__| |______/  | _| `._____||_______|| _| `._____||__| /__/     \__\

"""

lista_libros = []
dict_libros = {}


def obtener_dict():
    global lista_libros
    global dict_libros
    for libro in lista_libros:
        if libro.get_id() not in dict_libros:
            dict_libros[libro.get_id()] = {
                "titulo": libro.get_titulo(),
                "genero": libro.get_genero(),
                "ISBN": libro.get_ISBN(),
                "editorial": libro.get_editorial(),
                "autores": libro.get_autores(),
            }


def imprimir_libro(id):
    # print("Libro: ")
    print("ID:", id)
    print("titulo:", dict_libros[id]["titulo"])
    print("genero:", dict_libros[id]["genero"])
    print("ISBN:", dict_libros[id]["ISBN"])
    print("editorial:", dict_libros[id]["editorial"])
    print("autores:", dict_libros[id]["autores"])


# OPCION 1
def obtener_lista():
    global lista_libros
    # direccion = input("Escriba la dirección del archivo .txt o .csv: ")
    direccion = "libros.csv"
    try:
        open(direccion, "rb")
    except FileNotFoundError:
        print(f"Archivo {direccion} no encontrado")
        sys.exit(1)
    except OSError:
        print(f"Error de OS al tratar de abrir {direccion}")
        sys.exit(1)
    except Exception as err:
        print(f"Error inesperado al abrir {direccion}.", repr(err))
        sys.exit(1)
    else:
        with open(direccion, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                autores = row["autores"].split(",")
                id = len(lista_libros)
                libro = Libro(
                    id,
                    row["titulo"],
                    row["genero"],
                    row["ISBN"],
                    row["editorial"],
                    autores,
                )
                lista_libros.append(libro)

        # print("Archivo cargado")


# OPCION 2
def imprimir_libros():
    for id in dict_libros:
        imprimir_libro(id)
        print("-" * 10)


# OPCION 3
def agrega_libro():
    global lista_libros
    id = len(lista_libros)
    titulo = input("Titulo del libro: ")
    genero = input("Genero del libro: ")
    ISBN = input("ISBN del libro: ")
    editorial = input("Editorial de libro: ")
    autores = input("Autores del libro: ")
    libro_nuevo = Libro(id, titulo, genero, ISBN, editorial, autores)
    lista_libros.append(libro_nuevo)

    obtener_dict()


# OPCION 4
def elimina_libro():
    pass


# OPCION 5
def buscar_por_opcion(texto, opcion, dict_libros):
    a_buscar = input(texto).lower()
    for id in dict_libros:
        if str(dict_libros[id][opcion]).lower() == a_buscar:
            print("Libro encontrado! ")
            imprimir_libro(id)


def buscar_libro_5(dict_libros):
    resp = input("Buscar el libro por ISBN (I) o titulo (T)? ").upper()
    if resp == "I":
        buscar_por_opcion("Que ISBN quiere buscar?: ", "ISBN", dict_libros)

    elif resp == "T":
        buscar_por_opcion("Que titulo quiere buscar?: ", "titulo", dict_libros)


# OPCION 6
def ordenar_por_titulo():
    sorted_dict = dict(sorted(dict_libros.items(), key=lambda item: item[1]["titulo"]))
    print("Libros ordenados por titulo")
    print(sorted_dict)


# OPCION 7
def buscar_libro_7(dict_libros):
    resp = input("Buscar el libro por autor (A), editorial (E) o genero (G)? ").upper()
    if resp == "A":
        buscar_por_opcion("Que autor quiere buscar?: ", "autores", dict_libros)
    elif resp == "E":
        buscar_por_opcion("Que editorial quiere buscar?: ", "editorial", dict_libros)
    elif resp == "G":
        buscar_por_opcion("Que genero quiere buscar?: ", "genero", dict_libros)


# OPCION 8
def buscar_libro_numero_autores(dict_libros):
    num_autores_ingresado = int(input("Ingresar el número de autores: "))
    libros = []
    for id in dict_libros:
        libros.append(str(dict_libros[id]["autores"]).lower())

    dup = {x for x in libros if libros.count(x) == num_autores_ingresado}
    print(dup)

# OPCION 9

# OPCION 10
def guardar_libros_10(dict_libros):
    my_file= "libros.csv"
    print ("Guardando libros en el disco duro...")
    file = open(my_file, "w")
    file.close()
    with open(my_file, "w", encoding="utf-8") as file:
        file.write("titulo,genero,ISBN,editorial,autores\n")
        for id in dict_libros:
            datos = ",".join(['"'+str(dict_libros[id]["titulo"])+'"',str(dict_libros[id]["genero"]), str(dict_libros[id]["ISBN"]),'"'+str(dict_libros[id]["editorial"])+'"','"'+str(dict_libros[id]["autores"][0])+'"' ])        
            file.write(datos + "\n")
        file.close()
    print("Se guadaron los libros con éxito.")

opciones = {
    1: "Leer archivo",
    2: "Listar libros",
    3: "Agregar libro",
    4: "Eliminar libro",
    5: "Buscar libro por ISBN",
    6: "Ordenar libros por titulo",
    7: "Buscar libros por autor, editorial o genero",
    8: "Buscar libros por número de autores",
    9: "Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores)",
    10: "Guardar libros en archivo de disco duro (.txt o csv)",
}

funciones = {
    1: obtener_lista,
    2: imprimir_libros,
    3: agrega_libro,
    4: elimina_libro,
    5: buscar_libro_5,
    6: ordenar_por_titulo,
    7: buscar_libro_7,
    8: "todo",
    9: "todo",
    10: "todo",
}


def programa():
    print(ASCII_TITULO)
    for opcion in opciones:
        print(f"Opcion #{opcion}: {opciones[opcion]} ")
    obtener_lista()
    obtener_dict()
    while True:
        # print("lista_libros", lista_libros)
        # print("dict_libros", dict_libros)
        op = input("Escoja una opcion: ")
        if op == "" or not op.isnumeric():
            break
        op = int(op)

        if op == 1:
            obtener_lista()
        elif op == 2:
            imprimir_libros()
        elif op == 3:
            agrega_libro()
        elif op == 4:
            elimina_libro()
        elif op == 5:
            buscar_libro_5(dict_libros)
        elif op == 6:
            ordenar_por_titulo()
        elif op == 7:
            buscar_libro_7(dict_libros)
        elif op == 8:
            buscar_libro_numero_autores(dict_libros)
        elif op == 9:
            pass
        elif op == 10:
            guardar_libros_10(dict_libros)
            pass
        else:
            break
        # funciones[op](lista_libros)

        # print(dict_libros)
        # break


programa()
