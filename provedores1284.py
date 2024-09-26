print("Examen Paola Ramirez 22308051281284")
# Crear la clase
class Provedores1284:
    id_proveedor1284 = ""
    telefono1284 = 0
    gmail1284 = ""
    raiting1284 = 0
    fecha_registro1284 = ""
    tipo1284 = ""
    provincia1284 = ""
# funcion para mostrar datos
    def datos1284(self):
        print(f"id: {self.id_proveedor1284}")
        print(f"telfono: {self.telefono1284}")
        print(f"gmail: {self.gmail1284}")
        print(f"raiting: {self.raiting1284}") 
        print(f"fecha de registro: {self.fecha_registro1284}")
        print(f"tipo: {self.tipo1284}")
        print(f"provincia: {self.provincia1284}")
    
    def lista_empleados1284(self):
        Empleados = ["Zulema", "Sara", "Nicole", "Javier", "Hector", "Veronica", "Luna"]
        for x in Empleados:
            print(x)
    def tupla_artesanias1284(self):
        Artesanias = ("Ajolotes", "Jarrones", "Alebrijes", "Vajillas", "Casuelas", "Alcancias", "Figuras")
        for a in Artesanias:
            print(a)
    def diccionario_precio1284(self):
        Precios = {"Ajolotes:" : "$30.00", "Jarrones:" : "$500.00", "Alebrijes:" : "$650.00", "Vajilla:" : "$500.00", 
                "Casuelas:" : "$350.00", "Alcancias:" : "$700.00", "Figuras:" : "$800.00"}
        for p,b in Precios.items():
            print(p,b)
# funciones altas y bajas
    def altas1284(self):
        print("La operacion alta se realizo correctamente")
    def bajas1284(self):
        print("La operacion baja se realizo correctamente")
# objeto
Datos1284=Provedores1284()

Datos1284.id_proveedor1284 = 22308051281284
Datos1284.telefono1284 = 6564512545
Datos1284.gmail1284 = "PaolaRamirez@gmail.com"
Datos1284.raiting1284 = 4
Datos1284.fecha_registro1284 = "16/Septiembre/2020"
Datos1284.tipo1284 = "Proveedor de ceramica"
Datos1284.provincia1284 = "Chihuahua"
# objetos
print("Datos del Proveedor 1284")
Datos1284.datos1284()
print("Lista de Empleados 1284")
Datos1284.lista_empleados1284()
print("Tupla de artesanias 1284")
Datos1284.tupla_artesanias1284()
print("Diccionario de precios 1284")
Datos1284.diccionario_precio1284()

Datos1284.altas1284()
Datos1284.bajas1284()