# UC06 — Retail Intelligence Platform

## Présentation

Ce projet met en œuvre un pipeline de traitement
de données avec Python, PySpark et Hadoop HDFS.

Il s'inscrit dans le Jour 3 du projet Retail
Intelligence Platform.

L'objectif est de transformer des données de ventes
et de produits en indicateurs analytiques.

## Environnement

- Ubuntu 24.04 sous WSL2
- Python 3.12.3
- PySpark 4.3.0
- Apache Spark 4.3.0
- Mode local[1]
- Hadoop HDFS
- VS Code et Jupyter Notebook

## Architecture

RAW -> SILVER -> GOLD

### RAW

Sources brutes :
- store_sales : 667 579 lignes
- item : 17 820 lignes
- customer : 99 000 lignes, non transformées

### SILVER

Deux tables nettoyées et typées :
- store_sales
- item

Les données Silver sont enregistrées en Parquet.

### GOLD

Table :
ca_par_categorie

Indicateurs :
- Chiffre d'affaires net
- Quantités vendues
- Nombre de lignes de vente

Résultats :
- 9 catégories
- 667 579 lignes de vente représentées

## Question métier

Quelles catégories de produits génèrent
le plus de chiffre d'affaires net ?

Principaux résultats :

1. Music : 519 666 693,84
2. Books : 307 151 503,25
3. Movies & TV : 74 735 891,89

## Traitements

1. Lecture des fichiers DAT depuis HDFS.
2. Découpage des champs avec le séparateur pipe.
3. Nettoyage des chaînes vides.
4. Conversion des types.
5. Contrôles qualité.
6. Enregistrement des tables Silver.
7. Jointure entre ventes et articles.
8. Agrégation par catégorie.
9. Enregistrement de Gold en Parquet.
10. Comparaison CSV, JSON et Parquet.

## Contrôles qualité

Les contrôles portent sur :
- Complétude
- Unicité des articles
- Validité des prix et quantités
- Cohérence des dates
- Montants nets nuls
- Conservation des volumes
- Intégrité référentielle, à confirmer séparément

Résultat notable :
3 954 ventes présentent un montant net nul.
Elles ont été conservées après exploration.

## Livrables

- environnement.md
- inventaire_sources.md
- regles_nettoyage.md
- rapport_qualite.md
- comparaison_formats.md
- TP3_Retail_Intelligence.ipynb
- preuves/

## Reproduction

Prérequis :
- Python 3.12
- PySpark 4.3.0
- Hadoop HDFS opérationnel
- Jupyter Notebook

1. Démarrer HDFS.
2. Vérifier la présence des sources Raw dans HDFS.
3. Ouvrir TP3_Retail_Intelligence.ipynb.
4. Initialiser Spark en mode local[1].
5. Exécuter les cellules dans leur ordre logique.
6. Vérifier les tables Silver et Gold.
7. Consulter les rapports de qualité.

Les chemins HDFS doivent être adaptés
si la configuration de Hadoop est différente.

## Organisation HDFS

/retail-lake/raw/
/retail-lake/silver/
/retail-lake/gold/
/retail-lake/format_comparison/

## Conclusion

Le projet démontre un pipeline de traitement
de données allant des sources brutes à la production
d'indicateurs métier.

Les résultats sont stockés au format Parquet
pour faciliter leur réutilisation analytique.
