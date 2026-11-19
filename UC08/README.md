# UC08 — Analyse des données et visualisation

## Objectif

Analyser les données de ventes TPC-DS préparées dans
UC06, calculer des KPI métier et produire des
visualisations interprétables.

## Sources

- UC06/silver/store_sales/
- UC06/silver/item/
- UC06/gold/ca_par_categorie/

## KPI calculés

1. Chiffre d'affaires net
2. Quantité vendue
3. Nombre de lignes de vente

## Analyses métier

1. Performance des catégories de produits
2. Distribution des montants des lignes de vente

## Visualisations

- visualisations/visualisation_1.png :
  chiffre d'affaires net par catégorie
- visualisations/visualisation_2.png :
  quantités vendues par catégorie

## Exécution

Prérequis : Python, PySpark, Pandas, Matplotlib,
Jupyter et un environnement Java compatible avec Spark.

Depuis la racine du dépôt :

1. Activer l'environnement virtuel :

   source .venv/bin/activate

2. Ouvrir le notebook :

   UC08/notebooks/TP4_Retail_Intelligence.ipynb

3. Sélectionner le kernel Python - Retail TP4.

4. Exécuter les cellules dans l'ordre.

Le notebook utilise les fichiers Parquet locaux UC06.
Les chemins doivent être adaptés si le dépôt est installé
ailleurs que dans le répertoire personnel.

## Preuves

Les résultats exportés et la documentation se trouvent
dans preuves/uc08/.

## Limites

Les données sont synthétiques. La devise n'est pas
confirmée et le nombre de lignes de vente ne représente
pas nécessairement le nombre de transactions distinctes.
