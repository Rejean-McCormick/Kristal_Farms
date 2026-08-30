### A) Périmètre “black‑box” et frontières de données

1. **Quelles métriques exactes** l’hôte voit‑il côté locataire (énergie, ΔT, débits, uptime, bande passante, alarmes) — y a‑t‑il d’autres champs à exclure explicitement (logs applicatifs, métadonnées réseau, contenus) ?  
   La supervision hôte se limite aux métriques d’infrastructure **physiques** : énergie consommée (kWh, kW instantané), ΔT et débit de la boucle de refroidissement, état de fonctionnement/up-time du conteneur (via puissance ou ping de cœur de réseau), utilisation de la bande passante, et alarmes techniques (p. ex. température élevée, coupure fibre). **Aucun accès** aux données ou journaux internes du locataire n’est autorisé : pas de lecture des logs applicatifs, pas d’inspection du contenu réseau (hors volumétrie globale), ni de métadonnées sensibles.

2. **Attestation/confidentialité** : souhaites‑tu exiger une attestation matérielle (enclave/TEE) à l’embarquement du conteneur, ou la laisser **optionnelle** au contrat selon le locataire ?  
   **Optionnelle, selon les besoins du locataire.** L’attestation matérielle (enclave TEE) peut être proposée dans le bail pour garantir l’intégrité/confidentialité du conteneur, mais elle n’est pas imposée par défaut. En pratique, si un locataire requiert ce niveau de sécurité (données ultra-sensibles), une enclave matérielle sera intégrée contractuellement; sinon, le mode **“black-box”** standard (chiffrement et isolement sans TEE obligatoire) s’applique.

3. **Rétention** : combien de temps conservons‑nous les journaux **physiques** (énergie/chaleur/fibre) avant purge ou anonymisation ?  
   **Infini,** pour historique et statistiques.

### B) Baux & SLA (énergie, refroidissement, fibre)

1. **Tiers de service** : définissons‑nous des **niveaux de SLA** (p. ex. “Interactif garanti” vs “Batch modulable”) pour refléter le délestage priorisé ?  
   **Non.** Pas de différenciation de SLA en plusieurs tiers pour l’instant. Chaque locataire bénéficie d’un service **unique garanti** jusqu’à son plafond de consommation contractuel, sans scénario de délestage planifié (voir point suivant). Les éventuelles charges modulables (utilisation de surplus) restent du **best-effort** hors SLA formel.

2. **Délestage** : l’ordonnancement “heat‑first” permet de moduler certaines charges — veux‑tu le **formaliser en annexe** du bail (fenêtres, préavis, compensation) ?  
   Il n’y a pas de délestage prévu. Un plafond de consommation est offert aux locataires, une marge suffisante d’énergie est réservée aux besoins locaux (chauffage, développement industriel, etc.) et le surplus peut être offert pour l’IA (des projets d’entraînement de modèles pour des "Kristals" utilisent les surplus.)

3. **Fibre** : affichons‑nous l’objectif de **latence p95** et la **disponibilité** à ce stade du bail, ou renvoyons‑nous intégralement à la catégorie 4 (Connectivity) ?  
   On ne duplique pas ces chiffres ici – on renvoie à la section **Connectivité (catégorie 4)** pour les détails. Autrement dit, le bail mentionne que la connectivité réseau respecte un SLA élevé (disponibilité, latence) conforme aux standards, mais les valeurs cibles précises (p. ex. ≥99,9 % de dispo, latence p95 max X ms) seront définies et suivies dans la catégorie 4 dédiée.

### C) Clause “heat‑first” dans le bail

1. **Obligation d’usage** : imposons‑nous que tout locataire raccorde son conteneur à la **boucle liquide** quand c’est possible (vs. air seul) ?  
   Oui, c’est pour l’écologie, recyclage de chaleur. Mais des études plus poussées sur la rentabilité du recyclage de chaleur seront effectuées, car l’hydroélectricité est verte et peu chère à cet endroit.

2. **Seuils** : souhaites‑tu un **minimal** de chaleur valorisée (ex. % saisonnier) de la part des pads raccordables, ou gardons‑nous un engagement de moyens (raccordement \+ coopération) sans quota chiffré ?  
   Sans quota chiffré.

