# Image de base Python avec une version légère
FROM python:3.12-alpine

# Définition du répertoire de travail
WORKDIR /app

# Installation de Trivy et des dépendances Python (sous utilisateur root)
RUN apt-get update && \
    apt-get install -y wget && \
    wget -qO - https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Ajout d'un utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Changer le propriétaire du répertoire de travail
RUN chown -R appuser:appgroup /app

# Copie du code source
COPY . .

# Scan de sécurité
RUN trivy filesystem --no-progress --ignore-unfixed --severity HIGH,CRITICAL /app

# Passer à l'utilisateur non-root
USER appuser

# Exposition du port
EXPOSE 8000

# Démarrage de l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"] 