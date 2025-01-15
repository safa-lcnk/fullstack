---
✅ docker compose up -d

🌀 - Import des données dans MongoDB : 🌀
docker compose exec backend python importScript.py

🔱 - Suivre logs backend : 🔱
docker compose logs -f backend