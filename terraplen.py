# calculo de las tensiones en un terraplen
# version 12/05/2019
# Germán López Pineda
# Ingeniero de Caminos Canales y Puertos
# Profesor asociado de la Universidad de Córdoba


# importamos librerias 
import math



# datos geometricos del terraplen
print("Calculo de tensiones en la base de un terraplén")
print("El origen del eje x se localiza en el derrame izquierdo del terraplén")
print("El eje z se considera positivo hacia abajo\n")


b=float(input("Valor mitad del ancho de la base b[m]= "))
a=float(input("Valor del ancho del derrame a[m]= "))

h=float(input("Valor de la altura del terraplen h[m]="))



# datos fisicos del terraplen
p_e=float(input("Peso especifico del material del terraplen [kN/m3]="))


# valores de la geometria del dominio de definicion
x=float(input("coordenada x[m]="))
z=0.1 # valor de la profundidad
zf=float(input("Espesor del terreno natural considerado zf[m]="))
incremento_z=float(input("Incremento de z [m]="))

# datos carga
carga=p_e*h # calculo de la carga del terraplen

# generamos archivo y escritura de datos básicos
f = open ('terraplen.txt','w')
f.write("Valor del ancho de la semibase {0:0.2f} m\n".format(b))
f.write("Valor del ancho del derrame {0:0.2f} m\n".format(a))
f.write("Valor de la altura del terraplén {0:0.2f} m\n".format(h))
f.write("Potencia del terreno considerado {0:0.2f} m\n".format(zf))
f.write("Valor de la carga de tierras = {0:0.2f} [kN/m2]\n".format(carga))
f.write("Cálculos realizados para x= {0:0.2f} m\n\n".format(x))

while z<zf :

    beta_a=math.atan((b-x)/z)+math.atan((x-a)/z)
    beta_b=math.atan((x-b)/z)+math.atan((2*b-x-a)/z)
    alfa_a=math.atan((a-x)/z)+math.atan(x/z)
    alfa_b=math.atan((a-2*b+x)/z)+math.atan((2*b-x)/z)

    r_oa=math.sqrt(math.pow(x,2)+math.pow(z,2))
    r_ob=math.sqrt(math.pow(2*b-x,2)+math.pow(z,2))
    r_1a=math.sqrt(math.pow(x-a,2)+math.pow(z,2))
    r_1b=math.sqrt(math.pow(2*b-x-a,2)+math.pow(z,2))
    r_22=math.pow(b-x,2)+math.pow(z,2)

    # calculo de las tensiones
    tension_z=(carga/math.pi)*((beta_a+x*alfa_a/a-z*(x-b)/r_22)+(beta_b+(2*b-x)*alfa_b/a-z*(b-x)/r_22))
    # tension en x
    tension_x=(carga/math.pi)*((beta_a+x*alfa_a/a+z*(x-b)/r_22+2*z*math.log(r_1a/r_oa)/a)+beta_b+alfa_b*(2*b-x)/a+z*(b-x)/r_22+2*z*math.log(r_1b/r_ob)/a)
    # tension en xz
    tension_x_z=-(carga/math.pi)*(z*(alfa_a+alfa_b)/a-2*math.pow(z,2)/r_22)

    # escritura en el archivo de salida talud.txt
    f.write("sigma_z({0:0.2f})= {1:0.5f} sigma_x({0:0.2f})= {2:0.5f} kN/m2 \n".format(z,tension_z,tension_x))

    #incrementamos la variable
    z=z+incremento_z

     
f.close() # cerramos archivo

# imprimir datos de calculo

#print("Valor del ancho de la semibase {0:0.2f} m".format(b))
#print("Valor del ancho del derrame {0:0.2f} m".format(a))
#print("Valor de la altura del terraplén {0:0.2f} m".format(h))
#print("Valor de la carga de tierras = {0:0.2f} [kN/m2]".format(carga))
#print("Cálculos realizados para x= {0:0.2f} m".format(x))


# control del fin del programa
print('\nCálculo terminado ver resultados en archivo terraplen.txt ')
tecla=input()
