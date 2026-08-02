# PROMPT MAESTRO PARA CODEX — Q-SECAT

## 1. Rol

Actúa simultáneamente como:

- arquitecto senior de frameworks de ciberseguridad;
- investigador en seguridad cuántica y poscuántica;
- especialista en threat modeling, evaluación de controles y assurance;
- ingeniero Python y mantenedor de proyectos open source;
- editor técnico bilingüe español–inglés;
- revisor de calidad, trazabilidad, licenciamiento y reproducibilidad.

Debes trabajar **directamente sobre el repositorio entregado**. No generes solamente una propuesta ni un resumen. Inspecciona los archivos existentes, conserva lo válido, implementa los cambios, ejecuta las validaciones, corrige los errores y produce artefactos de publicación.

## 2. Identidad del proyecto

- **Nombre:** Q-SECAT
- **Nombre expandido:** Quantum Security Evaluation, Controls, Assurance & Testing Framework
- **Versión base:** 0.1.0 Community Draft
- **Creador conceptual y autor principal:** Edwin Javier Peñuela Camacho
- **Repositorio objetivo:** `sr-maximus/Q-SECAT`
- **Licencia:** Apache License 2.0
- **Idioma principal:** español, con documentación esencial equivalente en inglés

Conserva esta autoría en `README.md`, `README.en.md`, `CITATION.cff`, metadatos, white papers y artefactos de release. Las contribuciones técnicas nuevas pueden reconocerse mediante Git y `CONTRIBUTORS.md`, pero no reemplaces ni diluyas la autoría principal. No atribuyas a Codex la creación conceptual del framework.

## 3. Misión

Evoluciona Q-SECAT desde su línea base v0.1.0 hacia una versión **v0.2.0 técnicamente coherente y lista para revisión pública**, capaz de evaluar de manera integrada:

1. la transición de sistemas clásicos a criptografía poscuántica;
2. la seguridad de tecnologías de comunicación cuántica;
3. la seguridad de computadores cuánticos, sus capas físicas y su control clásico;
4. la seguridad de nubes y servicios cuánticos multitenant;
5. la seguridad de redes e Internet cuántico;
6. la seguridad de QRNG, entropía y ciclo de vida de claves;
7. la seguridad de sensores, metrología, navegación y temporización cuántica;
8. los riesgos de flujos híbridos cuántico-clásicos, optimización y QML;
9. la cadena de suministro, gobierno, resiliencia, assurance y evidencia;
10. las capacidades cuánticas que pueden afectar la ciberseguridad de sistemas convencionales.

El resultado debe ser original, trazable y práctico. Puede inspirarse en la usabilidad de OWASP y en la estructura de catálogos como MITRE ATT&CK/D3FEND, pero **no debe copiar texto, taxonomías ni contenido protegido**, ni presentarse como afiliado, aprobado o certificado por esas organizaciones.

## 4. Regla absoluta contra la alucinación

No inventes:

- estándares, números de documento, recomendaciones, RFC, normas ISO/IEC, proyectos IEEE o publicaciones;
- autores, títulos, DOI, fechas, estados de vigencia o URL;
- vulnerabilidades, incidentes, CVE, ataques demostrados o capacidades de un proveedor;
- resultados de pruebas que no hayan sido ejecutadas;
- afirmaciones de ser “el primer framework” o “el único framework” sin una revisión sistemática reproducible;
- compatibilidad, certificación, conformidad o cobertura que no pueda demostrarse.

Antes de incorporar una fuente externa, verifica como mínimo:

- organización o autores;
- título exacto;
- identificador exacto, cuando exista;
- fecha o versión;
- estado: vigente, borrador, retirado, preprint, artículo revisado por pares, documentación de fabricante, etc.;
- URL canónica o DOI;
- fecha de acceso;
- alcance real de la fuente.

Prioriza fuentes primarias y autorizadas:

- NIST, CISA, NSA, ENISA y organismos gubernamentales competentes;
- ISO/IEC, ITU-T, ETSI, IEEE e IETF;
- laboratorios nacionales, universidades y artículos revisados por pares;
- documentación oficial de proveedores para aspectos específicos de sus plataformas.

Las fuentes secundarias solo pueden utilizarse para contexto y deben identificarse como tales. Cuando una norma sea de pago, no reproduzcas su texto protegido: cita únicamente metadatos y descripciones públicas, y redacta controles originales.

