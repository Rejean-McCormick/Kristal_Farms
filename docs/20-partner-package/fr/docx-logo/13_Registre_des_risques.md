---
source_file: "13_Registre_des_risques.docx"
repository_status: "formatted French partner deliverable / compare against EN Markdown authority"
extraction_method: "pandoc"
extracted_on: "2026-08-17"
---

> **Repository note:** This Markdown is a searchable extraction of the supplied DOCX. It is not automatically authoritative. Validate claims and citations before promotion into partner-facing material.

# 

# **Kristal Farms — Registre des risques**

**Statut du document :** Ébauche de diligence destinée aux partenaires  
**Focalisation du projet :** côte du Labrador, avec Nain comme première cible et les communautés côtières du Labrador comme logique de réplication  
**Version :** v1.0  
**Préparé pour :** examen par les partenaires et diligence raisonnable  
**Distribution :** destinée aux partenaires ; les détails financiers et les hypothèses d’ingénierie propres aux sites ne seront partagés qu’après validation / NDA, le cas échéant

[**Kristal Farms — Registre des risques 1**](#kristal-farms-registre-des-risques)

> [1. Objectif 3](#objectif)
>
> [2. Méthode d’évaluation des risques 4](#méthode-dévaluation-des-risques)
>
> [Probabilité 4](#probabilité)
>
> [Impact 4](#impact)
>
> [Statut 4](#statut)
>
> [3. Matrice sommaire des risques 5](#matrice-sommaire-des-risques)
>
> [4. Registre détaillé des risques 7](#registre-détaillé-des-risques)
>
> [1. Risque lié à la ressource hydroélectrique et à la capacité ferme 7](#risque-lié-à-la-ressource-hydroélectrique-et-à-la-capacité-ferme)
>
> [2. Risque de sélection de site et de validation des données 8](#risque-de-sélection-de-site-et-de-validation-des-données)
>
> [3. Risque lié à l’interconnexion moyenne tension courte et au poste électrique 9](#risque-lié-à-linterconnexion-moyenne-tension-courte-et-au-poste-électrique)
>
> [4. Risque lié à l’accès côtier et à la logistique de ravitaillement maritime 10](#risque-lié-à-laccès-côtier-et-à-la-logistique-de-ravitaillement-maritime)
>
> [5. Risque lié à la glace, à la météo et à la construction saisonnière 11](#risque-lié-à-la-glace-à-la-météo-et-à-la-construction-saisonnière)
>
> [6. Risque de disponibilité et de résilience de la fibre 11](#risque-de-disponibilité-et-de-résilience-de-la-fibre)
>
> [7. Risque lié au consentement communautaire / CLPE 12](#risque-lié-au-consentement-communautaire-clpe)
>
> [8. Risque lié à la structure de gouvernance 14](#risque-lié-à-la-structure-de-gouvernance)
>
> [9. Risque lié aux permis environnementaux et au ΔT aquatique 15](#risque-lié-aux-permis-environnementaux-et-au-δt-aquatique)
>
> [10. Risque lié à l’utilisation de la chaleur 16](#risque-lié-à-lutilisation-de-la-chaleur)
>
> [11. Risque de compatibilité des bâtiments en hiver 17](#risque-de-compatibilité-des-bâtiments-en-hiver)
>
> [12. Risque lié au puits de chaleur estival 18](#risque-lié-au-puits-de-chaleur-estival)
>
> [13. Risque de panne ou de restriction de la source de refroidissement 19](#risque-de-panne-ou-de-restriction-de-la-source-de-refroidissement)
>
> [14. Risque lié à la demande des locataires et au taux d’occupation 20](#risque-lié-à-la-demande-des-locataires-et-au-taux-doccupation)
>
> [15. Risque lié au modèle commercial et aux SLA 21](#risque-lié-au-modèle-commercial-et-aux-sla)
>
> [16. Risque lié à la location en boîte noire et aux frontières des données 22](#risque-lié-à-la-location-en-boîte-noire-et-aux-frontières-des-données)
>
> [17. Risque lié aux coûts de construction et aux fournisseurs modulaires 23](#risque-lié-aux-coûts-de-construction-et-aux-fournisseurs-modulaires)
>
> [18. Risque lié aux opérations, au personnel et à la maintenance 24](#risque-lié-aux-opérations-au-personnel-et-à-la-maintenance)
>
> [19. Risque lié à la preuve des bénéfices publics et au tableau de bord 25](#risque-lié-à-la-preuve-des-bénéfices-publics-et-au-tableau-de-bord)
>
> [20. Risque de réplication au-delà de Nain 26](#risque-de-réplication-au-delà-de-nain)
>
> [5. Points de décision liés à la fermeture des risques 27](#points-de-décision-liés-à-la-fermeture-des-risques)
>
> [6. Risques qui ne devraient pas être cachés 27](#risques-qui-ne-devraient-pas-être-cachés)
>
> [7. Plan immédiat de diligence raisonnable 29](#plan-immédiat-de-diligence-raisonnable)
>
> [Technique 29](#technique)
>
> [Communauté et gouvernance 29](#communauté-et-gouvernance)
>
> [Commercial 29](#commercial)
>
> [8. Carte de responsabilité des risques 30](#carte-de-responsabilité-des-risques)
>
> [9. Questions ouvertes pour les partenaires 31](#questions-ouvertes-pour-les-partenaires)
>
> [10. Base documentaire 32](#base-documentaire)

##  

## 

## 1. Objectif

Ce registre des risques identifie les principaux risques qui doivent être évalués avant de faire passer Kristal Farms du concept au développement de projet aligné avec les partenaires.

Le registre est organisé autour de la thèse du projet :

- colocaliser le calcul avec de l’hydroélectricité froide ;

- placer les conteneurs de calcul modulaires près des utilisateurs de chaleur du village ;

- éviter les longs corridors de transmission à haute tension ;

- exporter le calcul par fibre, et non l’électricité ;

- réutiliser localement la chaleur des serveurs avant de la rejeter ;

- exploiter les conteneurs des locataires comme des plateformes de calcul en mode boîte noire ;

- prioriser la chaleur communautaire, le consentement, la gouvernance et la valeur locale mesurable.

Ce document n’est pas une évaluation finale des risques d’ingénierie, juridiques, environnementaux ou d’investissement. Il s’agit d’un cadre de diligence raisonnable de travail pour les conversations avec les partenaires.

## 2. Méthode d’évaluation des risques

### Probabilité

| **Évaluation** | **Signification**                                                                  |
|----------------|------------------------------------------------------------------------------------|
| Faible         | Peu probable selon le concept actuel, mais nécessite tout de même une surveillance |
| Moyenne        | Plausible et devrait être géré activement                                          |
| Élevée         | Probable à moins qu’une mesure d’atténuation spécifique soit réalisée              |

### Impact

| **Évaluation** | **Signification**                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Faible         | Gérable dans le cadre normal de la planification du projet                                                   |
| Moyen          | Pourrait retarder, redimensionner ou modifier matériellement le projet                                       |
| Élevé          | Pourrait bloquer l’investissement, l’obtention de permis, le consentement, la construction ou l’exploitation |

### Statut

| **Statut**            | **Signification**                                                                     |
|-----------------------|---------------------------------------------------------------------------------------|
| Ouvert                | Le risque nécessite encore des preuves, des contributions de partenaires ou une étude |
| Atténuation active    | Une voie d’atténuation existe et devrait être avancée                                 |
| Liste de surveillance | Le risque n’est pas bloquant pour l’instant, mais doit être suivi                     |
| Point de passage      | Doit être résolu avant une grande étape décisionnelle                                 |

## 

## 3. Matrice sommaire des risques

| **\#** | **Risque**                                                                  | **Probabilité**  | **Impact** | **Statut**            |
|--------|-----------------------------------------------------------------------------|------------------|------------|-----------------------|
| 1      | Risque lié à la ressource hydroélectrique et à la capacité ferme            | Moyenne          | Élevé      | Point de passage      |
| 2      | Risque de sélection de site et de validation des données                    | Moyenne          | Élevé      | Point de passage      |
| 3      | Risque lié à l’interconnexion moyenne tension courte et au poste électrique | Moyenne          | Élevé      | Ouvert                |
| 4      | Risque lié à l’accès côtier et à la logistique de ravitaillement maritime   | Moyenne          | Moyen      | Atténuation active    |
| 5      | Risque lié à la glace, à la météo et à la construction saisonnière          | Élevée           | Moyen      | Atténuation active    |
| 6      | Risque de disponibilité et de résilience de la fibre                        | Moyenne          | Élevé      | Point de passage      |
| 7      | Risque lié au consentement communautaire / CLPE                             | Moyenne          | Élevé      | Point de passage      |
| 8      | Risque lié à la structure de gouvernance                                    | Moyenne          | Élevé      | Ouvert                |
| 9      | Risque lié aux permis environnementaux et au ΔT aquatique                   | Moyenne          | Élevé      | Point de passage      |
| 10     | Risque lié à l’utilisation de la chaleur                                    | Moyenne          | Élevé      | Atténuation active    |
| 11     | Risque de compatibilité des bâtiments en hiver                              | Moyenne          | Moyen      | Atténuation active    |
| 12     | Risque lié au puits de chaleur estival                                      | Moyenne          | Moyen      | Atténuation active    |
| 13     | Risque de panne ou de restriction de la source de refroidissement           | Faible à moyenne | Élevé      | Atténuation active    |
| 14     | Risque lié à la demande des locataires et au taux d’occupation              | Moyenne          | Élevé      | Ouvert                |
| 15     | Risque lié au modèle commercial et aux SLA                                  | Moyenne          | Élevé      | Ouvert                |
| 16     | Risque lié à la location en boîte noire et aux frontières des données       | Faible à moyenne | Élevé      | Atténuation active    |
| 17     | Risque lié aux coûts de construction et aux fournisseurs modulaires         | Moyenne          | Élevé      | Ouvert                |
| 18     | Risque lié aux opérations, au personnel et à la maintenance                 | Moyenne          | Moyen      | Ouvert                |
| 19     | Risque lié à la preuve des bénéfices publics et au tableau de bord          | Faible à moyenne | Moyen      | Atténuation active    |
| 20     | Risque de réplication au-delà de Nain                                       | Moyenne          | Moyen      | Liste de surveillance |

## 

## 4. Registre détaillé des risques

### 1. Risque lié à la ressource hydroélectrique et à la capacité ferme

**Risque :  
**La ressource hydroélectrique ciblée pourrait ne pas fournir la capacité fiable, le profil saisonnier des débits, la production hivernale ou l’économie de développement nécessaires pour soutenir à la fois les besoins communautaires et une plateforme pilote de calcul.

**Pourquoi c’est important :  
**Le projet dépend d’une énergie propre locale. Si la ressource hydroélectrique est plus faible, plus saisonnière, plus coûteuse ou plus contrainte sur le plan environnemental que prévu, le projet pourrait devoir redimensionner la charge de calcul, retarder le pilote ou réviser sa stratégie de site.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Point de passage  
**Responsable principal :** Partenaire hydroélectrique / service public  
**Responsables de soutien :** Kristal Farms, conseiller en ingénierie, partenaire communautaire / gouvernemental

**Atténuation :**

- Réaliser une préfaisabilité hydroélectrique pour Nain / la rivière cible.

- Confirmer la production ferme hivernale, le débit saisonnier et les écrêtements prévus.

- Dimensionner la première plateforme de calcul selon la capacité ferme vérifiée, et non selon la production de pointe théorique.

- Préserver les priorités locales d’électricité et de chaleur communautaires avant d’allouer un surplus au calcul.

- Éviter de dépendre d’une logique de mégabarrage ou de longue transmission intérieure.

**Prochaines preuves nécessaires :**

- Données hydrologiques.

- Profil préliminaire de production.

- Estimation de la capacité ferme.

- Concept d’interconnexion.

- Contraintes environnementales.

- Documentation des projets hydroélectriques existants ou proposés.

### 2. Risque de sélection de site et de validation des données

**Risque :  
**Les informations actuelles sur les sites peuvent contenir des hypothèses préliminaires, incomplètes, dépassées ou non spécifiques au projet.

**Pourquoi c’est important :  
**Les documents destinés aux partenaires doivent distinguer les faits confirmés des hypothèses de présélection. Des affirmations non validées sur les sites peuvent nuire à la confiance des partenaires et créer des problèmes d’obtention de permis, de relations communautaires ou d’investissement.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Point de passage  
**Responsable principal :** Kristal Farms  
**Responsables de soutien :** partenaire hydroélectrique, conseiller cartographie / SIG, partenaire local

**Atténuation :**

- Maintenir un inventaire de sites unique et faisant autorité.

- Séparer les sites candidats, exclus et reportés.

- Étiqueter toutes les données préliminaires comme « à valider ».

- Utiliser Nain comme première cible uniquement si les données de site, d’énergie, de fibre et le processus communautaire le soutiennent.

- Garder les éléments relatifs au Nunavik, à Churchill Falls, à l’intérieur des terres et aux mégaprojets comme logique de comparaison ou d’exclusion, et non comme thèse centrale du projet.

**Prochaines preuves nécessaires :**

- KML actuel de la côte du Labrador.

- CSV d’inventaire des éléments.

- CSV de validation.

- Logique de classement des sites.

- Liste des sources pour chaque élément inclus et exclu.

### 3. Risque lié à l’interconnexion moyenne tension courte et au poste électrique

**Risque :  
**La connexion moyenne tension courte prévue entre la source hydroélectrique et le poste du village pourrait être plus difficile, coûteuse ou lente à réaliser que prévu.

**Pourquoi c’est important :  
**L’avantage de coût dépend de l’évitement d’une longue transmission à haute tension et du placement des conteneurs près des utilisateurs de chaleur. Si le concept de moyenne tension courte n’est pas faisable, l’architecture du projet devra être révisée.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Ouvert  
**Responsable principal :** Partenaire service public / ingénierie électrique  
**Responsables de soutien :** Kristal Farms, exploitant hydroélectrique, autorité locale

**Atténuation :**

- Confirmer les options de tracé moyenne tension.

- Confirmer la classe de tension, l’emprise, l’emplacement du poste, les besoins de protection, de mise à la terre et de comptage.

- Prioriser un centre énergétique en bordure du village ou près du port qui garde les boucles de chaleur courtes.

- Éviter une architecture qui place le calcul au barrage si la chaleur ne peut pas être réutilisée localement.

**Prochaines preuves nécessaires :**

- Schéma unifilaire conceptuel.

- Carte du tracé.

- Étude d’interconnexion.

- Concept de poste électrique.

- Fourchette préliminaire de coûts.

- Examen de constructibilité et de permis.

### 4. Risque lié à l’accès côtier et à la logistique de ravitaillement maritime

**Risque :  
**La livraison de l’équipement, la manutention des conteneurs, l’accès portuaire et les fenêtres saisonnières de ravitaillement maritime peuvent limiter le déploiement.

**Pourquoi c’est important :  
**Le modèle dépend d’une logistique maritime modulaire. Des fenêtres de navigation manquées, une capacité portuaire insuffisante ou des perturbations météorologiques pourraient retarder la construction et augmenter les coûts.

**Probabilité :** Moyenne  
**Impact :** Moyen  
**Statut :** Atténuation active  
**Responsable principal :** Partenaire logistique / maritime  
**Responsables de soutien :** fournisseur de centre de données modulaire, autorité locale, Kristal Farms

**Atténuation :**

- Concevoir autour de conteneurs modulaires standard de 20 ou 40 pieds.

- Utiliser des plateformes adjacentes au port ou en bordure du village lorsque possible.

- Planifier la séquence de construction et de livraison selon des fenêtres saisonnières réalistes.

- Prépositionner les pièces de rechange critiques, pompes, vannes, contrôles, matériaux de fibre et composants de boucle de chaleur.

- Éviter de promettre un accès maritime toute l’année.

**Prochaines preuves nécessaires :**

- Évaluation de la capacité portuaire.

- Calendrier de barge / ravitaillement maritime.

- Plan de levage et de transport.

- Évaluation de la zone de dépôt.

- Plan de stockage hivernal.

- Examen de la capacité des entrepreneurs locaux.

### 5. Risque lié à la glace, à la météo et à la construction saisonnière

**Risque :  
**La glace, les tempêtes, les cycles gel-dégel, l’obscurité hivernale et les courtes saisons de construction peuvent affecter le calendrier, les coûts et la maintenabilité.

**Pourquoi c’est important :  
**Les conditions côtières du Labrador exigent une planification prudente. Les fenêtres de construction et de maintenance peuvent être plus limitées que dans les marchés méridionaux des centres de données.

**Probabilité :** Élevée  
**Impact :** Moyen  
**Statut :** Atténuation active  
**Responsable principal :** Partenaire EPC / construction  
**Responsables de soutien :** partenaire local, partenaire logistique, responsable des opérations

**Atténuation :**

- Utiliser des modules et des skids préfabriqués afin de réduire le travail sur site.

- Concevoir toute la tuyauterie externe, les vannes et les contrôles avec protection contre le gel.

- Utiliser des composants critiques isolés et chauffés par traçage lorsque requis.

- Intégrer l’accès de maintenance dans l’aménagement des plateformes.

- Planifier la mise en service selon les fenêtres météorologiques.

**Prochaines preuves nécessaires :**

- Base de conception climatique.

- Hypothèses de charges de glace et de neige.

- Plan de construction saisonnier.

- Conception de la protection contre le gel.

- Plan d’accès pour maintenance d’urgence.

### 6. Risque de disponibilité et de résilience de la fibre

**Risque :  
**Le projet pourrait ne pas disposer d’une connectivité fibre suffisante, fiable, redondante ou commercialement acceptable pour les locataires de calcul.

**Pourquoi c’est important :  
**Kristal Farms exporte les résultats de calcul par fibre, et non l’électricité. Sans connectivité fiable, la location de capacité de calcul, la crédibilité des SLA et l’économie des partenaires s’affaiblissent.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Point de passage  
**Responsable principal :** Partenaire télécom / fibre  
**Responsables de soutien :** exploitant NOC, locataire de calcul, Kristal Farms

**Atténuation :**

- Confirmer le tracé, la capacité, la latence, la disponibilité et le plan de mise à niveau de la fibre.

- Concevoir des liens A/B vers les plateformes lorsque possible.

- Mettre en place la surveillance NOC et la réponse aux incidents.

- Définir quels types de charges de travail sont acceptables selon la latence et la fiabilité disponibles.

- Prioriser, dans les premières phases au besoin, les charges de calcul par lots, résilientes ou tolérantes aux délais.

- Garder les valeurs exactes de SLA hors des premiers documents destinés aux partenaires jusqu’à la validation télécom.

**Prochaines preuves nécessaires :**

- Tracé et propriété de la fibre.

- Devis de capacité.

- Estimation de latence.

- Historique de disponibilité.

- Options de redondance.

- Plan de réparation et d’épissure.

- Architecture NOC.

### 7. Risque lié au consentement communautaire / CLPE

**Risque :  
**Le projet pourrait ne pas obtenir ou maintenir le consentement communautaire, y compris le consentement libre, préalable et éclairé lorsque applicable.

**Pourquoi c’est important :  
**La légitimité communautaire n’est pas optionnelle. Sans consentement et alignement des bénéfices, le projet ne devrait pas avancer.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Point de passage  
**Responsable principal :** Partenaire communautaire / gouvernemental  
**Responsables de soutien :** Kristal Farms, conseiller juridique, leadership local

**Atténuation :**

- Commencer par l’information et l’écoute avant les engagements de site.

- Utiliser un processus CLPE commun avec des calendriers propres à chaque site.

- Distinguer clairement les principes confirmés des éléments de conception ouverts.

- S’assurer que la chaleur, les emplois, la formation et les bénéfices sont négociés localement.

- Éviter de présenter les modalités de gouvernance comme finalisées avant les décisions communautaires.

**Prochaines preuves nécessaires :**

- Plan d’engagement communautaire.

- Aperçu du processus CLPE.

- Calendrier décisionnel local.

- Priorités en matière de bénéfices.

- Registre des préoccupations et des réponses.

- Ébauche d’accord sur les bénéfices communautaires / cadre d’IBA.

### 8. Risque lié à la structure de gouvernance

**Risque :  
**Les conseils de projet, comités de chaleur, comités environnementaux, conseils Kristals, voies d’escalade et droits décisionnels pourraient rester indéfinis trop longtemps.

**Pourquoi c’est important :  
**Une gouvernance floue peut créer des différends entre l’hôte, les locataires, la communauté, le service public, le gouvernement et les utilisateurs de chaleur.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Ouvert  
**Responsable principal :** Responsable gouvernance / juridique  
**Responsables de soutien :** partenaire communautaire, Kristal Farms, partenaire service public, locataires

**Atténuation :**

- Séparer la gouvernance en principes confirmés, éléments de conception ouverts et décisions requises.

- Définir la composition des comités, les droits de nomination, le champ d’action, l’autorité décisionnelle, l’autorité consultative et les voies d’escalade.

- Définir les priorités d’allocation de chaleur avant l’exploitation.

- Définir l’autorité de publication pour les tableaux de bord publics.

- Définir le processus de griefs, de médiation et d’arbitrage.

**Prochaines preuves nécessaires :**

- Ébauche de charte de gouvernance.

- Ébauche des mandats des comités.

- Matrice des droits décisionnels.

- Processus de griefs.

- Calendrier d’escalade des différends.

- Commentaires de la communauté.

### 9. Risque lié aux permis environnementaux et au ΔT aquatique

**Risque :  
**Le rejet de chaleur, la prise d’eau / l’exutoire, la construction ou l’intégration hydroélectrique peuvent déclencher des enjeux de permis environnementaux ou des contraintes de conformité liées au ΔT.

**Pourquoi c’est important :  
**Le système dépend d’un refroidissement sans contact et d’un rejet de chaleur contrôlé. Tout dommage environnemental, dommage perçu ou manquement aux permis peut arrêter les opérations.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Point de passage  
**Responsable principal :** Responsable environnement / permis  
**Responsables de soutien :** partenaire hydroélectrique, ingénieur du système thermique, comité environnemental

**Atténuation :**

- Utiliser deux circuits scellés.

- Utiliser des échangeurs à plaques pour tous les échanges thermiques avec l’environnement.

- Garder l’eau de rivière / baie séparée des boucles informatiques et des boucles de bâtiments.

- Utiliser des refroidisseurs secs comme solution de secours.

- Surveiller en continu le ΔT, les débits, les températures et les alarmes.

- Réduire la charge informatique si les limites de ΔT sont approchées.

- Publier les indicateurs environnementaux dans le tableau de bord lorsque pertinent.

**Prochaines preuves nécessaires :**

- État de référence environnemental.

- Concept de prise d’eau / exutoire.

- Seuil de ΔT défini par le régulateur.

- Examen des poissons et habitats aquatiques.

- Parcours d’obtention des permis.

- Plan de surveillance.

- Plan de réponse aux incidents.

### 10. Risque lié à l’utilisation de la chaleur

**Risque :  
**Le village pourrait ne pas avoir suffisamment de demande de chaleur connectée pour absorber la chaleur des serveurs au moment et à l’échelle où elle est produite.

**Pourquoi c’est important :  
**La réutilisation de chaleur est un facteur central de différenciation. Si la chaleur utile est trop faible, le projet perd de la valeur communautaire et affaiblit son argument environnemental.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Atténuation active  
**Responsable principal :** Partenaire du système thermique  
**Responsables de soutien :** partenaire communautaire, propriétaires de bâtiments, Kristal Farms

**Atténuation :**

- Commencer par les bâtiments publics : clinique, école, hôtel de ville et autres charges prioritaires.

- Ajouter les logements voisins seulement après validation des charges publiques.

- Ajouter une serre comme puits de chaleur en mi-saison et en été.

- Inclure du stockage thermique stratifié.

- Phaser les plateformes de calcul seulement lorsque les puits de chaleur peuvent absorber la production attendue.

- Suivre la chaleur utile livrée et le HUF.

**Prochaines preuves nécessaires :**

- Inventaire des charges thermiques des bâtiments.

- Liste prioritaire des bâtiments publics.

- Tracé des conduites.

- Conception des sous-stations.

- Faisabilité de la serre.

- Dimensionnement du stockage thermique.

- Estimation saisonnière du HUF.

### 11. Risque de compatibilité des bâtiments en hiver

**Risque :  
**Les bâtiments existants pourraient nécessiter des températures d’alimentation plus élevées que ce que la chaleur des serveurs peut fournir directement.

**Pourquoi c’est important :  
**Si des bâtiments publics ou des habitations utilisent des radiateurs anciens exigeant 65 à 75 °C, le projet pourrait devoir ajouter des systèmes d’appoint, moderniser les émetteurs ou réduire la portée du service thermique.

**Probabilité :** Moyenne  
**Impact :** Moyen  
**Statut :** Atténuation active  
**Responsable principal :** Partenaire en ingénierie mécanique  
**Responsables de soutien :** propriétaires de bâtiments, exploitant thermique, partenaire communautaire

**Atténuation :**

- Réaliser un relevé des systèmes de chauffage des bâtiments.

- Identifier d’abord les bâtiments prêts pour la basse température.

- Installer au besoin une pompe à chaleur d’appoint centrale.

- Utiliser des ventilo-convecteurs, des émetteurs surdimensionnés ou des améliorations ciblées pour les bâtiments problématiques.

- Tester la performance lors des journées de conception les plus froides avant tout engagement complet de service.

**Prochaines preuves nécessaires :**

- Audits de bâtiments.

- Inventaire des radiateurs / émetteurs.

- Exigences en eau chaude domestique.

- Dimensionnement de l’appoint.

- Conception des sous-stations de bâtiment.

- Plan de tests de mise en service.

### 12. Risque lié au puits de chaleur estival

**Risque :  
**Pendant l’été, la serre et le stockage pourraient ne pas absorber suffisamment de chaleur des serveurs, forçant davantage de rejet de chaleur ou un écrêtement du calcul.

**Pourquoi c’est important :  
**Les limites des puits de chaleur estivaux peuvent réduire l’utilisation du calcul ou abaisser les indicateurs d’utilisation de chaleur.

**Probabilité :** Moyenne  
**Impact :** Moyen  
**Statut :** Atténuation active  
**Responsable principal :** Partenaire du système thermique  
**Responsables de soutien :** exploitant de serre, exploitant de calcul, comité environnemental

**Atténuation :**

- Utiliser la serre comme principal puits de chaleur en saison chaude.

- Ajouter du stockage pour compenser les décalages quotidiens de chaleur.

- Définir des déclencheurs opérationnels pour la planification ou la limitation du calcul.

- Augmenter la superficie de serre seulement lorsque cela est justifié opérationnellement et commercialement.

- Traiter le rejet comme dernier recours après la réutilisation et le stockage.

**Prochaines preuves nécessaires :**

- Modèle thermique de serre.

- Bilan thermique estival.

- Dimensionnement des réservoirs.

- Plan de ventilation et d’exploitation de la serre.

- Politique de planification du calcul.

- Cible saisonnière de HUF.

### 13. Risque de panne ou de restriction de la source de refroidissement

**Risque :  
**La source froide principale, par exemple l’eau de mer / de baie au port, pourrait être indisponible, restreinte, encrassée, prise par la glace ou temporairement inadaptée.

**Pourquoi c’est important :  
**Les plateformes de calcul exigent un refroidissement fiable. Une contrainte de refroidissement peut forcer une réduction de charge ou un arrêt.

**Probabilité :** Faible à moyenne  
**Impact :** Élevé  
**Statut :** Atténuation active  
**Responsable principal :** Exploitant du système de refroidissement  
**Responsables de soutien :** responsable environnemental, locataire de calcul, NOC / exploitant

**Atténuation :**

- Utiliser des échangeurs à plaques en titane sans contact pour les échanges avec l’eau de baie / mer.

- Ne pas dépendre de petites rivières comme principal puits de chaleur.

- Inclure des refroidisseurs secs comme solution de secours et soutien de mi-saison.

- Inclure des alarmes pour le débit, la température, la pression et le ΔT.

- Définir un processus d’écrêtement pour les charges de travail non critiques.

- Maintenir des pompes, contrôles et composants d’échangeurs de chaleur en stock.

**Prochaines preuves nécessaires :**

- Évaluation de la source froide.

- Conception de la prise d’eau / exutoire.

- Examen de l’encrassement biologique / corrosion.

- Dimensionnement des refroidisseurs secs.

- Plan de maintenance.

- Procédure d’intervention en cas de panne de refroidissement.

### 14. Risque lié à la demande des locataires et au taux d’occupation

**Risque :  
**Les locataires de calcul pourraient ne pas s’engager sur une capacité, une durée ou des conditions de bail suffisantes pour soutenir l’économie du pilote.

**Pourquoi c’est important :  
**L’occupation des plateformes et les revenus locatifs sont essentiels au modèle commercial. Les plateformes sous-utilisées créent tout de même des coûts fixes d’infrastructure.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Ouvert  
**Responsable principal :** Responsable commercial  
**Responsables de soutien :** Kristal Farms, investisseur en infrastructure, partenaires de calcul

**Atténuation :**

- Prioriser les locataires qui valorisent l’énergie renouvelable, la réutilisation de chaleur, la location en boîte noire et le déploiement modulaire.

- Offrir des baux de plateformes par phases plutôt que de surconstruire.

- Dimensionner la première plateforme selon la demande contractée.

- Éviter l’expansion spéculative de capacité avant la validation des locataires et de l’utilisation de chaleur.

- Séparer la location de calcul des éventuels usages Kristals d’intérêt public.

**Prochaines preuves nécessaires :**

- Pipeline de locataires.

- Lettres d’intérêt.

- Exigences de capacité.

- Exigences de SLA.

- Préférences de durée de bail.

- Critères d’admissibilité des locataires.

### 15. Risque lié au modèle commercial et aux SLA

**Risque :  
**Les attentes des partenaires concernant la tarification, les garanties de service, la valeur de la chaleur, le comptage, l’écrêtement et les responsabilités pourraient ne pas être alignées.

**Pourquoi c’est important :  
**Un partenaire peut contribuer du capital, du terrain, de l’électricité, de la fibre, de l’équipement, de la location de capacité ou un soutien communautaire. Des rôles flous peuvent retarder ou faire dérailler les négociations.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Ouvert  
**Responsable principal :** Responsable commercial / juridique  
**Responsables de soutien :** Kristal Farms, partenaire service public, investisseur, locataire de calcul, partenaire communautaire

**Atténuation :**

- Définir tôt les types de partenaires et les demandes spécifiques.

- Garder les données économiques sensibles sous NDA.

- Définir les frontières de services mesurés : électricité, refroidissement, exportation de chaleur, fibre, accès aux plateformes.

- Définir la réversibilité et les responsabilités de fin de bail.

- Éviter plusieurs niveaux de SLA jusqu’à ce que le modèle opérationnel les exige.

- Documenter séparément le calcul de surplus en mode meilleur effort et le service de plateforme garanti.

**Prochaines preuves nécessaires :**

- Ébauche de feuille de conditions.

- Aperçu des SLA.

- Plan de comptage.

- Concept de tarification / récupération des coûts de chaleur.

- Exigences d’assurance.

- Plan de retrait en fin de bail.

### 16. Risque lié à la location en boîte noire et aux frontières des données

**Risque :  
**Les locataires pourraient ne pas faire confiance aux frontières imposées par l’hôte, ou les hôtes / partenaires communautaires pourraient s’attendre à une visibilité incompatible avec la location en boîte noire.

**Pourquoi c’est important :  
**Le modèle de calcul du projet exige la confidentialité des locataires. L’hôte doit surveiller l’infrastructure physique sans accéder aux données des locataires, aux journaux, au contenu des modèles ou aux charges utiles des paquets.

**Probabilité :** Faible à moyenne  
**Impact :** Élevé  
**Statut :** Atténuation active  
**Responsable principal :** Responsable sécurité / location  
**Responsables de soutien :** exploitant NOC, locataire, conseiller juridique

**Atténuation :**

- Définir clairement les indicateurs visibles par l’hôte : énergie, ΔT / débit de refroidissement, disponibilité, bande passante agrégée et alarmes techniques.

- Exclure explicitement les journaux des locataires, les données applicatives, le contenu des modèles, la télémétrie interne et l’inspection des charges utiles de paquets.

- Offrir l’attestation matérielle en option selon les besoins des locataires.

- Séparer les activités communautaires / Kristals des charges de travail locataires en boîte noire.

- Utiliser des rapports anonymisés et agrégés pour les tableaux de bord publics.

**Prochaines preuves nécessaires :**

- Annexe sur les frontières des données.

- Architecture de sécurité.

- Politique de contrôle d’accès NOC.

- Clause de confidentialité locataire.

- Clause optionnelle d’attestation.

- Processus de notification d’incident.

### 17. Risque lié aux coûts de construction et aux fournisseurs modulaires

**Risque :  
**Les modules en conteneurs, plateformes, skids de refroidissement, matériaux de boucle de chaleur, composants fibre et travaux de construction éloignés pourraient coûter plus cher ou prendre plus de temps que prévu.

**Pourquoi c’est important :  
**Les travaux côtiers éloignés au Labrador peuvent être exposés aux délais des fournisseurs, aux contraintes d’expédition, au manque de main-d’œuvre spécialisée et à l’escalade des coûts des matériaux.

**Probabilité :** Moyenne  
**Impact :** Élevé  
**Statut :** Ouvert  
**Responsable principal :** Responsable EPC / approvisionnement  
**Responsables de soutien :** fournisseur de centre de données modulaire, partenaire logistique, investisseur

**Atténuation :**

- Utiliser des interfaces modulaires standard.

- Éviter les conceptions personnalisées sauf si nécessaires pour le climat froid ou la capture de chaleur.

- Préqualifier les fournisseurs de conteneurs, de refroidissement, d’alimentation, de contrôles et de composants fibre.

- Inclure des contingences pour le ravitaillement maritime, les délais météo et les pièces de rechange.

- Commencer par une plateforme pilote avant les plateformes d’expansion.

**Prochaines preuves nécessaires :**

- Liste restreinte de fournisseurs.

- Devis budgétaires.

- Calendrier des délais d’approvisionnement.

- Coûts d’expédition et d’installation.

- Stratégie de pièces de rechange.

- Provision pour risque de construction.

### 18. Risque lié aux opérations, au personnel et à la maintenance

**Risque :  
**Le projet pourrait ne pas disposer de suffisamment d’opérateurs locaux formés, de techniciens, de soutien NOC ou de capacité de maintenance pour assurer une exploitation fiable.

**Pourquoi c’est important :  
**Le modèle dépend d’une grande disponibilité, d’une livraison sécuritaire de chaleur et de la confiance communautaire. La capacité locale fait aussi partie de la thèse des bénéfices communautaires.

**Probabilité :** Moyenne  
**Impact :** Moyen  
**Statut :** Ouvert  
**Responsable principal :** Responsable des opérations  
**Responsables de soutien :** partenaire communautaire, fournisseur de formation, fournisseurs, exploitant NOC

**Atténuation :**

- Définir tôt les rôles locaux.

- Construire un programme de formation pour l’exploitation des plateformes, la surveillance de la boucle de chaleur, la sécurité et le soutien fibre / NOC de base.

- Utiliser la surveillance à distance pour l’encadrement spécialisé.

- Maintenir un inventaire local de pièces de rechange.

- Utiliser des accords de service fournisseurs pour les systèmes critiques.

- Suivre publiquement les emplois locaux et les heures de formation.

**Prochaines preuves nécessaires :**

- Modèle de dotation.

- Plan de formation.

- Budget O&M.

- Contrats de soutien fournisseurs.

- Liste de pièces de rechange.

- Procédures de sécurité.

### 

### 19. Risque lié à la preuve des bénéfices publics et au tableau de bord

**Risque :  
**Le projet pourrait échouer à démontrer la valeur communautaire d’une manière simple, fiable et auditable.

**Pourquoi c’est important :  
**Kristal Farms dépend de bénéfices visibles : chaleur livrée, diesel évité, emplois locaux, formation, améliorations de la fibre, disponibilité et production de serre. Si ces éléments ne sont pas mesurés et rapportés, la confiance pourrait diminuer.

**Probabilité :** Faible à moyenne  
**Impact :** Moyen  
**Statut :** Atténuation active  
**Responsable principal :** Responsable indicateurs / rapports  
**Responsables de soutien :** conseil de projet, comité de chaleur, comité environnemental, exploitant

**Atténuation :**

- Utiliser une fiche de suivi publique stable.

- Publier des mises à jour mensuelles du tableau de bord.

- Tenir des examens trimestriels avec les organes de gouvernance.

- Publier des rapports annuels.

- Centraliser les définitions des indicateurs dans le tableau de bord des mesures et le cadre d’audit.

- Utiliser un audit indépendant lorsque pertinent.

**Prochaines preuves nécessaires :**

- Définitions finales des indicateurs.

- Maquette du tableau de bord.

- Plan de propriété des données.

- Cadence d’examen.

- Plan d’audit.

- Format de rapport public.

### 

### 20. Risque de réplication au-delà de Nain

**Risque :  
**Un modèle qui fonctionne à Nain pourrait ne pas se répliquer facilement à Hopedale, Makkovik, Postville, Rigolet ou dans d’autres communautés côtières du Labrador.

**Pourquoi c’est important :  
**La logique d’expansion est la réplication côtière, mais chaque communauté peut différer en matière de ressource hydroélectrique, d’accès portuaire, de tracé fibre, de demande de chaleur, de gouvernance, de permis et de priorités locales.

**Probabilité :** Moyenne  
**Impact :** Moyen  
**Statut :** Liste de surveillance  
**Responsable principal :** Responsable stratégie Kristal Farms  
**Responsables de soutien :** partenaires locaux, partenaires hydro / fibre, partenaire communautaire / gouvernemental

**Atténuation :**

- Traiter Nain comme première cible et site d’apprentissage, et non comme preuve d’adéquation universelle.

- Construire une fiche d’évaluation de réplication.

- Séparer l’architecture standardisée des décisions propres à chaque site.

- Ne pas s’engager envers des communautés d’expansion avant la présélection locale et le consentement.

- Capturer les apprentissages de la plateforme pilote, de la boucle de chaleur, de la gouvernance et de la validation fibre.

**Prochaines preuves nécessaires :**

- Matrice de présélection communauté par communauté.

- Comparaison hydro / fibre / port / demande de chaleur.

- Feuille de route d’engagement local.

- Journal des hypothèses de réplication.

- Critères de décision d’expansion.

## 

## 5. Points de décision liés à la fermeture des risques

| **Point** | **Décision**                  | **Preuves minimales requises**                                                                            |
|-----------|-------------------------------|-----------------------------------------------------------------------------------------------------------|
| Point A   | Intérêt des partenaires       | Rôles des partenaires, structure préférée, allocation préliminaire des risques                            |
| Point B   | Données de site validées      | Données hydroélectriques, inventaire cartographique, présélection port / fibre / demande de chaleur       |
| Point C   | Processus communautaire lancé | Parcours CLPE, plan d’engagement, principes de gouvernance                                                |
| Point D   | Économie du pilote approuvée  | Intérêt des locataires, fourchette de capex, plan d’utilisation de chaleur, aperçu des SLA                |
| Point E   | Préparation à la construction | Permis, interconnexion, fibre, logistique, devis fournisseurs, plan O&M                                   |
| Point F   | Lancement opérationnel        | Boucle de chaleur mise en service, interfaces de plateformes, NOC, tableau de bord, procédures d’incident |

## 6. Risques qui ne devraient pas être cachés

Les enjeux suivants devraient être énoncés clairement dans les conversations avec les partenaires :

1.  Les données hydroélectriques et fibre doivent être validées avant le dimensionnement final.

2.  Nain est la première cible, et non un site final garanti tant que la diligence raisonnable n’est pas terminée.

3.  Le consentement communautaire et le CLPE sont des exigences de passage.

4.  La structure de gouvernance n’est pas entièrement finalisée et devrait être coconçue.

5.  Les projections financières ne devraient pas être présentées comme validées tant que les données des partenaires ne sont pas disponibles.

6.  La réutilisation de chaleur est centrale, mais l’utilisation saisonnière de la chaleur doit être soigneusement conçue.

7.  Le modèle devrait éviter la logique de mégaprojets intérieurs et les hypothèses de longue transmission haute tension.

8.  La location en boîte noire limite ce que l’hôte peut voir, même lorsque l’hôte est responsable de l’infrastructure physique.

## 7. Plan immédiat de diligence raisonnable

### Technique

- Préfaisabilité hydroélectrique.

- Concept d’interconnexion moyenne tension.

- Confirmation du tracé et de la capacité fibre.

- Évaluation portuaire et du ravitaillement maritime.

- Évaluation de la source froide et du ΔT.

- Inventaire des charges thermiques des bâtiments publics et des habitations voisines.

- Conception du concept de plateforme pilote.

### Communauté et gouvernance

- Plan d’engagement initial.

- Carte du processus CLPE.

- Priorités de bénéfices communautaires.

- Ébauche de modèle de gouvernance.

- Processus de griefs et d’escalade.

- Concept de tableau de bord public.

### Commercial

- Demande aux partenaires et matrice des rôles.

- Pipeline de locataires.

- Frontière des SLA.

- Catégories préliminaires de capex et d’opex.

- Matrice d’allocation des risques.

- Plan de salle de données sous NDA.

## 8. Carte de responsabilité des risques

| **Domaine de risque**              | **Responsable principal**                   |
|------------------------------------|---------------------------------------------|
| Ressource hydroélectrique          | Partenaire hydroélectrique / service public |
| Sélection de site                  | Kristal Farms + conseiller en ingénierie    |
| Interconnexion moyenne tension     | Partenaire service public / électrique      |
| Logistique                         | Partenaire maritime / logistique            |
| Fibre                              | Partenaire télécom / fibre                  |
| CLPE et consentement communautaire | Partenaire communautaire / gouvernemental   |
| Gouvernance                        | Responsable gouvernance / juridique         |
| Permis environnementaux            | Responsable environnement                   |
| Système thermique                  | Partenaire du système thermique             |
| Demande des locataires             | Responsable commercial                      |
| SLA et modèle de bail              | Responsable commercial / juridique          |
| Frontière boîte noire              | Responsable sécurité / location             |
| Construction                       | Responsable EPC / approvisionnement         |
| Opérations                         | Exploitant du site                          |
| Tableau de bord et audit           | Responsable indicateurs / rapports          |

## 9. Questions ouvertes pour les partenaires

1.  Quel partenaire devrait posséder le développement hydroélectrique ou l’achat de production hydroélectrique ?

2.  Quel partenaire possède la connexion moyenne tension et le poste électrique du village ?

3.  Qui possède et exploite l’aire des plateformes de calcul ?

4.  Qui possède la boucle de chaleur et les sous-stations de bâtiments ?

5.  Qui possède l’architecture fibre / NOC ?

6.  Quels bâtiments publics sont les premiers utilisateurs prioritaires de chaleur ?

7.  Quel est le processus local de consentement, d’examen et d’approbation de l’accord de bénéfices ?

8.  Quelles données peuvent être partagées avant NDA, et lesquelles doivent être placées dans la salle de données ?

9.  Quelles charges de travail locataires sont acceptables pour la première plateforme pilote ?

10. Quels risques doivent être fermés avant qu’un partenaire puisse émettre une lettre d’intention ?

## 10. Base documentaire

Ce registre des risques est fondé sur le corpus actuel de Kristal Farms, en particulier :

- Kristal Farms — Plan de recyclage de la chaleur.

- Document de référence interne Kristal Farms.

- Kristal Farms — Avantage de coût et justification stratégique.

- Documentation Kristal Farms.

- Potentiel hydroélectrique isolé au Nunavik et au Labrador.

- PDF de synthèse de style article Kristal Farms.

- Fichiers de contexte sur les fournisseurs et les centres de données modulaires.

Le registre des risques devrait être mis à jour après chaque grande conversation avec des partenaires, étude technique, rencontre communautaire et étape de validation des données de site.
