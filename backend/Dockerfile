# Image de base Python avec une version légère
FROM python:3.9-slim

# Définition du répertoire de travail
WORKDIR /app

# Installation de Trivy et des dépendances Python 
RUN apt-get update && \
    apt-get install -y wget && \
    wget -qO - https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Scan de sécurité
RUN trivy filesystem --no-progress --ignore-unfixed --severity HIGH,CRITICAL /app

# Exposition du port
EXPOSE 8000

# Démarrage de l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"] 