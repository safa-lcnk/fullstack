## 🐳 Bonnes Pratiques Docker

 📝 Conventions d'écriture

### Dockerfile
- Utiliser des commentaires explicites
- Organiser les instructions par ordre logique
- Minimiser le nombre de layers (combiner les RUN quand possible)
- Spécifier des versions précises des images de base
- Documenter chaque instruction importante

### docker-compose.yml
- Indentation cohérente (2 espaces)
- Grouper les services par fonction
- Nommer explicitement les volumes et networks
- Documenter les variables d'environnement

## 🔒 Bonnes Pratiques de Sécurité

1. **Gestion des utilisateurs**
   - Créer des utilisateurs non-root
   - Limiter les permissions
   - Utiliser USER dans Dockerfile

2. **Images**
   - Utiliser des images officielles minimales
   - Scanner les vulnérabilités (Trivy, Snyk)
   - Mettre à jour régulièrement les bases

3. **Secrets**
   - Ne pas exposer les variables sensibles
   - Chiffrer les données sensibles

4. **Réseau**
   - Limiter les ports exposés
   - Utiliser des réseaux isolés
   - Configurer les pare-feu

5. **Conteneurs**
   - Activer les options de sécurité
   - Limiter les ressources
   - Monitorer les conteneurs

## 🔍 Vérification des Droits Utilisateurs

Pour vérifier les droits et groupes :

 - Backend : docker compose exec backend sh -> ls -la
 - Frontend : docker compose exec frontend sh -> ls -la
 - MongoDB : docker compose exec mongodb sh -> ls -la

 - d : directory
 - r : read
 - w : write
 - x : execute

 - 1er groupe : user
 - 2eme groupe : group
 - 3eme groupe : other

 ## 🚀 Commandes Docker Essentielles
```bash
# Construire les images
docker compose build

# Démarrer les services
docker compose up -d

# Voir les logs
docker compose logs -f (backend, frontend, mongodb)

# Import des données dans MongoDB
docker compose exec backend python importScript.py

# Arrêter les services
docker compose down
```