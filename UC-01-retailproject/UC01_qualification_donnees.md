 Questions du TP: pour chaque relation envisagée, identifier les colonnes candidates, vérifier leur présence, comparer les types, examiner valeurs distinctes/doublons, vérifier les valeurs sans correspondance, décrire ce qui reste à confirmer.

**Explication.** Une relation n'est jamais supposée à partir du nom . Pour chacune, j'ai mesuré le taux de valeurs sans correspondance (« orphelines »).

| Relation | Colonnes | Test réalisé | Résultat | Statut |
|---|---|---|---|---|
| ventes magasin → produit | `ss_item_sk` → `i_item_sk` | orphelins | 0 | Vérifié |
| ventes magasin → date | `ss_sold_date_sk` → `d_date_sk` | orphelins | 0 | Vérifié |
| ventes magasin → magasin | `ss_store_sk` → `s_store_sk` | orphelins | 0 (12 magasins) | Vérifié |
| ventes magasin → client | `ss_customer_sk` → `c_customer_sk` | nuls et orphelins | 0 nul, 0 orphelin | Vérifié |
| ventes web → produit / client / date | `ws_item_sk`, `ws_bill_customer_sk`, `ws_sold_date_sk` | orphelins | 0 | Vérifié |
| retours magasin → ventes | (`sr_ticket_number`, `sr_item_sk`) → (`ss_ticket_number`, `ss_item_sk`) | correspondance | 37 902 / 37 902 | Vérifié |
| retours web → ventes | (`wr_order_number`, `wr_item_sk`) → (`ws_order_number`, `ws_item_sk`) | correspondance | 38 487 / 38 487 | Vérifié |
| clics → client | `wcs_user_sk` → `c_customer_sk` | valeurs non nulles | 100 % présentes dans `customer` ; mais 42,15 % de clics sans utilisateur | Vérifié (partiel) |
| clics → vente | `wcs_sales_sk` → ? | correspondance | 100 % des valeurs non nulles se retrouvent **à la fois** dans les commandes web et les tickets magasin | **À valider** (ambiguïté, voir E) |
| stocks → produit | `inv_item_sk` → `i_item_sk` | orphelins | 232 380 lignes (180 articles) sans correspondance dans `data/item` | Vérifié (anomalie ; explication via `data_refresh` = **Déduit**) |
| ventes web → entrepôt | `ws_warehouse_sk` → `w_warehouse_sk` | non testé | 158 nuls | À confirmer |
| ventes → promotion | `*_promo_sk` → `p_promo_sk` | non testé en détail | 158 nuls magasin, 121 web | À confirmer |
| client → adresse / démographie | `c_current_addr_sk`, `c_current_cdemo_sk`, `c_current_hdemo_sk` | non testé en détail | 18 à 29 nuls | À confirmer |

Cardinalités : un ticket/une commande → N lignes ; un article → N lignes de vente ; un client → N tickets (**Déduit** des comptages).

**Écart avec l'image « Tables principales »** (document joint) : l'image cite `ws_sk` comme clé de `web_sales` et `wcs_click_sk` comme clé de `web_clickstreams`. Or `web_sales` a 34 colonnes dont aucune ne correspond à un identifiant de ligne propre (la commande est `ws_order_number`) et `web_clickstreams` a 6 colonnes sans identifiant de clic. **À valider** avec le formateur.