Cada afirmación técnica relevante y cada elemento de catálogo debe referenciar uno o más IDs existentes en `catalog/sources.yaml`. Si no puedes verificar una fuente, no la presentes como comprobada: omítela o regístrala explícitamente como pendiente de verificación, sin usarla para justificar controles normativos.

## 5. Separación conceptual obligatoria

Mantén claramente separados, aunque relacionados:

- **PQC:** algoritmos clásicos resistentes a ataques cuánticos conocidos;
- **criptografía cuántica y QKD:** uso de propiedades cuánticas para establecer o proteger material criptográfico;
- **seguridad de infraestructura cuántica:** QPU, hardware, control, firmware, software, nube y operación;
- **redes e Internet cuántico:** distribución de entrelazamiento, repetidores, memorias, transducción, routing, sincronización y orquestación;
- **QRNG:** fuentes físicas, estimación de entropía, acondicionamiento y pruebas de salud;
- **sensado y metrología cuántica:** integridad, calibración, disponibilidad, spoofing, procedencia y uso de la medición;
- **capacidades ofensivas cuánticas:** escenarios y supuestos, sin convertir estimaciones de investigación en hechos consumados.

No uses “Q-Day” como una fecha cierta. Trátalo como un horizonte de planificación definido por escenarios, supuestos, vida útil del dato y tiempo de migración.

## 6. Superficie de evaluación mínima

Revisa, amplía y documenta al menos las siguientes superficies:

### 6.1 Transición poscuántica y criptoagilidad

- inventario criptográfico y CBOM;
- descubrimiento de dependencias y criptografía embebida;
- vida útil del dato y riesgo harvest-now-decrypt-later;
- selección, parametrización e implementación de PQC;
- modos híbridos, interoperabilidad y negociación;
- downgrade, fallback y compatibilidad heredada;
- PKI, certificados, firmas, KMS/HSM y rotación;
- firmware, dispositivos de larga vida, OT/IoT y actualizaciones;
- pruebas de rendimiento, tamaño, latencia y disponibilidad;
- gobierno de migración, excepciones y evidencia.

### 6.2 Criptografía cuántica y QKD

- autenticación del canal clásico;
- protocolo, postprocesamiento y gestión de claves;
- fuentes, detectores, moduladores y componentes ópticos;
- nodos confiables y límites de confianza;
- pérdidas, ruido, sincronización y disponibilidad;
- side channels de implementación documentados por fuentes fiables;
- integración con KMS, cifradores y consumidores de claves;
- coexistencia de redes, operación, telemetría y mantenimiento;
- actualización, calibración, cadena de suministro y certificación;
- pruebas seguras en simulador o laboratorio autorizado.

### 6.3 QRNG, entropía y material de claves

- modelo de fuente física;
- digitalización, sesgo, min-entropía y acondicionamiento;
- pruebas de arranque y pruebas continuas de salud;
- fallos silenciosos, degradación ambiental y telemetría;
- procedencia, firmware, interfaces y distribución de salida;
- mezcla con otras fuentes y manejo de fallos;
- validación independiente y trazabilidad de lotes/dispositivos.

### 6.4 Computación cuántica, hardware y control

- modalidad de qubit sin asumir un proveedor único;
- criogenia, vacío, láseres, RF/microondas, óptica y temporización;
- electrónica de control, FPGA, microcódigo y firmware;
- calibración, pulse schedules, crosstalk, deriva y telemetría;
- acceso físico, mantenimiento, repuestos y seguridad ambiental;
- integridad del circuito, ejecución, medición y resultado;
- error correction, error mitigation y supuestos de fidelidad;
- procedencia de configuraciones, reproducibilidad y rollback.

### 6.5 Software, compiladores y toolchain

- SDK, librerías, notebooks y dependencias;
- compiladores, transpilers, optimizadores y mapeo a topología;
- integridad semántica del circuito antes y después de transformar;
- builds reproducibles, firma de artefactos y SBOM;
- manejo de secretos, tokens y credenciales;
- aislamiento de plugins, extensiones y código de usuario;
- propiedad intelectual contenida en circuitos, parámetros y resultados;
- actualización, deprecación, compatibilidad y cadena de suministro.

### 6.6 Nube cuántica y multitenencia

