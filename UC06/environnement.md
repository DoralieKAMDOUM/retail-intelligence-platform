# UC06 — Fiche d'environnement technique

## 1. Présentation

Le projet Retail Intelligence Platform est développé dans
Ubuntu 24.04 sous WSL2.

Les traitements sont réalisés avec Apache Spark et PySpark,
à partir de notebooks Jupyter exécutés dans VS Code.

## 2. Versions utilisées

| Technologie | Version |
|---|---|
| Ubuntu | 24.04 |
| Python | 3.12.3 |
| PySpark | 4.3.0 |
| Apache Spark | 4.3.0 |

## 3. Mode d'exécution

- Mode Spark : local[1]
- Stockage : Hadoop HDFS
- Langage : Python
- Interface : Jupyter Notebook dans VS Code

Le mode local[1] limite Spark à un thread de calcul,
afin de réduire la consommation de ressources.

## 4. Organisation du stockage

### Répertoire du projet

~/retail-intelligence-platform/

### Notebook principal

UC06/TP3_Retail_Intelligence.ipynb

### Sources HDFS

/retail-lake/raw/tpcxbb/initial/

### Zone Silver

/retail-lake/silver/

### Zone Gold

/retail-lake/gold/

## 5. Architecture des données

RAW : conservation des données sources.

SILVER : nettoyage, typage et harmonisation des données.

GOLD : jointures et agrégations pour répondre aux
questions métier.

## 6. Vérification de l'environnement

Les versions ont été vérifiées directement dans le
notebook avec les commandes suivantes :

import sys
import pyspark

print(sys.version.split()[0])
print(pyspark.__version__)
print(spark.version)
print(spark.sparkContext.master)

Résultats obtenus :

Python : 3.12.3
PySpark : 4.3.0
Spark : 4.3.0
Mode : local[1]
