
**Question du TP :** identifier ≥ 5 limites, en examinant les 6 points listés.

| # | Limite ou incertitude | Preuve | Conséquence |
|---|---|---|---|
| L1 | Une table présente ne garantit pas des champs remplis | 90,13 % des clics sans `wcs_sales_sk`, 42,15 % sans utilisateur ; 74,3 % de marges négatives | Les analyses de conversion et de marge sont fragiles |
| L2 | Vente magasin ≠ vente web | 23 colonnes vs 34 ; web avec site, page, mode d'expédition, entrepôt, adresse de facturation et de livraison | Il faut un modèle commun explicite (canal) avant de comparer |
| L3 | Ligne / ticket / commande / transaction | 667 579 lignes magasin pour 89 100 tickets ; 4 136 doublons (ticket, item) | Toujours préciser l'unité de comptage de chaque KPI |
| L4 | Numérotation partagée entre canaux | Tickets magasin et commandes web couvrent la même plage 0–89 099 (89 100 valeurs communes) ; même nombre de tickets/commandes par année | Risque de fausse jointure ; clé = (canal, numéro) |
| L5 | Clics ≠ achats | 9,87 % des clics seulement portent un identifiant de vente | Un clic n'est pas un ajout au panier ; pas de notion de session ni d'action (pas de type d'événement) |
| L6 | Retours à distinguer des ventes | Retours jusqu'en 2007/2008, ventes jusqu'en 2005 | Calculer un taux de retour par date de vente d'origine, pas par date de retour |
| L7 | Corrélation ≠ causalité | Ex. une catégorie à fort CA a aussi plus de retours (Music en tête des deux) | Ne pas conclure à un problème qualité sans analyse du volume |
| L8 | Données synthétiques | CA quasi identique entre magasins ; panier moyen > 12 000 | Aucun enseignement commercial réel |
| L9 | Données de référence incomplètes | 180 articles d'inventaire absents de `item.dat` | Intégrer `data_refresh` ou exclure ces lignes (**À valider**) |
| L10 | Période 2005 partielle | Dernière vente le 2005-12-13 | Pas de comparaison annuelle avec 2005 |
| L11 | Documentation absente | Pas de README ni dictionnaire ; colonnes sans en-tête | Les noms de colonnes sont **Déduits** |
