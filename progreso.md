# Progreso · Tutor IA documental verificada

Mes actual: 1
Semana del mes: 1 (cierre original: 8 nov 2026; continúa abierta al 13 nov 2026)
Entregable del mes: script que inventaría PDFs → SQLite, en GitHub
Estado del entregable: en desarrollo; listado de PDFs con tamaños implementado. SQLite pendiente.

## Esta semana
- Objetivo actualizado por Carlos: recorrer una carpeta y sus subcarpetas, seleccionar PDFs e imprimir nombre y tamaño en bytes. Sin hash ni SQLite en esta tarea.
- Carga propuesta actualizada: aproximadamente 10 h (8 h de estudio y 2 h de ejercicio).
- Horas reales y estudio realizado: pendientes de registrar.
- Hecho: prácticas de listas, diccionarios, contadores, for, if, len() y normalización con lower().
- Hecho: inventario_v0.py utiliza pathlib, rglob("*"), is_file(), suffix.lower() y stat().st_size.
- Evidencia: salida de 12 PDFs, incluidos dos de una subcarpeta y uno con extensión .PDF; un DOCX y dos XLSX quedaron excluidos.
- Verificación independiente: tamaño de un PDF coincidente entre Python y Propiedades de Windows: 310572 bytes.
- Comprensión: Carlos explicó la diferencia entre iterdir() y rglob("*"), el propósito de lower() y que el script consulta sin modificar los archivos.
- Respaldo: cuatro scripts incorporados en 53fba07; integración y envío a GitHub confirmados en c00011f. Windows quedó limpio y sincronizado antes de esta actualización del registro.
- Evaluación: funcionalidad del ejercicio aprobada para la muestra observada. Semana completa y rúbrica formal pendientes.
- Pendiente: confirmar aplicación sobre una muestra de expediente contractual; los archivos revisados son principalmente guías y documentos de referencia.
- Pendiente: sincronizar el Mac.
- Bloqueo: ninguno reportado.

## Decisiones (ADR)
- Pendiente: revisar los ADR existentes en docs/adr y registrar aquí sus referencias exactas.

## Métricas del sistema (desde mes 4)
- Conjunto de verdad: 0 preguntas
- Recuperación correcta top-5: —
- Exactitud de respuesta: —
- Respuestas sin sustento: —
- Exactitud de cita: —

## Ingresos ligados al plan
- Sin información registrada.

## Próxima sesión
- Empezar por: cerrar las evidencias pendientes de la semana 1 y evaluar el ejercicio con la rúbrica.
- Confirmar muestra contractual, estudio realizado y horas reales.
- Sincronizar el Mac antes de trabajar allí.