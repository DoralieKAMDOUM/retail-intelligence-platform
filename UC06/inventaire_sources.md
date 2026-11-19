# UC06 — Inventaire technique des sources

## 1. Contexte

Dans le cadre du projet Retail Intelligence Platform,
les données sources sont stockées dans Hadoop HDFS.

Les fichiers proviennent d'un jeu de données de type
TPC-DS et sont organisés dans une architecture
Raw / Silver / Gold.

## 2. Sources identifiées

| Source | Format initial | Lignes | Colonnes | Taille approximative |
|---|---|---:|---:|---:|
| store_sales | DAT délimité par \| | 667 579 | 23 | 92,8 Mo |
| item | DAT délimité par \| | 17 820 | 22 | 6,8 Mo |
| customer | DAT délimité par \| | 99 000 | 18 | 13,3 Mo |

Les sources effectivement transformées en Silver
pour ce TP sont store_sales et item.

La source customer est disponible dans HDFS,
mais n'est pas utilisée dans l'agrégation Gold actuelle.

## 3. Source store_sales

### Chemin HDFS

/retail-lake/raw/tpcxbb/initial/store_sales/store_sales.dat

### Granularité

Une ligne correspond à un article vendu
dans une transaction en magasin.

### Colonnes principales

| Colonne | Description | Type Silver |
|---|---|---|
| ss_item_sk | Identifiant de l'article | integer |
| ss_customer_sk | Identifiant du client | integer |
| ss_ticket_number | Numéro de ticket | bigint |
| ss_quantity | Quantité vendue | integer |
| ss_sales_price | Prix de vente unitaire | decimal(18,2) |
| ss_ext_sales_price | Montant brut de la ligne | decimal(18,2) |
| ss_ext_discount_amt | Montant de remise | decimal(18,2) |
| ss_coupon_amt | Montant du coupon | decimal(18,2) |
| ss_net_paid | Montant net payé | decimal(18,2) |
| ss_net_profit | Profit net | decimal(18,2) |

Le schéma complet contient 23 colonnes.

## 4. Source item

### Chemin HDFS

/retail-lake/raw/tpcxbb/initial/item/item.dat

### Granularité

Une ligne correspond à un enregistrement
de référence d'article.

### Colonnes principales

| Colonne | Description | Type Silver |
|---|---|---|
| i_item_sk | Identifiant de l'article | integer |
| i_item_id | Identifiant métier | string |
| i_rec_start_date | Début de validité | date |
| i_rec_end_date | Fin de validité | date |
| i_current_price | Prix courant | decimal(18,2) |
| i_wholesale_cost | Coût de gros | decimal(18,2) |
| i_brand | Marque | string |
| i_class | Classe de produit | string |
| i_category | Catégorie | string |
| i_product_name | Nom du produit | string |

Le schéma complet contient 22 colonnes.

## 5. Source customer

### Chemin HDFS

/retail-lake/raw/tpcxbb/initial/customer/customer.dat

### Granularité

Une ligne correspond à un enregistrement client.

Cette source a été identifiée et chargée dans HDFS,
mais n'a pas été utilisée dans les transformations
Silver et Gold de ce TP.

## 6. Relations entre les sources

La jointure utilisée pour enrichir les ventes
avec les catégories de produits est :

store_sales.ss_item_sk = item.i_item_sk

Type de jointure : LEFT JOIN.

Cette jointure conserve les lignes de vente
même lorsqu'une catégorie n'est pas retrouvée.

## 7. Jeux de données produits

### Silver

/retail-lake/silver/store_sales
/retail-lake/silver/item

### Gold

/retail-lake/gold/ca_par_categorie

La table Gold contient neuf catégories et les
indicateurs suivants :

- chiffre_affaires_net
- quantite_vendue
- nombre_lignes_vente

## 8. Vérifications réalisées

- 667 579 lignes dans store_sales Silver.
- 17 820 lignes dans item Silver.
- 9 catégories dans Gold.
- 667 579 lignes de vente représentées dans Gold.
- Écriture et relecture des données au format Parquet.
