# Distribución de Probabilidades

+ Variable Discreta (Unidad 7)
    + Distribución Binomial
    + Dist Poisson

+ Variable Continua (Unidad 8)
    +Distribución normal


## Distribución Binomial

Partamos de un experimento aleatorio que pueda repetirse en las mismas condiciones N veces, y que el resutado de cada experimento no dependa de los demás. Por ejemplo: Tiramos un dado y queremos registrar si sale o no sale 4, este experimento lo repito 5 veces. Este experimento tiene el siguiente espacio muestral:

E= {éxito, fracaso}

Con esto podemos definir una variable aleatoria "x" que toma solo dos valores posibles

xsub1 = 1 (éxito ); xsub2 = 0 (fracaso) 

También podemos calcular las probabilidades de cada uno de estos valores

P(x=1) = 1/6 P(x=0)= 5/6

Si una variable toma solamente 2 valores

xsub1 y xsub2= 0

Si el experimento resulta un exito o un fracaso respectivamente se la denomina variable aleatoria de Bernoulli. A la probabilidad de x1 = 1 la simbolizamos con la letra p y a la de x2 = 0 con la letra q

Pn (h) = C(n,h) . p^h . q ^-h

### Ejemplo 

Quiero saber cual es la probabilidad que en 5 tiros del dado salgan exactamente dos 4.
 
 p = 1/6
 q = 5/6
 n = 5
 h = 2


P5(2) = C(5,2) . (1/6)^2 . (5/6)^3 = 0,160751

### Problema

En una fábrica de caramelos de Gelatina, envasan los caramelos en paquetes de a 15. Si el 30% de los caramelos que se fabrican son de limón y se envasan mezclados. Calcula la probabilidad de que en un paquete se encuentren:
    a. Solo dos caramelos de limón
    b. Al menos 3 caramelos de limón


## Distribución de Poisson
Por lo que hemos visto hasta el momento, los problemas sobre pruebas repetidas independientes con igual probabilidad cada una de ellas, se resuelven utilizando la distribución Binomial. Si el experimento Binomial se realiza un número "n" muy elevado de veces (n > 50) y la probabilidad de éxito en cada ensayo es reducida (p < 0,1) entonces se utiliza el modelo de distribución de Poisson

P(n,h) = e ^-lambda . lambda ^h / h!

lambda= n . p

e = 2718281...

### Problema
En cierto lugar, la probabilidad de tener un accidente de tránsito es de 0,02 cada vez que se viaja. Si se realizan 300 viajes cual es la probabilidad de tener 3 accidentes.

Ver hoja Accidente
## Distribución Normal

Es el modelo de distribución más utilizado en la práctica ya que multitud de fenómenos naturales se comportan según una distribución normal. Empleando cálculos bastante laboriosos, puedo demostrarse que el modelo de la función de densidad que corresponde a tales distribuciones viene dado por la siguiente fórmula: 

f(x) = 1 / Sigma. sqrt(2pi) . e ^-1/2.(x-Mu/Sigma)2 

Siendo Mu la media de la distribución y sigma su desviación típica o éstandard. La distribución normal queda definida por estos dos parámetros

x:N(mu,sigma); x:N(u,s)

La distribución normal se caracteriza porque los valores se distribuyen formando una campana, llamada Campana de Gauss, en torno a un valor central que coincide con el valor medio de la distribución.

Grafico campana

mu -sigma  Mu u + sigma


observando el gráfico podemos dar algunas características: 

+ Es simétrica respecto a la recta x = mu

+ Es asintótica al eje x

+ Posee puntos de inflexión en x = mu + sigma y x = mu - sigma

+ Son más probables los valores cercanos a la media. Conforme nos separamos de ese valor la prob va decreciendo y lo hará de manera mas o menos rápida dependiendo del desvío estándar. 

Uso de Tabla

z = x - mu / sigma 


x <-> z <-> P(x) N=0 sigma=1
### Ejemplo

x:N(20,5)

a P(x<21) = P(z < 21-20/5) = P(z < 0,2) = 0,5793

Ejercicios 