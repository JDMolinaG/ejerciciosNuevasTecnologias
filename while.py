#ejercicio 1
centinela = 'si'
mujer =0
hombre=0
total =0
while centinela == 'si':
    genero = input('Ingrese el genero: ')
    if genero == 'mujer':
        mujer=mujer +1
    elif genero == 'hombre':
        hombre = hombre +1
    centinela=input('quiere continuar?')
    
    
total = mujer+hombre
print('el total de mujeres fue: ',mujer)
print('el total de hombres fue: ',hombre)
print(total)
    
#---------------------------------------------------------

#ejercicio 2

analista = 0
desarrollador = 0
arquitecto = 0
centinela = 'si'
while centinela == 'si':
    cargo=input('ingrese el cargo: ')
    if cargo == 'analista':
        analista = analista+1
        pagoAnalista = 870000
    elif cargo == 'desarrollador':
        desarrollador = desarrollador+1
        pagoDesarrollador = 2300000
    elif cargo == 'arquitecto':
        arquitecto = arquitecto+1
        pagoArquitecto  = 790000
    centinela = input('quiere seguir? si/no ')

totalAnalista = analista * pagoAnalista
totalDesarrollador = desarrollador * pagoDesarrollador
totalArquitecto = arquitecto * pagoArquitecto
total = totalAnalista +totalDesarrollador+totalArquitecto

print('el total de costos de analistas fue: ',totalAnalista)
print('el total de costos de desarrolladores fue: ',totalDesarrollador)
print('el total de costos de arquitectos fue: ',totalArquitecto)
print('el total de costos de analistas fue: ',totalAnalista)
print('el total de costos generales fue: ',total)

#---------------------------------------------------------

#ejercicio 3

centinela = 'si'
ninos = 0
jovenes = 0
adultos = 0
while centinela == 'si':
    edad = int(input('ingrese la edad: '))
    if  edad >1 and edad <=15:
        ninos = ninos+ 1
    elif edad >=16 and edad <=18:
        jovenes = jovenes+1
    elif edad >18:
        adultos = adultos+1
    centinela = input('quiere seguir? si/no ')

sumaTotal = ninos+jovenes+adultos
promedioNinos = ninos / sumaTotal
promedioJovenes = jovenes / sumaTotal
promedioAdultos = adultos / sumaTotal

print('el total de personas fue: ',sumaTotal)
print('el promedio de niños fue: ',promedioNinos,ninos)
print('el promedio de jovenes fue: ',promedioJovenes,jovenes)
print('el promedio de adultos fue: ',promedioAdultos,adultos)

#---------------------------------------------------------

#ejercicio4

centinela = 'si'
sencillo =0
full = 0

while centinela == 'si':
    servicio = input('ingrese servicio: ')
    if servicio == 'sencillo':
        sencillo = sencillo +1
        costoSencillo = 12000
    elif servicio == 'full':
        full = full +1
        costoFull = 17000
    centinela = input('quiere seguir? si/no ')


totalSencillo = sencillo * costoSencillo
totalFull = full * costoFull

print('el total del servicio sencillo fue: ',totalSencillo,sencillo)
print('el total del servicio full fue: ',totalFull,full)


#---------------------------------------------------------

#primeros 20 pares

centinela = 0
x = 1
while centinela>=0 and centinela<40:
    if(x % 2 == 0):
        print(x)
    x=x+1
    centinela = centinela+1

#---------------------------------------------------------

#primeros 10 numeros

centinela = 0
x = 0
while centinela>=0 and centinela<10:
    x = x + 1
    print(x)
    centinela = centinela+1

#---------------------------------------------------------

#suma 30 pares

centinela = 0
x = 1
total = 0
while centinela>=0 and centinela<60:
    if x % 2 == 0:
        print(x)
        total += x
    x=x+1
    centinela = centinela+1
print('la suma total de los 30 numeros pares es: ',total)

#---------------------------------------------------------

#suma 10 impares

centinela = 0
x = 1
total = 0
while centinela>=0 and centinela<20:
    ifx % 2 == 1:
        print(x)
        total += x
    x=x+1
    centinela = centinela+1
print('la suma total de los 10 numeros impares es: ',total)

#---------------------------------------------------------

#10 numeros impares negativos

centinela = -1
x = 0
while centinela<=0 and centinela >=-20:  
    if x % 2 == 1:
        print(x)
    x = x - 1
    centinela = centinela - 1

#---------------------------------------------------------

#fibonacci

a = 0
b = 1
while b<10:
    print(b)
    a,b = b , a+b

#---------------------------------------------------------


#estadio atanasio

boletas = 0
centinela = 'si'
norte=0
sur=0
oriental=0
occidental=0
hombre = 0
mujer = 0
while centinela == 'si':
    tribuna = input('Ingrese la tribuna: ')
    genero = input('Ingrese el genero: ')
    if genero == 'hombre':
        if tribuna == 'norte':
            norte = norte +1
            hombre = hombre +1
        elif tribuna == 'sur':
            sur = sur +1
            hombre = hombre +1
        elif tribuna == 'oriental':
            oriental = oriental+1
            hombre = hombre +1
        elif tribuna == 'occidental':
            occidental = occidental+1
            hombre = hombre +1
    if genero == 'mujer':
        if tribuna == 'norte':
            norte = norte +1
            mujer = mujer +1
        elif tribuna == 'sur':
            sur = sur +1
            mujer = mujer +1
        elif tribuna == 'oriental':
            oriental = oriental+1
            mujer = mujer +1
        elif tribuna == 'occidental':
            occidental = occidental+1
            mujer = mujer +1
    centinela = input('quiere seguir? si/no ')

totalBoletas = norte+sur+oriental+occidental
print('El total de boletas fue: ',totalBoletas)
print('norte: ',norte,' sur: ',sur,' oriental: ',oriental,' occidental: ',occidental)
print('hombres: ',hombre,' mujeres: ', mujer)

#---------------------------------------------------------


#escuela de natacion

centinela = 'si'
basico = 0
experimentado = 0
profesional = 0
print('edades entre 4 a 8, y 9 a 12 y niveles basico experimentado y profesional')
while centinela == 'si':
    
    edad = int(input('ingrese la edad: '))
    nivel = input('Ingrese nivel: ')
    if edad>=4 and edad<=8 or edad>=9 and edad<=12:
        if nivel== 'basico':
            costoBasico = 120000
            basico += 1
        elif nivel == 'experimentado':
            costoExperimentado = 250000
            experimentado += 1
        elif nivel == 'profesional':
            costoProfesional = 280000
            profesional += 1
    centinela = input('quiere seguir? si/no ')

total = costoBasico + costoExperimentado + costoProfesional
totalBasico = costoBasico * basico
totalExperimentado = costoExperimentado * experimentado
totalProfesional = costoProfesional * profesional

print('el total general fue: ',total)
print('nivel basico: ',basico,' experimentado: ',experimentado,' profesional: ',profesional)
print('el total de basico fue: ',totalBasico)
print('el total de experimentado fue: ',totalExperimentado)
print('el total de profesional fue: ',totalProfesional)






