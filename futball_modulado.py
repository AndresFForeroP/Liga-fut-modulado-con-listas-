"""
Autor: Andres Forero
Fecha: 30/01/2025
Nombre :liga futball con modulos
descripcion: el programa permite agregar equipos con todos sus datos y programar fechas de partidos
se usan dos listas para el almacenamiento de todos sus datos
"""
import modules.menus as menus
import modules.funciones as func
from modules.Fgenerales import limpiar_p,pausar_p
import matplotlib.pyplot as plt
menu1 = 0
iEquipos = 1
#se crean dos listas una para el manejo del equipo y otra para el manejo de las fechas
equipos = []
nFechas = []
while menu1 != 9:
    menu2 = 0
    try:
        print(menus.MenuPrincipal)
        menu1 = int(input('Elige una opcion segun el menu '))
    except Exception:
        print("Valor invalido,solo ingrese el numero de la opcion del menu")
    limpiar_p()
    match menu1:
        case 1:
            #se manda la lista y desde el modulo se crea el equipo en su debida lista y la funcion devuelve la lista
            #toda su documentacion esta en su modulo
            func.crearEquipo(equipos)
            limpiar_p()
            while menu2 != 9:
                limpiar_p()
                print(f'MENU EQUIPO DE {equipos[len(equipos)-2].upper()}')
                try:
                    print(menus.MenuRegistro.center(45))
                    menu2 = int(input('Elige una opcion segun el menu '))
                except Exception:
                    print("Valor invalido,solo ingrese el numero de la opcion del menu")
                match menu2:
                    case 1:
                        limpiar_p()
                        #se manda la lista y desde el modulo agrega el jugador a su debida lista y la funcion devuelve la lista
                        #la forma de agregarse en la lista se repite con leves cambios tanto para agregarct como cmd y estadisticas
                        #toda su documentacion esta en su modulo
                        func.agregarJugador(equipos)
                        print(equipos)
                    case 2:
                        limpiar_p()
                        func.agregarct(equipos)
                        print(equipos)
                    case 3:
                        limpiar_p()
                        func.agregarcmd(equipos)
                        print(equipos)
                    case 4:
                        limpiar_p()
                        func.agregarestadisticas(equipos)
                        print(equipos)
        case 2:
            #se manda la lista y desde el modulo imprime la lista 
            #toda su documentacion esta en su modulo
            func.mostrarequipos(equipos)
            pausar_p()
        case 3:
            #Se manda las listas de equipo y nfechas, se almacenan los datos de las fechas en su debida lista
            #va fecha por fecha mostrando que partido se jugara en cada una
            #Toda su documentacion esta en su modulo
            func.almacenarfechas(nFechas,equipos)
            print(f'hay un total de {int(len(equipos)/2)} equipos registrados')
fig,ax = plt.subplots(facecolor = 'lightskyblue',figsize=(2,2),layout='constrained')
#ax.plot([equipos[0],equipos[2]],[len(equipos[1][1]),len(equipos[3][1])])
ax.scatter([equipos[0],equipos[2]],[int(len(equipos[1][1])/2),int(len(equipos[3][1])/2)])
ax.set_ylabel('Cantidad jugadores')
ax.set_xlabel('Equipos')
plt.show()