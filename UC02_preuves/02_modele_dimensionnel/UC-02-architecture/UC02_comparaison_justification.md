
# UC-02 — Comparaison et justification des choix

## 1. Architectures envisagées

Deux approches ont été étudiées :
- Data Warehouse relationnel
- Lakehouse

| Critère | Data Warehouse | Lakehouse |
|---|---|---|
| Données structurées | Très adapté | Adapté |
| Analyses SQL | Très adapté | Très adapté |
| Intégration Power BI | Directe avec PostgreSQL | Dépend de la plateforme |
| Données non structurées | Moins flexible | Très flexible |
| Mise en œuvre locale | Relativement simple | Plus complexe selon les outils |
| Évolutivité | Verticale et optimisation SQL | Potentiel distribué |
| Adéquation au TP | Forte | Possible mais non nécessaire |

## 2. Architecture retenue

L'architecture proposée repose sur un Data Warehouse
relationnel PostgreSQL organisé en plusieurs couches :

Sources → Ingestion → Staging → Data Warehouse
→ Data Marts → Power BI.

## 3. Justification des technologies

### Python
- Lecture des fichiers .dat.
- Contrôles de structure et de qualité.
- Automatisation des traitements.
- Journalisation des chargements.

### PostgreSQL
- Stockage relationnel.
- Jointures entre faits et dimensions.
- Transformations et agrégations SQL.
- Gestion des contraintes d'intégrité.

### Modèle dimensionnel
- Séparation des faits et dimensions.
- Analyse des ventes par produit, client et période.
- Réutilisation des dimensions communes.

### Power BI
- Création de tableaux de bord.
- Visualisation des KPI.
- Exploration interactive des résultats.

## 4. Contraintes identifiées

L'exploration UC-01 a montré que la table inventory
contient plus de 23 millions de lignes.

L'architecture devra donc prévoir :
- Des chargements efficaces, par exemple avec COPY.
- Des index adaptés aux requêtes.
- Une stratégie de traitement des rafraîchissements.
- Des contrôles de qualité et de traçabilité.
- Des tests de performance.

## 5. Limites

Le choix est effectué au stade de la conception.
Aucun test comparatif de performance entre PostgreSQL
et une solution Lakehouse n'a encore été réalisé.

Le dimensionnement définitif dépendra des ressources
matérielles et des besoins de consultation.

## 6. Compétences démontrées

C03 — Concevoir une architecture Data adaptée.

C10 — Justifier et documenter les choix techniques.
