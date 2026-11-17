Étape B– Définir les indicateurs Définissez au minimum cinq indicateurs adaptés au scénario.
Les indicateurs doivent couvrir, lorsque les données le permettent :
1. — nom du kpi ; chiffre d’affaires
2. sa définition métier; Le chiffre d'affaires représente le montant des ventes réalisées sur une période donnée.
3. sa formule; Somme des montants de ventes retenus sur la période
4. son unité; 
5. son périmètre; ensemble des ventes magasin et web, avec possibilité d'analyse par canal, magasin, produit et période.
6. sa fréquence de calcul;
7. les sources nécessaires;
- store_sales.dat
- web_sales.dat
- date_dim.dat
- store.dat,
- item.dat pour les analyses détaillées.
8. les éventuelles données manquantes;
9. les limites d’interprétation. Le chiffre d'affaires ne représente pas le bénéfice réalisé par l'entreprise. Une augmentation des ventes ne signifie pas nécessairement une amélioration de la rentabilité. le résultat dépendra de la définition retenue pour les remises, les taxes et les retours.

 

1. nom kpi — Nombre de transactions
2. Définition métier: il  vise à mesurer le nombre d'opérations d'achat réalisées sur une période.
Il permet egalement de suivre l'activité commerciale indépendamment des montants générés et d'observer si une variation du chiffre d'affaires s'accompagne d'une variation du nombre d'achats.

3. Formule : Nombre de transactions = Nombre d'identifiants de transaction distincts sur la période

4. Unité : nombre de transactions.

5. Périmètre : ventes magasin et web, par canal et par période.

6. Fréquence de calcul : quotidienne, avec consolidation mensuelle.

7. Sources nécessaires :

- `store_sales.dat`
- `web_sales.dat`
- `date_dim.dat`

8. Données manquantes ou à vérifier :

Il faut vérifier si les fichiers contiennent un identifiant permettant de distinguer une transaction complète d'une simple ligne de vente.

Les identifiants peuvent être différents entre le magasin et le web. Il faudra donc examiner leur structure avant de calculer un total global.

9. Limites d'interprétation :

Une transaction peut contenir plusieurs produits. Compter directement les lignes des fichiers risquerait donc de surestimer le nombre réel d'achats.

Si aucun identifiant fiable n'est disponible, l'indicateur devra être adapté ou déclaré non calculable.

1. NOM KPI — Panier moyen

2. Définition métier

Le panier moyen correspond au montant moyen dépensé lors d'une transaction.

Il permet de comprendre la valeur des achats et de comparer les comportements d'achat entre les canaux de vente.

4. Formule

Panier moyen = Chiffre d'affaires / Nombre de transactions

5. Unité : unité monétaire par transaction.

6. Périmètre : ventes magasin et web, avec comparaison par canal et par période.

7. Fréquence de calcul : quotidienne et mensuelle.

8. Sources nécessaires :

- `store_sales.dat`
- `web_sales.dat`
- `date_dim.dat`

9. Données manquantes ou à vérifier :

Le calcul nécessite un chiffre d'affaires correctement défini et un nombre de transactions fiable.

Il faudra notamment confirmer que plusieurs lignes appartenant à une même transaction ne sont pas comptées plusieurs fois.

10. Limites d'interprétation 

Le panier moyen peut augmenter sans que le nombre de clients ou de transactions augmente. Cette évolution peut être liée à des prix plus élevés ou à des achats plus importants.

Il ne permet donc pas, à lui seul, de conclure à une amélioration de la fidélité des clients.


1. Nom kpi — Quantités vendues

2. Définition métier**

Cet indicateur mesure le volume de produits vendus sur une période.

Contrairement au chiffre d'affaires, il permet d'étudier l'activité en unités physiques. Il est particulièrement utile pour identifier les produits les plus demandés et rapprocher les ventes des niveaux de stock.

**Formule**

Quantités vendues = Somme des quantités vendues sur la période

**Unité :** nombre d'unités vendues.

**Périmètre :** ventes magasin et web, avec analyse par produit, catégorie, canal et période.

**Fréquence de calcul :** quotidienne, hebdomadaire et mensuelle.

**Sources nécessaires :**

- `store_sales.dat`
- `web_sales.dat`
- `item.dat`
- `date_dim.dat`

**Données manquantes ou à vérifier :**

Il faudra identifier les colonnes de quantité et vérifier qu'elles représentent bien des unités vendues.

La relation entre les lignes de vente et les produits devra également être confirmée.

**Limites d'interprétation :**

