Ejercicios
**13.** Numero de 5 cifras con 1,2,4,6,8 y dos 8
<!-- C(5,2) x V(4,3)-->
`    _ _ _ _ _  `

De 5 lugares tomo 2 (sin importar el orden)
\(
C(n,k) = \frac{n!}{k!(n-k)!}
\)

Sustituimos \( n = 5 \) y \( k = 2 \):

\(
C(5,2) = \frac{5!}{2!(5-2)!}
\)

Simplificamos:

\(
C(5,2) = \frac{5!}{2! \cdot 3!}
\)

Desarrollamos los factoriales:

\(
5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1
\)
\(
2! = 2 \cdot 1
\)
\(
3! = 3 \cdot 2 \cdot 1
\)

Sustituimos:

\(
C(5,2) = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{(2 \cdot 1)(3 \cdot 2 \cdot 1)}
\)

Simplificamos términos comunes:

\(
C(5,2) = \frac{5 \cdot 4}{2 \cdot 1}
\)

\(
C(5,2) = \frac{20}{2}
\)

\(
C(5,2) = 10
\)

### Resultado primera parte:

\(
C(5,2) = 10
\)

### Cálculo de las variaciones \( V(4,3) \)
\(
C(5,2) \times V(4,3) = 10 \times 24 = 240
\)
La fórmula de variaciones (sin repetición) es:

\(
V(n,k) = \frac{n!}{(n-k)!}
\)

Sustituimos \( n = 4 \) y \( k = 3 \):

\(
V(4,3) = \frac{4!}{(4-3)!}
\)

Simplificamos:

\(
V(4,3) = \frac{4!}{1!}
\)

Desarrollamos los factoriales:

\(
4! = 4 \cdot 3 \cdot 2 \cdot 1
\)
\(
1! = 1
\)

Sustituimos:

\(
V(4,3) = \frac{4 \cdot 3 \cdot 2 \cdot 1}{1}
\)

Simplificamos:

\(
V(4,3) = 4 \cdot 3 \cdot 2
\)

\(
V(4,3) = 24
\)

### Resultado Segunda Parte:

\(
V(4,3) = 24
\)

### Resultado Final
\(
10 x 24 = 240
\)

<hr>

**15.** 
<!-- V'(2,4)-->
Cuatro niños, 2 habitaciones ¿cuántas formas hay de colocarlos? 
### Distribuciones de 4 niños en 2 habitaciones
### Ejemplo de distribuciones (4 niños, 2 habitaciones)

#### Caso 1: Todos en una habitación
- A: Niño1, Niño2, Niño3, Niño4
- B: —



#### Caso 2: Distribución 3–1
- A: Niño1, Niño2, Niño3
- B: Niño4

---

#### Caso 3: Distribución 2–2
- A: Niño1, Niño2
- B: Niño3, Niño4

**Resolución**

V'= (2,4 ) =

### Cálculo de las variaciones con repetición \( V'(2,4) \)

La fórmula de variaciones con repetición es:

\(
V'(n,k) = n^k
\)

Sustituimos \( n = 2 \) y \( k = 4 \):

\(
V'(2,4) = 2^4
\)

Desarrollamos:

\(
2^4 = 2 \cdot 2 \cdot 2 \cdot 2
\)

\(
2^4 = 16
\)

### Resultado final:

\(
V'(2,4) = 16
\)

<hr>

**21.** 
<!-- C(10,3) = v(10,3) / P3 = 10 x 9 x 8 / 3 x 2 x1 = 720/6 = 120 -->
10 empleados, turnos rotativos equitativos. Coinciden 3, dentro de cuántos domingos vuelve a coincidir?.

