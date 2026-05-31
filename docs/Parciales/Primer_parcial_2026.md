# Primer Parcial

## 1)
Los datos que se dan a continuación corresponden a los pesos en Kg. de ochenta personas:

a. Obténgase una distribución de datos en intervalos de amplitud t, siendo el primer intervalo 
`[50;55)`       
b. Calcule el porcentaje de personas de peso menor que 65 Kg.       
c. ¿Cuántas personas tienen peso mayor o igual que 70kg. Pero menor que 85?     

    60 66 77 70 66 68 57 70 66 52 75 65 69 71 58 66 67 74 61

    63 69 80 59 66 70 67 78 75 64 71 81 62 64 69 68 72 83 56

    65 74 67 54 65 65 69 61 67 73 57 62 67 68 63 67 71 68 76

    61 62 63 76 61 67 67 64 72 64 73 79 58 67 71 68 59 69 70

    66 62 63 66

## 2)
En un concurso sobre innovaciones tecnológicas se han presentado 10 equipos con sus ideas. Los equipos compiten entre ellos para elegir un ganador, un segundo y un tercer puesto. ¿Cuántas ternas se pueden formar?

## 3)
¿Cuántos numeros de 3 cifras se pueden formar con los dígitos 0, 1, 2, 3, 4 y 5?

## 4)
En un estudio sobre las preferencias de color sobre la indumentaria, arrojó que el 4% de los hombres y 1% de las mujeres tienen inclinación por el color negro. Además, 60% de los encuestados son mujeres. Ahora bien, si se selecciona al azar una persona encuestada y tiene preferencia por el color negro ¿Cuál es la probabilidad de que esta persona sea mujer?

## 5)

Un banco tiene cinco jóvenes ejecutivos en la casa matriz. Cada año en abril, selecciona al azar uno de estos cinco y lo transfiere como gerente a una de sus filiales. El lugar del elegido lo cubre con un nuevo joven ejecutivo. Calcula la probabilidad de que el joven ejecutivo dado:
a. Permanezca exactamente dos años en la casa matriz
b. Permanezca tres años o menos en la casa matriz


# Resolución - Primer Parcial

## 1) Distribución de pesos

### a) Distribución en intervalos de amplitud 5

Se tienen \(n=80\) observaciones.

| Intervalo | \(f_i\)  | \(f_{ir}\) |
|------------|---------|------------|
| \([50,55)\) | 3      | 0.0375     |
| \([55,60)\) | 7      | 0.0875     |
| \([60,65)\) | 16     | 0.2000     |
| \([65,70)\) | 25     | 0.3125     |
| \([70,75)\) | 16     | 0.2000     |
| \([75,80)\) | 8      | 0.1000     |
| \([80,85)\) | 5      | 0.0625     |
| **Total**   | **80** | **1.0000** |

### Fórmula utilizada

$$
\%=\frac{\text{casos favorables}}{\text{casos totales}}\times100
$$

### b) Porcentaje de personas con peso menor que 65 kg

Cantidad de personas:

$$
3+7+16=26
$$

Porcentaje:

$$
\frac{26}{80}\times100=32.5\%
$$

**Respuesta:** \(32.5\%\)

---

### c) Personas con peso mayor o igual que 70 kg y menor que 85 kg

Corresponde a:

$$
[70,75),\ [75,80),\ [80,85)
$$

Cantidad:

$$
16+8+5=29
$$

**Respuesta:** \(29\) personas.

---

# 2) Formación de ternas

Se elige:

- Primer puesto
- Segundo puesto
- Tercer puesto

Como el orden importa, se utilizan variaciones sin repetición.

### Fórmula utilizada

$$
V(n,r)=\frac{n!}{(n-r)!}
$$

Aplicando:

$$
V(10,3)=\frac{10!}{7!}
$$

$$
V(10,3)=10\cdot9\cdot8
$$

$$
V(10,3)=720
$$

**Respuesta:** \(720\)

---

# 3 Números de tres cifras

Dígitos disponibles:

$$
\{0,1,2,3,4,5\}
$$

### Método

Primera cifra:

$$
5
$$

(No puede ser cero)

Segunda cifra:

$$
6
$$

Tercera cifra:

$$
6
$$

Por el principio multiplicativo:

$$
5\cdot6\cdot6=180
$$

**Respuesta:** \(180\)

---

# 4) Preferencia por el color negro

Definimos:

- \(M\): mujer
- \(H\): hombre
- \(N\): prefiere negro

Datos:

$$
P(M)=0.60
$$

$$
P(H)=0.40
$$

$$
P(N|M)=0.01
$$

$$
P(N|H)=0.04
$$

Se pide:

$$
P(M|N)
$$

### Teorema de Bayes

$$
P(M|N)=\frac{P(N|M)P(M)}{P(N)}
$$

### Probabilidad total

$$
P(N)=P(N|M)P(M)+P(N|H)P(H)
$$

$$
P(N)=0.01(0.60)+0.04(0.40)
$$

$$
P(N)=0.006+0.016
$$

$$
P(N)=0.022
$$

### Aplicando Bayes

$$
P(M|N)=\frac{0.01(0.60)}{0.022}
$$

$$
P(M|N)=\frac{0.006}{0.022}
$$

$$
P(M|N)=0.2727
$$

$$
P(M|N)=27.27\%
$$

**Respuesta:** \(27.27\%\)

---

# 5) Permanencia de un ejecutivo

Cada año:

$$
P(\text{transferido})=\frac15
$$

$$
P(\text{permanece})=\frac45
$$

---

## a) Permanezca exactamente dos años

Debe:

- permanecer el primer año
- ser transferido el segundo

### Fórmula

$$
P(X=2)=\left(\frac45\right)\left(\frac15\right)
$$

$$
P(X=2)=\frac4{25}
$$

$$
P(X=2)=0.16
$$

**Respuesta:** \(16\%\)

---

## b) Permanezca tres años o menos

### Distribución geométrica

$$
P(X=k)=\left(\frac45\right)^{k-1}\left(\frac15\right)
$$

Entonces:

$$
P(X=1)=\frac15
$$

$$
P(X=2)=\frac45\frac15=\frac4{25}
$$

$$
P(X=3)=\left(\frac45\right)^2\frac15=\frac{16}{125}
$$

Sumando:

$$
P(X\le3)=P(X=1)+P(X=2)+P(X=3)
$$

$$
P(X\le3)=\frac15+\frac4{25}+\frac{16}{125}
$$

$$
P(X\le3)=\frac{25+20+16}{125}
$$

$$
P(X\le3)=\frac{61}{125}
$$

$$
P(X\le3)=0.488
$$

$$
P(X\le3)=48.8\%
$$

**Respuesta:** \(48.8\%\)

---

## Respuestas finales

1. a) Tabla de frecuencias obtenida.  
   b) \(32.5\%\)  
   c) \(29\) personas

2. \(720\)

3. \(180\)

4. \(27.27\%\)

5. a) \(16\%\)  
   b) \(48.8\%\)