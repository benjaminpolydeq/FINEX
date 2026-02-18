# 🏦 FINEX — Financial Expert Data Platform

> **Infrastructure souveraine de collecte, structuration et monétisation de données financières professionnelles.**

[![Python](https://img.shields.io/badge/Backend-Python%2072.7%25-3776AB?style=flat-square&logo=python)](https://python.org)
[![JavaScript](https://img.shields.io/badge/Frontend-JavaScript%2027.3%25-F7DF1E?style=flat-square&logo=javascript)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/Licence-Propriétaire-red?style=flat-square)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-En%20développement-orange?style=flat-square)]()

---

## 📋 Sommaire

- [Vision](#-vision)
- [Acteurs de la plateforme](#-acteurs-de-la-plateforme)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture technique](#-architecture-technique)
- [Stack technique](#-stack-technique)
- [Modèle économique](#-modèle-économique)
- [Structure du projet](#-structure-du-projet)
- [Prérequis & Installation](#-prérequis--installation)
- [Lancement](#-lancement)
- [Roadmap 24 mois](#-roadmap-24-mois)
- [Conformité & Sécurité](#-conformité--sécurité)
- [Prompt de génération IA](#-prompt-de-génération-ia)
- [Licence](#-licence)
- [Contact](#-contact)

---

## 🎯 Vision

FINEX est une **marketplace intelligente de données financières professionnelles déclassifiées**. Elle connecte des experts financiers, fournisseurs de datasets et acheteurs institutionnels au sein d'un écosystème sécurisé, conforme et monétisable.

La plateforme ambitionne de devenir l'**infrastructure de souveraineté des données financières africaines et internationales**, avec une approche mobile-first adaptée aux marchés émergents.

---

## 👥 Acteurs de la plateforme

### 1️⃣ Fournisseurs de données
- Experts financiers (fiscalité, investissement, comptabilité, crypto, finance d'entreprise)
- Comptables & auditeurs
- Analystes financiers
- Banques (données déclassifiées)
- Gouvernements (données publiques enrichies)
- Institutions économiques & statistiques

### 2️⃣ Acheteurs
- Entreprises IA & startups data
- Hedge funds & sociétés de gestion
- Fintechs
- Cabinets d'études de marché
- Institutions publiques & régulateurs

---

## ⚙️ Fonctionnalités

### Pour les fournisseurs (experts)
- Création de compte partenaire avec **vérification KYC**
- Upload de datasets (PDF, Excel, CSV, relevés bancaires)
- Définition du prix et des conditions d'accès
- Rédaction d'une description longue (textarea dédié)
- Dashboard revenus & statistiques d'usage
- Certification des données déclassifiées

### Pour les acheteurs
- Recherche intelligente via **moteur IA (RAG)**
- Filtres avancés : catégorie, région, continent, fourchette de prix (slider)
- Filtres sous forme de **chips horizontaux scrollables** avec état actif visuel
- **Sélection multiple** de datasets + bouton "Ajouter au panier"
- **Panier temporaire** avant achat consolidé
- Modal détaillée au clic sur une card (description complète + aperçu)
- Système de **notation & avis** post-achat (1–5 étoiles)
- **Wishlist / Favoris** (cœur sur chaque card) avec persistance `localStorage`
- Badge dynamique sur l'icône Favoris dans la sidebar
- Accès API sécurisé aux datasets achetés
- Dashboard analytique personnalisé

### Intelligence artificielle
- Architecture **RAG** pour interroger les datasets
- Classification automatique des données
- **Data Valuation Engine** — scoring qualité et évaluation du prix
- Détection d'anomalies et de données erronées
- Chat IA spécialisé finance
- Analyse automatique de documents financiers (PDF, Excel)
- Génération de rapports personnalisés
- Support multilingue

### Administration
- Panel administrateur complet
- Gestion des droits d'accès (RBAC)
- Traçabilité complète des transactions
- Registre d'audit (smart contracts ou ledger)
- Conformité RGPD & régulations financières internationales

---

## 🏗 Architecture technique

```
┌─────────────────────────────────────────────────────────┐
│                      CLIENTS                            │
│     Web (React/Next.js) · Mobile-first · PWA            │
│  Dashboard Expert · Dashboard Acheteur · Admin Panel     │
└─────────────────────────┬───────────────────────────────┘
                          │ REST API + WebSocket
┌─────────────────────────▼───────────────────────────────┐
│                    API GATEWAY                          │
│           FastAPI · Auth JWT · Rate Limiting            │
└────┬──────────────┬───────────────┬─────────────────────┘
     │              │               │
┌────▼────┐   ┌─────▼──────┐  ┌────▼────────────────────┐
│  Users  │   │  Datasets  │  │     AI / RAG Engine     │
│ Service │   │  Service   │  │  LLM · Embeddings       │
│  + KYC  │   │ + Pricing  │  │  Qdrant Vector DB       │
└────┬────┘   └─────┬──────┘  └─────────────────────────┘
     │              │
┌────▼──────────────▼─────────────────────────────────────┐
│                    DATA LAYER                           │
│    PostgreSQL · Data Lake chiffré · Versioning          │
│          Encryption at rest (AES-256) & TLS 1.3         │
└─────────────────────────────────────────────────────────┘
```

### Microservices
- **Users Service** — authentification, KYC, profils, rôles
- **Datasets Service** — upload, stockage, versioning, pricing
- **Marketplace Service** — recherche, filtres, panier, transactions, wishlist
- **AI Service** — RAG, embeddings, scoring qualité, valuation, chat
- **Analytics Service** — dashboards, rapports, prédictions

---

## 🛠 Stack technique

| Couche | Technologie |
|--------|-------------|
| **Backend** | Python (FastAPI) — 72.7% du code |
| **Frontend** | JavaScript (React / Next.js) — 27.3% du code |
| **Base de données** | PostgreSQL |
| **Base vectorielle** | Qdrant (ou Chroma) |
| **Authentification** | JWT + OAuth2 |
| **Communication** | REST API + WebSocket |
| **IA / LLM** | Architecture RAG + modèle LLM intégré |
| **Stockage** | Data Lake sécurisé (AES-256) |
| **Déploiement** | Docker · Kubernetes · CI/CD |
| **Persistance client** | localStorage (wishlist, panier, datasets publiés) |

---

## 💰 Modèle économique

| Source de revenus | Description |
|-------------------|-------------|
| **Marketplace datasets** | Commission sur chaque vente de dataset |
| **Abonnement premium acheteur** | Accès illimité et fonctions avancées |
| **Rémunération à l'usage** | API calls et volume de données téléchargé |
| **Rémunération par contribution** | Bonus fournisseur selon qualité et adoption |
| **Marketplace d'expertise** | Mise en relation consultant ↔ entreprise |
| **Rapports & études personnalisés** | Générés via IA pour clients institutionnels |

---

## 📁 Structure du projet

```
FINEX/
├── backend/
│   ├── app.py                   # Point d'entrée FastAPI
│   ├── requirements.txt         # Dépendances Python
│   ├── .env.example             # Variables d'environnement (template)
│   ├── core/
│   │   ├── config.py            # Configuration & settings
│   │   ├── security.py          # JWT, chiffrement, RBAC
│   │   └── database.py          # Connexion PostgreSQL / SQLAlchemy
│   ├── routes/
│   │   ├── auth.py              # Endpoints authentification & KYC
│   │   ├── datasets.py          # Endpoints datasets (CRUD, upload)
│   │   ├── marketplace.py       # Endpoints marketplace & transactions
│   │   └── ai.py                # Endpoints IA / RAG / chat
│   ├── models/
│   │   ├── user.py              # Modèle utilisateur / expert
│   │   ├── dataset.py           # Modèle dataset + versioning
│   │   └── transaction.py       # Modèle transaction & audit
│   └── services/
│       ├── rag_service.py       # Moteur RAG + embeddings Qdrant
│       ├── valuation.py         # Data Valuation Engine
│       ├── anomaly_detector.py  # Détection d'anomalies
│       └── kyc_service.py       # Vérification KYC
│
├── frontend/
│   └── pages/
│       ├── index.html           # Page d'accueil / landing
│       ├── dashboard.html       # Dashboard utilisateur
│       ├── marketplace.html     # Marketplace datasets
│       ├── wishlist.html        # Liste de favoris
│       └── admin.html           # Panel administrateur
│
└── LICENSE                      # Licence propriétaire
```

---

## 🚀 Prérequis & Installation

### Prérequis système

- **Python** 3.10+ — [Télécharger](https://www.python.org/downloads/)
- **Node.js** 18+ — [Télécharger](https://nodejs.org/)
- **PostgreSQL** 14+
- **Docker & Docker Compose** (recommandé)
- **Git**

### Installation

**1. Cloner le dépôt**

```bash
git clone https://github.com/benjaminpolydeq/FINEX.git
cd FINEX
```

**2. Configurer le backend**

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Renseigner : DATABASE_URL, JWT_SECRET, QDRANT_URL, LLM_API_KEY, etc.
```

**3. Configurer le frontend**

```bash
cd ../frontend
npm install
```

**4. Initialiser la base de données**

```bash
cd backend
python -m alembic upgrade head
```

---

## ▶️ Lancement

### Mode développement

```bash
# Terminal 1 — Backend
cd backend
uvicorn app:app --reload --port 8000

# Terminal 2 — Frontend
cd frontend
npx serve pages/ --port 3000
```

| Service | URL |
|---------|-----|
| API Backend | `http://localhost:8000` |
| Documentation API (Swagger) | `http://localhost:8000/docs` |
| Interface Frontend | `http://localhost:3000` |

### Mode Docker (recommandé pour la production)

```bash
docker-compose up --build
```

---

## 🗺 Roadmap 24 mois

| Phase | Période | Objectifs clés |
|-------|---------|----------------|
| **Phase 1 — MVP** | M1 → M6 | Auth + KYC, upload datasets, marketplace basique, paiement sécurisé |
| **Phase 2 — IA** | M7 → M12 | RAG, Data Valuation Engine, scoring qualité, chat IA, rapports auto |
| **Phase 3 — Scale** | M13 → M18 | API publique, multi-région, conformité RGPD avancée, accès institutionnel |
| **Phase 4 — Expansion** | M19 → M24 | Marchés africains, PWA mobile-first, partenariats gouvernementaux |

---

## 🔐 Conformité & Sécurité

- **KYC** obligatoire pour tout fournisseur de données
- **Chiffrement AES-256** au repos et **TLS 1.3** en transit
- **RGPD** et régulations financières internationales (DORA, MiFID II)
- **Traçabilité** complète via registre d'audit immuable
- **Certification** des données déclassifiées avant mise en vente
- Gestion des droits d'accès par rôle (**RBAC**)
- Détection de fraude et d'anomalies via IA

---

## 🤖 Prompt de génération IA

Le projet FINEX a été conçu et prototypé avec l'aide d'un assistant IA (Google Gemini via AI Studio). Voici le **prompt maître optimisé** utilisé pour générer l'architecture complète et les composants de la plateforme. Ce prompt peut être réutilisé pour étendre ou régénérer des parties du projet.

<details>
<summary><strong>📋 Cliquer pour afficher le prompt complet</strong></summary>

```
Tu es un architecte logiciel senior spécialisé en fintech, gouvernance des données,
IA et plateformes SaaS à grande échelle.

Ta mission est de concevoir et développer une application appelée FINEX.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 VISION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINEX est une plateforme légale de collecte, structuration et monétisation de données
financières professionnelles déclassifiées.

Elle permet :
- Aux experts financiers d'ouvrir un compte partenaire et partager des données légales
- D'être rémunérés selon la valeur et l'utilisation réelle de leurs données
- Aux entreprises IA, cabinets d'études et gouvernements d'acheter ces données via API
- De devenir le marché de référence des données financières pour l'industrie de l'IA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👥 ACTEURS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fournisseurs :
  - Experts financiers (fiscalité, investissement, comptabilité, crypto, finance d'entreprise)
  - Comptables, auditeurs, analystes
  - Banques (données déclassifiées), gouvernements (données publiques enrichies)
  - Institutions économiques et statistiques

Acheteurs :
  - Entreprises IA, startups data, hedge funds, fintechs
  - Cabinets d'études de marché, institutions publiques, régulateurs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 MODÈLE ÉCONOMIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Marketplace de datasets (commission sur vente)
- Abonnement premium acheteur (accès illimité + API)
- Rémunération par contribution (qualité, scoring)
- Rémunération à l'usage (API calls, volume téléchargé)
- Marketplace d'expertise (mise en relation expert ↔ entreprise)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚖️ EXIGENCES LÉGALES & CONFORMITÉ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Vérification KYC obligatoire pour tout fournisseur
- Certification des données déclassifiées avant mise en ligne
- Traçabilité complète des transactions (registre d'audit / smart contracts)
- Conformité RGPD, MiFID II, DORA et régulations financières locales
- Chiffrement AES-256 au repos, TLS 1.3 en transit
- Gestion des droits d'accès par rôle (RBAC)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 INTELLIGENCE ARTIFICIELLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Intégrer obligatoirement :
- Architecture RAG pour interroger et enrichir les datasets
- Système d'embeddings + base vectorielle (Qdrant)
- Classification automatique des données financières
- Data Valuation Engine (évaluation automatique du prix d'un dataset)
- Scoring qualité des données (0–100)
- Détection d'anomalies et de données erronées
- Chat IA spécialisé finance (questions sur les datasets)
- Analyse automatique de documents (PDF, Excel, relevés bancaires)
- Génération de rapports financiers personnalisés
- Support multilingue (FR, EN, AR minimum)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏗 ARCHITECTURE TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Backend (microservices) :
  - FastAPI (Python) · PostgreSQL · Qdrant
  - Authentification JWT + OAuth2
  - REST API + WebSocket
  - Data Lake sécurisé · Versioning datasets

Frontend :
  - React / Next.js
  - Dashboard fournisseur · Dashboard acheteur · Admin panel
  - Design system fintech moderne, mobile-first, PWA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 COMPOSANTS FRONTEND ATTENDUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Layout :
  - Sidebar responsive, bouton menu à droite sur mobile
  - Badge dynamique sur l'icône Favoris (count wishlist)
  - Navigation fluide entre Dashboard, Marketplace, Favoris, IA, Admin

DataMarketplace :
  - Cards datasets avec : titre, catégorie, région, prix, note, badge qualité
  - Checkbox de sélection sur chaque card + bouton "Ajouter au panier"
  - Panier temporaire (state) avant achat consolidé
  - Modal détaillée au clic sur une card (description longue, aperçu)
  - Filtres horizontaux scrollables avec état actif visuel :
      * Catégorie (fiscalité, investissement, comptabilité, crypto…)
      * Région géographique
      * Continent (Afrique, Europe, Amérique du Nord, Asie, Amérique du Sud, Océanie)
      * Fourchette de prix (range slider)
  - Cœur / icône favori sur chaque card (toggle wishlist, animation scale)
  - Notation 1-5 étoiles post-achat, persistée sur la card
  - Formulaire de soumission de dataset (titre, catégorie, prix, description textarea)
  - Persistance des datasets publiés dans localStorage (finex_published_datasets)

Wishlist :
  - Fusion des datasets mockés + datasets localStorage
  - Empty state avec CTA vers le Marketplace
  - Design cohérent avec les cards Marketplace

AIConsultant :
  - Interface chat avec l'IA spécialisée finance
  - Upload de documents pour analyse
  - Affichage structuré des réponses et rapports

Dashboard :
  - KPIs : revenus, datasets vendus, API calls, score qualité moyen
  - Graphiques d'activité (temporal)
  - Top datasets et top experts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌍 POSITIONNEMENT STRATÉGIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINEX doit devenir une infrastructure de souveraineté des données financières
africaines et internationales : scalable, sécurisée, mobile-first et adaptée
à la faible consommation de données des marchés émergents.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 LIVRABLES ATTENDUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Architecture complète (schéma microservices)
2. Schéma base de données (PostgreSQL + Qdrant)
3. Modèle économique détaillé
4. Data governance model
5. Plan de conformité légale (KYC, RGPD, audit)
6. Roadmap 24 mois (4 phases)
7. Risques et stratégies de mitigation
8. Avantage compétitif vs concurrents
9. Code fonctionnel des composants frontend (React/TypeScript)
10. Endpoints API REST documentés (FastAPI/Swagger)
```

</details>

---

## 📄 Licence

> ⚠️ **Ce logiciel est soumis à une licence propriétaire stricte.**

FINEX est la propriété exclusive de **Benjamin Amaad Kama**. Tous droits réservés.

Toute utilisation, copie, modification, distribution, publication ou exploitation est **strictement interdite** sans accord écrit préalable du titulaire des droits.

Il est formellement interdit de désassembler, décompiler ou procéder à une ingénierie inverse du logiciel.

Pour toute demande de licence : [benjokama@hotmail.fr](mailto:benjokama@hotmail.fr)

---

## 📬 Contact

**Auteur :** Benjamin Amaad Kama
**Email :** [benjokama@hotmail.fr](mailto:benjokama@hotmail.fr)
**Dépôt :** [github.com/benjaminpolydeq/FINEX](https://github.com/benjaminpolydeq/FINEX)

---

<div align="center">
  <sub><em>FINEX — L'infrastructure de souveraineté des données financières.</em></sub>
</div>
