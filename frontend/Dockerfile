# Image de base Node.js légère
FROM node:20.9.0-alpine

# Définition du répertoire de travail
WORKDIR /app

# Installation de Trivy pour le scan de sécurité
RUN apk add --no-cache wget tar \
    && wget -qO - https://github.com/aquasecurity/trivy/releases/download/v0.18.3/trivy_0.18.3_Linux-64bit.tar.gz | tar xz \
    && mv trivy /usr/local/bin

# Ajout d'un utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copie des fichiers de dépendances
COPY package*.json ./

# Installation des dépendances Node.js
RUN npm install

# Changer le propriétaire du répertoire de travail
RUN chown -R appuser:appgroup /app

# Copie du code source
COPY . .

# Lancement du scan de sécurité
RUN trivy filesystem --no-progress --ignore-unfixed --severity HIGH,CRITICAL /app

# Passer à l'utilisateur non-root
USER appuser

# Exposition du port
EXPOSE 3000

# Démarrage de l'application
CMD ["npm", "start"] 