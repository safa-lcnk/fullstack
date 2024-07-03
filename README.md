
---

# 📦 **Application en Trois Parties**

1. **Frontend** : React
2. **Backend** : FastAPI Python
3. **Base de Données** : MongoDB

---

## 🗄️ **1. Lancer un Container MongoDB avec son Volume**

```sh
docker volume create mongodb_data
```

```sh
docker run -d --name mongodb \
    -p 27017:27017 \
    -v mongodb_data:/data/db \
    mongo:latest
```

---

## ⚙️ **2. Dans le Dossier Backend**

### Créer un Nouvel Environnement Python

```sh
python3 -m venv env
```

### Se Connecter à l'Environnement Python

#### Sur Unix
```sh
source env/bin/activate
```

#### Sur Windows en PowerShell
```sh
env\Scripts\activate
```

### Installer les Dépendances Python
```sh
pip install -r requirements.txt
```

---

## 📥 **3. Charger les Données sur MongoDB**

1. **Ouvrir MongoDB Compass et Ajouter Graphiquement** :
    - **Base de Données** : `dashboard`
    - **Collection** : `cars`
2. **Lancer le Script de Chargement dans la DB dans le Dossier Backend** :

```sh
python3 importScript.py
```

---

## 🌐 **4. Démarrer le Frontend**

```sh
cd frontend
npm install
npm start
```

---

## 🔧 **5. Démarrer le Backend**

```sh
cd backend
python3 -m uvicorn main:app --reload
```

---

