def crearEquipo(equipos):
    #pido al usuario el nombre del equipo y agrego el nombre a la lista equipos
    #se agrega una lista adicional en equipos para que todos sus datos esten ahi
    #la estructura de las listas que se maneja es la siguiente: equipos[nombreequipo,[]]
    #cada vez que se agrega un equipo se agrega su nombre y una lista
    nomeq = input('Inserte el nombre del equipo ')
    while equipos.count(nomeq) >= 1:
        nomeq = input('Inserte el nombre del equipo que no este registrado ')
    equipos.append(nomeq)
    equipos.append([])
    #cuando se crea cada equipo dentro de la lista donde se van a almacenar los datos del equipo se agregan 4 textos y 4 listas
    #cada texto va junto a la lista que va a contener su informacion
    #su estructura es la siguiente: equipos['nombreequipo',['jugadores',[],'ct',[],'cmd',[],'Estadisticas',[]]]
    equipos[len(equipos) -1].append('jugadores')
    equipos[len(equipos) -1].append([])
    equipos[len(equipos) -1].append('ct')
    equipos[len(equipos) -1].append([])
    equipos[len(equipos) -1].append('cmd')
    equipos[len(equipos) -1].append([])
    equipos[len(equipos) -1].append('Estadisticas')
    equipos[len(equipos) -1].append([])
    #lleno la parte de estadisticas de 0 tan pronto como se creo el equipo 
    #la lista queda asi equipos['nombreequipo',['jugadores',[],'ct',[],'cmd',[],'Estadisticas',[0,0,0,0,0,0,0]]]
    for i in range(0,7):
        equipos[len(equipos) -1][7].append(0)
    return equipos
def agregarJugador(equipos):
    #se agrega el nombre del jugador y se le agrega una lista en la siguiente posicion para almacenar sus datos(dorsal,edad,posicion)
    #la lista queda de la siguiente manera: equipos['nombreequipo',['jugadores',['nombrejugador1',[dorsal,edad,pos]],'ct',[],'cmd',[],'Estadisticas',[0,0,0,0,0,0,0]]]
    Nombre = input('Ingrese el nombre del jugador ')
    equipos[len(equipos)-1][1].append(Nombre)
    equipos[len(equipos)-1][1].append([])
    dorsal = input('Ingrese el numero del dorsal del jugador ')
    equipos[len(equipos)-1][1][len(equipos[len(equipos)-1][1])-1].append(dorsal)
    edad = 0
    while edad <= 0:
        try:
            edad = int(input('Ingrese el numero del edad del jugador '))
        except Exception:
            print("inserta una edad valida en numero entero mayor a 0")
    equipos[len(equipos)-1][1][len(equipos[len(equipos)-1][1])-1].append(edad)
    pos1 = 0
    while pos1 <= 0 or pos1 >=5:
        print("""1.Delantero
2.Mediocampo
3.Defensa
4.Portero""")
        try:
            pos1 = int(input('ingresa un numero de la lista segun la posicion del jugador '))
        except Exception:
            print('solo ingrese numeros enteros segun las opciones')
        match pos1:
            case 1:
                pos = 'Delantero'
            case 2:
                pos = 'Mediocampo'
            case 3:
                pos = 'Defensa'
            case 4:
                pos = 'Portero'
    equipos[len(equipos)-1][1][len(equipos[len(equipos)-1][1])-1].append(pos)
    return(equipos)
def agregarct(equipos):
    #se agrega el nombre del ct y de la misma manera que el jugador se almacenan los datos pero en la lista de ct dentro de la lista del equipo 
    #la lista queda de la siguiente manera: equipos['nombreequipo',['jugadores',[],'ct',['nombrect',[cargo,edad]],'cmd',[],'Estadisticas',[0,0,0,0,0,0,0]]]
    Nombre = input('Ingrese el nombre del ct ')
    equipos[len(equipos)-1][3].append(Nombre)
    equipos[len(equipos)-1][3].append([])
    cargo = input('Ingrese el rol de ct ')
    equipos[len(equipos)-1][3][len(equipos[len(equipos)-1][1])-1].append(cargo)
    edad = 0
    while edad <= 0:
        try:
            edad = int(input('Ingrese el numero del edad del ct '))
        except Exception:
            print = "inserta una edad valida en numero entero mayor a 0"
    equipos[len(equipos)-1][3][len(equipos[len(equipos)-1][1])-1].append(edad)
    return equipos
