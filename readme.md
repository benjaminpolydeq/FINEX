# 🏦 FINEX

> **La place des experts financiers pour partager des données et générer de la valeur.**

FINEX est une plateforme web full-stack dédiée aux professionnels et experts financiers. Elle leur permet de partager, analyser et exploiter des données financières afin de créer de la valeur collective.

---

## 📋 Sommaire

- [Présentation](#présentation)
- [Stack technique](#stack-technique)
- [Architecture du projet](#architecture-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Lancement](#lancement)
- [Structure des dossiers](#structure-des-dossiers)
- [Licence](#licence)
- [Contact](#contact)

---

## Présentation

FINEX offre aux experts financiers un espace collaboratif pour :

- Partager et centraliser des données financières
- Analyser et visualiser des indicateurs clés
- Générer de la valeur à travers l'intelligence collective
- Accéder à des outils d'aide à la décision

---

## Stack technique

| Couche | Technologie |
|--------|-------------|
| **Backend** | Python (~73% du code) |
| **Frontend** | JavaScript (~27% du code) |
| **Architecture** | Client-serveur avec API REST |

---

## Architecture du projet

Le projet suit une architecture **séparation frontend/backend** :

```
FINEX/
├── backend/          # Serveur Python (API, logique métier, données)
├── frontend/
│   └── pages/        # Pages de l'interface utilisateur (JavaScript)
└── LICENSE
```

### Backend (Python)

Le backend Python gère :
- L'exposition des données via une API REST
- La logique métier financière
- Le traitement et la persistance des données

### Frontend (JavaScript)

Le frontend constitue l'interface utilisateur à travers les pages du répertoire `frontend/pages/`, consommant les données exposées par l'API backend.

---

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé :

- **Python** 3.8+ — [Télécharger](https://www.python.org/downloads/)
- **Node.js** 16+ (si un bundler JS est utilisé) — [Télécharger](https://nodejs.org/)
- **pip** (gestionnaire de paquets Python)
- **Git**

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/benjaminpolydeq/FINEX.git
cd FINEX
```

### 2. Configurer le backend

```bash
cd backend
pip install -r requirements.txt
```

> Si un fichier `.env` est requis, copiez le fichier d'exemple :
> ```bash
> cp .env.example .env
> # Remplissez les variables d'environnement nécessaires
> ```

### 3. Configurer le frontend

```bash
cd ../frontend
# Si des dépendances npm sont présentes :
npm install
```

---

## Lancement

### Démarrer le backend

```bash
cd backend
python app.py
# ou selon le framework utilisé :
# python -m flask run
# uvicorn main:app --reload
```

Le serveur backend sera disponible sur `http://localhost:5000` (ou le port configuré).

### Démarrer le frontend

Ouvrez les fichiers HTML du dossier `frontend/pages/` dans votre navigateur, ou servez-les via un serveur statique :

```bash
cd frontend
npx serve pages/
# ou
python -m http.server 3000
```

L'interface sera accessible sur `http://localhost:3000`.

---

## Structure des dossiers

```
FINEX/
├── backend/
│   ├── app.py              # Point d'entrée du serveur
│   ├── requirements.txt    # Dépendances Python
│   ├── routes/             # Définition des routes API
│   ├── models/             # Modèles de données
│   └── services/           # Logique métier
│
├── frontend/
│   └── pages/
│       ├── index.html      # Page d'accueil
│       ├── dashboard.html  # Tableau de bord
│       └── ...             # Autres pages
│
└── LICENSE                 # Licence propriétaire
```

---

## Licence

> ⚠️ **Ce logiciel est soumis à une licence propriétaire.**

FINEX est la propriété exclusive de **Benjamin Amaad Kama**. Tous droits réservés.

Toute utilisation, copie, modification, distribution ou exploitation est **strictement interdite** sans accord écrit préalable du titulaire des droits.

Pour toute demande de licence ou d'utilisation : [benjokama@hotmail.fr](mailto:benjokama@hotmail.fr)

---

## Contact

**Auteur :** Benjamin Amaad Kama  
**Email :** [benjokama@hotmail.fr](mailto:benjokama@hotmail.fr)  
**Dépôt :** [github.com/benjaminpolydeq/FINEX](https://github.com/benjaminpolydeq/FINEX)

---

*FINEX — La place des experts financiers.*
