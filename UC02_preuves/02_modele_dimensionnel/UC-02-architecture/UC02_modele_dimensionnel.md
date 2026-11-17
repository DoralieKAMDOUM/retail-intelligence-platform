# UC-02 — Modélisation dimensionnelle

## 1. Objectif

Concevoir un modèle analytique permettant de consolider les ventes en magasin, les ventes en ligne et les stocks afin de produire des indicateurs décisionnels.

## 2. Tables de faits

### FACT_STORE_SALES

- Source : `store_sales`
- Granularité envisagée : une ligne d'article vendu dans une transaction en magasin.
- Mesures : quantité, montant de vente, bénéfice net.
- Dimensions associées : produit, client, date.

### FACT_WEB_SALES

- Source : `web_sales`
- Granularité envisagée : une ligne d'article vendu dans une commande web.
- Mesures : quantité, montant de vente, bénéfice net.
- Dimensions associées : produit, client, date.

### FACT_INVENTORY

- Source : `inventory`
- Granularité envisagée : un état de stock pour un produit, un entrepôt et une date.
- Mesure : quantité en stock.
- Dimensions associées : produit et date.
- Limite : la dimension entrepôt n'est pas encore intégrée au périmètre des six tables explorées.

## 3. Dimensions

### DIM_ITEM

Informations descriptives sur les produits, leurs catégories et leurs caractéristiques.

### DIM_CUSTOMER

Informations permettant de segmenter les clients et d'analyser leurs achats.

### DIM_DATE

Calendrier analytique utilisé pour les analyses quotidiennes, mensuelles, trimestrielles et annuelles.

## 4. Principes de modélisation

Les dimensions communes seront réutilisées entre les tables de faits lorsque les clés et les règles métier le permettent.

Les ventes magasin et web conserveront leurs granularités respectives afin d'éviter les doubles comptages.

Les données de stock seront analysées comme des états à une date donnée, et non comme des ventes cumulables dans le temps.

## 5. Points à valider

- Unicité des clés des dimensions.
- Intégrité référentielle entre faits et dimensions.
- Rôle des différentes dates et clés clients.
- Gestion des versions de produits.
- Définition précise du chiffre d'affaires et des transactions.
- Intégration future de la dimension entrepôt.