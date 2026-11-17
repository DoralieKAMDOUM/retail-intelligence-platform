# UC-02 — Choix et justification de l'architecture

## 1. Contexte

Le projet Retail Intelligence Platform vise à centraliser et exploiter des données commerciales provenant de plusieurs fichiers structurés, notamment les ventes en magasin, les ventes en ligne, les produits, les clients et les stocks.

Deux ensembles de données sont disponibles : un chargement initial (`data/`) et un ensemble de rafraîchissement (`data_refresh/`).

## 2. Architecture retenue

Une architecture Data Warehouse en couches est proposée :

1. **Sources :** fichiers `.dat` initiaux et fichiers de rafraîchissement.
2. **Ingestion :** scripts Python pour lire, contrôler et charger les données.
3. **Staging :** conservation des données sources et traçabilité des chargements.
4. **Data Warehouse :** modélisation relationnelle et analytique dans PostgreSQL.
5. **Data Marts :** préparation des indicateurs pour les différents besoins métier.
6. **Restitution :** tableaux de bord Power BI.

## 3. Justification des choix

**Python :** permet de développer des traitements de fichiers et des contrôles de qualité avec les bibliothèques standard.

**PostgreSQL :** offre un moteur relationnel adapté aux jointures, aux transformations SQL et à la structuration des données analytiques.

**Modèle dimensionnel :** facilite l'analyse des ventes selon les produits, les clients et les périodes.

**Power BI :** permet de restituer les KPI et de proposer des tableaux de bord aux décideurs.

## 4. Gestion des rafraîchissements

Les données du dossier `data_refresh/` devront être intégrées avec des mécanismes permettant d'identifier les nouveaux enregistrements, de contrôler les doublons et d'éviter les chargements répétés.

Les règles d'insertion, de mise à jour ou de remplacement seront définies selon les clés et la granularité de chaque table.

## 5. Limites et hypothèses

L'architecture reste au stade de conception. Les contraintes de volumétrie, les clés de jointure, les règles d'actualisation et les capacités de l'environnement technique devront être confirmées avant l'implémentation.