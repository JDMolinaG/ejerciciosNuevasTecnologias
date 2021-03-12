#ejercicio 1
cuota = 0
interes = 0
años = 5
taza = 0.136
credito = float(input('ingrese el valor del credito: '))
interes = float(credito * taza * años)
creditoTotal = credito + interes
cuota = creditoTotal/años/12
print('su credito tiene una cuota de: ', cuota)


#ejercicio 2
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
telefono = input('Ingrese su telefono: ')

print('Su nombre es: '+ nombre)
print('Su edad es: '+ edad)
print('Su telefono es: '+ telefono)


#3
prestamo = float(input('ingrese valor de prestamos: '))
interesMensual = int(((prestamo)*0.018))
print('Los intereses mensuales es: ',interesMensual)
cuotaMensual = (prestamo/12) + interesMensual
print('cuota mensuales: ',cuotaMensual)
totalAnual = ((cuotaMensual*12)+cuotaMensual)
print('El valor a pagar anual es: ',totalAnual)
totalPagarDos = interesMensual*2
print('total a pagar en dos meses: ',totalPagarDos)
totalInteresAnual = interesMensual*12
print('total a pagar anual: ',totalInteresAnual)
totalCuotaNueve = (cuotaMensual*9)
print('total a pagar en nueve meses: ',totalCuotaNueve)


