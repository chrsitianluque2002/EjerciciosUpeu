#EjercicioUpeU-1 1
def  notafinalclh ():
  print ( "la nota final es" )
  #Lasvariable
  notafinalclh  =  0.00
  #losdatos de entrada
  U1 = float ( input ( "ingrese nota de la primera unidad:" ))
  U2 = float ( input ( "ingrese nota de la segunda unidad:" ))
  U3 = float ( input ( "ingrese nota de la tercera unidad:" ))
  TF = float ( input ( "ingrese nota del trabajo final:" ))
  #losproceso
  si  0 <= U1 <= 20  y  0 <= U2 <= 20  y  0 <= U3 <= 20  y  0 <= TF <= 20 :
    notafinalclh = ( U1 * ( 20 * 0.2 ) / 20 + U2 * ( 20 * 0.15 ) / 20 + U3 * ( 20 * 0.15 ) / 20 + TF * ( 20 * 0.5 ) / 20 )
    #losdatos de salida
    print ( " \ n la nota final es:" , notafinalclh )
  otra cosa :
    print ( " \ n ingrese bien los datosd, las notas solo estan comprendido de 0 a 20" )
#lanotafinalclh ()

#EjercicioUpeU-1 2
def  bonoprofesorclh ():
  print ( "el bono del profesor de acuerdo a su puntuacion" )
  #las variables
  montobonoclh  =  0.00
  #los datos de dentrada
  puntuacion = int ( input ( "ingrese puntos obtenidos:" ))
  SMin = float ( input ( "ingrese el salario minimo:" ))
  #los proceso
  si  puntuacion > = 50  y  puntuacion <= 100 :
    montobonoclh = SMin * 0.1
  elif  puntuacion > = 101  y  puntuacion <= 150 :
    montobonoclh = SMin * 0.4
  elif  puntuacion > = 151 :
    montobonoclh = SMin * 0.7
  #los datos de salida
  print ( "el bono que recibira es:" , montobonoclh )
#bonoprofesorclh ()

#EjercicioUpeU-1 3
def  vacunacovid19clh ():
  print ( "tipo de vacuna que se debe aplicar" )
  #la variable
  Tvacunaclh  =  ""
  F  =  "FEMENINO"
  M  =  "MASCULINO"
  #datos de entrada
  edad = int ( input ( "ingrese la edad de la persona:" ))
  sexo =  input ( "ingrese el sexo de la persona:" )
  #el proceso
  si  sexo == 'F'  o  sexo == 'M' :
    si  edad > = 70  y  sexo == 'F'  o  sexo == 'M' :
      Tvacunaclh = "C"
    elif  16 <= edad <= 69  y  sexo == 'F' :
      Tvacunaclh = "B"
    elif  16 <= edad <= 69  y  sexo == 'M' :
      Tvacunaclh = "A"
    elif  edad < 16  y  sexo == 'F'  o  sexo == 'M' :
      Tvacunaclh = "A"
    #losdatos de salida
  print ( "el tipo de vacuna que la persona debe recibir es:" , Tvacunaclh )
#la vacunacovid19chl ()

#EjercicioUpeU-1 4
def  operacionaritmeticachl ():
  print ( "operaciones aritmeticas" )
  #la variable
  resultadoclh =  0
  #los datos de entrada
  num1 = float ( input ( "ingrese el primer numero:" ))
  num2 = float ( input ( "ingrese el segundo numero:" ))
  operacion =  input ( "ingrese la operacion:" )
  #el proceso
  si  operacion == '+' :
    resultadoclh = num1 + num2
  elif  operacion == '-' :
    resultadoclh = num1 - num2
  elif  operacion == '/' :
    resultadoclh = num1 / num2
  elif  operacion == '*' :
    resultadoclh = num1 * num2
  elif  operacion == '^' :
    resultanteclh = num1 ** num2
  otra cosa :
    resultadoclh = "la operacion es incorrecta"
  #los datos de salida
  print ( "el resultado es:" , resultadoclh )
#laoperacionaritmeticaclh ()