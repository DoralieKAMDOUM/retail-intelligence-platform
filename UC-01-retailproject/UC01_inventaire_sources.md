Organisation des données

L'archive retail_project.zip contient deux répertoires principaux :

- data/ : ensemble principal des données du projet.

- data_refresh/ : ensemble complémentaire contenant une sélection de fichiers également présents dans data/.

L'inventaire de l'archive fait apparaître 36 fichiers, dont 24 dans data/ et 12 dans data_refresh/.

3. Inventaire des sources - STATUT  (ils sont tous verifiés)
Main dataset — data/
24 files — sizes from the ZIP archive, rounded to two decimal MB (decimal)
File path	Format	Size (MB)
customer/customer.dat	DAT	13.28
customer_address/customer_address.dat	DAT	5.39
customer_demographics/customer_demographics.dat	DAT	77.75
date_dim/date_dim.dat	DAT	15.40
household_demographics/household_demographics.dat	DAT	0.16
income_band/income_band.dat	DAT	0.0003
inventory/inventory.dat	DAT	424.94
item/item.dat	DAT	6.80
item_marketprices/item_marketprices.dat	DAT	4.20
item_marketprices/item_marketprices_audit.csv	CSV	0.0003
product_reviews/product_reviews.dat	DAT	56.36
promotion/promotion.dat	DAT	0.05
reason/reason.dat	DAT	0.0031
ship_mode/ship_mode.dat	DAT	0.0012
store/store.dat	DAT	0.0034
store_returns/store_returns.dat	DAT	4.34
store_sales/store_sales.dat	DAT	92.76
time_dim/time_dim.dat	DAT	5.11
warehouse/warehouse.dat	DAT	0.0006
web_clickstreams/web_clickstreams.dat	DAT	178.72
web_page/web_page.dat	DAT	0.0080
web_returns/web_returns.dat	DAT	5.38
web_sales/web_sales.dat	DAT	133.79
web_site/web_site.dat	DAT	0.0088

2. Refresh dataset — data_refresh/
12 files — exact names from the ZIP archive
File path	Format	Size (MB)
customer/customer.dat	DAT	0.13
customer_address/customer_address.dat	DAT	0.05
inventory/inventory.dat	DAT	4.29
item/item.dat	DAT	0.07
item_marketprices/item_marketprices.dat	DAT	0.04
item_marketprices/item_marketprices_audit.csv	CSV	0.15
product_reviews/product_reviews.dat	DAT	0.57
store_returns/store_returns.dat	DAT	0.05
store_sales/store_sales.dat	DAT	0.92
web_clickstreams/web_clickstreams.dat	DAT	1.82
web_returns/web_returns.dat	DAT	0.06
web_sales/web_sales.dat	DAT	1.38
 
 

6. Identification des clés et des relations potentielles

La documentation des tables principales fournit plusieurs identifiants candidats :

Table

Clé ou identifiant candidat

date_dim

d_date_sk

time_dim

t_time_sk

customer

c_customer_sk

item

i_item_sk

store

s_store_sk

warehouse

w_warehouse_sk

promotion

p_promo_sk

web_sales

ws_sk, ws_order_number

store_sales

Ticket et produit, combinaison à contrôler

inventory

Date, produit et entrepôt

### C.2 Valeurs nulles (comptées avec pandas)

| Table | Colonnes concernées (nombre de valeurs nulles) |
|---|---|
| `store_sales` | cdemo 238 ; hdemo 295 ; addr 448 ; promo 158 |
| `web_sales` | web_page 164 ; web_site 154 ; ship_mode 170 ; warehouse 158 ; promo 121 ; plus des nulls sur démographies et adresses (270 à 495 chacune) |
| `store_returns` | cdemo 21 ; hdemo 15 ; addr 42 ; reason 11 |
| `web_returns` | web_page 10 ; reason 7 ; démographies/adresses 19 à 63 |
| `inventory` | `inv_quantity_on_hand` : 5 999 |
| `web_clickstreams` | `wcs_sales_sk` : 6 102 498 (90,13 %) ; `wcs_user_sk` : 2 853 461 (42,15 %) ; `wcs_web_page_sk` : 164 |
| `customer` | 14 à 30 nuls par colonne (ex. email 23, naissance 18 à 30) |
| `item` | `i_item_desc` 4 ; `i_brand_id` 8 ; `i_brand` 6 ; `i_rec_end_date` 17 820 (toujours vide : normal pour des articles actifs, **Déduit**) |
| `item_marketprices` | prix 29 ; date de fin 30 |
| `time_dim` | `t_meal_time` 50 400 (vide hors repas : **Déduit**) |

### C.3 Anomalies visibles

1. **Marge négative** : 495 971 lignes de `store_sales` sur 667 579 (**74,3 %**) ont un `net_profit` négatif. La marge n'est donc pas exploitable telle quelle.
2. **Doublons (ticket, item)** : 4 136 en magasin, 4 076 en web. Une même référence peut apparaître sur plusieurs lignes d'un même ticket : à traiter par agrégation, pas par suppression.
3. **Retours postérieurs aux ventes** : ventes de 2001-01-01 à 2005-12-13 ; retours magasin jusqu'au 2007-11-14 et retours web jusqu'au 2008-03-18.
4. **Inventaire avec articles inconnus** : 232 380 lignes d'inventaire (180 articles, `item_sk` 17 820 à 17 999) n'existent pas dans `data/item/item.dat`. Ces 180 articles sont dans `data_refresh/item/item.dat`.
5. **Avis** : dates jusqu'au 2006-01-01, 5 contenus vides.
6. **Fichier d'audit CSV** : commence par une ligne vide, ce qui peut casser un chargement automatique.
7. **Données synthétiques évidentes** : 12 magasins avec un CA très proche (≈ 96,5 à 99,0 M chacun), pays de naissance aléatoires, adresses toutes aux États-Unis.

### C.4 Domaines absents ou incomplets

- Pas de table de **catalogue** (catalog_sales, etc.) : Non disponible.
- Pas de documentation, de README ni de dictionnaire de données dans l'archive : Non disponible.
- Aucun **fichier complémentaire** au sens du TP §3.6 (JSON applicatifs, météo, logistique) : Non disponible.
- Devise des montants : Non communiquée.
