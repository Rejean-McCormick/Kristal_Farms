---
source_file: "06_Architecture_Technique_FR_md.docx"
repository_status: "formatted French partner deliverable / compare against EN Markdown authority"
extraction_method: "pandoc"
extracted_on: "2026-08-17"
---

> **Repository note:** This Markdown is a searchable extraction of the supplied DOCX. It is not automatically authoritative. Validate claims and citations before promotion into partner-facing material.

# 06- Kristal Farms — Architecture technique

**Statut du document :** Version provisoire destinée aux partenaires  
**Dossier :** Documentation partenaire de Kristal Farms  
**Logique du site principal :** Nain d’abord ; réplication sur la côte du Labrador  
**Public cible :** Partenaires d’infrastructure, partenaires de services publics, fournisseurs de centres de données modulaires, partenaires fibre optique, locataires de calcul, réviseurs techniques communautaires et gouvernementaux  
**Objectif :** Expliquer l’architecture technique du modèle Kristal Farms sur la côte du Labrador avec suffisamment de clarté pour la diligence raisonnable des partenaires, sans présenter une spécification d’ingénierie complète.

[**06- Kristal Farms — Architecture technique 1**](#kristal-farms-architecture-technique)

> [1. Résumé technique exécutif 4](#résumé-technique-exécutif)
>
> [2. Principes de conception 5](#principes-de-conception)
>
> [2.1 Implantation axée sur le village 5](#implantation-axée-sur-le-village)
>
> [2.2 Parcours électrique court, pas de longue transmission 5](#parcours-électrique-court-pas-de-longue-transmission)
>
> [2.3 Exporter du calcul, pas des électrons 5](#exporter-du-calcul-pas-des-électrons)
>
> [2.4 Réutiliser → Stocker → Rejeter 5](#réutiliser-stocker-rejeter)
>
> [2.5 Deux circuits étanches 6](#deux-circuits-étanches)
>
> [2.6 Location en boîte noire 6](#location-en-boîte-noire)
>
> [2.7 Expansion modulaire 6](#expansion-modulaire)
>
> [2.8 Réversibilité 6](#réversibilité)
>
> [3. Vue d’ensemble du système 7](#vue-densemble-du-système)
>
> [3.1 Architecture de haut niveau 7](#architecture-de-haut-niveau)
>
> [3.2 Composants physiques principaux 8](#composants-physiques-principaux)
>
> [3.3 Limites fonctionnelles 9](#limites-fonctionnelles)
>
> [4. Architecture du site 10](#architecture-du-site)
>
> [4.1 Emplacement privilégié du site 10](#emplacement-privilégié-du-site)
>
> [4.2 Zones du site 10](#zones-du-site)
>
> [4.3 Accès au site et logistique 11](#accès-au-site-et-logistique)
>
> [4.4 Travaux civils 11](#travaux-civils)
>
> [5. Intégration hydroélectrique locale 12](#intégration-hydroélectrique-locale)
>
> [5.1 Objectif 12](#objectif)
>
> [5.2 Flux d’énergie 12](#flux-dénergie)
>
> [5.3 Priorité d’exploitation 12](#priorité-dexploitation)
>
> [5.4 Production diesel existante 13](#production-diesel-existante)
>
> [5.5 Validation requise 13](#validation-requise)
>
> [6. Courte connexion MT et poste de village 14](#courte-connexion-mt-et-poste-de-village)
>
> [6.1 Alimentation moyenne tension 14](#alimentation-moyenne-tension)
>
> [6.2 Poste de village 14](#poste-de-village)
>
> [6.3 Points de comptage 14](#points-de-comptage)
>
> [6.4 Qualité de l’électricité 15](#qualité-de-lélectricité)
>
> [7. Cour de plateformes de calcul 16](#cour-de-plateformes-de-calcul)
>
> [7.1 Concept de plateforme 16](#concept-de-plateforme)
>
> [7.2 Type de conteneur 16](#type-de-conteneur)
>
> [7.3 Disposition de la cour 16](#disposition-de-la-cour)
>
> [7.4 Logique d’expansion des plateformes 17](#logique-dexpansion-des-plateformes)
>
> [8. Norme d’interface des conteneurs 18](#norme-dinterface-des-conteneurs)
>
> [8.1 Philosophie d’interface 18](#philosophie-dinterface)
>
> [8.2 Interface électrique 18](#interface-électrique)
>
> [8.3 Interface de refroidissement 18](#interface-de-refroidissement)
>
> [8.4 Interface fibre optique 19](#interface-fibre-optique)
>
> [8.5 Contrôles et alarmes 19](#contrôles-et-alarmes)
>
> [8.6 Interface de sécurité physique 20](#interface-de-sécurité-physique)
>
> [9. Architecture de refroidissement 21](#architecture-de-refroidissement)
>
> [9.1 Objectif du refroidissement 21](#objectif-du-refroidissement)
>
> [9.2 Boucle informatique 21](#boucle-informatique)
>
> [9.3 Options de captage de chaleur 21](#options-de-captage-de-chaleur)
>
> [9.4 Échangeurs de chaleur à plaques 22](#échangeurs-de-chaleur-à-plaques)
>
> [9.5 Source froide 22](#source-froide)
>
> [9.6 Refroidisseurs secs 22](#refroidisseurs-secs)
>
> [9.7 Contrôles 23](#contrôles)
>
> [9.8 Essais de mise en service 23](#essais-de-mise-en-service)
>
> [10. Architecture de la boucle de chaleur 24](#architecture-de-la-boucle-de-chaleur)
>
> [10.1 Objectif 24](#objectif-1)
>
> [10.2 Utilisateurs de chaleur 24](#utilisateurs-de-chaleur)
>
> [10.3 Unités d’interface des bâtiments 24](#unités-dinterface-des-bâtiments)
>
> [10.4 Eau chaude sanitaire 24](#eau-chaude-sanitaire)
>
> [10.5 Chaleur pour serre 25](#chaleur-pour-serre)
>
> [10.6 Stockage thermique 25](#stockage-thermique)
>
> [10.7 Métriques de la boucle de chaleur 25](#métriques-de-la-boucle-de-chaleur)
>
> [11. Fibre optique et centre d’exploitation réseau 26](#fibre-optique-et-centre-dexploitation-réseau)
>
> [11.1 Objectif 26](#objectif-2)
>
> [11.2 Fonction du NOC 26](#fonction-du-noc)
>
> [11.3 Architecture fibre 26](#architecture-fibre)
>
> [11.4 Métriques réseau 27](#métriques-réseau)
>
> [11.5 Limite de sécurité réseau 27](#limite-de-sécurité-réseau)
>
> [12. Modèle de location en boîte noire 28](#modèle-de-location-en-boîte-noire)
>
> [12.1 Responsabilité de l’hôte 28](#responsabilité-de-lhôte)
>
> [12.2 Responsabilité du locataire 28](#responsabilité-du-locataire)
>
> [12.3 Ce que l’hôte voit 28](#ce-que-lhôte-voit)
>
> [12.4 Ce que l’hôte ne voit pas 29](#ce-que-lhôte-ne-voit-pas)
>
> [12.5 Attestation matérielle optionnelle 29](#attestation-matérielle-optionnelle)
>
> [13. Exploitation et surveillance 30](#exploitation-et-surveillance)
>
> [13.1 Modèle d’exploitation 30](#modèle-dexploitation)
>
> [13.2 Pile de surveillance 30](#pile-de-surveillance)
>
> [13.3 Métriques d’exploitation principales 30](#métriques-dexploitation-principales)
>
> [13.4 Tableau de bord public 31](#tableau-de-bord-public)
>
> [13.5 Maintenance 32](#maintenance)
>
> [14. Sécurité et contrôles environnementaux 33](#sécurité-et-contrôles-environnementaux)
>
> [14.1 Protection de l’eau sans contact 33](#protection-de-leau-sans-contact)
>
> [14.2 Confinement des fluides 33](#confinement-des-fluides)
>
> [14.3 Contrôle des rejets thermiques 33](#contrôle-des-rejets-thermiques)
>
> [14.4 Sécurité incendie et protection des personnes 33](#sécurité-incendie-et-protection-des-personnes)
>
> [14.5 Bruit 34](#bruit)
>
> [14.6 Climat froid et conditions côtières 34](#climat-froid-et-conditions-côtières)
>
> [15. Phasage 35](#phasage)
>
> [Phase 0 — Alignement technique 35](#phase-0-alignement-technique)
>
> [Phase 1 — Confirmation du site 35](#phase-1-confirmation-du-site)
>
> [Phase 2 — Préfaisabilité électrique et thermique 35](#phase-2-préfaisabilité-électrique-et-thermique)
>
> [Phase 3 — Ingénierie de la plateforme pilote 35](#phase-3-ingénierie-de-la-plateforme-pilote)
>
> [Phase 4 — Déploiement pilote 36](#phase-4-déploiement-pilote)
>
> [Phase 5 — Expansion de la boucle de chaleur 36](#phase-5-expansion-de-la-boucle-de-chaleur)
>
> [Phase 6 — Plateformes supplémentaires 36](#phase-6-plateformes-supplémentaires)
>
> [16. Matrice d’interface des partenaires 37](#matrice-dinterface-des-partenaires)
>
> [17. Lacunes de données techniques 38](#lacunes-de-données-techniques)
>
> [18. Livrables d’ingénierie requis ensuite 39](#livrables-dingénierie-requis-ensuite)
>
> [19. Énoncé de positionnement technique 40](#énoncé-de-positionnement-technique)

## 1. Résumé technique exécutif

Kristal Farms est un modèle d’infrastructure axé d’abord sur le village et d’abord sur la chaleur pour le calcul d’IA modulaire sur la côte du Labrador. Le projet installe des plateformes de calcul conteneurisées près du village, à proximité des bâtiments publics, des habitations, des utilisateurs de chaleur en serre, de la logistique portuaire, du point de terminaison de la fibre optique et des opérations locales. Une courte connexion moyenne tension relie une source hydroélectrique locale à un poste de village. Le calcul est exporté par fibre optique, et non par transport d’électricité sur de longues distances. La chaleur des serveurs est captée et réutilisée localement avant que tout surplus de chaleur ne soit rejeté.

Le modèle technique repose sur cinq interfaces :

1.  **Interface électrique** — service électrique mesuré et adossé à l’hydroélectricité, depuis le poste du village jusqu’à chaque plateforme de calcul.

2.  **Interface de refroidissement** — captage de chaleur en boucle fermée à partir des conteneurs des locataires, au moyen d’échangeurs de chaleur à plaques sans contact.

3.  **Interface thermique** — boucle de chaleur villageoise desservant les bâtiments publics, les habitations, le préchauffage de l’eau chaude sanitaire, le stockage et la demande des serres.

4.  **Interface fibre optique** — service fibre protégé depuis un centre local d’exploitation réseau jusqu’aux plateformes des locataires et à la connectivité régionale.

5.  **Interface d’exploitation** — surveillance côté hôte des seules métriques d’infrastructure physique, tandis que les locataires conservent le contrôle et la confidentialité à l’intérieur de conteneurs en « boîte noire ».

Le modèle n’est pas un campus isolé rattaché à un barrage. L’architecture centrale consiste à amener l’électricité depuis la source hydroélectrique vers le village et à placer les conteneurs là où la chaleur peut être utilisée. La valeur du projet dépend de l’intégration du calcul, de la chaleur, de la fibre optique et de l’infrastructure communautaire.

## 2. Principes de conception

### 2.1 Implantation axée sur le village

La cour de calcul devrait être située au port, à la limite du village ou dans un autre emplacement approprié adjacent au village, plutôt qu’à une prise d’eau ou une centrale hydroélectrique éloignée. Cela réduit la distance entre la chaleur des serveurs et les utilisateurs de chaleur. Cela améliore aussi l’accès pour le transport maritime saisonnier, les opérations, l’intervention d’urgence, le point de terminaison fibre et la visibilité communautaire.

### 2.2 Parcours électrique court, pas de longue transmission

Le projet devrait éviter la création de nouveaux corridors de transport haute tension de longue distance. L’électricité devrait être acheminée au moyen d’une courte alimentation moyenne tension depuis la source hydroélectrique locale vers un poste de village. Cela réduit le coût en capital, la complexité des autorisations, les pertes de ligne et les risques d’échéancier.

### 2.3 Exporter du calcul, pas des électrons

La production du site correspond à des services de données, à de la capacité de calcul et à du travail fondé sur le savoir. Le projet devrait privilégier l’exportation des résultats de calcul par fibre optique plutôt que le transport d’électricité sur de longues distances. C’est un élément central du modèle de la côte du Labrador : utiliser l’énergie localement et déplacer la valeur numériquement.

### 2.4 Réutiliser → Stocker → Rejeter

La chaleur des serveurs est traitée comme un produit utile. La hiérarchie d’exploitation est la suivante :

1\. Réutiliser la chaleur localement

2\. Stocker la chaleur lorsque la demande immédiate est inférieure à l’offre

3\. Rejeter seulement le surplus restant

Le système ne devrait rejeter de la chaleur qu’après avoir servi les charges prioritaires des bâtiments, les charges des serres et le stockage thermique disponible.

### 2.5 Deux circuits étanches

La boucle de refroidissement informatique et la boucle de chaleur du village/des bâtiments demeurent hydrauliquement séparées. La chaleur est transférée au moyen d’échangeurs de chaleur à plaques. Aucun fluide n’est mélangé entre l’équipement des locataires, les bâtiments du village et l’eau environnementale.

### 2.6 Location en boîte noire

L’hôte fournit l’électricité, le refroidissement, la fibre optique, la sécurité du site, le comptage et les opérations physiques. Le locataire contrôle l’intérieur du conteneur, y compris les serveurs, les applications, les données, les journaux, les modèles et la sécurité interne. La surveillance de l’hôte se limite aux métriques d’infrastructure physique.

### 2.7 Expansion modulaire

La capacité devrait croître par l’ajout de plateformes, et non par l’engagement dans un grand campus unique. Chaque plateforme devrait être un module séparé, avec des interfaces civiles, électriques, de refroidissement, de fibre optique, de comptage et de bail standardisées.

### 2.8 Réversibilité

L’infrastructure des plateformes devrait être amovible lorsque possible. Lorsqu’un bail prend fin, un conteneur peut être déconnecté et retiré, laissant une voie contrôlée de remise en état du site. C’est important pour le consentement communautaire, le risque de financement et le déploiement par phases.

## 3. Vue d’ensemble du système

### 3.1 Architecture de haut niveau

Source hydroélectrique locale

\|

\| courte alimentation MT

v

Poste de village / centre énergétique

\|

\| alimentations mesurées

v

Cour de plateformes de calcul près du port / de la limite du village

\|

\| captage de chaleur par boucles informatiques étanches

v

Station centrale d’échange thermique

\|

\| boucle de chaleur villageoise

v

Bâtiments publics / habitations / ECS / serre / stockage

\|

\| exportation de données

v

NOC local -\> concentrateur fibre régional -\> réseaux des locataires

### 3.2 Composants physiques principaux

| **Composant**                               | **Rôle**                                                                                                                                                      |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Source hydroélectrique locale               | Fournit de l’électricité renouvelable pour les charges du village et les plateformes de calcul, sous réserve d’études validées sur la ressource et le réseau. |
| Courte alimentation MT                      | Relie la source hydroélectrique au poste du village sans construction d’un long réseau de transport haute tension.                                            |
| Poste de village                            | Point central de transfert électrique, de protection, de comptage et de distribution.                                                                         |
| Cour de plateformes de calcul               | Cour modulaire clôturée pour les conteneurs des locataires, de préférence près du port ou de la limite du village.                                            |
| Équipement d’interface monté sur plateforme | Fournit le transfert électrique, les ports fibre, la connexion de refroidissement, le comptage de chaleur et les interfaces d’alarme.                         |
| Station centrale d’échange thermique        | Transfère la chaleur des serveurs vers la boucle de chaleur villageoise et gère la priorité de réutilisation, de stockage et de rejet.                        |
| Boucle de chaleur villageoise               | Distribue la chaleur utile aux bâtiments publics, aux habitations, au préchauffage de l’eau chaude sanitaire, au stockage et aux usages de serre.             |
| Interface de source froide                  | Assure le rejet final de chaleur par échange sans contact vers l’eau de mer/de baie ou vers des refroidisseurs secs.                                          |
| Centre d’exploitation réseau                | Héberge la fibre, le routage, le brassage, la surveillance et les systèmes de communication du site.                                                          |
| Tableau de bord d’exploitation              | Suit l’électricité, la chaleur, le refroidissement, la fibre, la disponibilité des plateformes, l’utilisation de la chaleur et les métriques de sécurité.     |

### 3.3 Limites fonctionnelles

L’architecture sépare les responsabilités en trois zones :

| **Zone**                       | **Contrôlée par**                              | **Portée**                                                                                                                      |
|--------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Zone d’infrastructure hôte     | Kristal Farms / entité locale d’exploitation   | Électricité, interfaces de refroidissement, boucle de chaleur, sécurité du site, transfert fibre, surveillance externe.         |
| Zone des conteneurs locataires | Locataire de calcul                            | Serveurs, stockage, systèmes d’exploitation, applications, charges de travail des modèles, chiffrement, télémétrie interne.     |
| Zone de chaleur communautaire  | Opérateur thermique du projet/de la communauté | Allocation de chaleur, unités d’interface des bâtiments, utilisation de chaleur en serre, stockage thermique, rapports publics. |

## 4. Architecture du site

### 4.1 Emplacement privilégié du site

La cour de plateformes de calcul privilégiée est un emplacement adjacent au village offrant :

- un accès pratique au transport maritime saisonnier ou au port ;

- une courte distance jusqu’au poste électrique ;

- une courte distance jusqu’aux utilisateurs de chaleur ;

- une terminaison fibre réalisable ;

- des travaux civils gérables ;

- de l’espace pour l’expansion progressive des plateformes ;

- des conditions acceptables de bruit, d’accès, de drainage, de neige et de séparation de sécurité ;

- une visibilité communautaire sans créer d’effets de nuisance.

Le site n’a pas besoin d’être directement à côté de la centrale hydroélectrique. La centrale fournit l’électricité ; le village fournit le puits thermique, la base d’exploitation, la base logistique et le contexte de bénéfices communautaires.

### 4.2 Zones du site

Le site devrait être planifié comme un ensemble de zones contrôlées :

A. Interface portuaire / logistique

B. Cour de plateformes de calcul

C. Poste électrique et zone d’appareillage de commutation

D. Station d’échange thermique et de pompage

E. Zone de stockage thermique

F. Serre / puits thermique saisonnier

G. Centre d’exploitation réseau

H. Zone de maintenance et de pièces de rechange

I. Portail de sécurité et contrôle d’accès

J. Zones de stockage de neige / drainage / corridors d’accès incendie

### 4.3 Accès au site et logistique

La cour de plateformes devrait permettre la livraison maritime saisonnière de conteneurs et d’équipements majeurs. Les hypothèses de conception devraient inclure :

- des plans standard de manutention et de levage des conteneurs ;

- de l’espace de dépôt pour les fenêtres de livraison ;

- des routes d’accès hivernales définies ;

- un stockage de pièces de rechange pour les pompes, vannes, capteurs, filtres, composants fibre et dispositifs de protection électrique critiques ;

- un accès pour équipement lourd permettant le remplacement des conteneurs ;

- un accès d’urgence pour les interventions incendie, électriques et mécaniques.

### 4.4 Travaux civils

Les travaux civils devraient rester simples et modulaires :

- fondations sur plateformes compactées ou berceaux en acier surélevés adaptés aux conditions locales du sol ;

- drainage conçu pour les cycles gel/dégel et les fortes précipitations ;

- itinéraires de gestion de la neige ;

- confinement autour des équipements au glycol ou à l’eau traitée ;

- périmètre clôturé et portails contrôlés ;

- corridors de service pour l’électricité, la fibre optique et les tuyauteries de chaleur ;

- séparation claire entre les zones publiques et l’infrastructure des locataires.

## 5. Intégration hydroélectrique locale

### 5.1 Objectif

L’intégration hydroélectrique est conçue pour servir les charges de calcul locales sans nécessiter un nouveau long corridor d’exportation haute tension. La source hydroélectrique doit être validée au moyen d’études hydrologiques, de réseau, environnementales et communautaires avant la prise d’engagements de projet.

### 5.2 Flux d’énergie

Source hydroélectrique

-\> production / interconnexion locale

-\> courte alimentation MT

-\> poste de village

-\> alimentations des plateformes, pompes, station thermique, NOC, systèmes auxiliaires

### 5.3 Priorité d’exploitation

Le modèle d’exploitation devrait préserver la sécurité énergétique de la communauté. Les plateformes de calcul ne devraient être ajoutées que lorsqu’il existe une marge de puissance suffisante et une valeur d’utilisation de chaleur. Les charges locales critiques doivent demeurer protégées.

Priorité d’exploitation suggérée :

1.  Charges critiques de la communauté.

2.  Pompes, contrôles et équipements de sécurité du système thermique.

3.  NOC et communications.

4.  Charges de plateformes locataires sous contrat.

5.  Calcul flexible/par lots ou activité de calcul excédentaire.

6.  Couche optionnelle de Kristals/calcul d’intérêt public lorsqu’un surplus d’énergie et une approbation de gouvernance existent.

### 5.4 Production diesel existante

La production diesel existante peut demeurer comme secours d’urgence pour les charges critiques de la communauté et les rares événements de panne. Le projet ne devrait pas dépendre du diesel pour les opérations normales de calcul. La réduction du temps de fonctionnement diesel est une métrique de valeur communautaire et environnementale, et non un substitut à la validation hydroélectrique.

### 5.5 Validation requise

Avant la conception finale, le projet nécessite :

- la validation de la ressource hydroélectrique ;

- le profil saisonnier de production ;

- l’évaluation de la puissance ferme par rapport à la puissance non ferme ;

- une étude de protection et d’interconnexion ;

- une évaluation de la qualité de l’électricité ;

- une analyse du réseau isolé et des échelons de charge, le cas échéant ;

- un plan de priorité des charges d’urgence ;

- un examen environnemental et des autorisations ;

- l’alignement avec le processus communautaire/CLPE.

## 6. Courte connexion MT et poste de village

### 6.1 Alimentation moyenne tension

L’alimentation MT devrait être courte, protégée et conçue pour une expansion par étapes. Elle devrait éviter le déboisement inutile d’emprises et éviter le surdimensionnement en vue de charges futures spéculatives.

Caractéristiques clés de conception :

- sortie mesurée de la source hydroélectrique ;

- protection et sectionnement de l’alimentation ;

- isolement des défauts ;

- mise à la terre et liaison équipotentielle ;

- tracé accessible en hiver ;

- marge pour l’ajout progressif de plateformes ;

- coordination avec l’infrastructure électrique existante du village.

### 6.2 Poste de village

Le poste de village est le centre électrique du projet. Il devrait prendre en charge :

- l’alimentation MT entrante depuis la source hydroélectrique ;

- des transformateurs abaisseurs au besoin ;

- les départs vers les plateformes ;

- les départs vers la station thermique ;

- les départs vers le NOC ;

- les charges auxiliaires de la boucle thermique des bâtiments ;

- le comptage à chaque interface majeure ;

- les relais de protection ;

- la surveillance de la qualité de l’électricité ;

- l’isolement de sécurité ;

- les procédures de consignation/verrouillage ;

- la sécurité physique et la protection contre les intempéries.

### 6.3 Points de comptage

Le comptage minimal devrait inclure :

| **Point de comptage**                         | **Objectif**                                                                    |
|-----------------------------------------------|---------------------------------------------------------------------------------|
| Sortie de la source hydroélectrique           | Établir la production totale et la disponibilité.                               |
| Entrée/sortie de l’alimentation MT            | Suivre les pertes d’alimentation et la qualité de l’électricité.                |
| Jeu de barres du poste                        | Suivre l’équilibre électrique au niveau du site.                                |
| Chaque départ de plateforme                   | Facturer l’électricité au locataire et surveiller le comportement de charge.    |
| Charges auxiliaires de la station thermique   | Suivre les pompes, contrôles, pompe à chaleur d’appoint et refroidisseurs secs. |
| Charge du NOC                                 | Suivre la charge de l’infrastructure de communication.                          |
| Compteurs de livraison de chaleur villageoise | Suivre la chaleur utile livrée par bâtiment ou par puits thermique.             |

### 6.4 Qualité de l’électricité

L’équipement de calcul des locataires est sensible aux événements de tension, aux harmoniques et aux pannes. Le poste et les interfaces de plateformes devraient inclure :

- la surveillance de la tension ;

- l’enregistrement des événements ;

- la surveillance des harmoniques au besoin ;

- la protection contre les surtensions ;

- la coordination sélective ;

- le séquencement progressif du démarrage et de l’arrêt ;

- une responsabilité claire de déclenchement en cas de défaut par plateforme.

## 7. Cour de plateformes de calcul

### 7.1 Concept de plateforme

Chaque plateforme de calcul est une position physique préparée pouvant recevoir un conteneur de centre de données modulaire. La plateforme n’est pas simplement un emplacement de stationnement ; c’est une interface d’infrastructure.

Une plateforme standard devrait fournir :

- un support structurel ;

- un transfert électrique ;

- un transfert de refroidissement ;

- un comptage de chaleur ;

- un transfert fibre ;

- une mise à la terre/liaison équipotentielle ;

- une détection de fuite, le cas échéant ;

- une interface d’alarme ;

- un contrôle d’accès physique ;

- un accès pour intervention incendie ;

- un accès pour le déneigement.

### 7.2 Type de conteneur

L’hypothèse de base est un conteneur de centre de données modulaire standard de 40 pieds ou une unité modulaire équivalente. Les fournisseurs peuvent proposer différents formats, mais chacun doit respecter les exigences d’interface du projet.

### 7.3 Disposition de la cour

La cour devrait être organisée pour :

- l’expansion modulaire ;

- un accès sécuritaire par grue/chariot élévateur ;

- la séparation entre conteneurs ;

- la clarté des corridors d’électricité et de tuyauterie ;

- l’accès de service des deux côtés de chaque conteneur ;

- l’accès d’urgence ;

- la gestion du bruit ;

- la gestion de la neige et du drainage ;

- le retrait ou le remplacement facile des plateformes.

### 7.4 Logique d’expansion des plateformes

L’expansion devrait être contrôlée par trois conditions :

1.  **Capacité électrique confirmée.** La capacité hydroélectrique et la capacité du poste sont validées pour la prochaine plateforme.

2.  **Puits thermique confirmé.** Les bâtiments publics, l’habitation, le stockage ou la demande de chaleur des serres peuvent utiliser productivement la chaleur ajoutée.

3.  **Capacité fibre confirmée.** Le NOC et la capacité de liaison principale peuvent soutenir l’accord de niveau de service du locataire.

Le calcul ne devrait pas croître plus vite que ce que la chaleur et la fibre peuvent soutenir.

## 8. Norme d’interface des conteneurs

### 8.1 Philosophie d’interface

L’hôte fournit les services externes. Le locataire possède l’environnement de calcul interne. L’interface doit être suffisamment standardisée pour permettre à plusieurs fournisseurs ou locataires conformes d’utiliser le site sans reconcevoir toute la cour.

### 8.2 Interface électrique

L’hôte devrait fournir :

- un transfert électrique mesuré ;

- la protection du départ de plateforme ;

- un point de mise à la terre et de liaison équipotentielle ;

- un sectionneur d’urgence ;

- la surveillance de la qualité de l’électricité ;

- la coordination du démarrage/de l’arrêt ;

- une limite maximale de charge contractuelle.

Le locataire devrait fournir :

- la distribution électrique interne ;

- un UPS ou une sauvegarde au niveau des racks si requis par la charge de travail du locataire ;

- la conception de redondance interne ;

- la protection de l’équipement interne au-delà du point de transfert hôte.

### 8.3 Interface de refroidissement

L’hôte devrait fournir :

- les connexions externes d’alimentation/retour de refroidissement ;

- un échangeur de chaleur à plaques ou une interface sans contact approuvée ;

- le comptage du débit et de la température ;

- la surveillance de la pression et des fuites ;

- des vannes d’isolement ;

- un chemin de dérivation/de limitation ;

- une connexion d’alarme pour température élevée, faible débit et excursions de ΔT.

Le locataire devrait fournir :

- le système interne de refroidissement des racks ;

- la gestion de la chimie du fluide côté locataire, le cas échéant ;

- la conception interne des pompes/vannes si elles sont dans le conteneur ;

- l’enveloppe d’exploitation sécuritaire et le profil de rejet thermique.

### 8.4 Interface fibre optique

L’hôte devrait fournir :

- des ports fibre doubles ou des liens A/B équivalents ;

- un brassage structuré par le NOC ;

- la surveillance de l’état des liens ;

- un point de démarcation convenu ;

- l’étiquetage physique des ports ;

- une protection de chemin lorsque possible.

Le locataire devrait fournir :

- l’équipement réseau interne ;

- le chiffrement ;

- le routage des charges de travail ;

- la cybersécurité côté locataire ;

- la télémétrie interne ;

- la disponibilité au niveau applicatif.

### 8.5 Contrôles et alarmes

L’hôte voit et enregistre les métriques d’infrastructure physique, notamment :

- la puissance appelée ;

- les événements de qualité de l’électricité ;

- la température d’alimentation/retour du refroidissement ;

- le débit du liquide de refroidissement ;

- la pression ;

- la chaleur livrée ;

- l’état des liens de plateforme ;

- le volume de bande passante ;

- les alarmes environnementales ;

- les alarmes d’accès ;

- l’état d’alarme incendie/fumée ;

- l’état externe du conteneur.

L’hôte ne voit pas :

- les journaux applicatifs du locataire ;

- les données du locataire ;

- les poids de modèles ;

- les prompts ou sorties des modèles ;

- les charges utiles des paquets ;

- les identités internes des utilisateurs ;

- les détails propriétaires des charges de travail ;

- les journaux de sécurité du locataire, sauf partage explicite par contrat.

### 8.6 Interface de sécurité physique

L’hôte contrôle le périmètre du site, l’accès à la cour, la couverture vidéo des zones externes, les journaux de badges/d’accès et l’accès d’urgence. L’accès propre au conteneur du locataire devrait être défini dans le bail, y compris qui peut entrer dans le conteneur et selon quelle procédure.

## 9. Architecture de refroidissement

### 9.1 Objectif du refroidissement

L’architecture de refroidissement capte une chaleur serveur de haute qualité, transfère la chaleur utile vers la boucle villageoise et protège l’équipement informatique lorsque la demande locale de chaleur est inférieure à la production thermique des serveurs.

### 9.2 Boucle informatique

La boucle informatique peut utiliser le refroidissement liquide direct, des échangeurs thermiques de portes arrière ou une autre approche approuvée de refroidissement de racks en boucle fermée.

Concept de température de base :

Alimentation informatique : environ 30–45 °C

Retour informatique : environ 45–60 °C

Les valeurs finales doivent être confirmées avec l’équipement du locataire, la densité des racks, la technologie de refroidissement des serveurs et les besoins d’utilisation de chaleur.

### 9.3 Options de captage de chaleur

| **Option**                              | **Cas d’utilisation**                                    | **Notes**                                                                                                        |
|-----------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Refroidissement liquide direct          | Charges de travail CPU/GPU à haute densité               | Meilleure qualité thermique et meilleure adéquation avec la récupération de chaleur utile.                       |
| Échangeurs thermiques de portes arrière | Rétrofit plus rapide ou complexité d’intégration moindre | Utile lorsque l’équipement du locataire n’est pas entièrement prêt pour le refroidissement liquide direct.       |
| Refroidissement par immersion           | Option potentielle à haute densité                       | Nécessite des procédures propres au fournisseur pour la maintenance, la manipulation des fluides et la sécurité. |

Le projet devrait privilégier l’option qui fournit une chaleur utile stable tout en préservant la modularité des locataires.

### 9.4 Échangeurs de chaleur à plaques

L’échange thermique devrait être sans contact. Les échangeurs de chaleur à plaques séparent :

- le fluide locataire/informatique du fluide de la boucle thermique hôte ;

- le fluide de la boucle thermique hôte des systèmes côté bâtiments ;

- la boucle de rejet hôte de l’eau de mer/de baie.

Du titane ou d’autres matériaux adaptés à la corrosion peuvent être requis aux interfaces avec l’eau de mer, sous réserve d’un examen d’ingénierie.

### 9.5 Source froide

La source froide finale privilégiée est l’eau de mer ou l’eau de baie près du port, au moyen d’un échange thermique sans contact. Des refroidisseurs secs fournissent une capacité de secours ou de mi-saison. L’architecture ne devrait pas dépendre d’une petite rivière comme puits thermique principal.

### 9.6 Refroidisseurs secs

Les refroidisseurs secs sont utilisés pour :

- le rejet thermique de secours ;

- l’exploitation en mi-saison ;

- les périodes de maintenance ;

- la protection lorsque le stockage thermique est plein ;

- le soutien à une limitation contrôlée.

Les refroidisseurs secs ne devraient pas remplacer l’objectif axé d’abord sur la chaleur. Ils constituent une couche de résilience et de sécurité.

### 9.7 Contrôles

Le système de contrôle du refroidissement devrait appliquer :

1.  la demande de chaleur des bâtiments en premier ;

2.  le préchauffage de l’eau chaude sanitaire, le cas échéant ;

3.  la charge du stockage thermique ;

4.  l’alimentation thermique de la serre ;

5.  les refroidisseurs secs ou le rejet vers la baie pour le surplus restant ;

6.  la limitation de charge si la capacité de rejet thermique devient contrainte.

### 9.8 Essais de mise en service

Avant l’exploitation par un locataire, l’acceptation du refroidissement devrait inclure :

- un essai de pression ;

- un essai d’étanchéité ;

- un essai des contrôles ;

- l’équilibrage des débits ;

- la vérification du ΔT ;

- le basculement vers un refroidisseur sec ;

- une alarme de température élevée ;

- une alarme de faible débit ;

- un essai de limitation sécuritaire ;

- la confirmation de l’absence de contamination croisée.

## 10. Architecture de la boucle de chaleur

### 10.1 Objectif

La boucle de chaleur est un système de valeur communautaire, et non un système d’élimination de déchets. Elle livre la chaleur des serveurs aux bâtiments publics, aux habitations, au préchauffage de l’eau chaude sanitaire, aux serres et au stockage thermique.

### 10.2 Utilisateurs de chaleur

Les utilisateurs prioritaires devraient être définis avec la communauté et le processus de gouvernance du projet. Un ordre de priorité probable est :

1.  clinique et services d’urgence ;

2.  école ;

3.  bâtiments communautaires ;

4.  installations municipales ;

5.  habitations voisines ;

6.  préchauffage de l’eau chaude sanitaire ;

7.  serre ;

8.  charges thermiques industrielles ou d’atelier optionnelles ;

9.  stockage ;

10. rejet.

### 10.3 Unités d’interface des bâtiments

Chaque raccordement de bâtiment devrait inclure :

- un échangeur de chaleur à plaques local ;

- des vannes d’isolement ;

- un compteur de chaleur ;

- une vanne de régulation ;

- un contrôle de pression différentielle au besoin ;

- une stratégie de protection contre le gel ;

- des dispositifs de prévention du retour et de la contamination ;

- une dérivation pour la maintenance ;

- une limite de propriété claire.

### 10.4 Eau chaude sanitaire

La chaleur des serveurs peut préchauffer l’eau chaude sanitaire au moyen de sous-stations de bâtiments. La montée finale en température et la protection contre la légionelle demeurent des responsabilités de conception propres à chaque bâtiment. Le projet ne devrait pas revendiquer la conformité finale de l’eau chaude sanitaire tant que les audits des bâtiments ne sont pas terminés.

### 10.5 Chaleur pour serre

La serre est un puits thermique saisonnier flexible. Elle est précieuse aux intersaisons et pendant les mois chauds, lorsque la demande de chauffage des bâtiments est plus faible. En plein hiver, les habitations et les bâtiments publics prioritaires devraient avoir préséance.

### 10.6 Stockage thermique

Le stockage thermique lisse les décalages quotidiens entre offre et demande de chaleur. Il peut :

- capter la chaleur excédentaire pendant les pics de calcul ;

- couvrir les pics de bâtiments du matin et du soir ;

- réduire le rejet ;

- améliorer le facteur d’utilisation de la chaleur ;

- donner du temps pour une limitation contrôlée des plateformes lorsque la demande évolue.

Le stockage devrait être dimensionné après connaissance des profils de charge mesurés des bâtiments et des profils de chaleur des plateformes pilotes.

### 10.7 Métriques de la boucle de chaleur

La boucle de chaleur devrait être mesurée par :

- MWh_th livrés ;

- facteur d’utilisation de la chaleur ;

- températures d’alimentation et de retour ;

- débit ;

- état de charge du stockage ;

- diesel déplacé ;

- chaleur livrée par catégorie de bâtiment ;

- chaleur livrée à la serre ;

- chaleur rejetée.

## 11. Fibre optique et centre d’exploitation réseau

### 11.1 Objectif

La fibre optique est le corridor d’exportation du projet. Le site n’exporte pas principalement de l’électricité ; il exporte des résultats de calcul, des charges de travail hébergées et des services de données.

### 11.2 Fonction du NOC

Le centre d’exploitation réseau devrait héberger :

- la terminaison fibre ;

- le répartiteur optique ;

- la commutation/le routage principaux ;

- les systèmes de surveillance ;

- la gestion hors bande ;

- les alimentations redondantes ;

- les équipements de communication ;

- le contrôle d’accès physique ;

- les contrôles environnementaux ;

- la documentation de brassage.

### 11.3 Architecture fibre

L’architecture privilégiée comprend :

Conteneur locataire

-\> doubles liens fibre de plateforme

-\> commutation/brassage NOC

-\> liaison principale protégée

-\> concentrateur régional

-\> réseaux locataires/nuage

La conception devrait utiliser des liens A/B de plateforme lorsque possible et une protection du chemin principal lorsque possible. Les routes et la redondance réelles dépendent de l’infrastructure fibre régionale disponible et de la participation des partenaires.

### 11.4 Métriques réseau

Le NOC devrait surveiller :

- la disponibilité des liens ;

- la latence p95 vers un concentrateur défini ;

- la gigue ;

- la perte de paquets ;

- les taux d’erreur ;

- l’utilisation de la bande passante ;

- les événements de basculement ;

- la durée des pannes ;

- le temps de réparation ;

- l’état des ports ;

- la qualité du signal optique.

### 11.5 Limite de sécurité réseau

L’hôte peut surveiller la disponibilité, la santé des liens, le volume de bande passante et l’état du routage. L’hôte ne devrait pas inspecter les charges utiles des paquets ni le trafic applicatif du locataire. La sécurité des données du locataire demeure la responsabilité du locataire, sauf exécution d’un contrat distinct de services gérés.

## 12. Modèle de location en boîte noire

### 12.1 Responsabilité de l’hôte

L’hôte est responsable de :

- la préparation du site de plateforme ;

- la livraison d’électricité jusqu’au point de démarcation ;

- la disponibilité de l’interface de refroidissement ;

- l’exploitation de la boucle de chaleur ;

- la disponibilité du transfert fibre ;

- la sécurité externe du site ;

- les alarmes physiques ;

- le comptage ;

- la maintenance de l’infrastructure hôte ;

- les rapports de tableau de bord pour les métriques physiques et communautaires.

### 12.2 Responsabilité du locataire

Le locataire est responsable de :

- le matériel serveur ;

- le stockage ;

- le réseau interne ;

- les systèmes d’exploitation ;

- les logiciels ;

- les données applicatives ;

- les données de modèles ;

- l’ordonnancement des charges de travail ;

- le chiffrement ;

- la surveillance interne ;

- les obligations de conformité du locataire ;

- le retrait de l’équipement à la fin du bail, sauf entente contraire.

### 12.3 Ce que l’hôte voit

L’hôte peut voir :

- les kW et kWh ;

- la tension et les événements de qualité de l’électricité ;

- le débit du liquide de refroidissement ;

- les températures du liquide de refroidissement ;

- le ΔT ;

- la chaleur livrée ;

- les alarmes externes ;

- l’état des liens ;

- le volume de bande passante ;

- la disponibilité ;

- l’occupation des plateformes ;

- les événements d’accès physique.

### 12.4 Ce que l’hôte ne voit pas

L’hôte ne voit pas :

- les fichiers du locataire ;

- les bases de données du locataire ;

- les prompts de modèles ;

- les sorties de modèles ;

- le contenu des paquets ;

- les métadonnées internes pouvant exposer des opérations confidentielles ;

- les informations des clients du locataire ;

- les algorithmes propriétaires.

### 12.5 Attestation matérielle optionnelle

L’attestation matérielle ou les environnements d’exécution de confiance peuvent être proposés lorsqu’un locataire exige une assurance d’intégrité supplémentaire. Cela devrait être propre au contrat, et non une exigence par défaut pour chaque locataire.

## 13. Exploitation et surveillance

### 13.1 Modèle d’exploitation

Kristal Farms nécessite une fonction d’exploitation locale appuyée par une expertise technique à distance. Le modèle d’exploitation devrait combiner :

- des techniciens locaux sur site ;

- un soutien NOC à distance ;

- le soutien d’un partenaire de services publics ;

- un opérateur du système thermique ;

- l’escalade du soutien locataire ;

- la coordination des interventions d’urgence ;

- les rapports communautaires.

### 13.2 Pile de surveillance

La pile de surveillance hôte devrait intégrer :

- la surveillance du poste électrique ;

- les données de compteurs de plateformes ;

- les journaux de qualité de l’électricité ;

- le SCADA de la boucle de chaleur ;

- les alarmes de refroidissement ;

- la télémétrie NOC ;

- le contrôle d’accès ;

- la couverture vidéo des zones externes ;

- les capteurs environnementaux ;

- les rapports de tableau de bord.

### 13.3 Métriques d’exploitation principales

| **Métrique**                  | **Objectif**                                                      |
|-------------------------------|-------------------------------------------------------------------|
| PUE                           | Suivre la surcharge énergétique de l’installation.                |
| WUE                           | Confirmer une consommation d’eau évaporative faible ou nulle.     |
| HUF                           | Suivre la part de réutilisation de chaleur utile.                 |
| MWh_th livrés                 | Montrer la valeur thermique communautaire réelle.                 |
| Diesel évité                  | Relier la valeur chaleur/électricité à la réduction de carburant. |
| Disponibilité des plateformes | Suivre la fiabilité.                                              |
| Occupation des plateformes    | Suivre l’utilisation.                                             |
| Disponibilité fibre           | Suivre la fiabilité de l’exportation des données.                 |
| Latence p95                   | Suivre la qualité de service vers le concentrateur.               |
| Chaleur rejetée               | Suivre les déchets restants et les occasions d’amélioration.      |
| Alarmes de sécurité           | Suivre l’intégrité du système et la qualité de la réponse.        |

### 13.4 Tableau de bord public

Un tableau de bord public ou destiné aux partenaires peut rapporter les métriques de valeur communautaire, en excluant les données confidentielles des locataires. Les éléments candidats du tableau de bord sont :

- chaleur totale livrée ;

- diesel évité ;

- chaleur fournie à la serre ;

- disponibilité des plateformes ;

- disponibilité fibre ;

- PUE/WUE ;

- emplois locaux/heures de formation ;

- incidents de service ;

- fenêtres de maintenance ;

- statut de l’audit annuel.

### 13.5 Maintenance

Les procédures de maintenance devraient inclure :

- une inspection saisonnière avant l’hiver ;

- le nettoyage/l’inspection des échangeurs de chaleur ;

- les essais des pompes ;

- l’exercice des vannes ;

- l’essai des refroidisseurs secs ;

- l’inspection du poste électrique ;

- l’essai du générateur d’urgence, le cas échéant ;

- l’essai de basculement fibre ;

- l’essai de séquencement démarrage/arrêt des plateformes ;

- l’essai de détection de fuite ;

- la simulation des contrôles et des alarmes.

## 14. Sécurité et contrôles environnementaux

### 14.1 Protection de l’eau sans contact

Tous les échanges environnementaux devraient être sans contact. L’eau de mer ou de baie ne devrait pas se mélanger au liquide de refroidissement informatique ni à l’eau de la boucle des bâtiments. Les échangeurs de chaleur à plaques et la surveillance réduisent le risque de contamination.

### 14.2 Confinement des fluides

Lorsque du glycol ou de l’eau traitée est utilisé, le système devrait inclure :

- un confinement secondaire lorsque possible ;

- une détection de fuite ;

- des vannes d’isolement ;

- du matériel d’intervention en cas de déversement ;

- des procédures de maintenance ;

- le suivi des inventaires ;

- un processus de rapports environnementaux.

### 14.3 Contrôle des rejets thermiques

Tout rejet final de chaleur vers l’eau de mer/de baie doit respecter les permis et limites de température applicables. La conception devrait surveiller la température d’entrée et de rejet et inclure des alarmes pour les excursions de ΔT.

### 14.4 Sécurité incendie et protection des personnes

Chaque conteneur et plateforme devrait inclure ou être interfacé avec :

- la détection incendie ;

- une stratégie de suppression appropriée ;

- un sectionneur d’urgence ;

- une voie d’accès pour les intervenants ;

- une signalisation claire ;

- un inventaire des matières dangereuses ;

- une procédure de contact d’urgence du locataire.

### 14.5 Bruit

Les sources de bruit comprennent les refroidisseurs secs, les pompes, les transformateurs, les générateurs lors des essais et les ventilateurs de conteneurs s’ils sont présents. La disposition de la cour devrait inclure des marges de recul, des choix d’enceintes, des limites d’exploitation et des vérifications sonores saisonnières lorsque nécessaire.

### 14.6 Climat froid et conditions côtières

La conception doit tenir compte de :

- la charge de neige ;

- l’exposition au vent ;

- la corrosion saline ;

- le givrage ;

- la protection contre le gel ;

- le tassement au dégel ;

- l’accès saisonnier ;

- la disponibilité des pièces de rechange ;

- le calendrier du transport maritime saisonnier.

## 15. Phasage

### Phase 0 — Alignement technique

- Confirmer les rôles des partenaires.

- Confirmer les documents sources.

- Confirmer la base de sélection du site.

- Identifier les contreparties des services publics, de la fibre, des fournisseurs modulaires et de la communauté.

- Établir un registre des décisions techniques.

### Phase 1 — Confirmation du site

- Valider l’emplacement candidat de plateforme adjacent au village.

- Confirmer la route portuaire/logistique.

- Confirmer l’emplacement du poste.

- Identifier les utilisateurs de chaleur.

- Confirmer le tracé préliminaire de la fibre.

- Lancer l’examen environnemental et communautaire.

### Phase 2 — Préfaisabilité électrique et thermique

- Validation de la ressource hydroélectrique.

- Concept d’alimentation MT.

- Concept de schéma unifilaire du poste.

- Étude de charge.

- Relevé de la demande de chaleur.

- Tracé initial des tuyauteries.

- Évaluation de la source froide.

- Concept de contrôles.

### Phase 3 — Ingénierie de la plateforme pilote

- Sélectionner la taille de la plateforme pilote.

- Définir l’interface de plateforme standard.

- Choisir l’approche de refroidissement.

- Définir la limite de l’accord de niveau de service du locataire.

- Définir le plan de comptage.

- Confirmer les exigences du NOC.

- Confirmer le personnel d’exploitation.

- Élaborer les essais de mise en service.

### Phase 4 — Déploiement pilote

- Construire l’infrastructure du poste et de la plateforme.

- Installer le premier conteneur.

- Mettre en service l’électricité, le refroidissement, la fibre, les contrôles et la boucle de chaleur.

- Exploiter pendant une première période d’essai saisonnière.

- Rapporter les métriques publiquement ou aux partenaires.

### Phase 5 — Expansion de la boucle de chaleur

- Ajouter des bâtiments prioritaires.

- Ajouter le préchauffage de l’eau chaude sanitaire lorsque faisable.

- Ajouter du stockage.

- Ajouter l’interface de serre.

- Ajuster les règles d’allocation de chaleur.

- Améliorer le HUF.

### Phase 6 — Plateformes supplémentaires

- Ajouter des plateformes seulement après confirmation de la capacité électrique, fibre et de puits thermique.

- Standardiser les interfaces.

- Ajouter de la redondance lorsque la demande le justifie.

- Répliquer les apprentissages dans la prochaine communauté côtière du Labrador.

## 16. Matrice d’interface des partenaires

| **Type de partenaire**                      | **Rôle technique**                                                           | **Points de décision clés**                                                                                     |
|---------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Service public / partenaire hydroélectrique | Disponibilité hydroélectrique, alimentation, poste, protection, comptage     | Puissance ferme, interconnexion, limite de propriété, procédures de panne.                                      |
| Communauté / partenaire gouvernemental      | Consentement au site, priorités de chaleur, bâtiments publics, gouvernance   | Accès au site, processus CLPE, allocation de chaleur, formation.                                                |
| Fournisseur de centre de données modulaire  | Conception des conteneurs, refroidissement des racks, intégration électrique | Norme de conteneur, plage de température de refroidissement, accès de maintenance.                              |
| Partenaire fibre / télécom                  | Route principale, intégration NOC, redondance, accord de niveau de service   | Bande passante, protection du chemin, latence, modèle de réparation.                                            |
| Locataire de calcul                         | Charge de travail, matériel interne, sécurité, charge locative               | Profil de charge, limite de boîte noire, besoins de disponibilité, isolation des données.                       |
| Investisseur en infrastructure              | Phasage, allocation des risques, bancabilité                                 | Séquence de capex, dépendances de revenus, jalons techniques.                                                   |
| Partenaire du système thermique             | Boucle des bâtiments, échangeurs, stockage, serre                            | Demande de chaleur, rénovations des bâtiments, sécurité de l’eau chaude sanitaire, dimensionnement du stockage. |

## 

## 17. Lacunes de données techniques

Les éléments suivants doivent être résolus avant l’ingénierie finale :

1.  Profil de production hydroélectrique confirmé.

2.  Puissance ferme disponible pour le calcul après les charges prioritaires communautaires.

3.  Tracé et coût de l’alimentation MT.

4.  Capacité du poste et modèle de propriété.

5.  Emplacement de la cour de plateformes et conditions géotechniques.

6.  Manutention portuaire et contraintes du transport maritime saisonnier.

7.  Route fibre, redondance, latence et obligations de réparation.

8.  Demande de chaleur par bâtiment et par saison.

9.  Exigences de rénovation des radiateurs/eau chaude sanitaire des bâtiments.

10. Profil d’absorption thermique de la serre.

11. Dimensionnement du stockage thermique.

12. Autorisations environnementales pour le rejet thermique vers la baie/l’eau de mer.

13. Technologie de refroidissement et enveloppe de température du locataire.

14. Profil de charge et comportement de montée en charge du locataire.

15. Plan de dotation et de formation pour l’exploitation du site.

16. Procédures d’incendie, de sécurité et d’intervention d’urgence.

17. Processus de gouvernance communautaire et d’allocation de chaleur.

18. Limites finales des accords de niveau de service et des baux.

## 18. Livrables d’ingénierie requis ensuite

Le prochain lot de travaux techniques devrait produire :

- dessin conceptuel d’aménagement du site ;

- schéma électrique unifilaire ;

- concept d’alimentation MT ;

- note de dimensionnement du poste ;

- norme d’interface des plateformes ;

- schéma de procédé de refroidissement et de chaleur ;

- carte du tracé de la boucle de chaleur ;

- concept de prise/rejet de source froide ;

- schéma fonctionnel du NOC ;

- liste de comptage et d’instrumentation ;

- narration de la séquence de contrôles ;

- liste de vérification de mise en service ;

- revue des modes de défaillance ;

- plan de dotation d’exploitation ;

- estimation préliminaire de capex par classe ;

- mise à jour du registre des risques.

## 19. Énoncé de positionnement technique

Kristal Farms est un modèle d’infrastructure côtière du Labrador qui combine hydroélectricité locale, calcul modulaire, réutilisation de chaleur, exportation par fibre optique et bénéfice communautaire. L’architecture est la plus robuste lorsqu’elle reste simple :

Parcours électrique court.

Conteneurs axés sur le village.

Chaleur utile d’abord.

Exportation par fibre optique.

Location en boîte noire.

Plateformes par phases.

Métriques visibles par la communauté.

C’est la base technique pour Nain comme première cible et pour les communautés côtières du Labrador comme logique de réplication.
