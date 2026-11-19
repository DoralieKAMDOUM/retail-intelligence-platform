# UC06 — Comparaison des formats CSV, JSON et Parquet

## 1. Objectif

Comparer trois formats de stockage utilisés dans
les traitements de données : CSV, JSON et Parquet.

La comparaison est réalisée sur le jeu de données Gold
contenant le chiffre d'affaires net par catégorie.

## 2. Jeu de données utilisé

Table : ca_par_categorie

Chemin HDFS :
/retail-lake/gold/ca_par_categorie

Nombre de lignes : 9

Colonnes :
- categorie
- chiffre_affaires_net
- quantite_vendue
- nombre_lignes_vente

## 3. Formats testés

Les données Gold ont été enregistrées avec PySpark
dans les trois formats suivants :

- CSV
- JSON
- Parquet

Répertoire HDFS :
/retail-lake/format_comparison/

## 4. Résultats des tests

| Format | Lignes relues | Taille HDFS |
|---|---:|---:|
| CSV | 9 | 434 octets |
| JSON | 9 | environ 1,1 Ko |
| Parquet | 9 | environ 1,7 Ko |

Les trois formats ont été écrits puis relus
avec succès dans Spark.

## 5. Comparaison technique

### CSV

Avantages :
- Format simple et lisible.
- Compatible avec de nombreux logiciels.
- Facile à exporter vers Excel.

Limites :
- Pas de conservation automatique des types.
- Pas de schéma intégré.
- Moins adapté aux analyses de gros volumes.

### JSON

Avantages :
- Format structuré et lisible.
- Adapté aux échanges de données et aux API.
- Peut représenter des structures imbriquées.

Limites :
- Répétition des noms de champs.
- Volume potentiellement important.
- Traitement analytique parfois plus coûteux.

### Parquet

Avantages :
- Format de stockage en colonnes.
- Conservation du schéma et des types.
- Compression et lecture sélective des colonnes.
- Adapté aux traitements analytiques avec Spark.

Limites :
- Peu lisible directement par un humain.
- Métadonnées supplémentaires.
- Peut être plus volumineux sur de très petits fichiers.

## 6. Interprétation

Sur notre jeu Gold de seulement 9 lignes,
CSV est le format le plus léger.

Parquet est plus volumineux en raison du coût
des métadonnées et de la structure du fichier.

Ce résultat ne signifie pas que CSV est
systématiquement plus performant.

Sur des volumes importants, Parquet est généralement
plus adapté aux traitements analytiques, notamment
grâce au stockage en colonnes et à la compression.

## 7. Choix retenu

Parquet est retenu pour les zones Silver et Gold
du projet Retail Intelligence Platform.

Justifications :
- Conservation des types de données.
- Intégration native avec Apache Spark.
- Adaptation aux traitements analytiques.
- Possibilité de relire uniquement certaines colonnes.

## 8. Limites de l'expérimentation

La comparaison porte uniquement sur les tailles
de stockage et la réussite des relectures.

Les temps d'écriture, les temps de lecture et
la consommation mémoire n'ont pas été mesurés.

Les résultats ne permettent donc pas de conclure
sur les performances relatives des trois formats.
