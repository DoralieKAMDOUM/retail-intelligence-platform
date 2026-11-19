# UC08 — Synthèse des analyses métier

## 1. Jeux de données utilisés

- Silver store_sales : 667 579 lignes de vente.
- Silver item : 17 820 articles.
- Gold ca_par_categorie : 9 catégories.

Les données proviennent du jeu TPC-DS et ont été
nettoyées et structurées lors de l'UC06.

## 2. KPI calculés

| KPI | Formule | Résultat |
|---|---|---:|
| Chiffre d'affaires net | SUM(ss_net_paid) | 1 150 529 586,37 |
| Quantité vendue | SUM(ss_quantity) | 33 755 474 |
| Nombre de lignes de vente | COUNT(*) | 667 579 |

Les résultats Silver et Gold sont identiques pour les
trois indicateurs.

## 3. Analyse métier 1 — Performance des catégories

Question : quelles catégories génèrent le plus de
chiffre d'affaires net ?

Résultats :
- Music : 45,17 % du CA net.
- Books : 26,70 % du CA net.
- Movies & TV : 6,50 % du CA net.

Constat :
Music et Books représentent ensemble 71,87 % du
chiffre d'affaires net.

Interprétation :
Le chiffre d'affaires est fortement concentré sur
deux catégories.

Limite :
Cette analyse ne mesure ni les marges ni la rentabilité.
Les données TPC-DS sont synthétiques.

Recommandation :
Approfondir l'analyse des catégories dominantes et
comparer leur chiffre d'affaires à leurs marges.

## 4. Analyse métier 2 — Distribution des ventes

Question : comment les montants des lignes de vente
sont-ils répartis ?

Résultats :
- Montant minimum : 0,00.
- Montant maximum : 18 745,00.
- Montant moyen : 1 723,44.
- Médiane approximative : 878,27.
- Quantité moyenne par ligne : 50,56.

Constat :
Le montant moyen est supérieur à la médiane.

Interprétation :
La distribution semble asymétrique, avec des lignes
de vente élevées qui influencent la moyenne.

Limite :
La médiane est approximative. Une analyse des
percentiles et des valeurs extrêmes permettrait
de confirmer cette interprétation.

Recommandation :
Étudier les percentiles et la distribution des
montants avant de définir des seuils métier.

## 5. Visualisations

- visualisation_1.png : CA net par catégorie.
- visualisation_2.png : quantités vendues par catégorie.

Les deux graphiques permettent de comparer la
contribution des catégories en valeur et en volume.

## 6. Limites générales

- Les données sont synthétiques.
- La devise des montants reste à confirmer.
- Le nombre de lignes de vente ne correspond pas
  nécessairement au nombre de transactions distinctes.
- Les résultats décrivent uniquement les données
  disponibles dans le périmètre analysé.
