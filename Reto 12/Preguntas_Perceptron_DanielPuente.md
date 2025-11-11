# Ejercicio 01 de Redes Neuronales

A continuación se presentan las preguntas y respuestas correspondientes al ejercicio 01 de redes neuronales, organizadas en formato claro y limpio para incluir en tu repositorio de GitHub.

---

## 1. ¿Qué representa un perceptrón dentro de una red neuronal y qué tipo de problemas puede resolver?
Un perceptrón es la unidad básica de una red neuronal. Recibe varias entradas (por ejemplo, atributos `x1, x2, x3`), aplica a cada una un peso (`w1, w2, w3`), suma el resultado y pasa esa suma por una función de activación. El perceptrón actúa como clasificador lineal, capaz de separar datos cuando una línea (o hiperplano) puede dividir correctamente las clases. Solo puede solucionar problemas linealmente separables.

---

## 2. ¿Cuál es el papel de los pesos en el perceptrón y cómo influyen en la salida final?
Los pesos determinan la influencia de cada entrada en la neurona. Para datos `X = [x1, x2, x3]` y pesos `W = [w1, w2, w3]`, el perceptrón calcula:

```
s = w1*x1 + w2*x2 + w3*x3
```

La salida `y` depende directamente de esos pesos. Modificarlos cambia la frontera de decisión del modelo, es decir, la forma en que clasifica los datos.

---

## 3. Cambia los valores de los pesos y analiza cómo varía la salida `y`. ¿Qué interpretación tiene este cambio?
Ejemplo en código:

```python
# Ejemplo base
W = [1, 0.4, 0.3]
print(perceptron(W, X))

# Cambiando pesos
otro_W = [0.5, 1, 0.1]
print(perceptron(otro_W, X))
```

Al cambiar los pesos:
- Si un peso aumenta, ese input tiene mayor impacto en la suma y en la salida.
- Si se reduce o coloca en cero, ese input afecta menos o nada.

Esto muestra cómo el modelo ajusta la importancia de cada atributo para clasificar datos.

---

## 4. ¿Por qué se utiliza una función de activación (como tanh) y qué ventajas tiene frente a una función lineal?
La función de activación introduce no linealidad, permitiendo que la red neuronal aprenda patrones complejos. Usar funciones como `tanh` o `sigmoide` limita el rango de la salida, estabiliza el aprendizaje y permite ajustar pesos de manera más efectiva. Sin una función de activación, el modelo sería una regresión lineal incapaz de resolver problemas no lineales.

---

## 5. Representa gráficamente la función tanh(s) y explica su comportamiento
Código utilizado:

```python
import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(-5, 5, 100)
plt.plot(s, np.tanh(s))
plt.title('Función tanh(s)')
plt.xlabel('s')
plt.ylabel('tanh(s)')
plt.grid(True)
plt.show()
```

Comportamiento:
- Para valores grandes positivos, `tanh(s)` tiende a 1.
- Para valores grandes negativos, tiende a -1.
- Cerca de cero, la salida es casi proporcional a `s`.

---

## 6. Diferencias entre tanh, sigmoide y ReLU

| Función | Rango | Comportamiento |
|--------|--------|----------------|
| tanh | -1 a 1 | Simétrica y centrada en cero |
| sigmoide | 0 a 1 | Asimétrica y no centrada |
| ReLU | 0 a ∞ | Lineal para positivos, salida no acotada |

- `tanh`: adecuada para valores positivos y negativos, aunque se satura.
- `sigmoide`: ideal para probabilidades, pero se satura más.
- `ReLU`: acelera el entrenamiento, evita gradiente desaparecido.

---

## 7. Sustituye tanh por sigmoide o ReLU y compara resultados
Para sigmoide:

```python
def perceptron_sigmoid(W, X):
    s = np.sum(W * X)
    return 1 / (1 + np.exp(-s))
```

Para ReLU:

```python
def perceptron_relu(W, X):
    s = np.sum(W * X)
    return max(0, s)
```

Diferencias:
- Sigmoide produce valores entre 0 y 1.
- ReLU devuelve 0 para valores negativos y acelera el entrenamiento.

---

## 8. ¿Cómo extender este modelo a una red con varias capas (MLP)?
Un perceptrón multicapa agrega una o más capas ocultas. Cada capa tiene varias neuronas con sus propios pesos. Las salidas de una capa son entradas para la siguiente. Esto permite resolver problemas no lineales complejos.

---

## 9. Añade un término de sesgo (bias) al modelo y explica su efecto
El sesgo permite desplazar la frontera de decisión:

```
s = w1*x1 + w2*x2 + w3*x3 + b
```

Este parámetro evita que la red dependa únicamente del origen y mejora la capacidad de clasificación.

---

## 10. Modificar el código para procesar múltiples entradas (matriz)

```python
X_matrix = np.array([
    [0.9, 0.3, 0.5],
    [0.1, 0.8, 0.5],
    [0.5, 0.5, 0.5],
    [1.0, 0.0, 0.0]
])

outputs = []
for X_vec in X_matrix:
    outputs.append(perceptron(W, X_vec))
```

Cada fila de la matriz es evaluada, generando un vector de salidas.

---

## 11. Comentario sobre pruebas en TensorFlow Playground
- Con datos linealmente separables, una sola neurona suele clasificar correctamente.
- Con datos complejos como espirales o círculos, un perceptrón simple falla.
- Añadir más capas y neuronas mejora la capacidad de aprendizaje.
- El riesgo de sobreajuste aumenta si la red es demasiado grande.

---

Fin del documento.

