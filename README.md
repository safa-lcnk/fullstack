---
 docker compose build --no-cache
 docker compose up -d

 Import des données dans MongoDB :
    docker compose exec backend python importScript.py

# 📦 **Application en Trois Parties**

1. **Frontend** : React
2. **Backend** : FastAPI Python
3. **Base de Données** : MongoDB

---

## 🐳 **Installation avec Docker**

1. **Construire et démarrer tous les services**
```sh
docker compose up --build
```

2. **Pour charger les données dans MongoDB**
```sh
docker compose exec backend python importScript.py
```

3. **Accéder aux services**
- Frontend : http://localhost:3000
- Backend : http://localhost:8000
- MongoDB : localhost:27017

---

## 🔧 **Installation Manuelle (Alternative)**

[... reste du README existant ...]
