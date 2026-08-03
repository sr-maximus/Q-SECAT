# Q-SECAT v0.1.0

## Quantum Security Evaluation, Controls, Assurance & Testing Framework

**Creador conceptual y autor principal:** Edwin Javier Peñuela Camacho<br>
**Estado:** borrador comunitario<br>
**Fecha de corte de fuentes:** 1 de agosto de 2026
**Licencia:** Apache-2.0

## Resumen

La ciberseguridad cuántica suele reducirse a la migración hacia criptografía poscuántica o, en el extremo opuesto, a la distribución cuántica de claves. Esa reducción deja por fuera superficies críticas: servicios de nube cuántica, compiladores y circuitos, electrónica de control, calibración, hardware, multitenencia, redes de entrelazamiento, fuentes cuánticas de entropía, sensores, metrología, sincronización, flujos híbridos, cadena de suministro y evidencia de aseguramiento.

Q-SECAT propone una metodología unificada para **comprender, modelar, controlar, probar y priorizar** riesgos en sistemas clásicos expuestos a la transición cuántica, sistemas cuánticos y sistemas habilitados por tecnologías cuánticas. El marco combina doce dominios de seguridad (`QSD`), doce tácticas adversarias (`QTA`), cuarenta y ocho técnicas (`QTE`), cuarenta y ocho controles (`QSC`), cuarenta y ocho pruebas (`QSTEST`), un Top 10 (`QST`) y seis niveles de aseguramiento (`QAL`). Todos los artefactos poseen identificadores estables y relaciones verificables por máquina.

La propuesta no afirma que todos los ataques descritos hayan ocurrido ni que exista una fecha cierta para un computador cuántico criptográficamente relevante. Cada técnica distingue su estado de evidencia, y el cálculo de riesgo separa la magnitud del riesgo de la confianza disponible. El objetivo es evitar tanto la subestimación como el alarmismo.

## 1. Problema de investigación

Existen, al menos, tres problemas diferentes bajo la expresión “seguridad cuántica”:

1. **Seguridad frente a capacidades cuánticas futuras:** protección de datos, firmas, identidades y protocolos clásicos mediante inventario criptográfico, criptoagilidad y migración a mecanismos poscuánticos.
2. **Seguridad de mecanismos criptográficos cuánticos:** protocolos, dispositivos y redes de QKD; autenticación clásica; administración de claves; nodos de confianza; fuentes y detectores reales.
3. **Seguridad de sistemas cuánticos:** hardware, firmware, calibración, software, compilación, nube, multitenencia, redes, sensores, cadenas de suministro y flujos clásicos-cuánticos.

Una metodología limitada a uno de esos grupos no permite razonar sobre dependencias sistémicas. Un algoritmo poscuántico puede fallar por integración, negociación, implementación o gestión de claves. Un protocolo QKD puede conservar una prueba teórica válida y, aun así, depender de autenticación clásica, componentes reales y servicios de administración. Un QPU puede operar correctamente mientras un atacante altera el compilador, la API, la cola, la calibración o la interpretación de resultados.

La pregunta central de Q-SECAT es:

> ¿Cómo evaluar de forma trazable y reproducible la seguridad del sistema completo, distinguiendo evidencia, hipótesis, controles, resultados de prueba e incertidumbre?

## 2. Revisión del panorama existente

La revisión no parte de la premisa de que “no existe nada”. Por el contrario, integra trabajos con alcances diferentes:

- NIST publicó FIPS 203, 204 y 205 para mecanismos poscuánticos y mantiene guías de migración y criptoagilidad.
- ISO/IEC 23837, ETSI QKD e ITU-T aportan requisitos, perfiles, interfaces y marcos para módulos y redes QKD.
- IEEE P1947 es un proyecto activo de estándar para un marco de ciberseguridad cuántica; no se trata como estándar final publicado en esta versión.
- QATT&CK propone una extensión de tipo ATT&CK para amenazas a infraestructura de computación cuántica.
- QRAMM y QUASAR se orientan principalmente a madurez, preparación y transición poscuántica.
- La literatura de Argonne y de seguridad de hardware cuántico estudia taxonomías, bancos de pruebas, crosstalk, calibración, compiladores, nube e IP.

