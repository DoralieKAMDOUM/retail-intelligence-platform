# UC07 — Organisation du Data Lake

## 1. Parcours retenu

Parcours B : Local / Open Source.

L'offre d'essai Azure n'étant plus disponible,
la plateforme est réalisée localement avec Hadoop HDFS
et Apache Spark.

La transposition Azure présentée ici est une proposition
d'architecture et non un déploiement effectif.

## 2. Organisation locale existante

Stockage HDFS :

/retail-lake/
    raw/
    bronze/
    silver/
        store_sales/
        item/
    gold/
        ca_par_categorie/
    quality/
    logs/
    format_comparison/

La présence de ces répertoires a été vérifiée
avec la commande hdfs dfs -ls.

Les traitements PySpark UC06 produisent les données
Silver et Gold au format Parquet.

## 3. Organisation ADLS Gen2 proposée

Compte de stockage :
stretailintelligence

Hierarchical Namespace : activé

Conteneur :
retail-lake

Organisation proposée :

retail-lake/
    bronze/
        tpcds/
            store_sales/
            item/
            customer/
    silver/
        store_sales/
        item/
    gold/
        ca_par_categorie/
    quality/
    logs/

Les noms sont illustratifs et devront respecter
les contraintes de nommage et de disponibilité Azure.

## 4. Rôle des zones

### Bronze

Fonction : conserver les données brutes reçues.

Données : fichiers sources TPC-DS.

Utilisateurs : processus d'ingestion et équipe Data.

Traçabilité : origine, date de chargement,
identifiant de traitement et nom du fichier source.

### Silver

Fonction : nettoyer, standardiser et contrôler
les données.

Données : tables store_sales et item au format Parquet.

Utilisateurs : Data Engineers et Data Analysts autorisés.

Traçabilité : version du traitement, contrôles qualité,
date de transformation et source Bronze.

### Gold

Fonction : fournir les données préparées pour
les analyses métier.

Données : agrégation ca_par_categorie au format Parquet.

Utilisateurs : analystes BI et consommateurs autorisés.

Traçabilité : règles de calcul des KPI, version du
traitement et date de publication.

## 5. Hierarchical Namespace (HNS)

Le HNS permet d'organiser ADLS Gen2 selon une
hiérarchie de répertoires et de fichiers.

Il facilite notamment :
- L'organisation des zones Bronze, Silver et Gold.
- Les opérations sur les répertoires.
- L'application d'ACL sur les chemins.
- La séparation des accès selon les responsabilités.

HNS ne remplace pas Azure RBAC ni Microsoft Entra ID.

## 6. Règles de nommage proposées

- Utiliser des noms explicites en minuscules.
- Éviter les espaces et caractères spéciaux.
- Identifier les datasets par leur nom métier.
- Conserver des conventions stables entre les zones.
- Prévoir des métadonnées de version et de chargement.

Exemples :

bronze/tpcds/store_sales/
silver/store_sales/
gold/ca_par_categorie/

## 7. Limites

Aucune ressource ADLS Gen2 n'a été déployée
dans le cadre de l'UC07.

Les chemins Azure sont une proposition de conception.

Les permissions, l'authentification et les opérations
cloud seront documentées et simulées conceptuellement.

## 8. Scénario Azure simulé

Ressources proposées :
- Un abonnement Azure actif.
- Un groupe de ressources rg-retail-intelligence.
- Un compte de stockage ADLS Gen2 avec HNS activé.
- Un conteneur retail-lake.
- Une instance Azure Data Factory.
- Un espace de travail Azure Synapse Analytics.

Pipeline envisagé :
1. Data Factory ingère les fichiers sources TPC-DS.
2. ADLS Gen2 conserve les fichiers dans Bronze.
3. Un Spark Pool Synapse transforme les données en Silver.
4. Spark calcule les agrégations Gold.
5. Synapse SQL permet d'interroger les données analytiques.
6. Les utilisateurs autorisés exploitent les résultats.

Contrôles envisagés :
- Vérification des fichiers et des volumes ingérés.
- Contrôle des schémas et des doublons.
- Vérification des résultats Silver et Gold.
- Contrôle des accès Entra ID, RBAC et ACL.
- Supervision des exécutions et des erreurs.

Ce scénario est une simulation conceptuelle.
Aucune de ces ressources Azure n'a été déployée pour UC07.
