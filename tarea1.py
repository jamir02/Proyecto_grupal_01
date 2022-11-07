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

ASCII_TITULO = """
 __       __  .______   .______       _______ .______       __       ___      
|  |     |  | |   _  \  |   _  \     |   ____||   _  \     |  |     /   \     
|  |     |  | |  |_)  | |  |_)  |    |  |__   |  |_)  |    |  |    /  ^  \    
|  |     |  | |   _  <  |      /     |   __|  |      /     |  |   /  /_\  \   
|  `----.|  | |  |_)  | |  |\  \----.|  |____ |  |\  \----.|  |  /  _____  \  
|_______||__| |______/  | _| `._____||_______|| _| `._____||__| /__/     \__\

"""

# OPCION 1
def obtener_lista(lista_libros) -> list:
    direccion = input("Escriba la dirección del archivo .txt o .csv: ")
    try:
        open(direccion, 'rb')
    except FileNotFoundError:
        print(f"Archivo {direccion} no encontrado")
        sys.exit(1)
    except OSError:
        print(f"Error de OS al tratar de abrir {direccion}")
        sys.exit(1)
    except Exception as err:
        print(f"Error inesperado al abrir {direccion}.",repr(err))
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
        print("Archivo cargado")

# TODO

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
    10: "Guardar libros en archivo de disco duro (.txt o csv)"
}

funciones = {
    1: obtener_lista,
}

def programa():
    while True:
        print(ASCII_TITULO)

        for opcion in opciones:
            print(f"Opcion #{opcion}: {opciones[opcion]} ")
    
        lista_inicial_libros, lista_libros = [], []
        op = int(input("Escoja una opcion: "))

        funciones[op](lista_inicial_libros)
        
        break
programa()