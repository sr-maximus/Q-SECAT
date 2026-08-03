FROM python:3.12-slim

LABEL org.opencontainers.image.title="Q-SECAT"
LABEL org.opencontainers.image.description="Quantum Security Evaluation, Controls, Assurance & Testing Framework"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.authors="Edwin Javier Peñuela Camacho"

WORKDIR /opt/qsecat
COPY . /opt/qsecat
RUN python -m pip install --no-cache-dir .

ENTRYPOINT ["qsecat"]
CMD ["coverage"]
