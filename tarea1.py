import csv

print ("¿Qué te gustaría hacer?")
print ("Opción 1: Leer archivo de disco duro")
print ("Opción 2: Listar libros")
print ("Opción 3: Agregar libro")
print ("Opción 4: Eliminar libro")
print ("Opción 5: Buscar libro por ISBN o por título")
print ("Opción 6: Ordenar libros por título")
print ("Opción 7: Buscar libros por autor, editorial o género.")
print ("Opción 8: Buscar libros por número de autores")
print ("Opción 9: Editar o actualizar datos de un libro")
print ("Opción 10: Guardar libros en archivo de disco duro")
print ("Opcion 0: Salir")

opcion = input("Elija una opción (1,2,3,4,5,6,7,8,9,10 o 0): ")
while (not(opcion in ['1','2','3','4','5','6','7','8','9','10','0'])):
    opcion = input("Por favor, escoja una opción (1,2,3,4,5,6,7,8,9,10 o 0): ")



## opcion 10

def Opcion_10(self):
        #Guradar libros en archivo
        my_path = 'nuevo_libro.csv'
        with open(my_path, 'w', encoding="utf-8",newline='') as file:
            writer = csv.DictWriter(file,fieldnames=self.fieldnames,delimiter='|')
            writer.writeheader()
            writer.writerows(self.lista)
        file.close()
        print("Se han guardado los libros en el archivo.")