# Unidad 2 - Técnicas de conteo

## 10.
+ S -> C -> R -> N
+ N -> S -> C -> R
+ S -> N -> C -> R
+ S -> C -> N -> R
+ N: 1 al 9



Entonces:  **Resultado:** N x 4; 9 x 4 = 36

 <hr

## 13. Numero de 5 cifras con 1,2,4,6,8 y dos 8
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

## 15. 
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

## 21. 
<!-- C(10,3) = v(10,3) / P3 = 10 x 9 x 8 / 3 x 2 x1 = 720/6 = 120 -->
10 empleados, turnos rotativos equitativos. Coinciden 3, dentro de cuántos domingos vuelve a coincidir?.

\(
C(10,3) = \frac{V(10,3)}{P_3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120
\)

 <hr> 

## 27.

La probabilidad de que las 4 cartas extraídas sean de palos diferentes se calcula como:
Sin reposición
\(
P=\frac{C(10,1)\cdot C(10,1)\cdot C(10,1)\cdot C(10,1)}{C(40,4)}
\)

donde:

- \( C(40,4) \) representa la cantidad total de maneras de elegir 4 cartas de una baraja de 40.
- Cada \( C(10,1) \) representa elegir 1 carta de un palo específico, ya que cada palo tiene 10 cartas.

Como hay 4 palos, debemos elegir:

- 1 carta del primer palo,
- 1 carta del segundo palo,
- 1 carta del tercer palo,
- 1 carta del cuarto palo.

Por eso multiplicamos:

\(
C(10,1)\cdot C(10,1)\cdot C(10,1)\cdot C(10,1)
\)

Esto cuenta todos los casos favorables donde las 4 cartas pertenecen a palos distintos.

Desarrollando:

\(
C(10,1)=10
\)

Entonces:

\(
P=\frac{10\cdot10\cdot10\cdot10}{C(40,4)} =\frac{10000}{91390}
\)

\(
P\approx 0.1094421
\)

Por lo tanto, la probabilidad es aproximadamente:

\(
10.94\%
\) 
<hr>

En el caso con reposición, después de sacar cada carta, esta vuelve al mazo.  
Por eso, en cada extracción siempre hay 40 cartas posibles.

La probabilidad de obtener 4 palos distintos puede plantearse como:

\(
P=\frac{C(10,1)\cdot C(10,1)\cdot C(10,1)\cdot C(10,1)\cdot 4!}{40^4}
\)

donde:

- \( C(10,1) \) representa elegir 1 carta de cada palo.
- Como hay 4 palos, aparece cuatro veces.
- \( 4! \) cuenta todas las formas posibles de ordenar esos 4 palos.
- \( 40^4 \) representa todos los posibles resultados al hacer 4 extracciones con reposición.

Sabemos que:

\(
C(10,1)=10
\)

Entonces:

\(
P=\frac{10\cdot10\cdot10\cdot10\cdot4!}{40^4}
\)

\(
P=\frac{10000\cdot24}{40^4}
\)

Como:

\(
40^4=2560000
\)

queda:

\(
P=\frac{240000}{2560000}
\)

\(
P=0.09375
\)

Por lo tanto:

\(
P=9.375\%
\)

### Explicación

El numerador cuenta los casos favorables:

- Elegimos una carta de cada palo.
- Luego multiplicamos por \( 4! \) porque esos 4 palos pueden aparecer en cualquier orden.

El denominador cuenta todos los posibles resultados con reposición:

- En cada extracción hay 40 posibilidades.
- Como se hacen 4 extracciones independientes:

\(
40\cdot40\cdot40\cdot40=40^4
\)

Por eso el resultado es menor que en el caso sin reposición.
<hr>

## 33. 

Armar Grupo 2 pediatras y un clínico
Disponible
+ 10 pediatras
+ 7 clínicos

Prob de qué Dr P y Dr S no estén juntos

<!-- C(2,0) . C (8,2) . C(7,1) + C(2,1) . C(8,1) . C(7,1) / C(10,2) . C(7,1) = 44/45-->

Total de formas de elegir el grupo:

\(
C(10,2)\cdot C(7,1)
\)

donde:

- \( C(10,2) \): elegir 2 pediatras entre 10.
- \( C(7,1) \): elegir 1 clínico entre 7.

---

Casos favorables: que **Dr P y Dr S no aparezcan juntos**.

Esto puede ocurrir de dos maneras:

### Caso 1: Ninguno de los dos entra

Elegimos los 2 pediatras entre los otros 8.

\(
C(2,0)\cdot C(8,2)\cdot C(7,1)
\)

### Caso 2: Solo entra uno de ellos

- Elegimos 1 entre Dr P y Dr S.
- Elegimos 1 pediatra adicional entre los otros 8.
- Elegimos 1 clínico.

\(
C(2,1)\cdot C(8,1)\cdot C(7,1)
\)

---

Entonces:

\(
P=\frac{C(2,0)\cdot C(8,2)\cdot C(7,1)+C(2,1)\cdot C(8,1)\cdot C(7,1)}{C(10,2)\cdot C(7,1)}
\)

Calculando:

\(
C(8,2)=28
\)

\(
C(2,1)=2
\)

\(
C(8,1)=8
\)

\(
C(10,2)=45
\)

Entonces:

\(
P=\frac{1\cdot28\cdot7+2\cdot8\cdot7}{45\cdot7}
\)

\(
P=\frac{196+112}{315}
\)

\(
P=\frac{308}{315}
\)

\(
P=\frac{44}{45}
\)

Por lo tanto, la probabilidad de que **Dr P y Dr S no estén juntos** es:

\(
\frac{44}{45}\approx0.9778
\)

o aproximadamente:

\(
97.78\%
\)


### Ejemplo Tablas
|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 7 | 2 | 4 | 1 | 2 | 1 | 5 | 4 | 3 |
| 6 | 2 | 6 | 1 | 0 | 2 | 4 | 7 | 5 | 1 |

