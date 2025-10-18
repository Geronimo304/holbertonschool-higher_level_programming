#!/usr/bin/python3
"""
Este módulo define una clase personalizada de Python llamada CustomObject
y demuestra cómo serializar y deserializar instancias de esta clase
utilizando el módulo pickle.

Características:
- Clase CustomObject con los atributos: name, age, is_student
- Método de instancia para mostrar los datos del objeto
- Métodos para serializar y deserializar usando pickle
- Manejo de excepciones para errores de archivos o de pickle
"""
import pickle
import os


class CustomObject:
    """
    Clase personalizada de Python con atributos básicos y métodos para
    serializar y deserializarse a sí misma usando el módulo pickle.

    Atributos:
        name (str): Nombre de la persona.
        age (int): Edad de la persona.
        is_student (bool): Indica si la persona es estudiante.
    """

    def __init__(self, name, age, is_student):
        """
        Inicializa una nueva instancia de CustomObject.

        Args:
            name (str): Nombre de la persona.
            age (int): Edad de la persona.
            is_student (bool): Verdadero si la persona es estudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Muestra en pantalla los valores de los atributos del objeto.
        """
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"¿Es estudiante?: {self.is_student}")

    def serialize(self, filename):
        """
        Serializa (guarda) el objeto actual en un archivo binario usando pickle.

        Args:
            filename (str): Nombre del archivo donde se guardará el objeto.

        En caso de error, muestra un mensaje indicando la causa.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (pickle.PickleError, IOError) as err:
            print(f"Error al serializar el objeto: {err}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializa (carga) un objeto desde un archivo binario usando pickle.

        Args:
            filename (str): Nombre del archivo desde el cual se cargará el objeto.

        Returns:
            CustomObject | None: Devuelve una instancia de CustomObject si tuvo éxito,
            o None si hubo un error o el archivo no existe.
        """
        if not os.path.exists(filename):
            print(f"El archivo {filename} no existe.")
            return None

        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("El objeto deserializado no es una instancia de CustomObject.")
                    return None
        except (pickle.PickleError, IOError, EOFError) as error:
            print(f"Error al deserializar el objeto: {error}")
            return None