La conclusión de diseño es una inferencia limitada a las fuentes revisadas: los componentes necesarios existen de forma fragmentada, pero no se identificó un artefacto público único que, simultáneamente, cubra el sistema completo, relacione amenaza-control-prueba-evidencia, ofrezca un esquema de evaluación legible por máquina y trate explícitamente la incertidumbre. Q-SECAT ocupa esa capa de integración; no sustituye las normas especializadas.

## 3. Alcance del ámbito cuántico

La ciencia de información cuántica suele agruparse en computación, comunicaciones y sensado/metrología. Para una evaluación de ciberseguridad, Q-SECAT amplía ese mapa con las capas clásicas y operacionales que hacen posible el servicio.

### 3.1 Tecnologías y capacidades incluidas

- **Criptografía poscuántica:** KEM, firmas, PKI, protocolos híbridos, code signing, HSM, dispositivos restringidos y migración.
- **Criptografía cuántica y QKD:** preparación y medición, distribución de entrelazamiento, autenticación, confirmación de claves, KMS, nodos de confianza y disponibilidad.
- **Redes e Internet cuántico:** enlaces, repetidores, memorias, transductores, orquestadores, enrutamiento, sincronización y metadatos de servicio.
- **QRNG y entropía:** fuente física, digitalización, acondicionamiento, pruebas de salud, DRBG, API y procedencia hasta el consumidor.
- **Computación cuántica:** QPU, modalidad física, criogenia/fotónica/trampas, electrónica, microcódigo, calibración, error mitigation/correction y medición.
- **Software cuántico:** SDK, dependencias, compilador, transpiler, optimizador, circuitos, registro de paquetes, build y decodificación de resultados.
- **Nube cuántica:** IAM, API, colas, planificador, almacenamiento, multitenencia, residencia, telemetría y responsabilidad compartida.
- **Flujos híbridos y QML:** datos, codificación de características, optimizadores clásicos, estado iterativo, modelos, orquestación y decisiones posteriores.
- **Sensado, metrología y temporización:** sensores, relojes/referencias, navegación, calibración, procedencia de mediciones y tolerancia a degradación.
- **Cadena de suministro y gobierno:** componentes, firmware, mantenimiento, soporte, concentración de proveedores, evidencia, competencias, incidentes y continuidad.

### 3.2 Tecnologías adyacentes

El marco permite extender perfiles para computación ciega o verificable, teleportación y distribución de estados, cómputo cuántico distribuido, secret sharing cuántico, autenticación y firmas cuánticas, comunicaciones cuánticas seguras directas, simuladores, annealing y tecnologías de transducción. Estas capacidades no se convierten automáticamente en categorías separadas: se modelan mediante los dominios, activos y técnicas que correspondan, y solo se crean nuevos identificadores cuando exista una diferencia semántica y evidencia suficiente.

## 4. Principios de diseño

1. **Sistema completo:** se evalúan planos de negocio, clásico, lógico cuántico, físico, control y suministro/aseguramiento.
2. **Separación conceptual:** PQC, QKD y seguridad de sistemas cuánticos no se confunden.
3. **Trazabilidad obligatoria:** cada hallazgo conecta activo, técnica, control, prueba, evidencia, tratamiento y propietario.
4. **Evidencia graduada:** una afirmación documental no equivale a una prueba reproducible ni a una evaluación independiente.
5. **Incertidumbre visible:** los escenarios tecnológicos no se presentan como predicciones exactas.
6. **Prueba proporcional y segura:** se comienza por revisión, análisis estático y simulación; el laboratorio físico exige autorización especializada.
7. **Neutralidad tecnológica:** los resultados se expresan como propiedades y evidencia, no como preferencia por un proveedor.
8. **Identificadores estables:** los IDs no se reciclan silenciosamente y las relaciones se validan automáticamente.

## 5. Arquitectura del marco

### 5.1 Seis planos de análisis

