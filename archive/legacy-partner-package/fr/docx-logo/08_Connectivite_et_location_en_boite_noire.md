---
source_file: "08_Connectivite_et_location_en_boite_noire.docx"
repository_status: "formatted French partner deliverable / compare against EN Markdown authority"
extraction_method: "pandoc"
extracted_on: "2026-08-17"
---

> **Repository note:** This Markdown is a searchable extraction of the supplied DOCX. It is not automatically authoritative. Validate claims and citations before promotion into partner-facing material.

# **Kristal Farms — Connectivité et location en boîte noire**

**Statut du document :** ébauche destinée aux partenaires  
**Ensemble documentaire :** Documentation partenaire de Kristal Farms  
**Géographie principale :** côte du Labrador, avec Nain comme première communauté cible  
**Version :** v0.1  
**Date :** 2 mai 2026

[**Kristal Farms — Connectivité et location en boîte noire 1**](#kristal-farms-connectivité-et-location-en-boîte-noire)

> [1. Objet 2](#objet)
>
> [2. Position centrale 3](#position-centrale)
>
> [3. Pourquoi la connectivité est importante 4](#pourquoi-la-connectivité-est-importante)
>
> [4. Architecture de connectivité 5](#architecture-de-connectivité)
>
> [4.1 Tronc régional 5](#tronc-régional)
>
> [4.2 Centre d’opérations réseau 5](#centre-dopérations-réseau)
>
> [4.3 Distribution locale 6](#distribution-locale)
>
> [4.4 Point de remise au niveau de la plateforme 6](#point-de-remise-au-niveau-de-la-plateforme)
>
> [5. Modèle de location en boîte noire 7](#modèle-de-location-en-boîte-noire)
>
> [5.1 Définition 7](#définition)
>
> [5.2 Pourquoi le modèle est nécessaire 7](#pourquoi-le-modèle-est-nécessaire)
>
> [6. Frontière de responsabilité 8](#frontière-de-responsabilité)
>
> [6.1 Responsabilités de Kristal Farms / de l’hôte 8](#responsabilités-de-kristal-farms-de-lhôte)
>
> [6.2 Responsabilités du locataire 8](#responsabilités-du-locataire)
>
> [6.3 Responsabilités partagées 9](#responsabilités-partagées)
>
> [7. Ce que l’hôte voit 10](#ce-que-lhôte-voit)
>
> [7.1 Indicateurs électriques 10](#indicateurs-électriques)
>
> [7.2 Indicateurs de refroidissement et de chaleur 10](#indicateurs-de-refroidissement-et-de-chaleur)
>
> [7.3 Indicateurs de santé réseau 11](#indicateurs-de-santé-réseau)
>
> [7.4 Indicateurs de sécurité et de site 11](#indicateurs-de-sécurité-et-de-site)
>
> [8. Ce que l’hôte ne voit jamais 12](#ce-que-lhôte-ne-voit-jamais)
>
> [9. Confidentialité réseau et séparation du trafic 13](#confidentialité-réseau-et-séparation-du-trafic)
>
> [9.1 Aucune inspection approfondie des paquets 13](#aucune-inspection-approfondie-des-paquets)
>
> [9.2 Segmentation du trafic 13](#segmentation-du-trafic)
>
> [9.3 Chiffrement 13](#chiffrement)
>
> [10. Attestation matérielle optionnelle 14](#attestation-matérielle-optionnelle)
>
> [11. Concept d’accord de niveau de service 15](#concept-daccord-de-niveau-de-service)
>
> [11.1 Un seul service standard, avec calcul excédentaire en mode meilleur effort 15](#un-seul-service-standard-avec-calcul-excédentaire-en-mode-meilleur-effort)
>
> [11.2 Domaines couverts par l’accord de niveau de service 15](#domaines-couverts-par-laccord-de-niveau-de-service)
>
> [11.3 Clause d’exploitation priorisant la chaleur 16](#clause-dexploitation-priorisant-la-chaleur)
>
> [12. Tableau de bord public et agrégation des données 17](#tableau-de-bord-public-et-agrégation-des-données)
>
> [13. Essais d’acceptation 18](#essais-dacceptation)
>
> [13.1 Essais d’acceptation de la connectivité 18](#essais-dacceptation-de-la-connectivité)
>
> [13.2 Essais d’acceptation de la boîte noire 18](#essais-dacceptation-de-la-boîte-noire)
>
> [13.3 Essais d’acceptation de l’interface thermique 19](#essais-dacceptation-de-linterface-thermique)
>
> [14. Sécurité, conformité et audit 20](#sécurité-conformité-et-audit)
>
> [14.1 Posture de sécurité 20](#posture-de-sécurité)
>
> [14.2 Audit annuel 20](#audit-annuel)
>
> [14.3 Accès légal et demandes de données 21](#accès-légal-et-demandes-de-données)
>
> [15. Modèle de confiance communautaire et locataire 22](#modèle-de-confiance-communautaire-et-locataire)
>
> [16. Points de conception ouverts 23](#points-de-conception-ouverts)
>
> [17. Demande de décision aux partenaires 24](#demande-de-décision-aux-partenaires)
>
> [18. Résumé 25](#résumé)

## 

## 1. Objet

Ce document explique comment Kristal Farms exporte des résultats de calcul par fibre optique tout en protégeant la confidentialité des locataires au moyen d’un modèle de location en boîte noire.

Le projet repose sur une frontière opérationnelle simple :

> Kristal Farms fournit l’infrastructure physique : électricité, refroidissement, exportation de chaleur, connectivité fibre, accès aux plateformes, comptage, systèmes de sécurité et opérations de site.  
> Le locataire contrôle l’environnement de calcul : matériel, système d’exploitation, pile logicielle, modèles, données applicatives, journaux et opérations de charge de travail.

L’hôte n’a pas besoin d’accéder aux données du locataire pour exploiter le site. Il n’a besoin que des indicateurs physiques et de santé réseau nécessaires au bon fonctionnement de l’alimentation électrique, du refroidissement, de la récupération de chaleur, de la fibre, de la sécurité et des systèmes de reddition de comptes communautaires.

Ce document s’adresse aux locataires de calcul, aux partenaires télécom/fibre, aux investisseurs en infrastructure, aux partenaires communautaires et gouvernementaux, ainsi qu’aux réviseurs techniques de diligence raisonnable.

## 

## 2. Position centrale

Kristal Farms n’est pas principalement un projet d’exportation d’électricité. C’est un projet d’exportation de calcul.

Le modèle de la côte du Labrador repose sur :

1.  Une électricité hydroélectrique ou renouvelable locale alimentant des plateformes de calcul près du village.

2.  Des conteneurs de données situés à proximité des utilisateurs de chaleur plutôt qu’à distance, près d’un barrage.

3.  La récupération de chaleur résiduelle pour les bâtiments publics, les maisons, l’eau chaude sanitaire et l’utilisation saisonnière en serre.

4.  L’exportation des résultats de calcul par fibre plutôt que l’exportation d’électricité par de longues lignes de transport à haute tension.

5.  Des charges de travail de locataires exploitées selon un modèle en boîte noire.

6.  Des opérations communautaires et hôtes limitées à la surveillance de l’infrastructure physique.

Cette approche permet au projet de conserver localement la valeur thermique tout en envoyant uniquement les données et les résultats de calcul vers des clients externes.

## 

##  

## 

## 3. Pourquoi la connectivité est importante

La connectivité est un système critique pour Kristal Farms, car le modèle d’affaires dépend de l’exportation de travail numérique plutôt que du transport massif d’électricité.

Le projet évite le modèle conventionnel consistant à construire de longues lignes à haute tension entre un site de production éloigné et des centres de charge situés au sud. Il utilise plutôt une connexion électrique locale plus courte pour alimenter des plateformes de calcul dans le village ou à proximité, puis relie ces plateformes aux marchés externes par fibre optique.

La couche de connectivité joue donc trois rôles :

1.  **Exportation du calcul des locataires  
    **Transport des données des locataires, des sorties de modèles, des résultats de lots, du trafic de plan de contrôle, des signaux de surveillance et des services orientés client entre le site de la côte du Labrador et les réseaux externes.

2.  **Opérations du site  
    **Soutien au centre d’opérations réseau, à la surveillance à distance, à l’accès de maintenance, aux alarmes, à la télémétrie, au contrôle des changements et à la réponse aux incidents.

3.  **Valeur communautaire  
    **Amélioration de la résilience du réseau local et possibilité d’extensions de service vers des installations communautaires telles que la clinique, l’école, le bureau municipal, les services d’urgence ou les bureaux de gouvernance du projet, lorsque cela est approprié.

Le système de fibre doit être traité comme une infrastructure critique, et non comme une utilité secondaire.

## 4. Architecture de connectivité

### 4.1 Tronc régional

L’architecture privilégiée est un tronc fibre à haute capacité reliant le site à un concentrateur régional, comme Goose Bay ou un autre point d’agrégation sud validé.

Le tronc régional devrait être conçu pour :

- le transport de données à haute capacité ;

- un tracé physiquement protégé lorsque possible ;

- une responsabilité claire en matière de propriété et de maintenance ;

- des engagements de réparation définis ;

- des procédures documentées d’épissure, de brassage et d’accès ;

- l’expansion future de la capacité ;

- la compatibilité avec le multiplexage dense en longueur d’onde lorsque l’échelle le justifie.

Le tronc devrait être validé avant qu’une plateforme pilote soit engagée commercialement. Un projet peut commencer avec une capacité limitée, mais la trajectoire d’expansion doit être claire avant de conclure des engagements plus importants avec des locataires.

### 4.2 Centre d’opérations réseau

Kristal Farms devrait inclure un petit centre d’opérations réseau au site portuaire ou dans une cour d’infrastructure en bordure du village.

Le centre d’opérations réseau est le point de contrôle opérationnel pour :

- la terminaison de fibre ;

- les répartiteurs optiques ;

- le brassage ;

- le routage et la commutation ;

- la surveillance environnementale ;

- la surveillance des liens ;

- la gestion des alarmes ;

- l’accès distant sécurisé ;

- le contrôle des changements ;

- la coordination des incidents ;

- les journaux d’accès physique ;

- les flux du tableau de bord communautaire.

Le centre d’opérations réseau devrait disposer, lorsque possible, d’alimentations électriques redondantes, d’une alimentation de secours pour les équipements réseau critiques, d’un accès contrôlé et d’une procédure opérationnelle documentée pour les fenêtres de maintenance et les interventions d’urgence.

### 4.3 Distribution locale

À partir du centre d’opérations réseau, des liaisons fibre locales se connectent à :

- des plateformes de calcul ;

- le bureau d’exploitation du projet ;

- la centrale thermique ou la station d’échangeurs de chaleur, si elle est séparée ;

- les systèmes de tableau de bord public ;

- les installations communautaires pertinentes, lorsqu’elles font partie de l’ensemble de bénéfices convenu.

Chaque plateforme de calcul devrait recevoir un point de remise réseau clairement défini. La conception privilégiée est une connectivité double A/B par plateforme, chaque chemin se terminant sur des commutateurs distincts ou des ports logiquement indépendants. Lorsque cela est possible, une diversité de routage devrait être introduite afin de réduire le risque de point de défaillance unique.

### 4.4 Point de remise au niveau de la plateforme

Le point de remise standard de la plateforme devrait inclure :

- des ports fibre étiquetés ;

- un point de démarcation physique ;

- la responsabilité de brassage côté locataire ;

- la responsabilité de brassage côté hôte ;

- les types de connecteurs acceptés ;

- l’allocation de bande passante ou la capacité engagée ;

- la frontière de surveillance ;

- le comportement de basculement ;

- les contacts d’escalade ;

- le processus de fenêtre de maintenance.

Le point de remise doit être assez simple pour permettre un déploiement modulaire, mais suffisamment strict pour soutenir l’auditabilité et l’application des engagements de niveau de service.

## 5. Modèle de location en boîte noire

### 5.1 Définition

La location en boîte noire signifie que l’hôte exploite l’infrastructure du site autour du conteneur du locataire sans accéder aux données, aux logiciels ou à l’environnement de calcul interne du locataire.

Le conteneur du locataire est traité comme une unité opérationnelle opaque. Kristal Farms fournit la plateforme et les services jusqu’à l’interface convenue. Le locataire exploite tout ce qui se trouve à l’intérieur de cette frontière.

L’hôte peut mesurer l’électricité, le refroidissement, le transfert de chaleur, l’état des liens et la bande passante agrégée. L’hôte ne peut pas inspecter le contenu du locataire, ses jeux de données, ses poids de modèles, ses journaux applicatifs, les charges utiles des paquets, son code propriétaire ou sa logique d’affaires.

### 5.2 Pourquoi le modèle est nécessaire

Ce modèle est nécessaire parce que Kristal Farms sert plusieurs groupes de parties prenantes ayant des intérêts différents :

- les locataires de calcul ont besoin de confidentialité et de contrôle commercial ;

- les communautés ont besoin d’une infrastructure transparente et d’un rapport clair sur les bénéfices ;

- les investisseurs ont besoin d’opérations mesurées et auditables ;

- les services publics ont besoin d’interfaces électriques et thermiques sécuritaires ;

- les partenaires télécom ont besoin d’une démarcation réseau claire ;

- les gouvernements ont besoin d’un cadre crédible en matière de confidentialité et de responsabilité.

La location en boîte noire permet à ces intérêts de coexister. L’hôte peut prouver que le site fonctionne de manière sécuritaire et qu’il apporte une valeur communautaire sans devoir accéder aux charges de travail privées des locataires.

## 

## 6. Frontière de responsabilité

### 6.1 Responsabilités de Kristal Farms / de l’hôte

Kristal Farms, ou l’exploitant/hôte désigné du site, est responsable de l’infrastructure physique et du côté utilités, notamment :

- les opérations de la cour de plateformes ;

- le contrôle d’accès physique ;

- la sécurité périmétrique ;

- la livraison d’électricité au niveau de la plateforme ;

- le comptage électrique ;

- l’interface de refroidissement ;

- l’interface d’exportation de chaleur ;

- le point de remise fibre ;

- la surveillance de disponibilité réseau ;

- les alarmes environnementales ;

- les systèmes incendie et sécurité à la frontière du site ;

- la réponse aux incidents au niveau du site ;

- la préparation des données du tableau de bord public ;

- la coordination de la maintenance ;

- le rapport d’infrastructure destiné à la communauté.

L’hôte coordonne également avec l’exploitant du système thermique, le partenaire fibre, le partenaire de service public, les organismes communautaires et les services d’urgence.

### 6.2 Responsabilités du locataire

Le locataire est responsable de l’environnement de calcul à l’intérieur de sa frontière en boîte noire, notamment :

- les serveurs détenus ou contrôlés par le locataire ;

- les systèmes d’exploitation ;

- la pile de virtualisation ou d’orchestration ;

- les cadres d’IA ;

- les poids de modèles ;

- le code applicatif ;

- les données du locataire ;

- le contrôle d’accès à l’intérieur de l’environnement du locataire ;

- le chiffrement du locataire ;

- les pratiques de sauvegarde du locataire ;

- la cybersécurité du locataire ;

- la planification des charges de travail du locataire ;

- les obligations de conformité du locataire ;

- la surveillance interne du locataire ;

- les relations clients du locataire.

Si un locataire exige une posture de sécurité plus élevée, par exemple une attestation matérielle, de l’informatique confidentielle ou des garanties d’isolement supplémentaires, ces exigences devraient être précisées dans le bail ou l’annexe de niveau de service.

### 6.3 Responsabilités partagées

Certains domaines nécessitent une coordination opérationnelle partagée :

- les fenêtres de maintenance ;

- les arrêts d’urgence ;

- le basculement fibre ;

- la mise en service et les essais d’acceptation des plateformes ;

- les contraintes d’exploitation priorisant la chaleur ;

- les incidents environnementaux ;

- la notification d’incidents de cybersécurité ;

- l’accès physique à un conteneur de locataire ;

- les demandes d’accès légal, le cas échéant ;

- le démantèlement et le retrait en fin de bail.

Ces responsabilités partagées doivent être documentées avant le début des opérations commerciales.

## 7. Ce que l’hôte voit

L’hôte ne voit que les indicateurs d’infrastructure nécessaires pour exploiter la plateforme de manière sécuritaire et fiable.

### 7.1 Indicateurs électriques

L’hôte peut surveiller :

- les kWh consommés ;

- les kW instantanés ;

- le facteur de puissance ;

- la tension ;

- le courant ;

- les harmoniques, lorsque pertinent ;

- l’état des départs électriques ;

- l’état des disjoncteurs ;

- les événements de qualité de l’alimentation ;

- les consommations anormales ;

- l’état d’énergisation de la plateforme.

Ces indicateurs sont nécessaires à la facturation, à la protection, à la planification du système et à l’exploitation sécuritaire.

### 7.2 Indicateurs de refroidissement et de chaleur

L’hôte peut surveiller :

- la température d’alimentation de la boucle informatique à l’interface hôte ;

- la température de retour de la boucle informatique à l’interface hôte ;

- le débit de la boucle de refroidissement ;

- la pression ;

- le ΔT à travers l’échangeur de chaleur ;

- la chaleur transférée ;

- l’état des pompes ;

- la position des vannes ;

- les seuils d’alarme ;

- l’état du rejet thermique ;

- la chaleur livrée aux bâtiments, au stockage ou aux systèmes de serre.

Ces indicateurs sont nécessaires parce que la récupération de chaleur fait partie du modèle de valeur communautaire du projet.

### 7.3 Indicateurs de santé réseau

L’hôte peut surveiller :

- l’état actif/inactif des liens ;

- l’utilisation agrégée de la bande passante ;

- l’état des ports ;

- le niveau du signal optique ;

- la perte de paquets au niveau du service ;

- la latence vers des points de test définis ;

- la gigue à des fins de santé du service ;

- les événements de basculement ;

- la disponibilité du routage ;

- la disponibilité du tronc ;

- la disponibilité de l’uplink de la plateforme.

L’hôte peut surveiller la performance réseau agrégée, mais pas le contenu du locataire.

### 7.4 Indicateurs de sécurité et de site

L’hôte peut surveiller :

- les alarmes de température à l’interface d’infrastructure ;

- les alarmes fumée/incendie ;

- les alarmes de fuite d’eau ;

- les alarmes de porte/contact lorsque convenu ;

- les journaux d’accès à la cour ;

- la couverture caméra des zones externes ou partagées ;

- les alarmes environnementales ;

- les indicateurs de tentative d’altération physique ;

- l’état des arrêts d’urgence ;

- les journaux de maintenance.

Ces systèmes protègent le site et la communauté sans donner à l’hôte accès aux données du locataire.

## 8. Ce que l’hôte ne voit jamais

L’hôte ne doit pas accéder, inspecter, collecter ni publier de données confidentielles du locataire.

L’hôte ne voit pas :

- les journaux applicatifs du locataire ;

- les journaux du système d’exploitation du locataire ;

- la télémétrie interne du locataire ;

- les jeux de données du locataire ;

- les poids de modèles du locataire ;

- les prompts du locataire ;

- les sorties du locataire, sauf lorsque celui-ci les publie volontairement ;

- le code du locataire ;

- les renseignements clients du locataire ;

- les charges utiles des paquets ;

- les résultats d’inspection approfondie des paquets ;

- les métadonnées sensibles au-delà des opérations agrégées de service ;

- le contenu des dispositifs de stockage ;

- le contenu de la mémoire ;

- les systèmes d’authentification du locataire ;

- la logique d’affaires du locataire ;

- les tableaux de bord internes de surveillance du locataire.

L’hôte ne convertit pas non plus les charges de travail des locataires en Kristals publics ou en productions de connaissance communautaire, sauf si le locataire y a explicitement consenti et si l’organisme de gouvernance pertinent a approuvé l’utilisation de données publiques ou consenties.

## 9. Confidentialité réseau et séparation du trafic

### 9.1 Aucune inspection approfondie des paquets

Le réseau devrait être exploité sans inspection approfondie des charges utiles des paquets des locataires. L’hôte peut effectuer la surveillance de niveau de service nécessaire pour vérifier si le réseau est disponible et fonctionne dans les plages convenues, mais le contenu du trafic des locataires demeure hors de la frontière de l’hôte.

### 9.2 Segmentation du trafic

Le trafic des locataires devrait être séparé du trafic communautaire, opérationnel et des tableaux de bord publics.

La segmentation recommandée comprend :

- des VLAN distincts ou une segmentation logique équivalente ;

- des domaines de routage propres aux locataires lorsque requis ;

- une frontière pare-feu au point de démarcation convenu ;

- un plan de gestion séparé pour l’infrastructure de l’hôte ;

- aucun identifiant partagé entre les systèmes du locataire et de l’hôte ;

- des listes de contrôle d’accès documentées ;

- un brassage et une configuration soumis au contrôle des changements.

### 9.3 Chiffrement

Les locataires devraient être censés chiffrer leur trafic de bout en bout. Kristal Farms ne devrait pas dépendre d’une visibilité côté hôte sur les données des locataires pour fournir le service réseau.

L’obligation de l’hôte est de livrer la connectivité physique et réseau selon la norme convenue. L’obligation du locataire est de sécuriser ses propres données et applications à l’intérieur de ce chemin réseau.

## 10. Attestation matérielle optionnelle

L’attestation matérielle devrait être offerte comme fonctionnalité contractuelle optionnelle, et non comme exigence par défaut pour tous les locataires.

Certains locataires peuvent exiger des environnements d’exécution de confiance, des fonctionnalités d’informatique confidentielle, des preuves de démarrage sécurisé, une attestation de micrologiciel ou d’autres preuves que l’environnement matériel est dans un état connu avant le déploiement des charges de travail.

La position recommandée est la suivante :

- la location standard utilise l’isolation en boîte noire, le chiffrement par le locataire et la séparation physique/réseau ;

- la location à sécurité accrue peut ajouter une attestation matérielle par contrat ;

- les exigences d’attestation doivent être précisées avant la mise en service de la plateforme ;

- les preuves d’attestation devraient être visibles par le locataire ou par un auditeur convenu, et non être traitées comme un droit de l’hôte d’inspecter les données du locataire ;

- l’attestation ne doit pas affaiblir la frontière en boîte noire.

Cette approche garde le modèle de base simple tout en permettant aux locataires à haute sécurité de négocier des contrôles plus stricts.

## 11. Concept d’accord de niveau de service

### 11.1 Un seul service standard, avec calcul excédentaire en mode meilleur effort

Le modèle initial privilégié est un seul niveau de service standard pour chaque locataire, jusqu’à ses limites contractuelles d’électricité et de connectivité.

Le projet devrait éviter plusieurs niveaux de service complexes lors de la première étape. Un locataire reçoit une enveloppe de service garantie définie par :

- un plafond de puissance contractuel ;

- une plage d’interface de refroidissement ;

- un point de remise fibre ;

- des conditions d’accès à la plateforme ;

- des règles de sécurité ;

- une méthode de comptage ;

- une procédure de fenêtre de maintenance ;

- une procédure de notification de panne ;

- une procédure d’escalade des incidents.

Le calcul excédentaire, y compris les charges de travail liées aux Kristals communautaires ou au traitement par lots non critique, peut être offert en mode meilleur effort en dehors de l’accord de niveau de service formel.

### 11.2 Domaines couverts par l’accord de niveau de service

Un accord complet devrait couvrir :

1.  **Service électrique  
    **Capacité contractuelle, comptage, tolérance de tension, gestion des pannes, maintenance planifiée, réduction d’urgence.

2.  **Service de refroidissement  
    **Débit, plages de température d’alimentation et de retour, interface d’échangeur de chaleur, rejet thermique d’urgence, fenêtres de maintenance, seuils d’alarme.

3.  **Exportation de chaleur  
    **Droit de l’hôte de récupérer la chaleur, mesure de l’énergie thermique, priorité des puits de chaleur communautaires, règle d’exploitation réutiliser → stocker → rejeter.

4.  **Connectivité  
    **Bande passante, cible de disponibilité, attente de basculement, rapport de latence, processus de réparation, avis de maintenance, point de démarcation.

5.  **Accès physique  
    **Autorisation d’accès, règles d’escorte, accès d’urgence, visites de maintenance du locataire, initiation au site, conformité en matière de sécurité.

6.  **Confidentialité  
    **Frontière en boîte noire, accès interdit à l’hôte, absence d’inspection des paquets, absence d’accès aux journaux du locataire, agrégation/anonymisation des indicateurs publics.

7.  **Rapports  
    **Rapports destinés au locataire, rapports opérationnels de l’hôte, champs du tableau de bord communautaire, règles d’agrégation publique.

8.  **Réponse aux incidents  
    **Contacts d’escalade, délais de notification, règles d’arrêt d’urgence, attentes de notification en cybersécurité, coordination des incidents environnementaux.

9.  **Fin de bail  
    **Démantèlement, retrait du matériel du locataire, responsabilité des équipements contenant des données, remise en état de la plateforme, clôture du comptage.

### 11.3 Clause d’exploitation priorisant la chaleur

L’accord de niveau de service devrait reconnaître le principe d’exploitation priorisant la chaleur. La chaleur récupérée des plateformes des locataires fait partie du modèle de bénéfice communautaire local.

Cependant, cette clause doit être rédigée avec soin. Le projet ne devrait pas promettre une réduction illimitée du calcul ni un contrôle arbitraire de l’hôte sur les opérations du locataire. À la place :

- le service contractuel du locataire demeure protégé dans les limites convenues ;

- la demande locale de chaleur et la sécurité de l’infrastructure sont incluses dans les procédures d’exploitation ;

- les charges de travail excédentaires en mode meilleur effort peuvent être modulées en fonction de la demande de chaleur ;

- les conditions d’urgence liées à la sécurité peuvent nécessiter une réduction ;

- le rapport communautaire sur la chaleur repose sur des indicateurs thermiques agrégés, et non sur le contenu des charges de travail du locataire.

## 

## 12. Tableau de bord public et agrégation des données

Kristal Farms devrait maintenir un tableau de bord ou une fiche de performance publique qui rend compte de la valeur du projet sans exposer l’information des locataires.

Les indicateurs liés à la connectivité et à la location peuvent inclure :

- la disponibilité agrégée des liens de plateformes ;

- la disponibilité du tronc ;

- la latence moyenne ou p95 vers un point de test régional défini ;

- le nombre de plateformes actives ;

- l’occupation agrégée des plateformes ;

- le total des kWh consommés par les plateformes ;

- le total de chaleur utile livrée ;

- le facteur d’utilisation de la chaleur ;

- les MWh_th livrés par type de puits ;

- le diesel évité ;

- la disponibilité de la fibre ;

- le nombre d’installations locales connectées ;

- le nombre d’incidents et d’événements de maintenance résolus.

Le tableau de bord public ne devrait jamais inclure les données de charges de travail propres aux locataires, les noms des locataires sans consentement, le contenu des paquets des locataires, les renseignements clients des locataires, l’information sur les modèles des locataires ou les détails de performance propriétaires.

## 13. Essais d’acceptation

Avant l’exploitation commerciale, la connectivité et la location en boîte noire devraient réussir les essais d’acceptation.

### 13.1 Essais d’acceptation de la connectivité

Les essais minimaux devraient inclure :

- tronc installé et testé ;

- liens fibre A/B des plateformes validés ;

- basculement démontré ;

- latence mesurée vers le point régional convenu ;

- bande passante testée au niveau contractuel ;

- niveaux de signal optique documentés ;

- surveillance active au centre d’opérations réseau ;

- escalade des alarmes testée ;

- procédure de maintenance testée ;

- flux du tableau de bord communautaire/public testé.

### 13.2 Essais d’acceptation de la boîte noire

Les essais minimaux devraient inclure :

- l’hôte ne peut pas accéder aux journaux applicatifs du locataire ;

- l’hôte ne peut pas inspecter les charges utiles des paquets du locataire ;

- le trafic du locataire et le trafic communautaire sont séparés ;

- la surveillance de l’hôte est limitée aux indicateurs physiques et de santé réseau convenus ;

- le processus de contrôle d’accès est documenté ;

- les journaux d’accès physique sont actifs ;

- les rapports publics utilisent l’agrégation ou l’anonymisation ;

- le flux d’attestation optionnelle est testé si le locataire l’exige.

### 

### 

###  

### 13.3 Essais d’acceptation de l’interface thermique

Comme la plateforme de calcul se connecte au système thermique, la mise en service devrait aussi vérifier :

- le débit de refroidissement dans la plage prévue ;

- les températures d’alimentation et de retour dans la plage prévue ;

- le ΔT mesuré correctement ;

- le compteur de chaleur mis en service ;

- le rejet thermique d’urgence disponible ;

- les seuils d’alarme configurés ;

- aucune interconnexion hydraulique entre les boucles informatiques et les boucles des bâtiments.

## 14. Sécurité, conformité et audit

### 14.1 Posture de sécurité

Le projet devrait utiliser une posture de sécurité en couches :

- sécurité physique de la cour ;

- accès contrôlé au centre d’opérations réseau ;

- brassage fibre étiqueté et journalisé ;

- contrôle des changements pour la configuration réseau ;

- chiffrement contrôlé par le locataire ;

- segmentation réseau ;

- surveillance côté hôte limitée à l’infrastructure ;

- piste d’audit pour les actions de l’hôte ;

- procédure de réponse d’urgence.

### 14.2 Audit annuel

Un audit indépendant annuel devrait examiner :

- la conformité à la frontière en boîte noire ;

- l’absence d’accès non autorisé aux données des locataires ;

- le périmètre de surveillance de l’hôte ;

- les journaux d’accès au centre d’opérations réseau ;

- les journaux de changement fibre ;

- les journaux d’accès physique ;

- l’agrégation des rapports publics ;

- la conformité à l’exploitation priorisant la chaleur ;

- les dossiers d’incident ;

- les mesures correctives.

L’audit devrait être conçu pour rassurer les locataires, les organismes communautaires, les investisseurs et les partenaires publics.

###  

### 14.3 Accès légal et demandes de données

Toute demande d’accès légal doit être traitée conformément au droit applicable et au cadre du bail.

Comme Kristal Farms n’est pas l’exploitant des systèmes des locataires, la position par défaut devrait être la suivante :

- l’hôte ne détient pas les données du locataire ;

- l’hôte ne peut pas divulguer des données qu’il ne possède pas ;

- les demandes relatives aux données du locataire devraient être dirigées vers le locataire, sauf obligation légale contraire ;

- l’hôte peut divulguer les dossiers physiques qu’il détient uniquement lorsque la loi l’exige ;

- les locataires devraient être avisés lorsque la loi le permet.

Cette section devrait être examinée par un conseiller juridique avant exécution.

## 

## 15. Modèle de confiance communautaire et locataire

Le projet a deux obligations de confiance :

1.  **Confiance des locataires  
    **Les locataires doivent avoir l’assurance que leurs données, modèles, code et opérations commerciales demeurent privés.

2.  **Confiance communautaire  
    **La communauté doit avoir l’assurance que le projet est sécuritaire, bénéfique, transparent et qu’il ne cache pas d’impacts matériels sur l’infrastructure.

Le modèle en boîte noire concilie ces obligations. Les détails des locataires demeurent privés, tandis que la performance de l’infrastructure destinée à la communauté demeure transparente.

L’hôte peut rendre compte publiquement de ce qui importe à la communauté :

- chaleur livrée ;

- diesel évité ;

- disponibilité ;

- fiabilité de la fibre ;

- emplois et formation ;

- bénéfices locaux ;

- performance environnementale ;

- réponse aux incidents.

L’hôte n’a pas besoin de révéler ce que les locataires calculent.

## 

## 16. Points de conception ouverts

Les points suivants devraient être résolus avant l’exécution finale avec les partenaires :

1.  Confirmer le tracé régional de la fibre et la structure de propriété.

2.  Confirmer si le centre d’opérations réseau est exploité par Kristal Farms, un partenaire télécom ou une entité d’exploitation conjointe.

3.  Confirmer les attentes en matière de délais de réparation pour les pannes du tronc et les défaillances de fibre locale.

4.  Définir l’engagement initial de bande passante par plateforme pilote.

5.  Définir l’architecture des liens A/B des plateformes.

6.  Définir si certaines installations communautaires reçoivent des améliorations fibre dans la première phase.

7.  Définir les champs du tableau de bord public et les règles d’agrégation.

8.  Définir la politique de divulgation des noms de locataires.

9.  Définir le forfait optionnel d’attestation matérielle.

10. Définir la portée de l’audit annuel et l’auditeur.

11. Définir les règles d’accès physique aux conteneurs des locataires.

12. Définir avec un conseiller juridique la procédure d’accès légal.

13. Définir le processus de retrait du matériel et de remise en état du site en fin de bail.

##  

##  

## 17. Demande de décision aux partenaires

Les partenaires qui examinent ce document sont invités à aider à confirmer :

1.  Si le tracé fibre proposé peut soutenir les phases pilote et d’expansion.

2.  Si un centre d’opérations réseau local au site portuaire ou en bordure du village est faisable.

3.  Quelle partie devrait exploiter la couche fibre et centre d’opérations réseau.

4.  Quel profil de bande passante et de latence est réaliste pour le premier déploiement à Nain.

5.  Quels engagements de niveau de service sont commercialement soutenables.

6.  Quels bénéfices communautaires de connectivité peuvent être inclus sans promettre excessivement.

7.  Quelles clauses de confidentialité des locataires sont requises pour des baux de calcul bancables.

8.  Si l’attestation matérielle optionnelle devrait être offerte dans le premier contrat locataire ou reportée à des phases ultérieures.

##  

## 

## 

## 18. Résumé

Kristal Farms dépend d’une séparation claire entre l’infrastructure et les opérations de calcul.

L’hôte fournit l’électricité, le refroidissement, l’exportation de chaleur, la fibre, la sécurité physique, le comptage et la transparence locale. Le locataire contrôle le matériel, les logiciels, les modèles, les données et les charges de travail à l’intérieur du conteneur de calcul.

Cette frontière rend le modèle de la côte du Labrador plus facile à présenter aux partenaires. Elle permet au projet de démontrer une valeur communautaire grâce à la chaleur, à la fibre, aux emplois et à des indicateurs transparents, tout en préservant la confidentialité exigée par les locataires de calcul sérieux.

Le résultat est un modèle opérationnel pratique :

> exporter le calcul par fibre, et non l’électricité ;  
> récupérer la chaleur localement, et non la gaspiller ;  
> exploiter les conteneurs des locataires comme des boîtes noires ;  
> rendre compte de la valeur de l’infrastructure de manière transparente ;  
> garder les données des locataires privées.
