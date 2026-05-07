"""Crea un sistema de viajes con dos tipos de usuarios: normales y premium.
El usuario tiene saldo y puede realizar viajes que cuestan km Ö $0.50.
Los usuarios premium tienen un descuento del 20% en cada viaje (polimorfismo).
El programa guarda un historial de los km de cada viaje en una lista.
Usa random para generar un n´umero de viaje aleatorio al registrar cada viaje."""
import random
class usuario: 
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.historial = []

    def calcular_costo(self, distancia): 
        return distancia*0.5

    def recargar_saldo(self, monto):
       if monto > 0:
        self.saldo += monto
        print(f"Saldo actualizado: {self.saldo}")
        
       else: 
        print("Monto inválido")   
    
    def realizar_viaje(self):
       distancia = float(input("Ingresar la distancia en km: "))
       costo = self.calcular_costo(distancia)
       if self.saldo >= costo: 
        self.saldo -= costo
        self.historial.append(distancia)
        numero_viaje = random.randit(1000, 9999)             
        print(f"El costo es de: {costo}, y su saldo restante es: {self.saldo}")

       else:
        print("Saldo insuficiente")

    def ver_hisotorial(self):
        if len(self.historial) == 0:
            print("No hay viajes")

        else: 
            print("Historial de viajes: ")
            for distancia in self.historial: 
                print(f"{distancia}km")
        
    def ver_perfil(self, detallado):
        if detallado: 
            print("Nombre: {self.nombre}")
            print("Tipo: Normal")
            print(f"Saldo: {self.saldo}")
            print(f"Viajes: {len(self.historial)}")

        else: 
            print(f"Nombre: {self.nombre}")
            print(f"Saldo: {self.saldo}")

    def gasto_total(self):
        total = 0
        for distancia in self.historial:
            total += self.calcular_costo(distancia)
        print(f"Gasto total: {total}")

class premium(usuario):
    def calcular_costo(self, distancia):
        return distancia * 0.5 * 0.8

    def ver_perfil(self, detallado):
        if detallado: 
            print("Nombre: {self.nombre}")
            print("Tipo: Premium")
            print(f"Saldo: {self.saldo}")
            print(f"Viajes: {len(self.historial)}")

        else: 
            print(f"Nombre: {self.nombre}")
            print(f"Saldo: {self.saldo}")


nombre = input("Ingrese su nombre: ")
saldo = float(input("Ingrese su saldo: "))

if input("Premium? (s/n): ") == "s":
    usuario = premium(nombre, saldo)

else:
    usuario = usuario(nombre, saldo)