3. **Pénalités/crédits** : en cas de non‑respect (refus de raccordement alors que possible), appliquons‑nous une **sur‑tarification énergie** ou une baisse de priorité d’ordonnancement ?  
   Nous contrôlons les connections, alors il n’y a pas de refus de raccordement possible.

### D) Gouvernance & comités

1. **Composition** : combien de sièges et **qui nomme** (communauté, opérateur public, opérateur site, locataires, serre) pour : *Project Council*, *Heat Committee*, *Environment Committee*, *Kristals Council* ?  
   Le projet est vu comme une collabo Canada, Québec et Labrador (Terre-Neuve). L’énergie est affaire provinciale, mais le commerce international fédéral. L’initiateur des Kristal Farms est impliqué, ainsi que les populations locales. La répartition des pouvoirs, la structure, n’est pas entièrement définie.

2. **Pouvoirs** : quels comités sont **consultatifs** vs **décisionnels** (ex. priorités chaleur saisonnières, publication du scorecard, arbitrages de délestage) ?  
   Non défini.

3. **Recours** : quel **process d’escalade** (délais, médiation, arbitrage) en cas de différend locataire ↔ opérateur ↔ communauté ?  
   Non défini.

### E) FPIC & accords de bénéfices (CBA/IBA)

1. **Étapes et échéances** : souhaites‑tu un **calendrier standard** (information → consultation → consentement → revue annuelle) ou laissons‑nous ces dates **paramétrables par site** (Playbook) ?  
   On fixe un **processus commun** (information initiale → consultation ↔ consentement formel → revues périodiques), mais les échéances précises sont **adaptées par site** via le Playbook local. Chaque communauté aura donc son calendrier FPIC propre, respectant les étapes clés tout en modulant le timing selon le contexte local.

2. **Bénéfices** : y a‑t‑il des **planchers** à inscrire (emplois locaux, heures de formation, quote‑part de chaleur sociale, approvisionnement local) ou restons‑nous sur des fourchettes indicatives non publiables ?  
   Pas de planchers chiffrés inscrits dans le bail central. On optera pour des **engagements indicatifs** (ex. ordre de grandeur d’emplois, de chaleur fournie, etc.) discutés avec la communauté, sans les figer comme obligation contractuelle publique. Ces cibles resteront flexibles et ajustées site par site plutôt que des minima universels gravés.

3. **Fonds communautaire** : confirmes‑tu la **mécanique** (alimentation, usages autorisés, comité de gestion, audit) à inscrire ici, ou la basculer dans Community Benefits ?  
   On entérine le principe du fonds communautaire (abondement, usages éligibles, gestion partagée, audit annuel), mais **la description détaillée sera placée dans la section “Community Benefits”** dédiée. Le bail fera simplement référence à ce fonds et à l’accord de bénéfices communautaires, sans en détailler ici tous les mécanismes (pour garder le volet communautaire bien séparé et clair).

### F) Scorecard public & cadence

1. **Liste finale** du scorecard centralisé (noms exacts, unités, formules) — confirmes‑tu que **toutes les définitions** vivent **uniquement ici** (les autres fichiers affichent les valeurs) ?  
   La liste finale des indicateurs suivis publiquement est arrêtée comme suit (avec définitions/formules détaillées dans ce document uniquement) :

   * **PUE** (Power Usage Effectiveness, ratio sans unité) – efficacité énergétique globale du site (cible basse en climat froid).

   * **WUE** (Water Usage Effectiveness, L/kWh) – consommation d’eau \~nulle grâce à la boucle fermée (WUE ≈ 0).

   * **ΔT rejet** (différentiel °C de l’eau de refroidissement en sortie) – conformité à la limite (heures hors seuil suivies).

   * **Disponibilité fibre** (%) – disponibilité du lien réseau (% du temps, cible ≥99,9%).

   * **Latence réseau (p95)** (ms) – latence aller-retour mesurée (50e/95e percentile, engagement SLA).

   * **Taux d’occupation des pads** (%) – proportion de la capacité IT installée utilisée sur site.

   * **Densité kW/containeur** (kW-IT par conteneur) – charge moyenne par module.

   * **HUF** (Heat Utilization Factor, %) – part de la chaleur **utile** réutilisée vs totale disponible.

   * **MWh\_th livrés** – chaleur livrée aux usagers locaux (MWh, ventilée par bâtiments, serre, stockage).

   * **Diesel évité** (MWh et en tCO₂e) – énergie diesel économisée (électricité \+ chaleur) et émissions CO₂ évitées en conséquence.

   * **Qualité air évitée** – estimation des NOₓ/particules non émises (par réduction du diesel).

   * **Revenus locaux** ($) – revenus générés pour la communauté (ventes de calcul, chaleur, fibre).

   * **OPEX site & ROI** – coûts d’exploitation du site et retour sur investissement indicatif.

   * **Emplois locaux créés** (nombre) et **heures de formation** dispensées.

   * **Achats locaux** (%) – part des dépenses injectées localement (approvisionnement, services).

   * **Production serre** (m² cultivés, kg/mois, nombre de paniers distribués).

   * **Kristals publiés** (nombre de capsules) – volume de connaissances AI publiées.

   * **Hit-rate Kristals** (%) – pourcentage de requêtes servis par les Kristals (mesure de réutilisation de calcul).

   * **kWh-IT évités** – énergie de calcul économisée grâce aux Kristals (kWh évités en répondant via connaissances existantes).  
     *(Toutes les définitions et formules de ces métriques sont regroupées* *exclusivement ici. Les autres documents/affichages n’en présenteront que les valeurs mesurées, pas les définitions.)*

