# Criterios de aceptación operativos — Q-SECAT v0.2.0

Codex debe marcar cada criterio como `PASS`, `FAIL` o `NOT EXECUTED`, incluyendo evidencia verificable.

## A. Autoría, licencia y gobierno

- [ ] Se conserva a Edwin Javier Peñuela Camacho como creador conceptual y autor principal.
- [ ] `LICENSE`, `NOTICE.md`, `CITATION.cff`, `CONTRIBUTING.md`, `DCO.md`, `CODE_OF_CONDUCT.md` y `SECURITY.md` son consistentes.
- [ ] No se incluye contenido copiado de OWASP, MITRE, ISO/IEC u otras fuentes.
- [ ] Las marcas se citan sin insinuar afiliación o aval.

## B. Investigación y fuentes

- [ ] Cada fuente nueva tiene título, autor/organización, fecha o versión, estado, URL/DOI y fecha de acceso.
- [ ] Se priorizan fuentes primarias y revisadas por pares.
- [ ] Las normas de pago no se reproducen textualmente.
- [ ] Las fuentes no verificables se eliminan o marcan claramente.
- [ ] Las afirmaciones experimentales o hipotéticas se distinguen de prácticas consolidadas.
- [ ] No se afirma que Q-SECAT es “el primero” sin evidencia reproducible.

## C. Catálogos

- [ ] Al menos 12 dominios.
- [ ] Al menos 12 tácticas, sin tácticas redundantes.
- [ ] Al menos 60 técnicas.
- [ ] Exactamente 10 riesgos prioritarios, salvo cambio metodológico justificado.
- [ ] Al menos 72 controles.
- [ ] Al menos 80 pruebas.
- [ ] Al menos 6 niveles de assurance.
- [ ] Al menos 8 perfiles.
- [ ] Catálogo de tipos de evidencia.
- [ ] Clasificación de madurez de evidencia.
- [ ] IDs únicos y estables.
- [ ] Ninguna referencia huérfana.
- [ ] Toda técnica enlaza controles, pruebas y fuentes.
- [ ] Todo control enlaza al menos una prueba.
- [ ] Toda prueba enlaza al menos un control y contiene condiciones de parada.

## D. Schemas y validadores

- [ ] JSON Schema de evaluación válido.
- [ ] JSON Schema de catálogos válido.
- [ ] Validación de IDs y prefijos.
- [ ] Validación de relaciones recíprocas.
- [ ] Validación de fuentes requeridas.
- [ ] Validación de perfiles.
- [ ] Mensajes de error accionables.

## E. Riesgo, assurance e incertidumbre

- [ ] Variables y pesos documentados.
- [ ] Impacto, likelihood, urgencia, efectividad, riesgo residual, confianza e incertidumbre son conceptos separados.
- [ ] La baja confianza no reduce artificialmente el riesgo.
- [ ] Se prueban límites mínimos y máximos.
- [ ] Se prueba monotonicidad.
- [ ] Se prueban valores inválidos.
- [ ] Se incluyen al menos tres ejemplos trabajados.
- [ ] Se evita falsa precisión y se documentan limitaciones.

## F. CLI

- [ ] `qsecat validate`.
- [ ] `qsecat score`.
- [ ] `qsecat coverage`.
- [ ] `qsecat traceability`.
- [ ] `qsecat export` a JSON, CSV y Markdown.
- [ ] `qsecat report` a HTML, Markdown, JSON y CSV.
- [ ] `qsecat sources`.
- [ ] `qsecat --version` o equivalente.
- [ ] Códigos de salida apropiados.
- [ ] HTML autocontenido y con escapado seguro.
- [ ] Operación normal sin acceso de red.

## G. Ejemplos

- [ ] Migración PQC.
- [ ] QKD.
- [ ] QRNG.
- [ ] Quantum cloud multitenant.
- [ ] Flujo híbrido.
- [ ] Red cuántica.
- [ ] Sensor o timing.
- [ ] Cadena de suministro.
- [ ] Todos los ejemplos son sintéticos, autorizados y validan contra schema.
- [ ] Los ejemplos de proveedores usan solo documentación oficial y no inventan vulnerabilidades.

## H. Documentación

- [ ] README español e inglés actualizados.
- [ ] White paper español e inglés.
- [ ] Landscape y fuentes.
- [ ] Arquitectura.
- [ ] Threat model.
- [ ] Controles.
- [ ] Testing methodology.
- [ ] Risk model.
- [ ] Evidence y assurance.
- [ ] Mappings.
- [ ] Guía organizacional y de evaluación.
- [ ] Developer guide.
- [ ] FAQ y glosario.
- [ ] Roadmap.
- [ ] Política de fuentes/no alucinación.
- [ ] Limitaciones y preguntas abiertas.
- [ ] No hay enlaces locales rotos.
- [ ] Las cantidades documentadas coinciden con los catálogos.

## I. Código y CI

- [ ] Instalación editable correcta.
- [ ] Python 3.11, 3.12 y 3.13 en CI.
- [ ] `pytest` aprobado.
- [ ] `ruff check` aprobado.
- [ ] Build de wheel y sdist aprobado.
- [ ] Package data sincronizada.
- [ ] Dockerfile no privilegiado.
- [ ] Dependabot configurado.
- [ ] Workflows con permisos mínimos.
- [ ] No hay secretos ni tokens.
- [ ] Artefactos y checksums reproducibles.

## J. Release

- [ ] Versión actualizada a 0.2.0 cuando todo lo anterior esté cumplido.
- [ ] `CHANGELOG.md`, `RELEASE-NOTES.md`, `CITATION.cff` y manifest actualizados.
- [ ] Matriz de trazabilidad exportada.
- [ ] Reporte de validación generado.
- [ ] ZIP `Q-SECAT-v0.2.0-GitHub-ready.zip` generado.
- [ ] `SHA256SUMS` generado y verificado.
- [ ] Comandos exactos de publicación documentados.