\(
C(10,3) = \frac{V(10,3)}{P_3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120
\)

 <hr> 

# Probabilidad

Probabilidad es el estudio de experimentos aleatorios, es decir aquellos experimentos de los cuales no es posible predecir el resultado. Una situación donde interviene el azar es un experiemto aleatorio si: 

+ Conocemos los resultados posibles
+ No podemos predecir el resultado
+ Lo podemos realizar tantas veces como se quiera, en las misma condiciones.

Supongamos que repetimos el experimento de lanzar un dado; sea ese el número en veces en que un 6 aparece y sea n el número de veces que se lanzó el dado. Se sabe la relación f= s/n llamada frecuencia relativa tiende a establilizarse a la larga. Esta estabilidad es la base de la tería de probabilidad.


## Espacio Muestral

Es el conjunto de los resultados posibles de un experimento aleatorio. Lo designamos con la letra E.

## Suceso

cada subconjunto de un espacio muestral se denomina suceso. Los sucesos pueden darse por extensión, es decir, nombrando a cada elemento, o por comprensión, estableciendo alguna propiedad que los caracterize.


### Ejemplo: 
Una bolsa contiene 10 bolillas numeradas: 
+ las bolillas 1, 2 y 3 son rojas..
+ las bolillas 4, 5 y 6 son azules.
+ las 8, 9, 10 son verdes

Extraemos una al azar

E= {r1, r2, r3, a4, a5, a6, a7, v8, v9, v10}

A= La bolilla que se extrjo no es roja"
A= {a4, a5, a6, a7, v8,v9,v10}

B={r2,a4,a6,v8,v10}
B="La bolilla exrtaida es par"

C="La bolilla que extrae es negra"


\(
C=\emptyset
\)
C= {}


## Problema

Una urna contiene 3 bolillas blancas y dos bolillas negras. Se considera el experimento aleatorio que consiste en sacar 3 bolillas de la urna, una tras otra y sin devolverla a la misma.

A. Halla el espacio muestral de este experiemnto
B. Nombra por extensión los siguientes sucesos: 

A= "La última bolilla extraida es blanca"
B= "Se sacaron al menos 2 bolillas blancas"
C= "No se sacaron dos bolillas seguidas del mismo color"
D= "Las tres bolillas resultaron negras"


### A. Espacio muestral

\(
S = \{BBB,\; BBN,\; BNB,\; BNN,\; NBB,\; NBN,\; NNB\}
\)

<hr>

### B. Sucesos por extensión

\(
A = \{BBB,\; BNB,\; NBB,\; NNB\}
\)

\(
B = \{BBB,\; BBN,\; BNB,\; NBB\}
\)

\(
C = \{BNB,\; NBN\}
\)

\(
D = \emptyset
\)

<hr>

### Operaciones entre sucesos
<!-- AUB -->
\(
A \cup B 
\)
Es el suceso que sucede si se cumple alguna de ellas o ambas a la vez.
<!-- AnB -->
\(
A \cap B
\)

Es el suceso que sucede si ambos sucesos ocurren a la vez
<!-- A' -->
\(
A' 
\)
Es el suceso que se cumple si A no se cumple

## Probabilidad de Laplace

Si A es un suceso asociado a una experimento aleatorio, con un espacio muestral finito y con resultsdos igualmente posibles definimos a la probabilidad como el siguiente cociente:


<!-- P(A)= Nº de casos favorables / Nº  casos posibles -->

\(
P(A) = \frac{\text{Nº de casos favorables}}{\text{Nº de casos posibles}}
\)

### Problemas

1. ¿cual es la probabilidad de Mariela y Lucía resulten seleccionadas en un concurso del que participan junto con otras 10 chicas más y en el que a través de un sorteo 2 de ellas ganarán el viaje?

2. En un armario hay 15 probetas, de las cualesa hay 10 que fueron fabricadas por X. Si se eligen 5 probetas al azar.  ¿Cuál es la probabilidad de que 3 de ellas hayan sido fabricadas por X?

### Respuestas
**1.**
#### Paso 1: Total de participantes

\(
12 \text{ chicas}
\)



#### Paso 2: Casos posibles

Se eligen 2 ganadoras de 12:

\(
C(12,2) = \frac{12 \cdot 11}{2 \cdot 1} = 66
\)



#### Paso 3: Casos favorables

Solo hay 1 forma de que ganen Mariela y Lucía:

\(
C(2,2) = 1
\)


#### Paso 4: Probabilidad

\(
P = \frac{1}{66}
\)

<hr>

**2.**
#### Paso 1: Total de probetas

\(
15 \text{ probetas} \Rightarrow 10 \text{ de X y 5 de otras}
\)


#### Paso 2: Casos posibles

Se eligen 5 probetas de 15:

\(
C(15,5)
\)


#### Paso 3: Casos favorables

Elegir 3 de X y 2 de las otras:

\(
C(10,3) \cdot C(5,2)
\)


#### Paso 4: Probabilidad

\(
P = \frac{C(10,3)\cdot C(5,2)}{C(15,5)}
\)


#### Paso 5: Cálculo

\(
C(10,3) = 120,\quad C(5,2) = 10,\quad C(15,5) = 3003
\)

\(
P = \frac{120 \cdot 10}{3003} = \frac{1200}{3003}
\)