| Plano | Objetos principales | Pregunta de seguridad |
|---|---|---|
| Negocio y misión | procesos, decisiones, seguridad humana, vida útil del dato | ¿Qué consecuencia material produciría un fallo? |
| Digital clásico | identidad, API, red, host, nube, almacenamiento | ¿Puede comprometerse el servicio sin tocar el fenómeno cuántico? |
| Lógico cuántico | algoritmos, circuitos, protocolos, mediciones | ¿Se preservan semántica, integridad y supuestos? |
| Físico cuántico | qubits, fotones, sensores, memorias, canales | ¿El ambiente o la implementación altera o filtra el comportamiento? |
| Control y soporte | firmware, electrónica, pulsos, calibración, tiempo | ¿Son auténticos, autorizados, observables y recuperables? |
| Suministro y aseguramiento | proveedores, build, actualización, evidencia | ¿Puede trazarse y sostenerse la confianza durante el ciclo de vida? |

### 5.2 Doce dominios QSD

| ID | Dominio |
|---|---|
| QSD-01 | Transición criptográfica y criptoagilidad |
| QSD-02 | Criptografía cuántica y QKD |
| QSD-03 | Redes e Internet cuántico |
| QSD-04 | QRNG, entropía y ciclo de vida de claves |
| QSD-05 | Hardware cuántico y ambiente físico |
| QSD-06 | Electrónica de control, firmware y calibración |
| QSD-07 | Software, compiladores y circuitos cuánticos |
| QSD-08 | Nube cuántica, API y multitenencia |
| QSD-09 | Flujos híbridos y aprendizaje automático cuántico |
| QSD-10 | Sensado, metrología y temporización cuántica |
| QSD-11 | Cadena de suministro, procedencia y ciclo de vida |
| QSD-12 | Gobierno, aseguramiento y resiliencia |

Una evaluación debe marcar cada dominio como `applicable`, `inherited`, `not_applicable` o `unknown`. El estado `unknown` no es neutral: crea una brecha de evaluación.

## 6. Modelo adversario

Q-SECAT adopta la utilidad operacional de una matriz de tácticas y técnicas, sin afirmar afiliación ni equivalencia con MITRE ATT&CK.

### 6.1 Tácticas QTA

Las doce tácticas representan objetivos: reconocimiento; preparación de recursos/suministro; acceso inicial; compromiso del plano de control clásico; manipulación de calibración/ambiente; manipulación de circuito/trabajo/dato; abuso de recursos compartidos; canal lateral/fuga; abuso de identidad/claves/aleatoriedad; manipulación de canal/red cuántica; persistencia/evasión/evidencia; y degradación/denegación/corrupción.

### 6.2 Técnicas QTE

Cada técnica registra:

- dominio y tácticas;
- descripción y precondiciones;
- propiedades de seguridad afectadas;
- observables;
- riesgos Top 10 relacionados;
- control y prueba enlazados;
- referencias;
- estado de evidencia.

### 6.3 Estados de evidencia

| Estado | Significado |
|---|---|
| `established-classical` | debilidad clásica conocida, aplicable a la pila cuántica |
| `demonstrated-lab` | demostración experimental o prueba reproducible |
| `documented-implementation-class` | clase reconocida en normas, perfiles o literatura técnica |
| `plausible-research` | hipótesis sustentada en propiedades del sistema, aún no suficientemente demostrada |
| `observed-incident` | incidente público y atribuible |

El estado de evidencia no prueba explotabilidad universal. La evaluación debe demostrar que las precondiciones se cumplen en el activo concreto.

## 7. Modelo defensivo y de pruebas

### 7.1 Controles QSC

Los controles se redactan como resultados verificables. Cada uno incluye objetivo, guía de implementación, evidencia esperada, técnicas mitigadas, prueba asociada y QAL mínimo recomendado. Las familias principales son:

- inventario y visibilidad de dependencias;
- identidad, autorización y separación de funciones;
- integridad, firma, atestación y procedencia;
- aislamiento, planificación y gobierno de recursos;
- monitoreo, líneas base y detección de anomalías;
- resiliencia, fallback, recuperación y salida de proveedor;
- reproducibilidad e independencia del aseguramiento.

### 7.2 Clases de prueba QSTEST

| Clase | Método | Entorno predeterminado |
|---|---|---|
| T1 | revisión documental | no invasivo |
| T2 | análisis estático/configuración/CBOM | offline o solo lectura |
| T3 | simulación/emulación | simulador |
| T4 | integración aislada | tenant o laboratorio dedicado |
| T5 | validación física controlada | laboratorio especializado autorizado |
| T6 | aseguramiento independiente | tercero competente |

