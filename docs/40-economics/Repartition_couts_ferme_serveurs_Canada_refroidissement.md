---
source_file: "Rapport #U2014 R#U00e9partition des co#U00fbts d#U2019une ferme de serveurs au Canada, incluant le refroidissement.docx"
repository_status: "working source / requires validation"
extraction_method: "pandoc"
extracted_on: "2026-08-17"
---

> **Repository note:** This Markdown is a searchable extraction of the supplied DOCX. It is not automatically authoritative. Validate claims and citations before promotion into partner-facing material.

# **Rapport — Répartition des coûts d’une ferme de serveurs au Canada, incluant le refroidissement**

## 1. Résumé exécutif

Pour une ferme de serveurs au Canada, surtout au Québec, une estimation réaliste du coût total annualisé est :

| **Poste**                                                         | **Part typique du coût total** |
|-------------------------------------------------------------------|--------------------------------|
| Serveurs, GPU, stockage, réseau                                   | **50–65 %**                    |
| Infrastructure bâtiment + électrique + sécurité + réseau physique | **15–25 %**                    |
| Électricité totale                                                | **10–25 %**                    |
| Refroidissement total, inclus dans les deux lignes ci-dessus      | **8–15 %**                     |

La proportion simple à retenir est donc :

**≈ 75–85 % infrastructure / serveurs  
≈ 15–25 % électricité  
dont ≈ 8–15 % du coût total lié au refroidissement**