def agregarcmd(equipos):
    #se agrega el nombre del cmd y de la misma manera que el jugador se almacenan los datos pero en la lista de cmd dentro de la lista del equipo 
    #la lista queda de la siguiente manera: equipos['nombreequipo',['jugadores',[],'ct',[],'cmd',['nombrecmd',['cargo','edad']],'Estadisticas',[0,0,0,0,0,0,0]]]
    Nombre = input('Ingrese el nombre del cmd ')
    equipos[len(equipos)-1][5].append(Nombre)
    equipos[len(equipos)-1][5].append([])
    cargo = input('Ingrese el rol de cmd ')
    equipos[len(equipos)-1][5][len(equipos[len(equipos)-1][1])-1].append(cargo)
    edad = 0
    while edad <= 0:
        try:
            edad = int(input('Ingrese el numero del edad del cmd '))
        except Exception:
            print = "inserta una edad valida en numero entero mayor a 0"
    equipos[len(equipos)-1][5][len(equipos[len(equipos)-1][1])-1].append(edad)
    return equipos
def agregarestadisticas(equipos):
    #se agregan las estadisticas del equipo y se almacenan en su debida lista, en el primer bloque se usa un while para garantizar
    #que la cantidad de partidos jugados coincicda con la suma de pp+pe+pg
    #en el caso de pj = 16 pp = 3 pe =5  pg = 8 gf = 10 gc = 8 y pt = (pg*3) + pe
    #la lista se veria de esta manera: equipos['nombreequipo',['jugadores',[],'ct',[],'cmd',[],'Estadisticas',[16,3,5,8,10,8,29]]]
    partidos = 1
    while partidos !=0:
        try:
            equipos[len(equipos)-1][7][0] = int(input('Ingrese la cantidad partidos jugados '))
        except Exception:
            equipos[len(equipos)-1][7][0] = int(input('ERROR solo numeros enteros,Ingrese la cantidad partidos jugados '))
        partidos = equipos[len(equipos)-1][7][0]
        try:
            equipos[len(equipos)-1][7][1] = int(input('Ingrese la cantidad partidos perdidos '))
        except Exception:
            equipos[len(equipos)-1][7][1] = int(input('ERROR solo numeros enteros,Ingrese la cantidad partidos perdidos '))
        partidos -= equipos[len(equipos)-1][7][1]
        try:
            equipos[len(equipos)-1][7][2] = int(input('Ingrese la cantidad partidos empatados '))
        except Exception:
            equipos[len(equipos)-1][7][2] = int(input('ERROR solo numeros enteros,Ingrese la cantidad partidos empatados '))
        partidos -= equipos[len(equipos)-1][7][2]
        try:
            equipos[len(equipos)-1][7][3] = int(input('Ingrese la cantidad partidos ganados '))
        except Exception:
            equipos[len(equipos)-1][7][3] = int(input('ERROR solo numeros enteros,Ingrese la cantidad partidos ganados '))
        partidos -= equipos[len(equipos)-1][7][3]
        if partidos !=0:
            print(f'ERROR en cantidad de partidos, se jugaron {equipos[len(equipos)-1][7][0]}')
            print(f'Se perdieron {equipos[len(equipos)-1][7][1]}')
            print(f'Se empataron {equipos[len(equipos)-1][7][2]}')
            print(f'Se ganaron {equipos[len(equipos)-1][7][3]}')
            if (equipos[len(equipos)-1][7][0] > (equipos[len(equipos)-1][7][1])+ equipos[len(equipos)-1][7][2] + equipos[len(equipos)-1][7][3]):
                print('Faltaron partidos por registrar')
            else:
                print(f'Registraste mas de {equipos[len(equipos)-1][7][0]} partidos')
    try:
        equipos[len(equipos)-1][7][4] = int(input('Ingrese la cantidad de goles que hizo el equipo '))
    except Exception:
        equipos[len(equipos)-1][7][4] = int(input('ERROR solo numeros enteros,Ingrese la cantidad de goles que hizo el equipo '))
    try:
        equipos[len(equipos)-1][7][5] = int(input('Ingrese la cantidad de goles que le hicieron al equipo '))
    except Exception:
        equipos[len(equipos)-1][7][5] = int(input('ERROR solo numeros enteros,Ingrese la cantidad de goles que le hicieron al equipo '))
    equipos[len(equipos)-1][7][6] = (equipos[len(equipos)-1][7][3]) * 3 + (equipos[len(equipos)-1][7][2])
    return equipos
