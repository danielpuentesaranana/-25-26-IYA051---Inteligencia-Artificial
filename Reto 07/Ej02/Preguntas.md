### Preguntas Ejercicio 2

## 2.1 ¿Qué propósito tiene la función generador_datos_simple()?
La función generador_datos_simple() permite crear datos artificiales (ficticios) donde la variable y depende linealmente de X con una pendiente beta y un nivel de ruido controlado. Su utilidad es que así se pueden probar y estudiar modelos estadísticos (como la regresión lineal) conociendo la “verdad” subyacente, algo imposible de saber en el mundo real.
## 2.2 ¿Por qué se introduce un término de error aleatorio en la generación de datos?
El error aleatorio (ruido) se introduce para simular la realidad, donde casi nunca hay una respuesta exacta para un mismo valor de X. Representa toda esa variabilidad y factores externos que no controlamos o que influyen en los fenómenos reales. Así, el experimento resulta mucho más realista que si todos los puntos estuvieran en perfecta línea recta.
## 2.3 ¿Qué papel tiene el parámetro beta en la simulación?
Beta determina la fuerza y dirección de la relación entre X e y. Es la pendiente teórica de la recta: si beta=10, y aumenta 10 unidades por cada unidad adicional en X (sin ruido). Cambiar beta nos permite ver si el modelo es capaz de aprender relaciones muy fuertes o más débiles, y cómo influyen en la precisión de la predicción.
## 2.4 ¿Por qué se realiza la división de los datos 70% / 30% en entrenamiento y test? ¿harías otra división? ¿en función de qué se cogen esos porcentajes?
Esta división separa los datos para crear el modelo (70 %, entrenamiento) y para comprobar si generaliza bien (30 %, test). Así conseguimos evaluar el rendimiento del modelo en datos “nuevos” y evitar que solo memorice. A veces se usa 80/20 o 60/40, según la cantidad de datos o lo relevante que sea medir bien el test. Si tengo pocos datos quizás usaría más porcentaje para test, y si tengo muchísimos, con un 20 % ya es suficiente.
## 2.5 ¿Qué información proporcionan los atributos coef_ e intercept_ después del entrenamiento? Semejanzas y diferencias respecto del código del ej01.
Son la pendiente y el valor inicial de la recta que mejor ajusta los datos:

En Ej02 (simulado): y = 40.60 + 10.29·X

En Ej01 (real): y = 327.39 + 84.78·X
En ambos casos nos dicen cuánto sube y por cada unidad de X y de dónde parte la predicción. La diferencia es que en el simulado los coeficientes reflejan el valor que nosotros pusimos, mientras que en el real son mucho mayores y dependen de los datos que tenemos.
## 2.6 Cuánto vale R^2. Interprétalo y compáralo con el ej01.
Ej02: R² train = 0.65, test = 0.58 → El modelo explica bastante bien el patrón.

Ej01: R² train = 0.88, test = -13.23 → Entrena bien pero en test es desastroso (el modelo no generaliza nada, hay sobreajuste o los datos de test no tienen la misma tendencia).
En resumen: en el simulado el modelo es útil, en el real falla al predecir fuera de los datos de entrenamiento.
## 2.7 ¿Por qué son diferentes los valores de R^2 del test y del entrenamiento? ¿Qué valores desearíamos tener en ellos?
Las diferencias surgen por la aleatoriedad y porque el modelo puede ajustarse un poco más (o menos) a los datos de entrenamiento, que son los que ha “visto”. Lo ideal sería que ambos fueran altos (cerca de 1) y similares. Si R² de test es muy menor que el de train, podría haber sobreajuste (el modelo memoriza); si ambos son bajos, la relación lineal es débil o hay mucho ruido aleatorio.
## 2.8 ¿Qué pasaría si aumentamos el parámetro desviacion en el generador de datos? ¿para qué querríamos hacer esto?
Al aumentar la “desviacion”, el error aleatorio será mayor y los puntos estarán menos alineados; la nube de puntos estará mucho más dispersa y será más difícil para el modelo ajustar una recta con precisión. R² bajará y el error cuadrático medio subirá. Es útil para probar hasta qué punto es robusto el modelo cuando los datos tienen mucho ruido o variabilidad.
## 2.9 ¿Por qué el código hace reshape((muestras,1)) al generar X e y?
Porque scikit-learn espera que las variables independientes (X) y dependientes (y) tengan el formato de arrays de dos dimensiones, donde cada fila es una muestra y cada columna una característica. Al hacer reshape((muestras,1)), garantizamos que los datos tengan la forma adecuada. Si no se hace, puede dar errores de dimensiones.
## 2.10 Si yo hago X=50, ¿qué significaría respecto al ejemplo y al modelo calculado?
En este contexto sería pedirle al modelo la predicción de y para X=50 usando la ecuación final ajustada. Es decir, para tu modelo:

y = 40.60 + 10.29 × 50 = 40.60  + 514.50 = 555.10

Por lo que, usando los datos aprendidos, el modelo te diría que para X=50, lo esperado sería y ≈ 555.10.
