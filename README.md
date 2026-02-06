# 🌿 Eco-Traffic Seattle 
### Prédiction des Niveaux de Congestion par Enrichissement de Données via Web Scraping

---

## 👥 Authors
* **Mohamed Raed Bouhali**
* **Ilef Ben Hassen**

---

## 📖 1. Présentation du Projet
**Titre :** `SmartTraffic Seattle : Système de Prédiction de Congestion Urbaine par Enrichissement Multisources`

Dans le cadre du module **"Python for Data Science 2"**, ce projet transforme des données statiques de comptage de véhicules en un outil prédictif dynamique. 

**Objectif Principal :** Prédire le niveau de trafic (**Fluide, Modéré, Critique**) sur les axes routiers de Seattle en combinant des données historiques et des données contextuelles extraites en temps réel (Météo/News).

---

## ⚙️ 2. Spécifications Fonctionnelles
| Module | Description |
| :--- | :--- |
| **[Data_Ingestion]** | Collecte automatisée des données météo 2022 et extraction d'incidents via Web Scraping. |
| **[Predictive_Core]** | Classification du niveau de trafic basée sur les caractéristiques géospatiales et temporelles. |
| **[User_Interface]** | Visualisation interactive sur un Dashboard **React** pour consulter l'état futur du trafic sur une carte. |
| **[Service_Access]** | Exposition des prédictions via une **API REST FastAPI** pour une intégration tierce. |

---

## 🛠️ 3. Spécifications Techniques

### 🧠 A. Data Pipeline & ML (Phase 1 & 2)
* **Sources :** Données SDOT (`trafficFlow.csv`) enrichies par Scraping (**BeautifulSoup/Selenium**).
* **Prétraitement :** Nettoyage, Feature Engineering (saisonnalité, heures de pointe, jours fériés).
* **Équilibrage :** Utilisation de **SMOTE** pour gérer le déséquilibre des classes (Congestion Critique).
* **Modélisation :** Comparaison **Random Forest** vs **XGBoost** avec optimisation via **GridSearchCV**.
* **Gouvernance :** Suivi des métriques et versioning des modèles via **MLflow**.

### 🌐 B. Architecture Logicielle & Déploiement (Phase 3)
* **Backend :** Framework **FastAPI** avec gestion des prédictions unitaires et par lots (batch).
* **Frontend :** Framework **React (Vite)** avec intégration de cartes dynamiques (**Leaflet**).
* **DevOps :** Conteneurisation avec **Docker** et orchestration via **Docker-Compose**.

---

## 📌 Livrables Attendus
1.  ✅ **Dépôt GitHub** avec code source documenté.
2.  ✅ **Environnement virtualisé** prêt à l'emploi via Docker.
3.  ✅ **Dashboard interactif** fonctionnel.

---