2. **Cadence de publication** et **lieu d’hébergement** (site web public, salle municipale, rapport mensuel ?) ; souhaites‑tu une **revue trimestrielle** conjointe avec les comités ?  
   On opte pour une **transparence proactive** : le tableau de bord sera mis à jour **mensuellement en ligne** sur un site web public accessible à tous (avec éventuellement un affichage local résumé à la mairie/centre communautaire). Un **rapport trimestriel** plus détaillé sera également produit, faisant l’objet d’une **revue conjointe avec les comités** concernés (Comité chaleur, Environnement, Conseil du projet, etc.) pour discuter des performances et ajustements si besoin. Enfin, un **bilan annuel** global sera publié et présenté publiquement (incluant les indicateurs socio-économiques consolidés), assurant un suivi régulier à la fois technique et communautaire.

### G) Sécurité, conformité, audits

1. **Audit périodique** : souhaites‑tu un **audit annuel** (physique \+ procédural) des frontières black‑box et du respect heat‑first ? Par qui (auditeur tiers, comité environnement) ?  
   Oui – prévoir un **audit indépendant annuel** couvrant deux volets : **(a) Black-box & confidentialité** (vérifier l’étanchéité des données, la séparation des rôles, l’absence d’accès non autorisé aux données locataires) et **(b) Règle “heat-first” & environnement** (s’assurer que la chaleur est bien valorisée en priorité, ΔT conforme, etc.). Ces audits seraient menés par un **tiers externe qualifié** pour garantir l’impartialité – par exemple une firme d’audit ou un expert mandaté – avec la participation des comités concernés pour la transparence (le comité environnement pour la partie chaleur/ΔT, et éventuellement un représentant du conseil du projet pour la partie données). Le rapport d’audit serait partagé aux parties prenantes et un plan d’action défini en cas de non-conformité.

2. **Incident** : en cas d’incident **privacy** ou **environnement ΔT**, quel **protocole de notification** (délais, parties prenantes, publication sur le dashboard) valider ?  
   En cas d’incident majeur – par exemple une violation de confidentialité (breach “privacy”) ou un dépassement critique de ΔT environnemental – l’opérateur applique un protocole strict : **notification immédiate** des parties prenantes clés, enquête accélérée et communication transparente. Concrètement, un **avis initial** serait émis sous 24 heures aux acteurs concernés : locataire(s) impacté(s), autorités régulatrices si pertinent (p. ex. ministère Environnement pour ΔT), et comités locaux (environnement, conseil du projet). Parallèlement, l’incident est inscrit dans le registre interne et un **RCA (Root Cause Analysis)** est lancé, avec conclusions sous \~48 heures. Une fois les faits éclaircis et les mesures correctives engagées, un **compte-rendu** de l’incident et de sa résolution est publié (dans le respect de la confidentialité) : mention dans le tableau de bord public mensuel (indicateur d’incident) et diffusion d’un rapport synthétique accessible à la communauté. Ce processus assure une **alerte rapide**, une **médiation/transparence** (via le guichet unique des griefs) et une **traçabilité publique** des résolutions, renforçant la confiance.

### H) Réversibilité / fin de bail