Cada prueba especifica hipótesis, precondiciones, procedimiento, criterios de aceptación, evidencia, posibles resultados, seguridad y QAL. Un resultado `inconclusive` nunca se trata como `pass`.

### 7.3 Registro mínimo

Una prueba reproducible conserva ID y versión, autorización, objetivo, herramientas y versiones, configuración, datos/semilla, backend, snapshot de calibración cuando aplique, resultados, limitaciones, hashes, ejecutor, revisor y fechas.

## 8. Aseguramiento y evidencia

Los niveles QAL evitan mezclar profundidad de evidencia con efectividad del control:

| Nivel | Denominación | Evidencia mínima |
|---|---|---|
| QAL-0 | no sustentado | afirmación sin artefacto verificable |
| QAL-1 | documentado | propietario, alcance y registro versionado |
| QAL-2 | revisado | revisión estática/arquitectónica trazable |
| QAL-3 | probado reproduciblemente | simulación o integración repetible con criterios |
| QAL-4 | laboratorio controlado | validación física bajo condiciones registradas |
| QAL-5 | asegurado independientemente | reproducción competente o esquema formal aplicable |

QAL califica una afirmación específica, no “certifica” el sistema entero.

## 9. Modelo matemático de riesgo e incertidumbre

El modelo es ordinal y transparente. Sus valores permiten priorizar dentro de un mismo perfil y política de pesos; no representan una probabilidad física exacta.

### 9.1 Impacto

Se califican de 0 a 5: confidencialidad, integridad, disponibilidad, seguridad/misión, privacidad/IP y regulación/soberanía.

\[
I = 0.60\max(v_i) + 0.40\sum_i w_i v_i
\]

Pesos iniciales: 0.16, 0.22, 0.16, 0.20, 0.12 y 0.14, respectivamente.

### 9.2 Urgencia cuántica

Para exposición criptográfica se usa un escenario de brecha temporal:

\[
G = X + Y - Z
\]

- `X`: vida útil de confidencialidad o confianza;
- `Y`: duración estimada de migración;
- `Z`: horizonte de amenaza aprobado para el escenario.

`Z` no es una predicción. La urgencia se transforma a una escala 1–5 según bandas versionadas. Cuando faltan datos, se usa un valor central de 3 y se reduce la confianza.

### 9.3 Probabilidad ordinal

\[
L = 0.25E_x + 0.20F + 0.20A + 0.20U + 0.15S
\]

Los factores 0–5 son exposición, factibilidad, capacidad del actor, urgencia y sigilo/persistencia.

### 9.4 Efectividad del control

\[
M = implementation \times (0.40 + 0.60\times assurance)
\]

La fórmula impide otorgar crédito completo a una implementación sin evidencia suficiente.

### 9.5 Riesgo base y residual

\[
R_{base} = 100\times\frac{I}{5}\times\frac{L}{5}
\]

\[
R_{residual} = R_{base}(1-M)
\]

Bandas: bajo `<20`, moderado `<40`, alto `<60`, muy alto `<80` y crítico `>=80`.

### 9.6 Confianza e intervalo

\[
C = 0.35M_e + 0.25Q_s + 0.25R_p + 0.15T_a
\]

Los factores son madurez de evidencia, calidad de fuente, reproducibilidad y aplicabilidad temporal/contextual.

\[
R_{low}=R(0.65+0.35C)
\]

\[
R_{high}=\min(100,R(1.35-0.35C))
\]

La confianza modifica el rango, no el riesgo central. Riesgo alto con confianza baja significa necesidad urgente de obtener mejor evidencia, no permiso para ignorarlo.

## 10. Ciclo de evaluación

