# EJERCICIOS SVM – Daniel Puente 

## Ejercicio 1

### ¿Qué es un modelo de clasificación SVM y cuál es el principio fundamental en el que se basa para separar las clases de datos?

Un algoritmo de aprendizaje supervisado llamado **modelo de clasificación SVM** tiene como objetivo hallar un **hiperplano o frontera de decisión ideal** que divida las clases de datos de la mejor manera posible.  
La idea fundamental es **maximizar la separación entre las clases**, encontrando el hiperplano que establezca la mayor distancia posible entre los puntos de una clase y los de la otra.  
Se les conoce como **vectores soporte** a los puntos que están más cerca del borde y son los que definen la ubicación del hiperplano.

---

### ¿Qué función cumple la instrucción `make_blobs()` y por qué es útil para este tipo de prácticas de aprendizaje supervisado?

Para crear conjuntos de datos sintéticos que se agrupan en “blobs” o “nubes”, se utiliza la función **`make_blobs()`**.  
Esto posibilita la creación de datos linealmente separables (o no) de manera simple, lo cual facilita experimentar con el comportamiento del SVM.

---

### En el modelo `svm.SVC(kernel='linear', C=1000)`, ¿qué representan los parámetros *kernel* y *C*, y cómo afectan al comportamiento del clasificador?

- El parámetro **kernel='linear'** indica que el modelo utilizará una frontera de decisión lineal (una recta en 2D o un plano en dimensiones mayores).  
- El parámetro **C** controla el grado de penalización por errores:  
  - Un valor de **C alto (como 1000)** obliga al modelo a clasificar correctamente casi todos los puntos, lo que puede llevar al **sobreajuste**.

---

### ¿Qué información devuelve el método `clf.decision_function(xy)` y cómo se utiliza para representar las fronteras de decisión y los márgenes del modelo?

El método **`decision_function(xy)`** devuelve el **valor de la función de decisión** del SVM para cada punto del espacio.  
Estos valores indican la **distancia al hiperplano**:

- Valores positivos → un lado del hiperplano.  
- Valores negativos → el otro lado.  
- Valores cercanos a 0 → puntos sobre el borde o margen.

Esto permite dibujar las **fronteras de decisión y los márgenes** del modelo de forma visual.

---

### ¿Qué son los “vectores soporte” (`clf.support_vectors_`) y qué papel juegan en la construcción de la frontera de decisión del SVM?

Los **vectores soporte** son los puntos del conjunto de datos que se encuentran más cerca del hiperplano de separación.  
Son **fundamentales**, ya que **determinan directamente la posición y orientación del hiperplano**.  
El modelo ajusta la frontera para que quede a la máxima distancia posible de estos vectores, y **solo ellos** influyen en la definición del margen.

---

### ¿Por qué se utiliza una malla de puntos (`np.meshgrid`) para evaluar la función de decisión y cómo se relaciona esto con la visualización del modelo?

La función **`np.meshgrid`** genera una rejilla de puntos en el plano que cubre el rango de los datos.  
Esta rejilla se pasa a la función de decisión para calcular el valor del modelo en cada punto del espacio, lo que **permite dibujar las fronteras de decisión y los márgenes** de forma visual y continua en el gráfico.

---

### En términos de generalización del modelo, ¿qué podría ocurrir si se usara un valor de *C* demasiado alto o demasiado bajo, y por qué?

- Si **C es demasiado alto**, el modelo intenta clasificar todos los puntos correctamente, incluso los que son ruido o atípicos → **sobreajuste** (el modelo generaliza mal).  
- Si **C es demasiado bajo**, el modelo tolera más errores → **subajuste**, con una frontera demasiado simple que no refleja bien la verdadera separación entre clases.

---

## Ejercicio 2

### ¿Cuál es el objetivo del modelo SVM en esta práctica y por qué se utilizan únicamente dos especies del conjunto de datos “Iris”?

El objetivo es entrenar un modelo SVM que **clasifique el tipo de flor**, diferenciando entre **Iris versicolor** e **Iris virginica** a partir de las medidas de los sépalos.  
Solo se usan estas dos especies para convertir el problema en una **clasificación binaria**, lo que facilita la interpretación y la visualización de la frontera de decisión.

---

### ¿Qué representan las variables *X* y *y* después de filtrar los datos (`y != 0`) y seleccionar solo las dos primeras columnas (`:2`)?

- **X** contiene las dos primeras columnas del dataset, que corresponden a las medidas de los sépalos:  
  - longitud del sépalo (*sepal length*)  
  - anchura del sépalo (*sepal width*)  
- **y** son las etiquetas de clase (0, 1 o 2).  
  Al aplicar `y != 0`, se eliminan las flores *setosa* (etiqueta 0), quedando solo *versicolor* (1) y *virginica* (2).  

En resumen:  
**X** son las características numéricas y **y** las clases binarias para entrenar el modelo.

---

### ¿Por qué es importante dividir el conjunto de datos en entrenamiento y test, y qué proporciones se utilizan en este código?

Dividir los datos permite **evaluar la capacidad de generalización** del modelo, comprobando si el SVM aprende patrones reales y no solo memoriza los datos.  
En este caso, el código usa una división de **90 % entrenamiento / 10 % test**.  
Así, la mayor parte se usa para entrenar y una pequeña fracción para medir su rendimiento en datos nuevos.

---

### El código utiliza tres tipos de kernel: `linear`, `rbf` y `poly`.  
Explica brevemente qué tipo de frontera de decisión genera cada uno y cuándo puede ser más apropiado usar cada caso.

- **Linear:** genera una frontera recta. Ideal cuando los datos son linealmente separables.  
- **RBF:** genera fronteras curvas y flexibles. Ideal cuando la separación no es lineal.  
- **Poly:** crea fronteras polinómicas (curvas o giros según el grado). Útil si la relación entre variables tiene forma polinómica.

---

### ¿Qué función cumple `clf.decision_function()` y cómo se utiliza su resultado para visualizar las regiones de clasificación en el gráfico?

La función **`clf.decision_function()`** calcula la **distancia de cada punto al límite de decisión**.  
Sus valores se usan para **colorear las regiones de clasificación** y dibujar las **fronteras y márgenes** con funciones como `plt.pcolormesh()` y `plt.contour()`.

---

### ¿Por qué se usa una malla (`np.mgrid`) para representar las zonas de decisión del modelo?  
¿Qué ventajas tiene frente a representar solo los puntos de datos?

La malla crea una rejilla de puntos que cubre todo el espacio de las variables, permitiendo visualizar **de forma continua** las zonas de clasificación.  
Esto ofrece una **frontera clara y completa**, mientras que solo mostrar los puntos no permite ver cómo el modelo separa realmente las clases.

---

### ¿Qué diferencias se pueden observar al comparar los resultados visuales de los tres kernels?  
¿Qué conclusiones se pueden extraer sobre la complejidad del modelo y el riesgo de sobreajuste?

- **Lineal:** frontera recta, simple y estable.  
- **RBF:** fronteras curvas, alto ajuste, posible sobreajuste.  
- **Polinomial:** equilibrio entre simplicidad y flexibilidad.  

En resumen:  
Cuanto más **complejo** es el kernel, mayor capacidad tiene el modelo para adaptarse, pero también **aumenta el riesgo de sobreajuste** y de fallar al predecir datos nuevos.
