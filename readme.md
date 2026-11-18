J1 – Retail Intelligence Platform 

Contenu :

UC01_reponses.md : besoin métier, KPI, inventaire des sources, qualification, relations, limites, questions de recul (TP p.7-13).
UC02_reponses.md : contraintes, comparaison DW / Data Lake / Lakehouse, architecture Bronze-Silver-Gold, composants, flux, gouvernance, local vs Azure (TP p.13-19).
preuves/ : scripts Python (a1.py, a2.py, a3.py) et leurs sorties (a1.out, a2.out) utilisés pour mesurer les volumes, nulls, doublons et jointures.

Reproduire les mesures : décompresser retail_project.zip dans /home/claude/kit/ (ou adapter la variable B en tête de chaque script), puis python3 a1.py, a2.py, a3.py.

Limites à connaître :

Version et provenance du kit : non communiquées.
Noms de colonnes : déduits du schéma TPC-DS/TPCx-BB (fichiers sans en-tête), à confirmer avec la spécification TPCx-BB.
Architecture : conception logique, rien n'a été déployé.
Les statuts « À valider » sont à trancher avec le formateur.

J2 – Retail Intelligence Platform

Contenu :

UC03 – Hadoop/HDFS : installation et configuration de Hadoop 3.5.0 sous Ubuntu WSL2, mise en place d'un Data Lake (Raw, Bronze, Silver, Gold, Quality, Logs), importation des fichiers TPCx-BB (store_sales, customer, item), vérification des services, des volumes, des permissions et des accès HDFS.

UC04 – Apache NiFi : installation de NiFi 2.12.0, création du pipeline GetFile → PutHDFS, ingestion des données vers /retail-lake/raw/nifi, suivi de la provenance et tests de gestion des erreurs.

Preuves : retail-project-preuves.zip contient les captures d'écran, configurations, résultats des commandes HDFS, inventaire des fichiers, journaux d'erreurs et tests de correction.

Résultats : HDFS opérationnel, 784 399 enregistrements répartis dans 3 fichiers TPCx-BB (107,7 Mo), ingestion NiFi réussie et erreur contrôlée corrigée.

Limites : infrastructure locale mono-nœud, sans déploiement distribué ni automatisation complète du traitement des données.
