## Cette application est en 3 parties : 
1 - Frontend en React
2 - Backend en FastAPI Python
3 - Une base de données MongoDB

## 1 - Lancer un container mongoDB avec ses volumes

```sh
docker volume create mongodb_data
```

```sh
docker run -d --name mongodb \
    -p 27017:27017 \
    -v mongodb_data:/data/db \
    mongo:latest
```

## 2 - Dans le dossier backend :

- lancer un nouvel environnement python
```sh
python3 -m venv env
```

- se connecter à l'environnement python env
sur unix : 
```sh
source env/bin/activate
```

sur windows en powershell:
```sh
env\Scripts\activate
```

- Installer les dépendances python
```sh
pip install -r requirements.txt
```

## 3 - Charger les données sur MongoDB

1 - Ouvrir Mongo Compass et y ajouter graphiquement: 
    - la base de données dashboard
    - la collection cars
2 - Lancer le script de chargement dans la DB dans le dossier backend:

```sh
python3 importScript.py
```

## 4 - Démarrer le front :

```sh
cd frontend
npm install
npm start
```

## 5 - Démarrer le backend

```sh
cd backend
python3 -m uvicorn main:app --reload
```

