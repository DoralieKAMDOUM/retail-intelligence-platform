# UC06 — Règles de nettoyage des données

## 1. Objectif

Transformer les données brutes de la zone Raw en données
structurées, typées et exploitables dans la zone Silver.

Deux sources ont été traitées :
- store_sales : données de ventes en magasin.
- item : référentiel des articles.

Les transformations sont réalisées avec PySpark 4.3.0.

## 2. Lecture et structuration

Les fichiers sources sont au format DAT, avec le caractère
pipe (|) comme séparateur.

Les données sont chargées depuis HDFS avec spark.read.text().

La fonction split() permet de séparer les champs et de leur
attribuer les noms de colonnes correspondant aux schémas.

## 3. Gestion des valeurs manquantes

Règle appliquée aux deux sources :

- Supprimer les espaces superflus avec trim().
- Transformer les chaînes vides en valeurs NULL.
- Conserver les valeurs NULL lorsque leur absence est autorisée.

Pour store_sales :
- Exclure les lignes sans ss_item_sk.
- Exclure les lignes sans ss_quantity.
- Exclure les lignes dont ss_quantity <= 0.

Pour item :
- Exclure les lignes sans i_item_sk.

Les contrôles effectués après transformation montrent
l'absence de valeurs NULL dans les champs essentiels
vérifiés.

## 4. Conversion des types

### store_sales

- Identifiants et quantités : integer.
- Numéro de ticket : bigint.
- Montants et prix : decimal(18,2).

La fonction try_cast() est utilisée afin de convertir
les valeurs sans provoquer d'échec sur les valeurs
non convertibles.

### item

- Identifiants numériques : integer.
- Prix et coûts : decimal(18,2).
- Dates de validité : date.
- Catégories et marques : string.

Les dates sont converties avec to_date() au format
yyyy-MM-dd.

## 5. Contrôles de validité

### item

Résultats observés sur 17 820 lignes Silver :

| Contrôle | Résultat |
|---|---:|
| i_item_sk NULL | 0 |
| i_category NULL | 0 |
| i_current_price NULL | 0 |
| Identifiants i_item_sk dupliqués | 0 |
| Prix négatifs | 0 |
| Dates de fin antérieures au début | 0 |
| Dates de début manquantes | 0 |

### store_sales

Résultats observés sur 667 579 lignes Silver :

| Contrôle | Résultat |
|---|---:|
| ss_item_sk NULL | 0 |
| ss_quantity NULL | 0 |
| ss_net_paid NULL | 0 |
| ss_ticket_number NULL | 0 |
| Quantités <= 0 | 0 |
| Montants nets négatifs | 0 |
| Prix de vente négatifs | 0 |
| Montants nets égaux à zéro | 3 954 |

## 6. Traitement des montants nuls

3 954 lignes présentent ss_net_paid = 0,
soit environ 0,59 % des ventes.

L'exploration a montré deux situations :
- Des lignes avec un prix de vente égal à zéro.
- Des lignes dont le montant est intégralement
  compensé par un coupon.

Décision :
Conserver ces enregistrements dans Silver.

Justification :
Un montant net nul ne prouve pas à lui seul
que la vente est erronée.

Ces lignes participent aux quantités vendues,
mais leur contribution au chiffre d'affaires net est nulle.

## 7. Gestion des doublons

L'unicité de i_item_sk a été contrôlée.

Résultat : 0 identifiant dupliqué.

Aucune suppression de doublons n'a été appliquée
sur le référentiel item.

Les doublons éventuels de store_sales doivent
être analysés selon la granularité métier
avant toute suppression.

## 8. Enrichissement et jointure

Jointure réalisée :

store_sales.ss_item_sk = item.i_item_sk

Type : LEFT JOIN.

Objectif :
Enrichir les ventes avec les catégories de produits.

Les catégories absentes sont remplacées par
"Non renseignée" lors de l'agrégation Gold.

Le contrôle d'intégrité référentielle doit être
conservé comme preuve distincte.

## 9. Agrégation métier

Question :
Quelles catégories génèrent le plus de
chiffre d'affaires net ?

Indicateurs calculés :

- chiffre_affaires_net = SUM(ss_net_paid)
- quantite_vendue = SUM(ss_quantity)
- nombre_lignes_vente = COUNT(*)

La table Gold contient 9 catégories.

Le total des lignes agrégées est de 667 579.

## 10. Stockage des résultats

Les données nettoyées sont enregistrées en Parquet :

/retail-lake/silver/store_sales
/retail-lake/silver/item

La table analytique est enregistrée dans :

/retail-lake/gold/ca_par_categorie

Les résultats ont été relus avec Spark pour
vérifier leur disponibilité et leur contenu.
