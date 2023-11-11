import json
def crearVehiculo(codigo, marca, modelo, precio, kilometraje):
    Vehiculo = {
        "codigo": codigo,
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "kilometraje":kilometraje
    }
    with open("datos/vehiculos.json", "r") as archivo:
        Vehiculos = json.load(archivo)
        if codigo in Vehiculos:
            return False
        else:
            Vehiculos[codigo] = Vehiculo
            with open("datos/vehiculos.json", "w") as archivo:
                json.dump(Vehiculos, archivo, indent=4)
                print("el Vehiculo a sido creado correctamente")
def actualizarVehiculo(codigo, marca, modelo, precio, kilometraje):
    with open("datos/vehiculos.json", "r") as archivo:
        Vehiculos = json.load(archivo)
        if codigo in Vehiculos:
            Vehiculos[codigo]["marca"] = marca
            Vehiculos[codigo]["modelo"] = modelo
            Vehiculos[codigo]["precio"] = precio
            Vehiculos[codigo]["kilometraje"]=kilometraje
            with open("datos/vehiculos.json", "w") as archivo:
                json.dump(Vehiculos, archivo, indent=4)
                print("el Vehiculo a sido actualizado correctamente")
        else:
            print("Este Vehiculo no existe")
def eliminarVehiculo(codigo):
    with open("datos/vehiculos.json", "r") as archivo:
        Vehiculos = json.load(archivo)
        if codigo in Vehiculos:
            del Vehiculos[codigo]
            with open("datos/vehiculos.json", "w") as archivo:
                json.dump(Vehiculos, archivo, indent=4)
                print("Vehiculo eliminado correctamente")
        else:
            print("Este Vehiculo no existe")
def mostrarVehiculos():
    with open("datos/vehiculo.json", "r") as archivo:
        Vehiculos = json.load(archivo)
        if len(Vehiculos) == 0:
            print("No hay Vehiculos")
        else:
            print("<------------ Vehiculos ------------>")
            for Vehiculo in Vehiculos:
                print(f"Codigo: {Vehiculos[Vehiculo]['codigo']}")
                print(f"Marca: {Vehiculos[Vehiculo]['marca']}")
                print(f"Modelo: {Vehiculos[Vehiculo]['modelo']}")
                print(f"Precio: {Vehiculos[Vehiculo]['precio']}")
                print(f"Kilometraje: {Vehiculos[Vehiculo]['kilometraje']}")
                print("------------------------------------")
            print("<---------------------------------->")
