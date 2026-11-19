# UC06 — Rapport de contrôles qualité

## 1. Objectif

Évaluer la qualité des données utilisées dans le projet
Retail Intelligence Platform avant leur exploitation
analytique.

Les contrôles portent sur les tables Silver :
- store_sales
- item

Les vérifications sont réalisées avec PySpark 4.3.0.

## 2. Contrôle des volumes

| Jeu de données | Nombre de lignes |
|---|---:|
| store_sales Silver | 667 579 |
| item Silver | 17 820 |
| Gold — CA par catégorie | 9 |

Le total des lignes de vente représentées dans
l'agrégation Gold est de 667 579.

## 3. Complétude

### Table item

| Colonne | Valeurs NULL |
|---|---:|
| i_item_sk | 0 |
| i_category | 0 |
| i_current_price | 0 |

Conclusion :
Aucune valeur manquante détectée dans les trois
colonnes essentielles contrôlées.

### Table store_sales

| Colonne | Valeurs NULL |
|---|---:|
| ss_item_sk | 0 |
| ss_quantity | 0 |
| ss_net_paid | 0 |
| ss_ticket_number | 0 |

Conclusion :
Aucune valeur manquante détectée dans les quatre
colonnes essentielles contrôlées.

## 4. Unicité

### Table item

Contrôle :
GROUP BY i_item_sk, puis recherche des identifiants
présents plusieurs fois.

Résultat :
0 identifiant dupliqué.

Conclusion :
La clé i_item_sk est unique dans la table Silver item.

### Table store_sales

Aucun contrôle exhaustif des doublons métier
n'a encore été réalisé.

Une ligne de vente ne peut pas être considérée
comme un doublon uniquement parce qu'elle partage
un numéro de ticket avec une autre ligne.

## 5. Validité des données

### Table item

| Contrôle | Résultat |
|---|---:|
| Prix courants négatifs | 0 |
| Dates de fin antérieures au début | 0 |
| Dates de début manquantes | 0 |

### Table store_sales

| Contrôle | Résultat |
|---|---:|
| Quantités inférieures ou égales à 0 | 0 |
| Montants nets négatifs | 0 |
| Prix de vente négatifs | 0 |
| Montants nets égaux à 0 | 3 954 |

## 6. Analyse des montants nuls

3 954 lignes présentent un montant net payé nul,
soit environ 0,59 % des 667 579 lignes de vente.

L'exploration d'un échantillon a montré :

Cas 1 :
- Prix de vente : 0
- Montant brut : 0
- Montant net payé : 0

Cas 2 :
- Prix de vente positif
- Coupon égal au montant brut
- Montant net payé : 0

Décision :
Conserver ces lignes dans Silver.

Justification :
Un montant net payé égal à zéro ne constitue pas,
à lui seul, une preuve d'erreur.

Ces lignes contribuent aux quantités vendues,
mais pas au chiffre d'affaires net.

## 7. Cohérence et intégrité référentielle

Jointure métier :

store_sales.ss_item_sk = item.i_item_sk

Une jointure LEFT est utilisée pour conserver
toutes les lignes de vente.

Les identifiants item sont uniques.

Le contrôle des ventes sans article correspondant
a été prévu avec une jointure LEFT ANTI.

Son résultat numérique doit être confirmé
avant de conclure à une intégrité complète.

## 8. Contrôle de l'agrégation Gold

Question métier :
Quelles catégories génèrent le plus de
chiffre d'affaires net ?

Résultats :
- 9 catégories produites.
- 667 579 lignes de vente représentées.
- Aucune multiplication du nombre de lignes
  constatée dans le total agrégé.

Principales catégories :

| Catégorie | Chiffre d'affaires net |
|---|---:|
| Music | 519 666 693,84 |
| Books | 307 151 503,25 |
| Movies & TV | 74 735 891,89 |
| Clothing & Accessories | 56 754 855,82 |
| Electronics | 55 715 087,49 |

Les montants sont exprimés dans l'unité monétaire
du jeu de données source.

## 9. Vérification des formats

La table Gold a été enregistrée dans trois formats :

| Format | Nombre de lignes |
|---|---:|
| CSV | 9 |
| JSON | 9 |
| Parquet | 9 |

La relecture a confirmé les mêmes volumes.

Les tailles mesurées dans HDFS sont :
- CSV : 434 octets
- JSON : environ 1,1 Ko
- Parquet : environ 1,7 Ko

## 10. Bilan

Les contrôles réalisés montrent :

- L'absence de valeurs NULL dans les colonnes
  essentielles vérifiées.
- L'unicité des identifiants du référentiel item.
- L'absence de prix négatifs dans les champs testés.
- L'absence de quantités invalides dans Silver.
- La présence de 3 954 ventes à montant net nul,
  conservées après analyse.
- La conservation des 667 579 lignes de vente
  dans l'agrégation Gold.
- La réussite des écritures et relectures Parquet.

Limites :
- Les contrôles de complétude ne couvrent pas
  toutes les colonnes.
- Les doublons métier des ventes restent à analyser.
- Le résultat chiffré du contrôle d'intégrité
  référentielle reste à confirmer.
