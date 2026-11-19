# UC08 — Dictionnaire des KPI

Les définitions ci-dessous sont celles utilisées dans UC08.
Elles devront être comparées au dictionnaire UC01.

## KPI 1 — Chiffre d'affaires net

- Définition : somme des montants nets des lignes de vente.
- Formule : SUM(ss_net_paid)
- Source : Silver store_sales
- Champ : ss_net_paid
- Filtre : lignes conservées après nettoyage UC06
- Granularité : globale ou par catégorie
- Unité : unité monétaire du jeu de données
- Résultat global : 1 150 529 586,37

## KPI 2 — Quantité vendue

- Définition : nombre total d'unités vendues.
- Formule : SUM(ss_quantity)
- Source : Silver store_sales
- Champ : ss_quantity
- Filtre : ss_quantity > 0, appliqué dans UC06
- Granularité : globale ou par catégorie
- Unité : unités vendues
- Résultat global : 33 755 474

## KPI 3 — Nombre de lignes de vente

- Définition : nombre d'enregistrements de vente.
- Formule : COUNT(*)
- Source : Silver store_sales
- Filtre : lignes conservées après nettoyage UC06
- Granularité : globale ou par catégorie
- Unité : lignes de vente
- Résultat global : 667 579

Attention : ce KPI ne représente pas le nombre de
transactions distinctes.
