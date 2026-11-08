# ADR 003 · PDFs reales fuera de Git
Fecha de la decisión: 2026-11-07, aportada por Carlos.
Contexto: los expedientes pueden contener datos personales; repositorio público.
Decisión: guardar PDFs reales en datos/ y excluirlos de Git.
Alcance: ignorar datos/, archivos PDF, bases *.db y auxiliares *.db-*.
Alternativa descartada: publicar expedientes junto con el código.
Consecuencia: los datos locales no se sincronizan mediante GitHub.
Control: revisar archivos rastreados y diff antes de cada publicación.
Límite: .gitignore no retira contenido ya publicado ni limpia su historial.
Norma citada por Carlos: Ley 1581 de 2012; no se acredita cumplimiento por ignorar archivos.