Au Québec, cette part électrique pourrait augmenter pour les grands centres de données, car Hydro-Québec a proposé un tarif de **13 ¢/kWh** pour les centres de données de plus de **5 MW**, applicable à partir de la deuxième moitié de 2026 sous réserve d’approbation réglementaire. ([<u>Hydro-Québec News</u>](https://news.hydroquebec.com/news/press-releases/all-quebec/hydro-quebec-proposing-regie-energie-new-rate-large-data-centres-adjustment-rate-cryptographic-use-applied-blockchains.html))

## 2. Définition des catégories de coûts

### A. Serveurs et équipements IT

Ce poste comprend :

| **Élément**  | **Exemples**                           |
|--------------|----------------------------------------|
| Calcul       | serveurs CPU, GPU, accélérateurs IA    |
| Stockage     | SSD, HDD, baies de stockage            |
| Réseau IT    | switches, cartes réseau, fibre interne |
| Remplacement | renouvellement tous les 3 à 5 ans      |

Dans les grands centres de données, les serveurs restent souvent le poste principal. Le modèle de James Hamilton, cité par Data Center Knowledge, évaluait les coûts mensuels d’un grand centre à environ **57 % pour les serveurs**, **8 % pour le réseau**, **18 % pour distribution électrique + refroidissement**, **4 % autres infrastructures**, et **13 % pour l’électricité**. ([<u>DataCenterKnowledge</u>](https://www.datacenterknowledge.com/servers/hamilton-servers-dominate-data-center-costs))

### B. Infrastructure physique

Ce poste comprend :

| **Élément**     | **Exemples**                                         |
|-----------------|------------------------------------------------------|
| Bâtiment        | terrain, structure, salles techniques                |
| Électricité     | transformateurs, UPS, génératrices, PDUs             |
| Refroidissement | chillers, CRAH/CRAC, pompes, tours d’eau, échangeurs |
| Sécurité        | contrôle d’accès, incendie, surveillance             |
| Redondance      | N+1, 2N, double alimentation                         |

Dans la construction, les systèmes électriques sont souvent le poste le plus lourd, autour de **40–45 %** du coût de construction, tandis que les systèmes HVAC/refroidissement sont souvent autour de **15–20 %**. ([<u>ENCOR Advisors</u>](https://encoradvisors.com/data-center-cost/))

## 3. Portion électricité

L’électricité totale ne sert pas seulement aux serveurs. Elle couvre :

| **Usage électrique**                    | **Part typique de l’électricité consommée** |
|-----------------------------------------|---------------------------------------------|
| Serveurs et équipements IT              | **50–70 %**                                 |
| Refroidissement                         | **15–40 %**                                 |
| UPS / pertes électriques / distribution | **5–15 %**                                  |
| Éclairage et autres auxiliaires         | **1–5 %**                                   |

Ressources naturelles Canada indique qu’environ **la moitié** de l’énergie d’un centre de données est consommée par les serveurs, et qu’environ **40 %** peut aller au refroidissement dans des configurations moins efficaces ou classiques. ([<u>Natural Resources Canada</u>](https://natural-resources.canada.ca/energy-efficiency/energy-star/products/list-certified-products/data-centres)) Une autre ventilation citée par Data Center Knowledge donne **55 %** pour serveurs/équipements, **30 %** pour le refroidissement, **12 %** pour pertes de distribution/UPS, et **3 %** pour l’éclairage. ([<u>DataCenterKnowledge</u>](https://www.datacenterknowledge.com/business/using-a-total-cost-of-ownership-tco-model-for-your-data-center))

## 4. Le rôle du PUE

Le PUE, ou **Power Usage Effectiveness**, mesure :

**PUE = énergie totale du centre / énergie consommée par les équipements IT**

Un PUE de **1,00** voudrait dire que toute l’énergie va directement aux serveurs. En pratique :

| **PUE**   | **Lecture**        |
|-----------|--------------------|
| 1,10–1,25 | Très efficace      |
| 1,25–1,40 | Bon centre moderne |
| 1,40–1,70 | Moyen / ancien     |
| \>1,70    | Inefficace         |

L’Uptime Institute rapportait un PUE moyen mondial d’environ **1,56** en 2024, tandis que beaucoup de constructions récentes atteignent environ **1,30** ou mieux. ([<u>upsite.com</u>](https://www.upsite.com/blog/why-pue-remains-flat-and-what-should-be-done-about-it/))

Au Canada, le climat froid aide à réduire les coûts de refroidissement, car il permet plus souvent le **free cooling** ou l’utilisation de l’air extérieur. Le Régie de l’énergie du Canada note que le Canada attire les centres de données grâce à ses prix d’électricité relativement bas dans certaines provinces, son électricité propre et son climat frais. ([<u>Canada Energy Regulator</u>](https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2024/market-snapshot-energy-demand-from-data-centers-is-steadily-increasing-and-ai-development-is-a-significant-factor.html))

## 5. Détail de la portion refroidissement

Le refroidissement doit être séparé en trois coûts :

| **Type de coût**                         | **Description**                                                      | **Part typique du coût total** |
|------------------------------------------|----------------------------------------------------------------------|--------------------------------|
| CAPEX refroidissement                    | chillers, CRAH/CRAC, pompes, tuyauterie, tours, échangeurs, contrôle | **4–8 %**                      |
| Électricité du refroidissement           | énergie pour évacuer la chaleur                                      | **3–8 %**                      |
| Maintenance / eau / filtres / traitement | entretien, consommables, surveillance                                | **1–3 %**                      |
| **Total refroidissement**                | capital + énergie + maintenance                                      | **8–15 %**                     |

Pour les centres IA à forte densité, surtout avec refroidissement liquide, la portion peut monter à :

**10–20 % du coût total**, selon la densité, la redondance et la technologie choisie.

Turner & Townsend estime que, dans la construction d’un centre de données, la partie mécanique incluant les équipements représente environ **22 %** pour un centre air-cooled et **33 %** pour un centre liquid-cooled; les centres liquid-cooled coûtent aussi en moyenne **7–10 %** de plus que des centres air-cooled comparables en capacité IT. ([<u>reports.turnerandtownsend.com</u>](https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/data-centre-cost-trends))

## 6. Exemple chiffré : centre de données de 1 MW IT au Québec

Hypothèses :

| **Hypothèse**    | **Valeur**   |
|------------------|--------------|
| Charge IT        | 1 MW continu |
| PUE              | 1,30         |
| Tarif électrique | 0,13 \$/kWh  |
| Heures par année | 8 760        |

### Calcul

Énergie IT annuelle :

**1 MW × 8 760 h = 8,76 GWh**

Énergie totale avec PUE 1,30 :

**8,76 GWh × 1,30 = 11,388 GWh**

Coût électrique annuel :

**11 388 000 kWh × 0,13 \$ = 1,48 M\$ / an**

Surplus non-IT :

**11,388 GWh − 8,76 GWh = 2,628 GWh**

Si le refroidissement représente environ **60–80 %** de ce surplus, alors :

| **Poste**                           | **Estimation**         |
|-------------------------------------|------------------------|
| Électricité totale                  | **1,48 M\$ / an**      |
| Électricité directement IT          | **1,14 M\$ / an**      |
| Électricité non-IT totale           | **0,34 M\$ / an**      |
| Électricité liée au refroidissement | **0,20–0,27 M\$ / an** |

Donc, dans cet exemple, le **refroidissement électrique seul** coûte environ :

**200 000 à 270 000 \$ par MW IT par an**

Mais le **refroidissement complet**, incluant équipements amortis et maintenance, serait plutôt autour de :

**0,5 à 1,2 M\$ par MW IT par an**, selon le type de système, la redondance et la densité des racks.

## 7. Ventilation recommandée pour un modèle financier

Pour un centre de données canadien moderne, hors coût logiciel et hors personnel administratif :

| **Poste**                           | **Fourchette prudente** |
|-------------------------------------|-------------------------|
| Serveurs / GPU / stockage           | **50–65 %**             |
| Réseau IT                           | **5–10 %**              |
| Infrastructure électrique           | **10–18 %**             |
| Infrastructure refroidissement      | **4–8 %**               |
| Bâtiment, terrain, sécurité, autres | **5–10 %**              |
| Électricité IT                      | **8–18 %**              |
| Électricité refroidissement         | **3–8 %**               |
| Maintenance refroidissement         | **1–3 %**               |

Version simplifiée :

| **Grande catégorie**                                            | **Part**    |
|-----------------------------------------------------------------|-------------|
| IT : serveurs, GPU, réseau, stockage                            | **55–70 %** |
| Infrastructure physique                                         | **15–25 %** |
| Électricité totale                                              | **10–25 %** |
| Refroidissement total, inclus dans infrastructure + électricité | **8–15 %**  |

## 8. Conclusion

Pour une ferme de serveurs au Canada, la meilleure estimation générale est :

**Infrastructure + serveurs : 75–85 %  
Électricité : 15–25 %  
Refroidissement total : 8–15 % du coût total**

Le refroidissement est souvent perçu comme énorme parce qu’il représente une grande partie de la **construction mécanique** et de l’**énergie non-IT**. Mais dans le coût total annualisé, les serveurs, GPU et équipements IT restent habituellement le poste dominant. Dans un centre moderne au Canada avec un bon PUE, le refroidissement électrique seul peut être aussi bas que **3–8 % du coût total**, mais le refroidissement complet, avec équipements et maintenance, se situe plutôt autour de **8–15 %**.
