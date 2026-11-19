# UC08 — Description des jeux de données

## Silver — store_sales

- Provenance : TPC-DS, données store_sales transformées dans UC06
- Format : Parquet
- Chemin : UC06/silver/store_sales/
- Volume : 667 579 lignes
- Granularité : ligne de vente
- Champs utilisés :
  - ss_item_sk : identifiant de l'article
  - ss_quantity : quantité vendue
  - ss_net_paid : montant net
  - ss_ticket_number : identifiant du ticket
- Qualité : contrôles des valeurs nulles, quantités
  positives et montants négatifs réalisés dans UC06

## Silver — item

- Provenance : TPC-DS, données item transformées dans UC06
- Format : Parquet
- Chemin : UC06/silver/item/
- Volume : 17 820 lignes
- Granularité : enregistrement d'article
- Champs utilisés :
  - i_item_sk : identifiant de l'article
  - i_category : catégorie
- Qualité : absence de doublons sur i_item_sk
  et contrôles des champs essentiels dans UC06

## Gold — ca_par_categorie

- Provenance : agrégation UC06 des ventes et articles
- Format : Parquet
- Chemin : UC06/gold/ca_par_categorie/
- Volume : 9 lignes
- Granularité : catégorie de produits
- Champs :
  - categorie
  - chiffre_affaires_net
  - quantite_vendue
  - nombre_lignes_vente

## Justification du choix

Les données Silver permettent de calculer les KPI
globaux et les statistiques descriptives sur les ventes.

Les données Gold permettent de comparer les performances
des catégories sans recalculer les agrégations.

Les deux niveaux permettent également de vérifier
la cohérence des résultats.

## Limites

- Les données TPC-DS sont synthétiques.
- La devise des montants reste à confirmer.
- Le périmètre étudié couvre les ventes en magasin
  disponibles dans les fichiers sélectionnés.