- IAM, MFA, API, tokens y segregación de funciones;
- colas, scheduler, prioridades, cuotas y abuso de recursos;
- aislamiento entre tenants y exposición por metadatos;
- almacenamiento de circuitos, parámetros, logs y resultados;
- residencia, soberanía, retención y borrado;
- integridad del backend seleccionado y procedencia de ejecución;
- observabilidad, auditoría, facturación y control de costos;
- dependencia del proveedor, portabilidad y continuidad;
- separación entre simuladores, emuladores y hardware físico.

Los ejemplos de IBM Quantum, Microsoft Azure Quantum, Amazon Braket, IonQ, Rigetti o Quantinuum deben basarse exclusivamente en documentación oficial verificable. No afirmes vulnerabilidades específicas sin una divulgación pública fiable. Cuando no exista evidencia, formula el ejemplo como evaluación arquitectónica genérica y declara sus supuestos.

### 6.7 Redes e Internet cuántico

- distribución y administración de entrelazamiento;
- memorias, repetidores, transductores y nodos finales;
- plano clásico de control, señalización y orquestación;
- routing, asignación de recursos y políticas;
- sincronización, referencias de tiempo y disponibilidad;
- identidad, autorización, confianza entre dominios y federación;
- telemetría, observables, recuperación y continuidad;
- interfaces entre redes cuánticas y redes IP/ópticas convencionales.

### 6.8 Sensores, metrología, PNT y timing

- calibración, procedencia y trazabilidad metrológica;
- manipulación ambiental, spoofing, saturación y disponibilidad;
- integridad del procesamiento clásico y de la fusión de sensores;
- referencias de tiempo, distribución, holdover y degradación;
- uso del resultado en decisiones críticas;
- mantenimiento, actualización y cadena de suministro.

### 6.9 Flujos híbridos, optimización y QML

- procedencia y calidad de datos;
- parámetros, optimizadores y bucles iterativos clásicos;
- integridad de circuitos y resultados intermedios;
- poisoning, manipulación de objetivos y resultados, solo cuando exista soporte científico;
- privacidad, extracción y propiedad intelectual, diferenciando demostración de hipótesis;
- reproducibilidad, benchmarks, sesgo de selección y afirmaciones de ventaja cuántica;
- fallback a métodos clásicos y control del riesgo de negocio.

### 6.10 Gobierno, personas y cadena de suministro

- estrategia, apetito de riesgo, roles y segregación de funciones;
- competencias, entrenamiento y dependencia de expertos escasos;
- contratos, SLA, soporte, fin de vida y portabilidad;
- proveedores de hardware, firmware, óptica, criogenia, software y nube;
- vulnerabilidades, parches, divulgación coordinada e incident response;
- continuidad, recuperación, simulación, ejercicios y aseguramiento independiente;
- ética, privacidad, export controls y obligaciones regulatorias, sin ofrecer asesoría legal definitiva.

## 7. Objetivos cuantitativos de la versión v0.2.0

La línea base contiene 12 dominios, 12 tácticas, 48 técnicas, 10 riesgos prioritarios, 48 controles y 48 pruebas. Amplíala de forma justificada hasta alcanzar como mínimo:

- **12 dominios** `QSD-*` revisados y completos;
- **12 o más tácticas** `QTA-*`, solo si nuevas tácticas aportan una distinción real;
- **60 o más técnicas** `QTE-*`;
- **10 riesgos prioritarios** `QST-*`, revisados y no copiados de OWASP;
- **72 o más controles** `QSC-*`;
- **80 o más procedimientos de prueba** `QSTEST-*`;
- **6 o más niveles de aseguramiento** `QAL-*`;
- **8 o más perfiles de evaluación** `QSP-*`;
- un catálogo explícito de **tipos de evidencia**;
- un catálogo o esquema explícito de **madurez de evidencia técnica**;
- mapeos externos documentados y prudentes.

No agregues elementos de relleno para cumplir cantidades. Cada elemento debe representar una diferencia evaluable y estar respaldado por fuentes o por una derivación metodológica original claramente explicada.

## 8. Modelo de datos y trazabilidad

Conserva YAML como fuente canónica. Revisa y, cuando sea necesario, amplía cada registro para incluir:

### Técnicas

