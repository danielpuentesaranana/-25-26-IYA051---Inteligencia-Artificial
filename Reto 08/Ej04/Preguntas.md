# Preguntas ejercicio 4

---

### ¿Qué tipo de problema de aprendizaje automático se está abordando en este caso y cuál es la variable objetivo?

Es un problema de **clasificación supervisada**. El modelo aprende a distinguir, a partir de ejemplos, si una canción estará en el Top de la lista Billboard o no. La variable objetivo es “Top” (1 = sí entra, 0 = no entra).

---

### ¿Por qué es necesario dividir los datos en variables de entrada X y variable objetivo y antes de entrenar el modelo?

Es necesario separar los datos porque el modelo necesita aprender a predecir el valor de la variable objetivo (Top) a partir de las variables de entrada (duración, género, colaboraciones, ranking, popularidad, etc). Así se entrena para encontrar esa relación y posteriormente puede hacer predicciones.

---

### ¿Qué función cumplen los parámetros criterion, min_samples_split, min_samples_leaf, max_depth y class_weight al crear el árbol de decisión?

- **criterion**: Define el método para medir la calidad de la división (“gini” o “entropy”), así el árbol decide cómo separar mejor los datos.
- **min_samples_split**: Número mínimo de muestras para dividir un nodo, evita ramas con muy pocos datos.
- **min_samples_leaf**: Número mínimo de muestras en una hoja, ayuda a evitar hojas demasiado pequeñas.
- **max_depth**: Profundidad máxima del árbol, controla el número de divisiones (complexidad) y limita sobreajuste.
- **class_weight**: Permite dar más importancia a una clase (por ejemplo, “Top”) en el aprendizaje, útil si los datos están desequilibrados.

---

### ¿Por qué se utiliza el parámetro class_weight={1:3.5} en este ejercicio?

Se usa para **dar más peso** a la clase “1” (canciones Top). Así el árbol prestará más atención a los ejemplos de canciones exitosas, ayudando a predecir mejor aunque haya menos ejemplos de ese tipo en los datos.

---

### ¿Qué significa la precisión (accuracy) del modelo y cómo se calcula en el código?

La **precisión (accuracy)** indica el porcentaje de predicciones correctas sobre el total de casos. Se calcula comparando las predicciones del modelo con los valores reales del test, usando por ejemplo `metrics.accuracy_score(y_test, y_pred)`. Mide qué tan bien acierta el modelo.

---

### ¿Qué diferencia hay entre los métodos predict() y predict_proba()?

- **predict()**: Devuelve directamente la clase asignada (por ejemplo, Sí o No Top).
- **predict_proba()**: Devuelve el porcentaje o probabilidad de pertenecer a cada clase (por ejemplo, 80% Top, 20% No Top), útil para saber el grado de certeza.

---

### ¿Qué implicaciones tiene que el árbol tenga una profundidad máxima (max_depth = 4)?

Limitar la profundidad máxima a 4 evita que el árbol se vuelva demasiado complejo y se sobreajuste a los datos de entrenamiento. Así se obtiene un modelo más general, que funciona mejor para casos nuevos, aunque a veces el resultado puede ser menos preciso para los ejemplos del entrenamiento.