1. **Autorizar y limitar:** propietario, autoridad, terceros, datos, stop conditions y ruta de divulgación.
2. **Descomponer el sistema:** seis planos, activos, dependencias y límites de confianza.
3. **Inventariar y valorar:** versiones, propietarios, criptografía, datos, misión, actualizaciones y proveedores.
4. **Seleccionar dominios:** aplicar perfiles y justificar exclusiones/herencias.
5. **Modelar amenazas:** actor, acceso, QTA, QTE, activo, consecuencia y observables.
6. **Seleccionar controles:** relación técnica-control y evidencia esperada.
7. **Diseñar pruebas:** método menos intrusivo que pueda producir evidencia suficiente.
8. **Ejecutar y registrar:** resultados, hashes, limitaciones y QAL.
9. **Calcular riesgo:** impacto, probabilidad, control, residual, confianza y rango.
10. **Tratar y revalidar:** evitar, reducir, asignar contractualmente o aceptar con propietario, fecha y criterio de salida.

## 11. Top 10 de riesgos prioritarios

1. Criptografía vulnerable a capacidades cuánticas protegiendo datos de larga vida.
2. Inventario criptográfico incompleto y criptoagilidad insuficiente.
3. Compromiso del plano de control clásico.
4. Cadena no confiable de software, compilador o circuito.
5. Aislamiento débil en servicios cuánticos compartidos.
6. Manipulación de calibración, ruido o ambiente.
7. Fallos de autenticación, implementación y nodos de confianza en QKD.
8. QRNG opaco y ciclo de vida de claves deficiente.
9. Fallos de integridad/disponibilidad en redes, flujos híbridos o sensado.
10. Brechas de cadena de suministro, ciclo de vida y aseguramiento.

El Top 10 es una vista ejecutiva. La evaluación técnica usa las técnicas, controles y pruebas subyacentes; no basta con marcar diez casillas.

## 12. Conformidad, límites y no afirmaciones

Una evaluación puede declarar “realizada con Q-SECAT” cuando incluye alcance, autorización, aplicabilidad de dominios, amenazas, controles, pruebas/evidencia, riesgos, confianza, limitaciones y tratamiento. No puede declarar “certificación Q-SECAT”.

Q-SECAT no afirma:

- que exista hoy un CRQC operativo;
- una fecha cierta de “Q-day”;
- que QKD sea seguro solo por utilizar física cuántica;
- que PQC elimine fallos de implementación, integración o claves;
- que toda técnica haya sido observada en incidentes reales;
- que una puntuación demuestre seguridad.

El modelo debe calibrarse con casos reales autorizados, revisión de expertos y evolución de estándares. Los riesgos correlacionados, la seguridad física y la seguridad de misión pueden requerir métodos complementarios como FMEA, HAZOP o STPA.

## 13. Implementación de referencia

El repositorio incluye:

- catálogos YAML y matriz CSV;
- JSON Schema de evaluación;
- CLI Python para validar, comprobar trazabilidad y calcular riesgo;
- evaluación de ejemplo;
- pruebas automatizadas;
- Dockerfile y CI de GitHub Actions;
- documentación de fuentes, gobierno y contribución.

Comandos principales:

```bash
qsecat coverage
qsecat validate examples/assessment-example.yaml
qsecat score examples/assessment-example.yaml
pytest
```

## 14. Agenda de validación

Antes de declarar una versión estable se requieren:

- revisión pública por criptógrafos, especialistas QKD, hardware, redes, nube, sensores y aseguramiento;
- estudios de caso autorizados en múltiples perfiles;
- calibración empírica de pesos y umbrales;
- adaptadores para CBOM/SBOM/SARIF;
- comparación explícita y versionada con normas y marcos externos;
- reproducción independiente del CLI, esquema y relaciones;
- gobierno multiinstitucional y proceso formal de asignación de IDs.

## 15. Cita y autoría

> Peñuela Camacho, E. J. (2026). *Q-SECAT: Quantum Security Evaluation, Controls, Assurance & Testing Framework* (v0.1.0, Community Draft).

La creación conceptual, estructura del modelo y autoría principal se atribuyen a **Edwin Javier Peñuela Camacho**. Las futuras contribuciones deberán registrarse mediante el historial Git, `CONTRIBUTORS.md` y notas de versión.

## Referencias

La bibliografía verificable, con tipo de fuente, año y URL, se mantiene en [`docs/sources.md`](sources.md) y en el catálogo legible por máquina [`catalog/sources.yaml`](../catalog/sources.yaml). Las fuentes se clasifican para no equiparar normas oficiales, investigación revisada, preprints, tesis, proyectos comunitarios y documentación de implementaciones.