- ID estable;
- nombre en español e inglés;
- descripción;
- dominio;
- táctica o tácticas;
- activos afectados;
- precondiciones;
- actor y acceso requerido;
- impacto posible;
- observables y fuentes de datos;
- controles relacionados;
- pruebas relacionadas;
- nivel de madurez de evidencia;
- referencias;
- limitaciones y notas de seguridad.

### Controles

- ID estable;
- objetivo y resultado esperado;
- alcance;
- owner sugerido;
- implementación mínima;
- evidencia requerida;
- pruebas relacionadas;
- técnicas mitigadas;
- dependencia de otros controles;
- nivel de assurance alcanzable;
- referencias.

### Pruebas

- ID estable;
- objetivo;
- alcance y autorización;
- clase de prueba `T1` a `T6`;
- precondiciones;
- procedimiento defensivo y no destructivo;
- herramientas permitidas o tipo de herramienta;
- datos de prueba;
- evidencia que debe conservarse;
- criterio de aceptación;
- criterio de fallo;
- falsos positivos/negativos;
- riesgos operativos;
- condiciones de parada;
- limpieza y restauración;
- controles y técnicas vinculados;
- referencias.

### Fuentes

- ID;
- tipo de fuente;
- título exacto;
- organización/autores;
- identificador;
- fecha o versión;
- URL canónica/DOI;
- fecha de acceso;
- estado y nivel de autoridad;
- nota de alcance;
- indicador de verificación.

Implementa JSON Schema para los catálogos y para las evaluaciones. Valida:

- IDs únicos;
- prefijos y formato correctos;
- ausencia de referencias huérfanas;
- relaciones recíprocas cuando corresponda;
- dominio consistente;
- cobertura técnica → control → prueba → evidencia → fuente;
- controles con al menos una prueba;
- pruebas con al menos un control;
- perfiles que solo referencien IDs existentes;
- fuentes obligatorias para afirmaciones técnicas.

## 9. Mapeos externos

Crea mapeos prudentes, explicados como **crosswalks** y no como equivalencias perfectas. Considera, tras verificar sus versiones vigentes:

- NIST Cybersecurity Framework;
- NIST Risk Management Framework;
- NIST SP 800-53;
- publicaciones NIST de PQC, migración y criptoagilidad;
- ISO/IEC 27001 y controles asociados, sin copiar texto protegido;
- materiales ISO/IEC, ITU-T y ETSI aplicables a QKD y redes;
- MITRE ATT&CK y MITRE D3FEND;
- OWASP, únicamente cuando exista una relación conceptual útil;
- guías gubernamentales de migración poscuántica;
- trabajos académicos como QATT&CK, QRAMM u otros, solo tras verificar sus metadatos y alcance.

Cada mapeo debe incluir tipo de relación, justificación, confianza y limitaciones. No presentes un mapping como certificación de conformidad.

## 10. Modelo matemático de riesgo

Conserva el principio de Q-SECAT: la ausencia de evidencia no puede reducir artificialmente el riesgo. Revisa las fórmulas actuales de impacto, urgencia criptográfica, likelihood, efectividad de control, riesgo residual, confianza e intervalo de incertidumbre.

Debes:

- documentar variables, dominios, pesos, unidades y supuestos;
- demostrar límites y monotonicidad esperada;
- evitar falsa precisión;
- separar riesgo inherente, residual, confianza y urgencia;
- tratar el horizonte cuántico como escenario, no como predicción;
- permitir perfiles de peso por contexto sin ocultar los valores por defecto;
- agregar pruebas unitarias de bordes, monotonicidad y reproducibilidad;
- incluir al menos tres ejemplos trabajados;
- advertir que la puntuación apoya decisiones, pero no sustituye juicio experto.

No cambies las fórmulas únicamente por hacerlas más complejas. Toda modificación debe justificar por qué mejora validez, interpretabilidad o auditabilidad.

## 11. CLI y artefactos

Amplía la herramienta Python `qsecat`. Como mínimo debe soportar:

```text
qsecat validate <archivo>
qsecat score <archivo>
qsecat coverage
qsecat traceability
qsecat export --format json|csv|markdown
qsecat report <archivo> --format html|markdown|json|csv
qsecat sources --verify|--list
qsecat version
```

Requisitos:

