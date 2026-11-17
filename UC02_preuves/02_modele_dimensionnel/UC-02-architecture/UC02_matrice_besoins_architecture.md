
# UC-02 — Matrice de traçabilité des besoins métier

## Objectif

Démontrer comment les composants de l'architecture Data
répondent aux besoins décisionnels identifiés dans l'UC-01.

| Besoin métier | Sources | Traitement prévu | Restitution |
|---|---|---|---|
| Suivre le chiffre d'affaires | store_sales, web_sales | Agrégation des ventes par période | Tableau de bord commercial |
| Comparer les canaux magasin et web | store_sales, web_sales | Harmonisation des mesures et ajout du canal | Comparaison des canaux |
| Identifier les produits performants | item, store_sales, web_sales | Jointures et agrégations par produit | Classement des produits |
| Suivre les stocks | inventory, item, date_dim | Analyse des quantités par produit et date | Tableau de bord stocks |
| Analyser les clients | customer, tables de ventes | Jointures et regroupements par client | Analyse clientèle |
| Étudier l'évolution des ventes | date_dim, tables de ventes | Agrégations temporelles | Évolution mensuelle et annuelle |

## Correspondance avec l'architecture

1. Les fichiers .dat constituent les sources de données.
2. Python assure l'ingestion et les contrôles techniques.
3. La zone de staging conserve les données avant transformation.
4. PostgreSQL structure les faits et les dimensions.
5. Les Data Marts préparent les indicateurs décisionnels.
6. Power BI restitue les résultats aux utilisateurs métier.

## Points de vigilance

Les règles de calcul du chiffre d'affaires, la définition
d'une transaction et les clés de jointure devront être
validées avant la mise en production des indicateurs.

Les données de rafraîchissement devront être intégrées
sans créer de doublons ni écraser incorrectement les données.

## Compétence démontrée

C01 — Relier les choix d'architecture aux besoins métier.
