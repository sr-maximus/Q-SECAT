# Publicación de Q-SECAT en GitHub

**Repositorio objetivo:** `sr-maximus/Q-SECAT`<br>
**Primera versión:** `v0.1.0` — Community Draft

## 1. Crear el repositorio y publicar la rama principal

Desde la carpeta descomprimida:

```bash
git init
git branch -M main
git add .
git commit -s -m "feat: publish Q-SECAT v0.1.0 community draft"

gh auth status
gh repo create sr-maximus/Q-SECAT \
  --public \
  --description "Quantum Security Evaluation, Controls, Assurance & Testing Framework" \
  --source . \
  --remote origin \
  --push
```

El `-s` incorpora el `Signed-off-by` requerido por el DCO del proyecto.

## 2. Configuración recomendada del repositorio

En **Settings**:

- habilitar Issues y Discussions;
- habilitar Private vulnerability reporting;
- exigir pull request para `main` cuando exista más de un mantenedor;
- exigir que finalice `Q-SECAT CI` antes de fusionar;
- impedir force-push y eliminación de `main`;
- activar Dependabot para dependencias Python y GitHub Actions;
- conservar licencia Apache-2.0 y `CITATION.cff` visibles.

Topics recomendados:

```text
quantum-cybersecurity post-quantum-cryptography qkd qrng
quantum-computing security-testing risk-assessment security-framework
```

## 3. Crear la primera versión

```bash
git tag -s v0.1.0 -m "Q-SECAT v0.1.0 Community Draft"
git push origin v0.1.0

gh release create v0.1.0 \
  dist/q_secat-0.1.0-py3-none-any.whl \
  dist/q_secat-0.1.0.tar.gz \
  dist/qsecat-matrix.csv \
  dist/qsecat-coverage.json \
  dist/qsecat-example-score.json \
  --title "Q-SECAT v0.1.0 — Community Draft" \
  --notes-file RELEASE-NOTES.md
```

La firma de tag requiere una clave de firma configurada. Cuando no exista, use un tag anotado (`git tag -a`) y documente esa limitación en la versión.

## 4. Descripción sugerida para GitHub

> Open, evidence-oriented framework for evaluating post-quantum, quantum and quantum-enabled system security through domains, adversary techniques, controls, safe tests, assurance levels and an uncertainty-aware risk model.

## 5. Control editorial previo a publicar

```bash
python -m pip install -e .[dev]
python scripts/sync_package_data.py --check
python scripts/check_traceability.py
qsecat validate examples/assessment-example.yaml
qsecat score examples/assessment-example.yaml
pytest
```

Antes de una publicación pública también se debe revisar:

- que no haya credenciales, información de proveedores ni evidencias sensibles;
- que cada fuente siga accesible y conserve el alcance citado;
- que las afirmaciones nuevas indiquen su estado de evidencia;
- que `CHANGELOG.md`, `CITATION.cff` y la versión de todos los catálogos coincidan;
- que la versión continúe identificándose como borrador hasta revisión independiente.

## 6. Siguiente etapa de gobernanza

La versión 0.1.0 atribuye la creación conceptual y autoría principal a **Edwin Javier Peñuela Camacho**. Para avanzar hacia 1.0, el proyecto debería publicar un proceso de decisiones, convocar revisores de distintas disciplinas cuánticas y registrar conflictos de interés. Las contribuciones posteriores no deben borrar ni reemplazar la autoría original; deben añadirse de forma trazable.
