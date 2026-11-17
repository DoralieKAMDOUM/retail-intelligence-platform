 
# UC-01 — Fiche de cadrage métier
## Projet : Retail Intelligence Platform

**Formation :** Mastère Développement, Data & IA – IPSSI  
**Module :** Business Intelligence, décisionnel et architecture analytique  
**Cas d'utilisation :** UC-01 – Analyser le besoin métier et explorer les sources

### Comment et pourquoi j'ai structurer mon projet ainsi
cette premiere partie est constitué de:

- Contexte:	Expliquer la situation de l'entreprise
- Problématique:	Formuler le problème central
- Objectifs:	Définir ce que le projet doit accomplir
- Parties prenantes:	Identifier les futurs utilisateurs
-  Périmètre:	Délimiter ce qui sera étudié
- Sources:	Identifier les données nécessaires
- Contraintes:	Anticiper les limites
- Résultats attendus:	Définir les productions attendues
- Critères de réussite:	Déterminer comment évaluer le travail

### 1. Contexte du projet

Retail Intelligence est une enseigne de distribution disposant de plusieurs canaux de vente. Son activité génère des données relatives aux ventes, aux produits, aux clients, aux magasins et aux stocks.

Ces données proviennent de différents systèmes et nécessitent une analyse préalable afin de déterminer dans quelle mesure elles peuvent répondre aux besoins décisionnels de l'entreprise.

Dans une démarche d'amélioration du pilotage commercial, Retail Intelligence souhaite construire une plateforme analytique permettant de disposer d'indicateurs cohérents, de comparer les performances et de mieux comprendre l'évolution de son activité.

### 2. Problématique métier

Comment Retail Intelligence peut-elle exploiter et structurer ses données commerciales afin de disposer d'indicateurs fiables, de comparer les performances de ses différents canaux de vente et d'améliorer la prise de décision ?

### 3. Objectif général

Définir les besoins fonctionnels et décisionnels d'une plateforme analytique destinée à améliorer le pilotage des activités commerciales de Retail Intelligence.

### 4. Objectifs spécifiques

- Identifier les besoins des différents utilisateurs métier.
- Définir les principales questions décisionnelles.
- Proposer des indicateurs clés de performance (KPI) adaptés aux besoins.
- Identifier et inventorier les sources de données disponibles.
- Évaluer la qualité, la structure et l'exploitabilité des données.
- Identifier les relations possibles entre les différents domaines de données.
- Documenter les limites, les hypothèses et les besoins non couverts.

### 5. Parties prenantes

| Acteur | Responsabilité | Besoin principal |
|---|---|---|
| Direction générale | Piloter la performance globale | Disposer d'une vision consolidée de l'activité |
| Direction commerciale | Suivre les ventes et les produits | Identifier les tendances et les performances commerciales |
| Responsable de magasin | Piloter un établissement | Analyser les ventes de son magasin |
| Contrôleur de gestion | Analyser les indicateurs financiers | Comparer les performances et suivre les écarts |
| Responsable des stocks | Suivre la disponibilité des produits | Identifier les risques de rupture ou de surstock |
| Équipe Data engineer | Préparer et fiabiliser les données | Garantir la qualité et la cohérence des informations |

### 6. Périmètre fonctionnel

Le périmètre initial concerne les domaines suivants, sous réserve de leur disponibilité et de leur exploitabilité :

- Ventes réalisées en magasin.
- Ventes réalisées sur le canal web.
- Produits et caractéristiques associées.
- Clients et informations disponibles.
- Magasins.
- Stocks et inventaires.
- Retours de produits.
- Dimensions temporelles.

Les données de navigation web et de promotion pourront également être étudiées selon les besoins et les fichiers réellement disponibles.

### 7. Sources de données

La source principale du projet est le jeu de données synthétique TPCx-BB (TPC Express Big Bench).

Les données seront étudiées afin d'identifier leurs formats, leurs volumes, leurs colonnes, leurs identifiants et leurs éventuelles anomalies.

La disponibilité d'un fichier ne garantit pas automatiquement que les informations qu'il contient sont suffisantes pour répondre à un besoin métier.

### 8. Contraintes et points de vigilance

- Les données utilisées sont synthétiques et ne représentent pas nécessairement toutes les caractéristiques d'une entreprise réelle.
- Les indicateurs doivent être définis en fonction des informations réellement disponibles.
- Les relations entre les sources doivent être vérifiées avant toute exploitation.
- Les éventuelles valeurs manquantes, incohérences et limites de documentation doivent être signalées.
- Les besoins non couverts par les données disponibles doivent être clairement identifiés.

### 9. Résultats attendus

À l'issue du cadrage et de l'analyse des sources, le projet devra disposer :

- D'une compréhension formalisée des besoins métier.
- D'une identification des utilisateurs et de leurs questions décisionnelles.
- D'un premier dictionnaire de KPI.
- D'un inventaire documenté des sources.
- D'une première évaluation de la qualité des données.
- D'une liste des limites et hypothèses.

Ces éléments serviront de base à la conception de l'architecture analytique dans l'UC-02.

### 10. Critères de réussite

Le cadrage sera considéré comme satisfaisant si les besoins métier sont clairement formulés, si les utilisateurs et leurs décisions sont identifiés et si les indicateurs envisagés sont cohérents avec les objectifs du projet.

 