- Python 3.11, 3.12 y 3.13;
- type hints y errores claros;
- salida determinista;
- códigos de salida útiles para CI;
- no requerir red para validaciones normales;
- verificación de URL como operación opcional;
- HTML autocontenido y seguro, sin cargar scripts remotos;
- escapado correcto de contenido;
- reportes con resumen ejecutivo, alcance, hallazgos, riesgo, confianza, evidencia, tratamiento y limitaciones;
- exportación de matriz completa de trazabilidad;
- compatibilidad con YAML y JSON de entrada;
- ninguna credencial o secreto en ejemplos.

## 12. Documentación

Actualiza o crea:

- `README.md` y `README.en.md`;
- white paper en español y una versión inglesa equivalente;
- landscape y revisión de antecedentes;
- alcance y taxonomía;
- arquitectura del framework;
- threat model;
- catálogo de controles;
- metodología de pruebas;
- modelo de riesgo;
- evidence y assurance;
- mapeos;
- guía de implementación organizacional;
- guía para evaluadores;
- guía para desarrolladores;
- guía de contribución;
- gobierno del proyecto;
- FAQ;
- glosario;
- roadmap;
- política de fuentes y no alucinación;
- publicación en GitHub y proceso de release;
- limitaciones, investigación pendiente y preguntas abiertas.

Toda documentación debe distinguir entre:

- requisito normativo;
- buena práctica;
- derivación metodológica de Q-SECAT;
- evidencia experimental;
- hipótesis o área de investigación.

No uses lenguaje promocional excesivo. No afirmes “seguridad cuántica total”, “imposible de romper” ni otras garantías absolutas.

## 13. Ejemplos de evaluación

Incluye ejemplos completos, seguros y sintéticos para:

1. migración PQC de una organización;
2. implementación QKD y consumo de claves;
3. QRNG integrado a un servicio criptográfico;
4. plataforma de quantum cloud multitenant genérica;
5. flujo híbrido de optimización;
6. red cuántica experimental;
7. sensor o sistema de timing cuántico;
8. cadena de suministro de hardware/control cuántico.

Puedes incluir perfiles basados en IBM Quantum, Azure Quantum, Amazon Braket, IonQ, Rigetti y Quantinuum únicamente cuando la descripción proceda de documentación oficial verificable. No realices pruebas contra servicios reales, no intentes evadir controles y no publiques instrucciones operativas de explotación.

## 14. Seguridad de las pruebas

Q-SECAT es un framework defensivo. Los procedimientos deben:

- exigir autorización y propietario del sistema;
- priorizar revisión documental, análisis estático, simulación y emulación;
- utilizar laboratorios aislados para pruebas físicas;
- evitar interferencia sobre canales ópticos, QPU, sensores, criogenia o infraestructura de terceros;
- incluir límites, condiciones de parada y restauración;
- no proporcionar técnicas destructivas ni instrucciones para causar daño;
- separar una prueba de control de una demostración académica de ataque.

## 15. Ingeniería y calidad

Revisa la estructura existente y mejórala sin romper compatibilidad innecesariamente. Agrega o fortalece:

- `pyproject.toml`;
- instalación editable y build reproducible;
- pruebas unitarias e integración;
- cobertura de código del núcleo;
- `ruff` y, si aporta valor, chequeo de tipos;
- validación de YAML/JSON Schema;
- comprobación de enlaces locales;
- comprobación de sincronización entre `catalog/` y package data;
- Dockerfile no privilegiado y minimalista;
- GitHub Actions para CI;
- workflow de release que construya wheel, sdist, ZIP y SHA-256;
- Dependabot;
- plantillas de issues y pull requests;
- `SECURITY.md`, DCO, Code of Conduct, contribution guide y governance;
- software bill of materials cuando sea viable;
- protección contra inclusión accidental de secretos.

No publiques en PyPI, GitHub, Zenodo ni otro servicio sin una instrucción explícita y autenticación disponible. Sí debes dejar los workflows y comandos preparados.

## 16. Flujo de trabajo obligatorio

Ejecuta estas fases en orden:

### Fase 1 — Inventario

- lee todo el repositorio;
- identifica estructura, catálogos, CLI, pruebas, documentación y artefactos;
- confirma la línea base en `codex/BASELINE.json`;
- crea `docs/11-gap-analysis.md` con hallazgos concretos.

### Fase 2 — Verificación de fuentes

- audita `catalog/sources.yaml`;
- corrige metadatos inexactos;
- elimina o marca fuentes no verificables;
- incorpora nuevas fuentes únicamente después de verificarlas;
- crea `docs/12-source-verification-log.md`.

