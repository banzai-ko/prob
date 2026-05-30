# Modelo 2

## 1. 

Un postulante que se somete a una  entrevista laboral debe realizar un examen psicofísico con 10 preguntas para ser aceptado. Se desea saber: a. ¿Cuantos exámenes podrá evaluar el analista de RRHH para aceptar el postulante? Justificar



Exámenes que cumplen la condición de aprobación.

Si la condición es:

\(
\text{aprobar con al menos 7 respuestas correctas}
\)

casos favorables:

- exactamente 7 correctas
- exactamente 8 correctas
- exactamente 9 correctas
- exactamente 10 correctas

Usamos combinatoria:


### Cálculo de las combinaciones

Usamos la fórmula de combinaciones:

\(
C(n,m)=\frac{n!}{m!(n-m)!}
\)

Donde:

- \(n\): total de elementos
- \(m\): elementos que se eligen
- \(!\): factorial

---

### 1) Casos con 7 respuestas correctas

\(
C(10,7)=\frac{10!}{7!(10-7)!}
\)

\(
C(10,7)=\frac{10!}{7!3!}
\)

Desarrollamos:

\(
10!=10 \cdot 9 \cdot 8 \cdot 7!
\)

Entonces:

\(
C(10,7)=\frac{10 \cdot 9 \cdot 8 \cdot 7!}{7!(3 \cdot 2 \cdot 1)}
\)

Simplificamos \(7!\):

\(
C(10,7)=\frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1}
\)

\(
C(10,7)=\frac{720}{6}
\)

\(
C(10,7)=120
\)

---

### 2) Casos con 8 respuestas correctas

\(
C(10,8)=\frac{10!}{8!(10-8)!}
\)

\(
C(10,8)=\frac{10!}{8!2!}
\)

Desarrollamos:

\(
10!=10 \cdot 9 \cdot 8!
\)

Entonces:

\(
C(10,8)=\frac{10 \cdot 9 \cdot 8!}{8!(2 \cdot 1)}
\)

Simplificamos \(8!\):

\(
C(10,8)=\frac{10 \cdot 9}{2}
\)

\(
C(10,8)=45
\)

---

### 3) Casos con 9 respuestas correctas

\(
C(10,9)=\frac{10!}{9!(10-9)!}
\)

\(
C(10,9)=\frac{10!}{9!1!}
\)

Desarrollamos:

\(
10!=10 \cdot 9!
\)

Entonces:

\(
C(10,9)=\frac{10 \cdot 9!}{9!}
\)

Simplificamos:

\(
C(10,9)=10
\)

---

### 4) Casos con 10 respuestas correctas

\(
C(10,10)=\frac{10!}{10!(10-10)!}
\)

\(
C(10,10)=\frac{10!}{10!0!}
\)

Sabemos que:

\(
0!=1
\)

Entonces:

\(
C(10,10)=1
\)

---

### Total de formas de aprobar

\(
120+45+10+1=176
\)

Respuesta final:

\(
\boxed{176}
\)

## 2. 
Una clase consta de seis varones y diez mujeres la tercera parte del primer grupo y la quinta parte del segundo usan anteojos. Se pide:

+ a. Realizar el diagrama de venn
+ b. La prob de que un alumno seleccionado al azar use anteojos o sea mujer.
+ c. La prob de que un alumno seleccionado al azar sea varón y no use anteojos.


Datos:

- Total de alumnos:

\(
16
\)

- Varones:

\(
6
\)

- Mujeres:

\(
10
\)

- Varones con anteojos:

\(
2
\)

- Mujeres con anteojos:

\(
2
\)

Entonces:

- Total que usan anteojos:

\(
2+2=4
\)

- Varones sin anteojos:

\(
6-2=4
\)

---
### b) Probabilidad de que un alumno use anteojos o sea mujer

Sea:

- \(A\): “usa anteojos”
- \(V\): “es varón”

Entonces:

\(
\overline{V}
\)

representa “ser mujer”.

Queremos calcular:

\(
P(A \cup \overline{V})
\)

Usamos:

\(
P(A \cup \overline{V})=P(A)+P(\overline{V})-P(A \cap \overline{V})
\)

#### Datos

- Alumnos con anteojos:

\(
4
\)

- Mujeres:

\(
10
\)

- Mujeres con anteojos:

\(
2
\)

Entonces:

\(
P(A)=\frac{4}{16}
\)

\(
P(\overline{V})=\frac{10}{16}
\)

\(
P(A \cap \overline{V})=\frac{2}{16}
\)

#### Sustituyendo

