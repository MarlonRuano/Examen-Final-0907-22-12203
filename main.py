from Mantenimiento_vehiculo import *
from Reportes import*
import sys
def menuprincipal():
    print("1. Crear Vehiculo")
    print("2. Actualizar Vehiculo")
    print("3. Eliminar Vehiculo")
    print("4. Listar Vehiculos")
    print("5. Reportes")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        codigo = input("Código: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        precio = input("Precio: ")
        kilometraje = input("Kilometraje: ")
        crearVehiculo(codigo, marca, modelo, precio, kilometraje)
    elif opcion == "2":
        codigo = input("Código: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        precio = input("Precio: ")
        kilometraje = input("Kilometraje: ")
        actualizarVehiculo(codigo, marca, modelo, precio, kilometraje)
    elif opcion == "3":
        codigo = input("Código: ")
        eliminarVehiculo(codigo)
    elif opcion == "4":
        mostrarVehiculos()
    elif opcion == "5":
        correo = input("Correo")
        nombre = input("Nombre")
        esVehiculos = input ("Vehiculo")
        enviarCorreo(correo, nombre, esVehiculos)
    elif opcion == "6":
        exit()
def principal():
    if len(sys.argv) > 1:
        menuArgumento()
    else:
        menuprincipal()
principal()