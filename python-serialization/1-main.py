from task_01_pickle import CustomObject

# Crear una instancia del objeto
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serializar el objeto
obj.serialize("object.pkl")

# Deserializar el objeto
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
if new_obj:
    new_obj.display()
else:
    print("Deserialization failed.")