\(
P(A \cup \overline{V})=\frac{4}{16}+\frac{10}{16}-\frac{2}{16}
\)

\(
P(A \cup \overline{V})=\frac{12}{16}
\)

\(
P(A \cup \overline{V})=\frac{3}{4}
\)

#### Respuesta

\(
\boxed{\frac{3}{4}}
\)

### c) Probabilidad de que un alumno seleccionado al azar sea varón y no use anteojos

Sea:

- \(V\): “ser varón”
- \(A\): “usar anteojos”

“No usar anteojos” se representa por:

\(
\overline{A}
\)

Queremos calcular:

\(
P(V \cap \overline{A})
\)

#### Datos

- Varones totales:

\(
6
\)

- Varones con anteojos:

\(
2
\)

Entonces, varones sin anteojos:

\(
6-2=4
\)

Total de alumnos:

\(
16
\)

#### Cálculo

\(
P(V \cap \overline{A})=\frac{4}{16}
\)

\(
P(V \cap \overline{A})=\frac{1}{4}
\)

#### Respuesta

\(
\boxed{\frac{1}{4}}
\)

## 3)

Uno de cada 25 adultos de cierta población está afectado de una enfermedad para la cual se ha desarrollado una prueba diagnóstica. La prueba es tal que, cuando un individuo padece la enfermedad, el resultado es positivo en un 98% de las veces, mientras que un individuo sano tendrá un resutado positivo solamente el 3% de las veces. Eligiendo un individuo al azar de esta poblacion:

### a. Realizar la figura del análisis
### b. Hallar la prob de que el test de positivo
### c. Hallar la prob de que padezca la enfermedad, sabiendo que el resultado fue positivo


Sea:

- \(E\): “tener la enfermedad”
- \(P\): “dar positivo en el test”

Datos:

\(
P(E)=\frac{1}{25}=0.04
\)

\(
P(\overline{E})=1-0.04=0.96
\)

\(
P(P \mid E)=0.98
\)

\(
P(P \mid \overline{E})=0.03
\)

Queremos calcular:

\(
P(P)
\)
### Fórmula de probabilidad total

Si \(A_1, A_2, \dots, A_n\) forman una partición del espacio muestral, entonces:

\(
P(B)=P(B \mid A_1)P(A_1)+P(B \mid A_2)P(A_2)+\cdots+P(B \mid A_n)P(A_n)
\)

o de forma resumida:

\(
P(B)=\sum_{i=1}^{n} P(B \mid A_i)P(A_i)
\)

En este ejercicio:

- \(E\): tener la enfermedad
- \(\overline{E}\): no tener la enfermedad

Entonces:

\(
P(P)=P(P \mid E)P(E)+P(P \mid \overline{E})P(\overline{E})
\)
Usamos la fórmula de probabilidad total:

\(
P(P)=P(P \mid E)\cdot P(E)+P(P \mid \overline{E})\cdot P(\overline{E})
\)

Sustituyendo:

\(
P(P)=0.98\cdot0.04+0.03\cdot0.96
\)

\(
P(P)=0.0392+0.0288
\)

\(
P(P)=0.068
\)

### Respuesta

\(
\boxed{0.068}
\)

o equivalentemente:

\(
\boxed{6.8\%}
\)

### c) Hallar la probabilidad de que padezca la enfermedad sabiendo que el resultado fue positivo

Sea:

- \(E\): “padecer la enfermedad”
- \(P\): “dar positivo”

Datos:

\(
P(E)=0.04
\)

\(
P(\overline{E})=0.96
\)

\(
P(P \mid E)=0.98
\)

\(
P(P \mid \overline{E})=0.03
\)

Primero calculamos:

\(
P(P)
\)

usando probabilidad total:

\(
P(P)=P(P \mid E)P(E)+P(P \mid \overline{E})P(\overline{E})
\)

Sustituyendo:

\(
P(P)=0.98\cdot0.04+0.03\cdot0.96
\)

\(
P(P)=0.0392+0.0288
\)

\(
P(P)=0.068
\)

---

Ahora aplicamos el teorema de Bayes:

\(
P(E \mid P)=\frac{P(P \mid E)P(E)}{P(P)}
\)

Sustituyendo:

\(
P(E \mid P)=\frac{0.98\cdot0.04}{0.068}
\)

\(
P(E \mid P)=\frac{0.0392}{0.068}
\)

\(
P(E \mid P)\approx0.5765
\)

### Respuesta

\(
\boxed{P(E \mid P)\approx0.5765}
\)

o equivalentemente:

\(
\boxed{57.65\%}
\)