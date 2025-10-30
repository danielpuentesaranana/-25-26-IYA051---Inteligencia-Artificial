## Preguntas de Regresión Lineal

### 1.1 ¿Cuál es el objetivo principal de la regresión lineal en este ejercicio?
El objetivo realmente va más allá de trazar una simple línea: lo que buscamos es descubrir hasta qué punto existe una relación directa y consistente entre el aumento de la temperatura media del planeta y la concentración de CO2. Si conseguimos ajustar bien una recta a los datos, podremos no solo entender esta relación, sino también anticipar valores futuros de CO2 con base en predicciones de temperatura, lo que es clave para analizar escenarios de cambio climático.
### 1.2 ¿Qué representan las variables X e y en el código y cómo se formalizan (tipo de estructura de datos)?
En el contexto de este ejercicio, X son los valores de la anomalía de temperatura media anual (esto es, cuánto se desvía la temperatura de la media de referencia), mientras que y indica la concentración correspondiente de CO2 en la atmósfera ese mismo año. En el código, primero estas variables son listas en Python, luego columnas en un DataFrame de pandas, y finalmente, para el modelo, se utilizan como arrays de NumPy, que es la forma esperada por scikit-learn para entrenamiento y predicción.
### 1.3 ¿Qué hace el siguiente código?     regr = LinearRegression()       regr.fit(X_train, y_train)
Primero se crea una instancia del modelo de regresión lineal, es decir, un "modelo vacío" listo para ser entrenado. El método .fit(X_train, y_train) toma los datos de entrada y salida del conjunto de entrenamiento, y calcula los mejores coeficientes posible (pendiente e intercepto) para acercar la predicción del modelo a los resultados reales. En la práctica, es donde "aprende" la relación lineal entre temperatura y CO2
### 1.4 ¿Qué significan los parámetros coef_ e intercept_ del modelo?
coef_ representa la pendiente de la recta de regresión, y nos dice en cuánto se espera que cambie el valor de CO2 por cada unidad que aumenta la temperatura.

intercept_ es el punto de corte con el eje Y, es decir, el valor estimado de CO2 cuando la anomalía de temperatura es 0. Juntos, estos parámetros definen por completo la ecuación de nuestra predicción lineal.
### 1.5 Ecuación matemática del modelo de regresión obtenida. Si vuelvo a ejecutar el código, ¿varían los coeficientes de la ecuación? ¿por qué?
La ecuación es:
y= intercepto + coeficiente × X
Donde intercepto y coeficiente son los parámetros obtenidos en el entrenamiento.
Si se repite la ejecución exactamente con los mismos datos y configuración, los coeficientes serán idénticos porque la regresión lineal es un proceso determinista (no depende del azar, salvo que añadieses ruido o mezclases el orden de los datos al azar).
### 1.6 ¿Qué hace el siguiente bloque de código y qué representa la gráfica resultante? ¿qué diferencia hay entre y_train e y_test, y por qué se separan estos dos tipos de datos? 
#### plt.scatter(X_train, y_train, color="red") 
#### plt.scatter(X_test, y_test, color="blue")
#### plt.plot(X_train, regr.predict(X_train), color="black")

Este bloque de código es fundamental para visualizar el funcionamiento del modelo. Dibuja los datos usados en el entrenamiento en rojo, los de prueba en azul, y la línea negra muestra cómo el modelo intenta ajustarse a los datos conocidos.
La diferencia entre y_train y y_test está en su rol: los primeros se usan para enseñar al modelo, y los segundos se dejan "escondidos" para comprobar si el modelo realmente es capaz de generalizar, es decir, si también acierta cuando se enfrenta a datos nuevos que no ha visto.

### 1.7 ¿Qué miden las métricas MSE y R^2 que aparecen en el código?
MSE (Error Cuadrático Medio): aporta una visión cuantitativa del error de predicción: indica, en promedio, cuánto se desvían las predicciones del modelo respecto a los valores reales, penalizando más los errores grandes (pues se eleva al cuadrado la diferencia).

R² (Coeficiente de determinación): mide cuánta "culpa" de la variabilidad de la variable dependiente (CO2) podemos atribuir a la variable independiente (temperatura). Un valor cercano a 1 significa que la relación es fuerte; un valor bajo indica que hay otros factores influyendo o que la relación lineal no es suficiente.
### 1.8 Explica los resultados de R^2 en entrenamiento y de test.
Un resultado alto de R² en entrenamiento muestra que el modelo explica muy bien los datos que ha visto. Si, además, el valor de R² en test es también alto y muy similar al de entrenamiento, significa que el modelo generaliza correctamente: es capaz de acertar con datos que nunca ha visto.
Si, por el contrario, el R² en test baja mucho respecto al de entrenamiento, es señal de sobreajuste, es decir, el modelo "memorizó" los datos de entrenamiento pero no aprendió la relación real.
### 1.9 ¿Cómo se haría una predicción nueva con el modelo entrenado? Formalízalo en código con un ejemplo.
Para hacer una predicción, se le pasa al modelo el nuevo valor de temperatura dentro de un array 2D como requiere scikit-learn:

nuevo_valor = np.array([[0.8]])  # Ejemplo: anomalía de temperatura = 0.8
prediccion = regr.predict(nuevo_valor)

Esto devolvería la concentración estimada de CO2 para esa anomalía de temperatura.

### 1.10 ¿Qué parámetros o configuraciones se podrían cambiar para mejorar el modelo?
El modelo puede mejorar ajustando algunos aspectos, por ejemplo:

Probar a modificar el porcentaje de datos de entrenamiento y test, o usar más datos históricos si están disponibles.

Preprocesar los datos buscando y eliminando valores atípicos.

Combinar más variables relevantes si estuvieran disponibles, no solo temperatura y CO2.