def mostrarequipos(equipos):
    #este bloque de codigo imprime la informacion de todos los equipos que estan registrados, el bloque toma los todos datos que se han ido almacenando en las listas
    #se usa exactamente la ubicacion tanto de los nombres de los equipos,nombres de jugadores,sus datos y estadisticas
    print(f'Estan registrados {int(len(equipos)/2)} equipos los equipos son')
    for i in range(0,len(equipos)):
        if i % 2 == 0:
            print(f'⚽ {equipos[i]} con {int((len(equipos[i+1][1]))/2)} jugadores ⚽')
            for j in range(0,len(equipos[i+1][1]),2):
                print(f'- {equipos[i+1][1][j]} con el dorsal {equipos[i+1][1][j+1][0]} es {equipos[i+1][1][j +1][2]} y tiene {equipos[i+1][1][j +1][1]} años')
            print('los cts son ')
            for j in range(0,len(equipos[i+1][3]),2):
                print(f'- {equipos[i+1][3][j]}  es {equipos[i+1][3][j+1][0]} y tiene {equipos[i+1][3][j+1][1]} años')
            print('los cmd son ')
            for j in range(0,len(equipos[i+1][5]),2):
                print(f'- {equipos[i+1][5][j]}  es {equipos[i+1][5][j+1][0]} y tiene {equipos[i+1][5][j+1][1]} años')
            print('las estadisticas del equipo son')
            print(f'se jugaron {equipos[i+1][7][0]} partidos')
            print(f'se ganaron {equipos[i+1][7][3]}, se empataron {equipos[i+1][7][2]} y se perdieron {equipos[i+1][7][1]}  partidos')
            print(f'metieron {equipos[i+1][7][4]} goles y les metieron {equipos[i+1][7][5]} goles')
            print(f'el equipo logro un total de {equipos[i+1][7][6]} puntos')
    return equipos
def almacenarfechas(nFechas,equipos):
    #Este bloque es el que permite almacenar en la lista nFechas toda la informacion de las fechas y nombre de los equipos que tendran partido ese dia
    #en el caso de que colombia se enfrente a argentia el 03/02/2025 la lista se vera de esta manera
    #nFechas[partido1,[03,02,2025,'colombia','argentina']]
    cFechas = 0
    j = 1
    while cFechas <= 0:
        try:
            cFechas = int(input('Ingrese la cantidad de fechas a ingresar '))
        except Exception:
            print('ERROR,Ingrese una cantidad de fechas valida')
        else:
            break
    for i in range(0,cFechas):
        dia = mes = año = 0
        nFechas.append('partido' + str(i + 1))
        nFechas.append([])
        while dia <= 0 or dia > 31:
            try:
                dia = int(input(f'Ingrese el dia del partido # {i + 1} '))
            except Exception:
                print('ERROR,Ingrese un dia valido en numero del 1 al 31')
            else:
                break
        nFechas[i+j].append(dia)
        while mes <= 0 or mes > 12:
            try:
                mes = int(input(f'Ingrese el mes del partido # {i + 1} '))
            except Exception:
                print('ERROR,Ingrese un mes valido en numero del 1 al 12')
            else:
                break
        nFechas[i+j].append(mes)
        while año <= 0:
            try:
                año = int(input(f'Ingrese el año del partido # {i + 1} '))
            except Exception:
                print('ERROR,Ingrese un año valido en numero entero')
            else:
                break
        nFechas[i+j].append(año)
        for k in range(0,len(equipos)):
            if k % 2 == 0:
                print(f'⚽ {equipos[k]} ⚽')
        if int(len(equipos)/2) >=2:
            equipo1 = equipo2 = 'h'
            while equipos.count(equipo1) == 0:
                try:
                    equipo1 = input(f'Ingrese el nombre del primer equipo de los registrados que se va a enfrentar el {dia}/{mes}/{año} ')
                except Exception:
                    print('ingrese un nombre de equipo de la lista')
            nFechas[i+j].append(equipo1)
            while equipos.count(equipo2) == 0:
                try:
                    equipo2 = input(f'Ingrese el nombre del segundo equipo de los registrados que se va a enfrentar el {dia}/{mes}/{año} ')
                    while equipo1 == equipo2:
                        print(f'ya ingresaste a {equipo1},no se pueden jugar partidos si son el mismo equipo ')
                        equipo2 = input(f'Ingrese el nombre del segundo equipo de los registrados que se va a enfrentar el {dia}/{mes}/{año} ')
                except Exception:
                    print('ingrese un nombre de equipo de la lista')
            nFechas[i+j].append(equipo2)
        j += 1
    if len(nFechas[1]) > 3:
        for i in range(0,len(nFechas),2):
            if i % 2 == 0:
                print(f'El partido del dia {nFechas[i+1][0]}/{nFechas[i+1][1]}/{nFechas[i+1][2]}')
                print(f'Se jugara un partido entre {nFechas[i+1][3]} y {nFechas[i+1][4]}')
    x = input('dale enter para continuar...')
    return nFechas,equipos