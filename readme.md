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