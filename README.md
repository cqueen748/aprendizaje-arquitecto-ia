# Aprendizaje de arquitectura de IA · CRAI 2036

## Objetivo
Desarrollar la capacidad de diseñar, construir, evaluar y supervisar sistemas de IA documental, comenzando por un inventario de PDFs y avanzando hacia API, bases de datos, RAG local, MCP y auditoría.

Aprender Python, Git y SQL mediante ejercicios aplicados a gestión documental, para comprender el código, comprobar resultados, tomar decisiones de arquitectura y dirigir desarrollos con apoyo de IA y especialistas. El primer producto de aprendizaje será un inventario documental reproducible, probado y documentado; las capacidades adquiridas deberán poder reutilizarse en soluciones CRAI.

Este aprendizaje complementa el juicio empresarial y la supervisión técnica de Carlos; no tiene como objetivo convertirlo en desarrollador de software de tiempo completo. Se mantiene la visión rectora CRAI 2036: **«Construir una posición dentro de la economía de la inteligencia».**

## Estado
Preparación del entorno y cuatro scripts conservados en `mes-01-02-python-git-sql/semana-00-entorno/`. No acreditan el ejercicio ancla ni la semana 1. La implementación de `inventario_v0.py` está pendiente y corresponde al estudiante con tutoría.

- [Progreso y pendientes](progreso.md)
- [Hoja de ruta](docs/hoja-de-ruta.md)
- [Decisiones de arquitectura](docs/adr/)
- [Plan de semana 1: 11,5 h](mes-01-02-python-git-sql/semana-01/PLAN.md)
- [Notas de semana 1](mes-01-02-python-git-sql/semana-01/NOTAS.md)

## Organización
Los meses 1–2 reúnen Python, Git y SQL; el mes 3, API, PostgreSQL y Docker; el mes 4, RAG local; y los meses 5–6, MCP y auditoría. Las carpetas futuras se crearán cuando contengan trabajo real. La instrucción de Carlos del 8 de noviembre sitúa el inventario PDF → SQLite como entregable del mes 1, sustituyendo la referencia anterior a semana 8. Está no iniciado; la secuencia concreta de SQLite queda por programar.

El material anterior de Matemáticas, CS50 y Proyectos se conserva en `_archivo-plan-anterior/`. `03-Python/` queda como referencia hacia la nueva ubicación y `05-Notas/` se conserva.

## Reglas
- Un commit por sesión, con mensaje en español que describa cambios reales.
- Solo código, notas y ADR sin información confidencial. No subir expedientes, credenciales ni datos de clientes.
- `datos/`, archivos PDF y bases `*.db` quedan fuera de Git. Los ejemplos compartidos serán sintéticos y sin datos personales.
- `.gitignore` no elimina archivos ya rastreados ni su historial; revisar lo preparado antes de publicar.
- No marcar dominio por tiempo, código generado o certificados. Registrar evidencias y evaluación del tutor por separado.
- Un entorno `.venv` por equipo; no se sincroniza por Git.

## Mac y Windows
Al iniciar: revisar `git status` y, con el árbol limpio, ejecutar `git pull --ff-only` en el repositorio. Si falla o hay cambios locales, detener la sincronización y revisar con el tutor; no descartar cambios.

Al cerrar: revisar `git diff`, preparar únicamente archivos previstos con `git add <rutas>`, revisar `git diff --cached`, crear un commit y ejecutar `git push`. Confirmar el resultado antes de cambiar de equipo. El otro equipo recibe los cambios con `git pull --ff-only`; cada equipo conserva su entorno virtual.

Los PDFs y las bases excluidos no se trasladan mediante Git. Su manejo autorizado requiere un mecanismo independiente.
