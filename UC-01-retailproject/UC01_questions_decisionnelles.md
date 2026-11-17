# UC-01 — Questions décisionnelles
## Retail Intelligence Platform

**Module :** BI, décisionnel et architecture analytique  
**Cas d'utilisation :** UC-01 — Analyse des besoins métier  
**Étape :** A — Comprendre les utilisateurs

---

## 1. Objectif du document

le document vise à identifier les principaux utilisateurs de la future plateforme analytique Retail Intelligence, à formaliser leurs besoins en informations et à définir les décisions métier que ces informations pourront soutenir.

Les besoins sont classés selon trois niveaux de priorité : indispensable, utile et complémentaire.

## 2. Identification des utilisateurs et de leurs responsabilités

| Profil utilisateur | Responsabilités principales |
|---|---|
| Direction générale | Suivre la performance globale de l'enseigne et orienter les décisions stratégiques. |
| Direction commerciale | Piloter les ventes, analyser les performances des produits et des canaux de distribution. |
| Responsable de magasin | Suivre les résultats de son établissement et adapter les actions commerciales locales. |
| Contrôleur de gestion | Analyser les indicateurs financiers et comparer les performances entre périodes et activités. |
| Responsable des stocks | Suivre les niveaux de stock et anticiper les besoins de réapprovisionnement. |
| Équipe Data | Assurer l'intégration, la qualité, la cohérence et la mise à disposition des données. |

## 3. Questions décisionnelles par profil

### 3.1 Direction générale

**Besoin :** disposer d'une vision consolidée de la performance de l'entreprise.

| ID | Question métier | Décision possible | Priorité |
|---|---|---|---|
| Q01 | Comment évolue le chiffre d'affaires global de l'enseigne au fil des mois ? | Ajuster les orientations stratégiques selon l'évolution de l'activité. | Indispensable |
| Q02 | Quel canal de vente contribue le plus au chiffre d'affaires global ? | Orienter les investissements commerciaux entre les différents canaux. | Indispensable |

### 3.2 Direction commerciale

**Besoin :** comprendre les performances commerciales afin d'optimiser les ventes.

| ID | Question métier | Décision possible | Priorité |
|---|---|---|---|
| Q03 | Quels produits génèrent les montants de ventes les plus élevés ? | Renforcer la mise en avant des produits performants. | Indispensable |
| Q04 | Comment évoluent les quantités vendues par catégorie de produits ? | Adapter les actions commerciales selon les tendances observées. | Utile |

### 3.3 Responsable de magasin

**Besoin :** piloter les résultats de son établissement.

| ID | Question métier | Décision possible | Priorité |
|---|---|---|---|
| Q05 | Comment évolue le chiffre d'affaires de mon magasin par période ? | Ajuster les objectifs et les actions commerciales locales. | Indispensable |
| Q06 | Quels produits sont les moins vendus dans mon magasin ? | Réexaminer l'assortiment ou la mise en avant de certains produits. | Utile |

### 3.4 Contrôleur de gestion

**Besoin :** disposer d'indicateurs permettant de comparer les résultats financiers.

| ID | Question métier | Décision possible | Priorité |
|---|---|---|---|
| Q07 | Quels magasins réalisent les chiffres d'affaires les plus élevés ? | Identifier les écarts de performance entre établissements. | Indispensable |
| Q08 | Quelle est l'évolution du montant des retours par canal de vente ? | Identifier les activités nécessitant des analyses ou actions correctives. | Utile |

### 3.5 Responsable des stocks

**Besoin :** suivre la disponibilité des produits et améliorer la gestion des stocks.

| ID | Question métier | Décision possible | Priorité |
|---|---|---|---|
| Q09 | Quels produits présentent les niveaux de stock les plus faibles par magasin ? | Prioriser les réapprovisionnements. | Indispensable |
| Q10 | Quels produits présentent des stocks élevés par rapport aux quantités vendues ? | Réexaminer les commandes et les volumes de stockage. | Utile |

### 3.6 Équipe Data engineer

**Besoin :** garantir la fiabilité et l'exploitabilité des informations mises à disposition.

| ID | Question métier | Décision possible | Priorité |
|---|---|---|---|
| Q11 | Quelle proportion des enregistrements comporte des valeurs manquantes dans les champs essentiels ? | Prioriser les contrôles et les corrections de qualité. | Indispensable |
| Q12 | Quelles relations entre ventes, produits, clients et magasins présentent des références sans correspondance ? | Identifier les problèmes de rapprochement et fiabiliser les futures analyses. | Indispensable |

## 4. Synthèse des besoins

Les questions décisionnelles identifiées couvrent six domaines principaux :

- **Performance globale :** évolution du chiffre d'affaires et contribution des canaux.
- **Performance commerciale :** ventes par produit et catégorie.
- **Performance des magasins :** suivi et comparaison des établissements.
- **Analyse financière :** suivi des ventes et des retours.
- **Gestion des stocks :** disponibilité des produits et rapprochement avec les ventes.
- **Qualité des données :** complétude et cohérence des références.

Au total, douze questions décisionnelles ont été formulées pour six profils utilisateurs.

## 5. Hypothèses et points à vérifier

Les questions présentées correspondent aux besoins décisionnels envisagés pour Retail Intelligence. Leur faisabilité n'est pas encore démontrée.

Les vérifications suivantes seront nécessaires :

- Confirmer la présence des informations permettant de calculer les montants de ventes.
- Vérifier l'existence des identifiants de produits, magasins, clients et dates.
- Déterminer si les ventes magasin et web peuvent être comparées.
- Examiner les informations disponibles concernant les retours.
- Vérifier si les données de stock permettent une analyse par produit et par magasin.
- Contrôler les valeurs manquantes et les références sans correspondance.

Ces points seront étudiés lors de l'exploration et de la qualification des données.

## 6. Conclusion

L'identification des utilisateurs et des questions décisionnelles permet de préciser les besoins de la future plateforme analytique.

Les questions prioritaires concernent principalement le suivi des ventes, la comparaison des performances, la disponibilité des produits et la fiabilité des données. 