
# UC-01 — Schéma des besoins métier

## Objectif

Identifier les besoins décisionnels de la plateforme Retail
Intelligence Platform et les relier aux sources de données
disponibles.

## Schéma fonctionnel

```mermaid
flowchart TD
    A["Retail Intelligence Platform"]

    A --> B["Analyser les performances commerciales"]
    A --> C["Analyser les produits"]
    A --> D["Surveiller les stocks"]
    A --> E["Analyser les clients"]

    B --> F["store_sales / web_sales"]
    C --> G["item"]
    D --> H["inventory"]
    E --> I["customer"]

    F --> J["CA, quantités vendues, panier moyen"]
    G --> K["Ventes par produit et catégorie"]
    H --> L["Niveaux de stock et disponibilité"]
    I --> M["Répartition des ventes par client"]

    J --> N["Tableaux de bord décisionnels"]
    K --> N
    L --> N
    M --> N

    O["date_dim : analyse temporelle"] --> N

    N --> P["Décisions : ventes, assortiment,
    réapprovisionnement, fidélisation"]
```

## Interprétation

Le schéma présente quatre axes d'analyse :
- Performance commerciale
- Performance des produits
- Gestion des stocks
- Analyse des clients

Les sources identifiées alimenteront des indicateurs
permettant aux décideurs de suivre l'activité commerciale.

La dimension temporelle date_dim permettra d'analyser
l'évolution des indicateurs par période.

Les calculs définitifs des KPI dépendront de la validation
des règles métier et des relations entre les tables.

# UC-01 — Schéma des besoins métier

## Objectif

Identifier les besoins décisionnels de la plateforme Retail
Intelligence Platform et les relier aux sources de données
disponibles.

## Schéma fonctionnel

```mermaid
flowchart TD
    A["Retail Intelligence Platform"]

    A --> B["Analyser les performances commerciales"]
    A --> C["Analyser les produits"]
    A --> D["Surveiller les stocks"]
    A --> E["Analyser les clients"]

    B --> F["store_sales / web_sales"]
    C --> G["item"]
    D --> H["inventory"]
    E --> I["customer"]

    F --> J["CA, quantités vendues, panier moyen"]
    G --> K["Ventes par produit et catégorie"]
    H --> L["Niveaux de stock et disponibilité"]
    I --> M["Répartition des ventes par client"]

    J --> N["Tableaux de bord décisionnels"]
    K --> N
    L --> N
    M --> N

    O["date_dim : analyse temporelle"] --> N

    N --> P["Décisions : ventes, assortiment,
    réapprovisionnement, fidélisation"]
```

## Interprétation

Le schéma présente quatre axes d'analyse :
- Performance commerciale
- Performance des produits
- Gestion des stocks
- Analyse des clients

Les sources identifiées alimenteront des indicateurs
permettant aux décideurs de suivre l'activité commerciale.

La dimension temporelle date_dim permettra d'analyser
l'évolution des indicateurs par période.

Les calculs définitifs des KPI dépendront de la validation
des règles métier et des relations entre les tables.
