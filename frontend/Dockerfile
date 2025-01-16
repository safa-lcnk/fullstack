# Étape 1 : Construction
# Utilisation d'une image Node.js légère pour la construction
FROM node:20.9.0-alpine AS builder  

# Définition du répertoire de travail à /app
WORKDIR /app  

# Copie des fichiers de dépendances (package.json et package-lock.json)
COPY package*.json ./  

# Installation des dépendances Node.js
RUN npm install  

# Copie du code source de l'application dans le conteneur
COPY . .  

# Construction de l'application React (génération des fichiers statiques)
RUN npm run build  

# Étape 2 : Production
# Utilisation d'une image Nginx légère pour servir les fichiers statiques
FROM nginx:alpine  

# Copier les fichiers construits dans le répertoire de Nginx
COPY --from=builder /app/build /usr/share/nginx/html  

# Vérifier les droits d'accès pour Nginx
RUN chown -R nginx:nginx /usr/share/nginx/html  

# Exposition du port 80 pour que Nginx puisse servir l'application
EXPOSE 80  

# Commande pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"] 