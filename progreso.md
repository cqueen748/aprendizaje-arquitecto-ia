# Progreso · Tutor IA documental verificada

Mes actual: 1
Semana del mes: 1 (cierre original: 8 nov 2026; evaluación formal pendiente al 27 nov 2026)
Entregable del mes: script que inventaría PDFs → SQLite, en GitHub
Estado del entregable: en desarrollo. Inventario v1 recibe y valida la carpeta por argumento, lista nombres y tamaños en bytes y cuenta PDFs. Probado en Mac; prueba de v1 en Windows pendiente. SQLite pendiente.

## Avances y evidencias
- Alcance del inventario v0: recorrer una carpeta y sus subcarpetas, seleccionar PDFs, imprimir nombre y tamaño en bytes y contar los PDFs encontrados. Sin hash ni SQLite en este ejercicio.
- Carga propuesta anterior: aproximadamente 10 h (8 h de estudio y 2 h de ejercicio). No equivale a tiempo ejecutado.
- Horas reales y detalle del estudio realizado: pendientes de registrar.
- Hecho: prácticas de listas, diccionarios, contadores, for, if, len() y normalización con lower().
- Hecho: inventario_v0.py utiliza pathlib, rglob("*"), is_file(), suffix.lower() y stat().st_size.
- Evidencia: 12 PDFs listados y contados, incluidos dos de una subcarpeta y uno con extensión .PDF; un DOCX y dos XLSX quedaron excluidos.
- Verificación independiente: tamaño de un PDF coincidente entre Python y Propiedades de Windows: 310572 bytes.
- Comprensión: Carlos explicó la diferencia entre iterdir() y rglob("*"), el propósito de lower(), el carácter de consulta del script y la ubicación del incremento del contador dentro del filtro.
- Decisión de alcance: Carlos aceptó los documentos de prueba como muestra suficiente para cerrar este ejercicio; se retira el requisito de repetirlo con un expediente contractual.
- Evaluación: ejercicio de inventario completado para el alcance acordado y la muestra observada. Semana completa y rúbrica formal pendientes.

## Sesión del 26 nov 2026 · Argumentos en Mac
- Objetivo: recibir una ruta desde la terminal y validar la entrada antes de utilizarla.
- Hecho: practica_argumentos.py utiliza sys.argv, len(), Path, is_dir() y sys.exit(1).
- Control 1: exige exactamente dos elementos en sys.argv: nombre del script y una ruta.
- Control 2: comprueba que la ruta corresponda a una carpeta existente.
- Prueba sin argumento: mostró el aviso solicitado sin provocar IndexError tras guardar la versión corregida.
- Prueba con ruta inexistente: mostró el aviso de ruta no válida y no mostró el mensaje de éxito.
- Prueba con carpeta existente: mostró "Se encontró la carpeta: mes-01-02-python-git-sql/semana-01".
- Dificultad detectada: confusión entre cantidad de elementos y posiciones de una lista.
- Refuerzo: ejemplos progresivos con listas de nombres, ciudades y argumentos.
- Evidencia de comprensión: Carlos distinguió una lista de un elemento en posición 0, identificó sys.argv[1] cuando hay dos elementos y explicó los dos controles.
- Incidencia: se ejecutó una versión anterior del archivo; se comprobó el contenido guardado mediante cat -n y se repitió la prueba.
- Evaluación: tres casos básicos comprobados mediante las salidas compartidas. Retención sin pistas pendiente de comprobar en otra sesión.
- Duración real: pendiente de informar por Carlos.
- Alcance: práctica separada; la recepción de argumentos todavía no está integrada en inventario_v0.py.

## Sesión del 27 nov 2026 · Inventario v1 en Mac
- Objetivo: integrar la recepción y validación de la carpeta en el inventario, conservando inventario_v0.py.
- Hecho: inventario_v1.py recibe la ruta mediante sys.argv[1], comprueba la cantidad de argumentos y valida la carpeta con is_dir().
- Prueba sin argumento: mostró el aviso solicitado y se detuvo.
- Prueba con ruta inexistente: mostró el aviso de ruta no válida y se detuvo.
- Prueba con datos/expediente_prueba: listó tres PDFs con sus tamaños y mostró total 3.
- Prueba con datos/expediente_prueba/anexos: listó un PDF de 310572 bytes y mostró total 1.
- Muestra preparada por Carlos: dos PDFs en la carpeta principal y uno en anexos.
- Evidencia: salidas de ejecución compartidas por Carlos; no se realizó inspección directa de su equipo.
- Incidencia: se ejecutó una versión sin los cambios guardados; después de guardar se repitió la prueba con el resultado esperado.
- Dificultad detectada: inicialmente propuso modificar la línea del código para cambiar de carpeta.
- Refuerzo: ejecución del mismo script con dos rutas diferentes, sin modificar el código.
- Evidencia de comprensión guiada: identificó "datos/expediente_prueba" como argumento para volver a contar los tres PDFs.
- Evaluación: cuatro casos observados con resultados esperados en Mac. Retención sin pistas y ejecución de v1 en Windows pendientes.
- Duración real: pendiente de informar por Carlos.

## Respaldo y sincronización
- 53fba07: incorporación de cuatro scripts de práctica.
- c00011f: integración con los cambios del plan y envío confirmado.
- cf47718: actualización anterior de progreso.md enviada a GitHub.
- c6c8077: contador de PDFs enviado a GitHub.
- Mac actualizado desde 7b39be6 hasta c6c8077 mediante fast-forward.
- 8655128: practica_argumentos.py guardado en el Mac y enviado a GitHub.
- Sincronización de Windows con 51af72c y prueba de inventario_v1.py: pendientes.
- f07fd90: registro de la práctica de argumentos y evidencias enviado a GitHub.
- 51af72c: inventario_v1.py enviado a GitHub.

## Decisiones (ADR)
- Pendiente: revisar los ADR existentes en docs/adr y registrar sus referencias exactas.
- Pendiente: conciliar los documentos de planificación con el alcance aceptado, la muestra de prueba y el uso de bytes.

## Métricas del sistema (desde mes 4)
- Conjunto de verdad: 0 preguntas
- Recuperación correcta top-5: —
- Exactitud de respuesta: —
- Respuestas sin sustento: —
- Exactitud de cita: —

## Ingresos ligados al plan
- Sin información registrada.
 
## Próxima sesión
- Recuperar sin pistas la diferencia entre cantidad de elementos, posiciones y argumentos.
- Comprobar sin pistas cómo seleccionar otra carpeta mediante el argumento de ejecución.
- Probar inventario_v1.py en Windows después de sincronizar el repositorio.
- Registrar horas reales y completar la evaluación formal pendiente.
- Conciliar NOTAS.md, PLAN.md y las referencias a los ADR.
- Sincronizar Windows antes de retomar allí.
