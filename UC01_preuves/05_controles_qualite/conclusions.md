### Synthèse des contrôles de qualité

Les contrôles exploratoires réalisés sur 11 fichiers ont permis d'évaluer la structure et plusieurs caractéristiques de qualité des données.

L'analyse n'a révélé aucune ligne présentant un nombre de champs différent de celui attendu. Ce résultat constitue un premier indicateur favorable à l'intégration des données dans la future plateforme analytique.

Des valeurs manquantes ont néanmoins été identifiées dans plusieurs tables. La table `item` présente notamment au moins un champ vide dans chacun de ses enregistrements, ce qui nécessite une vérification des colonnes concernées.

Par ailleurs, 912 227 occurrences de valeurs numériques négatives ont été détectées, exclusivement dans les tables `store_sales` et `web_sales`, y compris leurs fichiers de rafraîchissement. Ces valeurs ne doivent pas être considérées automatiquement comme des anomalies : leur interprétation dépend de la colonne concernée et des règles métier.

Enfin, aucun doublon exact n'a été identifié dans les échantillons contrôlés, limités aux 10 000 premières lignes de chaque fichier.

Ces résultats permettent de repérer les principaux points de vigilance avant l'intégration des données. Des contrôles complémentaires seront nécessaires sur les clés métier, les relations entre tables et la cohérence des montants financiers.

**Preuves conservées :** `UC01_preuves/05_controles_qualite/controles_qualite.csv` et capture des résultats.