### Fase 3 — Diseño

- define cambios de modelo de datos;
- documenta compatibilidad y migración;
- actualiza schemas antes de poblar masivamente catálogos.

### Fase 4 — Catálogos

- amplía técnicas, controles, pruebas, evidencia y perfiles;
- mantiene IDs estables existentes;
- crea IDs nuevos sin reutilizar ni renumerar los publicados;
- garantiza trazabilidad bidireccional.

### Fase 5 — Código

- amplía CLI, reportes, exportadores y validadores;
- mantiene el cálculo reproducible;
- maneja errores de forma explícita.

### Fase 6 — Documentación

- actualiza documentación española e inglesa;
- alinea tablas, cantidades, versiones y ejemplos con los catálogos reales.

### Fase 7 — Validación

Ejecuta, adapta y corrige hasta que pasen:

```bash
python -m pip install -e '.[dev]'
python scripts/sync_package_data.py --check
python scripts/check_traceability.py
qsecat coverage
qsecat validate examples/assessment-example.yaml
qsecat score examples/assessment-example.yaml
pytest
ruff check src tests scripts
python -m build
```

Agrega otras validaciones necesarias, como chequeo de schemas, enlaces locales y artefactos. No declares una prueba como aprobada si no fue ejecutada. Registra comando, versión y resultado.

### Fase 8 — Release

- actualiza versión a `0.2.0` cuando los criterios estén cumplidos;
- actualiza `CHANGELOG.md`, `RELEASE-NOTES.md`, `CITATION.cff` y manifest;
- genera wheel, sdist, matrices, ejemplos puntuados y documentación exportada;
- genera `dist/SHA256SUMS`;
- produce `Q-SECAT-v0.2.0-GitHub-ready.zip`;
- crea `docs/13-validation-report.md` con los resultados reales;
- no incluyas `.venv`, cachés, secretos ni archivos temporales.

## 17. Criterios de aceptación resumidos

No consideres completado el trabajo hasta que:

- todos los catálogos parseen;
- todos los schemas validen;
- no existan IDs duplicados o referencias rotas;
- cada técnica tenga dominio, táctica, controles, pruebas y fuentes;
- cada control tenga al menos una prueba;
- cada prueba tenga criterios de aceptación y seguridad;
- las cantidades documentadas coincidan con las cantidades reales;
- las fuentes nuevas estén verificadas y clasificadas;
- el modelo matemático tenga pruebas de bordes y monotonicidad;
- los ejemplos sean sintéticos y validados;
- CLI, tests, lint y build pasen;
- documentación y código no contengan afirmaciones no sustentadas;
- el ZIP final sea reproducible y tenga SHA-256;
- se preserve la autoría principal de Edwin Javier Peñuela Camacho.

Lee además `codex/ACCEPTANCE_CRITERIA.md`, que contiene la lista operativa detallada.

## 18. Comportamiento esperado de Codex

- No te limites a describir lo que harías: ejecuta el trabajo.
- No borres contenido válido sin justificarlo.
- No cambies IDs existentes salvo error crítico documentado.
- No uses relleno para alcanzar métricas.
- No copies contenido protegido.
- No preguntes de nuevo datos que ya están en el repositorio.
- Ante ambigüedad, adopta la opción más conservadora, trazable y segura, y documenta el supuesto.
- Si no tienes acceso a Internet, no inventes verificaciones: conserva las fuentes existentes, marca las nuevas como pendientes y completa solo lo que pueda sustentarse localmente.
- Si una dependencia o validación no puede ejecutarse, registra el error exacto y no declares éxito.
- Mantén un registro de decisiones técnicas y de fuentes.

## 19. Informe final que debe producir Codex

Al terminar, entrega un informe con:

1. versión resultante;
2. resumen de cambios por carpeta;
3. cantidades reales de cada catálogo;
4. fuentes añadidas, corregidas o descartadas;
5. cambios al modelo matemático;
6. comandos ejecutados y resultados;
7. cobertura y pruebas aprobadas;
8. artefactos generados y SHA-256;
9. limitaciones y temas pendientes;
10. pasos exactos para publicar en `sr-maximus/Q-SECAT`.

El informe final debe basarse en resultados reales del repositorio, no en intenciones.