Un produit vendu en grande quantité ne génère pas nécessairement un chiffre d'affaires élevé.

Par ailleurs, additionner des quantités de produits très différents donne une indication globale du volume, mais ne permet pas toujours une comparaison métier pertinente.

### KPI-05 — Taux d'évolution du chiffre d'affaires

**Définition métier**

Cet indicateur mesure la variation relative du chiffre d'affaires entre deux périodes comparables.

Il permet d'identifier les périodes de croissance ou de recul de l'activité et de suivre les tendances commerciales.

**Formule**

Taux d'évolution (%) = ((CA période actuelle - CA période précédente) / CA période précédente) × 100

**Unité :** pourcentage (%).

**Périmètre :** ensemble de l'entreprise, par canal, magasin ou catégorie de produits.

**Fréquence de calcul :** mensuelle, avec possibilité de comparaison annuelle.

**Sources nécessaires :**

- `store_sales.dat`
- `web_sales.dat`
- `date_dim.dat`

**Données manquantes ou à vérifier :**

Il faudra vérifier que les dates permettent de constituer des périodes comparables et que l'historique est suffisamment complet.

**Limites d'interprétation :**

Une hausse du chiffre d'affaires peut provenir d'une augmentation des prix plutôt que des quantités vendues.

Les variations saisonnières peuvent également influencer les résultats. Une comparaison entre deux mois consécutifs ne suffit donc pas toujours à expliquer une tendance.

Si le chiffre d'affaires de la période précédente est nul, le taux d'évolution ne peut pas être calculé avec cette formule.

### KPI-06 — Taux de retour des produits

**Définition métier**

Le taux de retour permet d'évaluer la proportion de produits retournés par rapport aux quantités vendues.

Cet indicateur peut contribuer à identifier des catégories de produits présentant des retours fréquents et à orienter des analyses complémentaires sur la qualité des produits ou les conditions de vente.

**Formule**

Taux de retour (%) = (Quantités retournées / Quantités vendues) × 100

**Unité :** pourcentage (%).

**Périmètre :** ventes magasin et web, avec analyse par produit, catégorie, canal et période.

**Fréquence de calcul :** mensuelle.

**Sources nécessaires :**

- `store_returns.dat`
- `web_returns.dat`
- `store_sales.dat`
- `web_sales.dat`
- `item.dat`
- `date_dim.dat`

**Données manquantes ou à vérifier :**

Il faudra identifier les champs de quantité retournée et déterminer si les retours peuvent être reliés aux ventes d'origine.

La définition de la période devra être précisée : date de vente ou date de retour.

**Limites d'interprétation :**

Un retour peut avoir lieu plusieurs jours ou semaines après la vente. Comparer directement les retours et les ventes d'un même mois peut donc produire un résultat difficile à interpréter.

Un taux de retour élevé ne prouve pas nécessairement un problème de qualité : les causes peuvent être multiples et ne sont pas forcément renseignées dans les données.

---

## 3. Tableau de synthèse

| KPI                    | Unité               | Fréquence principale | Utilisateurs concernés                                           |
| ---------------------- | ------------------- | -------------------- | ---------------------------------------------------------------- |
| Chiffre d'affaires     | Unité monétaire     | Quotidienne          | Direction générale, direction commerciale, contrôleur de gestion |
| Nombre de transactions | Transactions        | Quotidienne          | Direction commerciale, responsables de magasin                   |
| Panier moyen           | Montant/transaction | Mensuelle            | Direction commerciale, responsables de magasin                   |
| Quantités vendues      | Unités              | Quotidienne          | Direction commerciale, responsables des stocks                   |
| Taux d'évolution du CA | %                   | Mensuelle            | Direction générale, contrôleur de gestion                        |
| Taux de retour         | %                   | Mensuelle            | Direction commerciale, contrôleur de gestion                     |

## 4. Points de validation avant calcul

La définition des indicateurs constitue une première étape. Leur calcul ne devra commencer qu'après vérification de la structure des fichiers.

Les points prioritaires sont les suivants :

1. Identifier les champs correspondant aux montants, aux quantités et aux dates.
2. Déterminer la granularité des données de ventes : transaction, commande ou ligne de vente.
3. Vérifier les identifiants permettant de relier les ventes aux produits et aux magasins.
4. Examiner les différences de structure entre les ventes magasin et web.
5. Définir une règle cohérente de prise en compte des remises et des retours.
6. Contrôler la disponibilité et la continuité des données historiques.

Les indicateurs dont les informations nécessaires sont absentes ou insuffisantes seront signalés comme non calculables ou à confirmer.

 