1. **Dépose et remise en état** : délais pour **déconnexion** d’un conteneur, responsabilités de **logistique retour** (port), et **état du pad** à la restitution (norme de propreté/remise) — veux‑tu une **annexe type** ?  
   À la fin du bail, la procédure de réversibilité sera clairement encadrée (idéalement via une **annexe type** détaillant étapes et responsabilités). En principe : le locataire dispose de **30 à 90 jours** pour **retirer son conteneur** du pad une fois le bail expiré ou résilié. La coordination logistique (débranchement, grutage, transport jusqu’au port d’embarquement) est à la charge du locataire, en concertation avec l’opérateur du site pour les accès sécurisés et calendriers (fenêtre hors grand froid, etc.). Le pad doit être **remis en état initial** : nettoyage, aucune détérioration au-delà de l’usure normale, démontage de tout aménagement spécifique du locataire. L’annexe de fin de bail précisera les standards de propreté et d’intégrité attendus, ainsi que les modalités de constat (inspection conjointe) et, le cas échéant, les pénalités si le site n’est pas restitué conforme.

2. **Transfert** : autorisons‑nous le **transfert de bail/pad** entre locataires (cession), sous quelles conditions (validation de sécurité, continuité de chaleur) ?  
   **Transfert encadré oui**, mais soumis à approbation. Un locataire sortant pourra céder son bail (et donc le pad associé) à un tiers **uniquement avec l’accord préalable** de l’opérateur/hôte et en respectant certaines conditions : le nouveau locataire doit être **éligible** (mêmes critères de sécurité et conformité que tout entrant, y compris respect des règles de confidentialité black-box et de valorisation de chaleur), et s’engager par écrit à reprendre **toutes les obligations** du bail (notamment la connexion au réseau de chaleur, SLA, etc.) sans interruption. L’objectif est d’assurer une **continuité de service** (pas de trou dans la fourniture de chaleur locale, ou compensation si interruption) et de **préserver la sécurité** (vérification du profil du repreneur, conformité export si applicable). En pratique, la cession n’est donc possible que dans le cadre d’un processus validé (due diligence du nouvel entrant, consentement du conseil du projet si requis), pour éviter tout transfert inopportun ou non maîtrisé.

### I) Admissibilité des locataires & posture géopolitique

1. **Eligibility** : locataires autorisés (gouvernements, universités, entreprises) — confirmes‑tu l’**ouverture globale** avec **neutralité**, sans exclusion de principe, tout en gardant une **conformité export** standard ?  
   Oui, on maintient une **ouverture globale et neutre** quant au type de locataires : toute entité éligible – qu’il s’agisse d’une entreprise privée, d’une institution publique/gouvernementale ou d’une université, locale ou internationale – peut candidater pour louer un pad. Aucune catégorie n’est exclue a priori, dans un esprit de neutralité (pas de discrimination par nationalité ou secteur), sous réserve bien sûr de satisfaire aux exigences légales et sécuritaires. En particulier, on respectera les **règles standard d’exportation** et de sanctions internationales : un locataire soumis à des restrictions légales (p. ex. entité sur liste de contrôle, usage interdit par la loi canadienne) sera écarté. Hormis ces contraintes réglementaires, le programme reste ouvert à tous les locataires **conformes**, sans juger de l’usage final tant qu’il respecte le cadre du bail et les lois en vigueur.

2. **Usage** : interdisons‑nous explicitement certains **cas d’usage** (ex. non alignés avec la communauté) via une **liste négative** dans le bail ?  
   **Pas de liste noire prédéfinie** dans le bail. On ne souhaite pas s’engager dans la voie d’interdire contractuellement des usages spécifiques au-delà du cadre légal existant. L’approche retenue est celle de la **neutralité d’usage** : tant que le locataire respecte les lois et réglementations (aucune activité illicite), et les obligations communautaires générales (p. ex. ne pas nuire à la communauté d’accueil), nous n’imposons pas de restrictions supplémentaires sur la nature des calculs effectués. En pratique, cela signifie pas d’ingérence sur les cas d’usage (pas de censure de projets « non-alignés » politiquement par exemple), sauf si un usage venait explicitement en conflit avec les engagements locaux (dans ce cas un dialogue via les comités serait privilégié). Le bail se concentre donc sur le **respect des exigences techniques et éthiques de haut niveau** (conformité légale, respect environnemental, valeurs FPIC), sans établir de liste négative d’usages interdits a priori.

---

