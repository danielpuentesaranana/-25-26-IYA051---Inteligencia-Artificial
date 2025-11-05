# Preguntas Ejercicio 1: Regresión Logística

---

## 1. ¿Qué tipo de problema de aprendizaje supervisado se está resolviendo en esta práctica y por qué?

Se está resolviendo un **problema de clasificación supervisada multiclase**. El objetivo es asignar cada usuario a una de las tres categorías de sistemas operativos (Windows, Mac, Linux) basándose en sus características de uso. Es supervisado porque contamos con datos etiquetados de entrenamiento donde ya conocemos la clase real de cada usuario, lo que permite al modelo aprender patrones y aplicarlos a nuevos casos.

---

## 2. ¿Por qué la regresión logística es apropiada para un problema de clasificación multiclase?

La regresión logística, aunque originalmente diseñada para clasificación binaria, se extiende a problemas multiclase mediante estrategias como **One-vs-Rest (OvR)** o **multinomial**. Calcula probabilidades para cada clase y selecciona aquella con mayor probabilidad. Es apropiada porque:
- Es computacionalmente eficiente
- Proporciona probabilidades interpretables
- Funciona bien cuando las clases son linealmente separables
- Ofrece resultados estables y reproducibles

---

## 3. ¿Qué significan las variables independientes (duración, páginas, acciones y valoración) en el contexto del modelo?

Estas variables representan características del comportamiento del usuario en una sesión web:
- **Duración:** tiempo total de la sesión de navegación
- **Páginas:** número de páginas visitadas durante la sesión
- **Acciones:** cantidad de interacciones realizadas (clics, formularios, etc.)
- **Valoración:** puntuación o calificación asignada por el usuario

Estas características permiten al modelo identificar patrones de uso asociados a cada sistema operativo, ya que usuarios de diferentes plataformas pueden mostrar comportamientos distintivos.

---

## 4. ¿Cómo se interpreta el resultado de la predicción 2 en el modelo entrenado?

El resultado de predicción **2** indica que el modelo ha clasificado al usuario en la **clase 2**, que según la codificación típica del dataset correspondería a uno de los tres sistemas operativos (por ejemplo, Linux si la codificación es: 0=Windows, 1=Mac, 2=Linux). Esta predicción se basa en que las características introducidas tienen mayor similitud con los patrones aprendidos para esa clase durante el entrenamiento.

---

## 5. ¿Qué diferencias existen entre los conceptos de precisión, recuperación (recall) y f1-score en el informe de clasificación?

- **Precisión (Precision):** Del total de predicciones positivas para una clase, ¿cuántas fueron correctas? Mide la exactitud de las predicciones positivas.
  - Fórmula: `VP / (VP + FP)`
  
- **Recuperación (Recall):** Del total de casos reales de una clase, ¿cuántos fueron correctamente identificados? Mide la capacidad de encontrar todos los casos positivos.
  - Fórmula: `VP / (VP + FN)`
  
- **F1-Score:** Media armónica entre precisión y recall. Proporciona un balance entre ambas métricas, siendo especialmente útil cuando las clases están desbalanceadas.
  - Fórmula: `2 × (Precisión × Recall) / (Precisión + Recall)`

---

## 6. ¿Qué representa cada celda en la matriz de confusión y cómo se calculan los verdaderos y falsos positivos?

La **matriz de confusión** es una tabla que compara las predicciones del modelo con las clases reales:

|                | Pred. Clase 0 | Pred. Clase 1 | Pred. Clase 2 |
|----------------|---------------|---------------|---------------|
| **Real Clase 0** | VP₀ (aciertos) | Error        | Error        |
| **Real Clase 1** | Error        | VP₁ (aciertos) | Error        |
| **Real Clase 2** | Error        | Error        | VP₂ (aciertos) |

- **Diagonal principal:** Verdaderos Positivos (predicciones correctas)
- **Fuera de diagonal:** Errores de clasificación (Falsos Positivos y Falsos Negativos)

Para cada clase:
- **Verdaderos Positivos (VP):** casos correctamente clasificados como esa clase
- **Falsos Positivos (FP):** casos incorrectamente clasificados como esa clase
- **Falsos Negativos (FN):** casos de esa clase que fueron clasificados en otra

---

## 7. ¿Por qué es importante dividir el conjunto de datos en entrenamiento (80%) y prueba (20%)?

La división es fundamental por varias razones:
- **Evitar sobreajuste:** Si evaluáramos con los mismos datos usados para entrenar, el modelo podría simplemente "memorizar" los ejemplos sin aprender patrones generalizables
- **Validación real:** El conjunto de prueba simula datos nuevos nunca vistos, permitiendo medir el verdadero rendimiento del modelo
- **Estimación honesta:** Proporciona una métrica realista de cómo funcionará el modelo en producción con datos reales

La proporción 80/20 es un estándar que balancea tener suficientes datos para entrenar y suficientes para evaluar de forma significativa.

---

## 8. ¿Qué función cumple el parámetro random_state=7 en la división de los datos?

El parámetro **random_state=7** fija la semilla del generador de números aleatorios, garantizando que:
- La división entrenamiento/prueba sea **reproducible**: ejecutar el código varias veces produce exactamente la misma partición
- Los resultados sean **comparables**: permite que diferentes personas o experimentos trabajen con los mismos subconjuntos
- Los experimentos sean **verificables**: facilita la depuración y validación científica del trabajo

El valor específico (7) no tiene significado especial; cualquier número entero serviría para el mismo propósito.

---

## 9. Si se agregara una nueva característica (por ejemplo, "tiempo medio por página"), ¿cómo se modificaría el código para incluirla en el modelo?

Bastaría con añadir esa columna al CSV y asegurarse de que aparece en el DataFrame. El código de selección de variables ya la utilizaría automáticamente para entrenar y predecir, sin ningún ajuste extra salvo en las predicciones individuales.
