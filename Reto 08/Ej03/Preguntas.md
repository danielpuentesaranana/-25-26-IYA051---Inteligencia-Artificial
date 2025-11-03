# Preguntas ejercicio 3

---

### ¿Qué tipo de problema de aprendizaje automático se está resolviendo y por qué?

Se trata de un **problema de clasificación supervisada**, donde el objetivo es que el algoritmo aprenda, a partir de ejemplos con etiquetas, a distinguir entre tres tipos de flores (Setosa, Versicolor y Virginica). El modelo utiliza los datos de entrenamiento con las variables conocidas para poder predecir la clase de nuevas muestras desconocidas.

---

### ¿Qué representa el dataset “Iris” y qué tipo de variables contiene?

El dataset Iris es un conjunto clásico en machine learning que contiene 150 muestras de flores. Cada muestra tiene 4 variables numéricas: longitud y anchura del sépalo, longitud y anchura del pétalo. Además, cada muestra está etiquetada con la especie de la flor. Las variables son **numéricas de tipo continuo** y la etiqueta es **categórica**.

---

### Explorar abriendo el fichero en bruto y también con librerías python.

Al abrir el fichero en bruto se pueden ver los valores organizados por columnas, con mediciones y species. Con librerías como `sklearn` o `pandas` se puede cargar el dataset automáticamente, obtener resúmenes estadísticos, visualizar las primeras filas y analizar fácilmente la distribución de las especies y las mediciones de los atributos.

---

### ¿Qué papel cumple el método fit() en el modelo de árbol de decisión?

El método `fit()` es fundamental, ya que se encarga de **entrenar el modelo**. Utiliza los datos de entrada y las etiquetas para crear la estructura del árbol de decisión, aprendiendo los criterios óptimos de clasificación según los patrones presentes en los datos.

---

### ¿Por qué es importante visualizar el árbol de decisión generado con graphviz?

Visualizar el árbol con herramientas como graphviz es muy importante porque permite **entender de manera intuitiva** las decisiones que toma el modelo, verificar en qué puntos realiza las particiones y qué condiciones son relevantes para la clasificación. Así se puede comprobar si el modelo es lógico y mejorar su interpretabilidad.

---

### ¿Qué significa el resultado que devuelve la función predict() en este contexto?

La función `predict()` en este contexto da como resultado la **especie estimada de la flor** para cada conjunto de valores introducidos. Básicamente, asigna una clase (Setosa, Versicolor o Virginica) a cada muestra según lo aprendido en el entrenamiento.

---

### ¿Qué ventajas y desventajas tienen los árboles de decisión frente a kNN algoritmos de clasificación?

- **Ventajas árbol de decisión**: Son modelos intuitivos, rápidos al clasificar, y fáciles de visualizar e interpretar. Permiten ver claramente las operaciones que lleva a cabo el modelo.
- **Desventajas árbol de decisión**: Pueden sobreajustar si tienen demasiadas ramas, y su precisión puede verse superada por otros modelos.
- **Ventajas kNN**: No necesita entrenamiento, basta con almacenar los datos. Suele tener buena precisión si la elección de k es adecuada.
- **Desventajas kNN**: Puede ser lento en predicción para conjuntos grandes, y no ofrece una explicación clara de la clasificación.

---

### Si cambiáramos los valores de entrada (por ejemplo, 4, 2, 1, 0.2), qué crees que ocurriría y por qué?

El modelo aplicaría los criterios aprendidos para esos valores y devolvería la especie más probable según las ramas y cortes del árbol. Si los valores son cercanos a uno de los grupos del dataset original, elegirá ese grupo como predicción; si son extremos o ambiguos, escogerá la especie que el árbol considere más próxima según sus particiones.

