# Image de base Node.js légère
FROM node:18-alpine

# Définition du répertoire de travail
WORKDIR /app

# Installation de Trivy pour le scan de sécurité
RUN apk add --no-cache wget tar \
    && wget -qO - https://github.com/aquasecurity/trivy/releases/download/v0.18.3/trivy_0.18.3_Linux-64bit.tar.gz | tar xz \
    && mv trivy /usr/local/bin

# Copie des fichiers de dépendances
COPY package*.json ./

# Installation des dépendances Node.js
RUN npm install

# Copie du code source
COPY . .

# Lancement du scan de sécurité
RUN trivy filesystem --no-progress --ignore-unfixed --severity HIGH,CRITICAL /app

# Exposition du port
EXPOSE 3000

# Démarrage de l'application
CMD ["npm", "start"] 