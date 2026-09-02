# Kristal Geospatial Platform — Architecture système

**Version :** 0.1
**Statut :** Architecture proposée
**Date :** 2026-08-30
**Projet :** Kristal Farms
**Portée :** plateforme géospatiale publique, explorateur professionnel et futur moteur de scénarios

---

# 1. Résumé exécutif

Kristal Geospatial Platform est une plateforme Web géospatiale destinée à représenter, documenter et éventuellement simuler des systèmes énergétiques nordiques pouvant intégrer de nouvelles infrastructures renouvelables, des charges communautaires prioritaires, du calcul flexible et des corridors de télécommunication.

Le produit doit remplir simultanément trois fonctions :

1. **Showcase promotionnel**
   - communiquer visuellement la proposition Kristal;
   - démontrer un haut niveau de sérieux technique;
   - produire une expérience cartographique mémorable;
   - permettre à des investisseurs, partenaires, communautés et décideurs de comprendre rapidement le modèle.
2. **Explorateur technique**
   - afficher des données géospatiales et leurs sources;
   - distinguer faits, observations, hypothèses et inconnues;
   - permettre la consultation par des professionnels du SIG, de l'énergie, des télécommunications et du développement territorial;
   - fournir filtres, timeline, comparaison, provenance et export.
3. **Plateforme évolutive de modélisation**
   - supporter ultérieurement des scénarios énergétiques;
   - intégrer hydrologie, topographie, fibre, transport, environnement et coûts;
   - comparer différentes architectures de sites;
   - devenir un véritable outil d'aide à la décision sans devoir réécrire le système.

La plateforme doit être **data-driven**. Les couches, projets et données ne doivent pas être encodés individuellement dans le frontend.

Le modèle général retenu est :

```text
                     ONE DATA MODEL
                         PostGIS
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
      WEB EXPERIENCE       QGIS           OPEN APIs
     MapLibre/deck.gl   professionals       OGC
          │
          ▼
   ┌───────────────┐
   │   SHOWCASE    │
   │   EXPLORER    │
   │   SCENARIOS   │
   └───────────────┘

```

---

# 2. Principes fondamentaux

## 2.1 Une plateforme, pas une carte codée en dur

Le frontend ne doit pas contenir de logique particulière du type :

```typescript
if (site.name === "Inukjuak") {
  // comportement spécial
}

```

La définition d'une couche, de ses attributs, de ses filtres, de son rendu et de ses relations doit provenir d'un catalogue ou d'un modèle de données.

Ajouter une couche `ports`, `watersheds` ou `fibre_routes` ne devrait normalement pas nécessiter de créer un composant React propre à cette couche.

---

## 2.2 Une seule source de vérité

La source de vérité géospatiale opérationnelle est :

```text
PostgreSQL + PostGIS

```

Les autres formats sont des représentations dérivées :

- GeoJSON pour petits échanges;
- GeoParquet pour analyse volumineuse;
- MVT pour rendu Web;
- PMTiles pour releases publiques;
- COG pour rasters;
- GeoPackage pour certains échanges SIG;
- 3D Tiles ultérieurement si nécessaire.

---

## 2.3 Séparer géographie, connaissances et hypothèses

Une donnée documentée n'est pas nécessairement une géométrie.

Le système distingue au minimum :

```text
PLACE
ASSET
PROJECT
CORRIDOR

OBSERVATION
EVIDENCE
SOURCE

SCENARIO
ASSUMPTION

```

Une preuve peut donc avoir :

```text
geometry = NULL

```

sans être considérée comme incomplète.

Elle peut être reliée à une communauté, un projet, une région ou une autre entité géographique.

---

## 2.4 La provenance est une fonctionnalité centrale

Tout fait important doit pouvoir répondre à :

```text
Qui affirme cela?
Quelle est la source?
Quand la source a-t-elle été publiée?
Quand a-t-elle été consultée?
Quel passage ou tableau supporte l'affirmation?
Est-ce vérifié, interprété ou hypothétique?

```

Le panneau de provenance fait partie du produit principal.

Ce n'est pas une fonction administrative cachée.

---

# 3. Règles Kristal obligatoires

Ces règles doivent être intégrées au modèle et aux validations du logiciel.

## KR-01 — Priorité communautaire

Les charges communautaires sont prioritaires.

Dans un scénario énergétique :

```text
generation
   ↓
protected community interface
   ├── community priority load
   └── flexible compute

```

Le calcul doit être réduit avant une charge communautaire essentielle.

---

## KR-02 — Planning margin ≠ compute capacity

Une marge de planification électrique ne doit jamais être affichée ou convertie automatiquement en :

```text
available compute capacity

```

Le modèle de données doit conserver une distinction explicite entre :

```text
planning_margin_kw

```

et une éventuelle :

```text
validated_hosting_capacity_kw

```

Ces variables ont des significations différentes.

---

## KR-03 — Nouvelle génération et compute doivent être modélisés ensemble

Un scénario Kristal multi-MW normal doit disposer de son propre concept de génération ou d'approvisionnement électrique.

La plateforme ne doit pas implicitement supposer que les réseaux communautaires existants possèdent plusieurs MW inutilisés.

---

## KR-04 — L'emplacement du compute n'est pas prédéterminé

Un scénario peut représenter :

```text
generation_side
community_side
split

```

La plateforme ne doit pas imposer universellement une configuration village-side ou dam-side.

---

## KR-05 — La récupération de chaleur est optionnelle

La chaleur constitue une possibilité économique et technique.

Elle ne doit pas être traitée comme une obligation.

Les scénarios pourront représenter :

```text
no_heat_reuse
local_heat_reuse
district_heat
industrial_heat

```

---

## KR-06 — La fibre est le corridor principal d'export de valeur

L'architecture Kristal considère la fibre comme un élément structurant.

Mais :

- route;
- capacité;
- redondance;
- landing;
- fournisseur;
- SLA;

restent des données à documenter.

Une ligne cartographique hypothétique ne doit jamais être présentée comme une route fibre confirmée.

---

## KR-07 — Les projets externes sont des références

Innavik, Lac-Robertson, Quaqtaq, Puvirnituq, Nain Wind et d'autres projets comparables doivent pouvoir être représentés avec :

```text
role = external_reference

```

et non :

```text
role = kristal_candidate

```

sauf changement de statut explicite et documenté.

---

## KR-08 — Aucun ranking implicite

Le système fonctionne actuellement en :

```text
screening_mode = unranked
ranking_allowed = false

```

L'interface ne doit pas créer indirectement un classement par :

- couleurs vert/orange/rouge;
- taille des marqueurs;
- ordre de liste;
- étoiles;
- scores;
- badges « best opportunity ».

Un futur système de classement nécessitera une méthodologie transparente et une décision de gouvernance explicite.

---

# 4. Expérience produit

La plateforme utilise le même moteur et les mêmes données avec plusieurs modes UX.

---

# 5. Mode Showcase

Le Showcase est l'expérience promotionnelle.

Objectif :

> permettre à une personne non spécialiste de comprendre la proposition Kristal en quelques minutes tout en donnant l'impression d'une plateforme technique mature.

## 5.1 Caractéristiques

- interface minimale;
- navigation guidée;
- animations;
- caméra cartographique contrôlée;
- storytelling;
- chiffres clés;
- transitions entre régions;
- terrain lorsque pertinent;
- visualisation des flux énergétiques;
- diagrammes synchronisés à la carte;
- photographies et illustrations;
- callouts techniques courts;
- possibilité d'ouvrir l'Explorer.

Exemple :

```text
CANADA
  ↓
fly north
  ↓
NUNAVIK
  ↓
isolated energy systems appear
  ↓
renewable reference projects
  ↓
generation → community → compute → fibre
  ↓
OPEN EXPLORER

```

---

# 6. Mode Explorer

L'Explorer est l'interface professionnelle.

Exemple :

```text
┌────────────────────────────────────────────────────────────┐
│ KRISTAL EXPLORER         Search      2029       Share     │
├───────────────┬──────────────────────────────┬─────────────┤
│ LAYERS        │                              │ EVIDENCE    │
│               │                              │             │
│ ☑ Communities │                              │ Project     │
│ ☑ Energy      │            MAP               │ Sources     │
│ ☑ Telecom     │                              │ Confidence  │
│ ☑ Logistics   │                              │ Status      │
│ ☐ Environment │                              │ Notes       │
│               │                              │             │
├───────────────┴──────────────────────────────┴─────────────┤
│ 2025 ━━━━━━━━━━━━━━━━━●━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2032  │
├────────────────────────────────────────────────────────────┤
│ Data       Compare       Scenario       Export             │
└────────────────────────────────────────────────────────────┘

```

## 6.1 Fonctions prévues

- catalogue des couches;
- légende dynamique;
- filtres;
- recherche;
- sélection spatiale;
- panneaux de données;
- panneau Evidence;
- timeline;
- liens permanents;
- comparaison;
- export;
- téléchargement;
- métadonnées;
- scénarios ultérieurs.

---

# 7. Stack technologique cible

## 7.1 Frontend

```text
React
TypeScript
Next.js
MapLibre GL JS
deck.gl

```

### Rôles

**React / TypeScript**

Architecture de l'interface et logique de produit.

**Next.js**

Shell Web, routes, pages promotionnelles, référencement, génération de contenu statique et intégration de l'Explorer.

Next.js n'est pas une dépendance architecturale fondamentale : le frontend doit rester suffisamment découplé pour qu'un remplacement soit possible.

**MapLibre GL JS**

Moteur cartographique principal :

- basemap;
- vector tiles;
- symboles;
- terrain;
- globe;
- interactions;
- styles pilotés par les données.

**deck.gl**

Visualisations spécialisées :

- flux;
- arcs;
- heatmaps;
- agrégations;
- grands datasets;
- couches analytiques GPU;
- visualisations de scénarios.

---

# 8. 3D

CesiumJS ne fait pas partie du MVP.

Il constitue une extension possible lorsque des données justifient réellement son utilisation :

- LiDAR;
- photogrammétrie;
- DEM haute résolution;
- infrastructures;
- BIM;
- CAD;
- barrages;
- conduites forcées;
- réservoirs;
- lignes électriques détaillées.

Architecture future possible :

```text
[ MAP ] [ ENGINEERING 3D ]

 MapLibre      Cesium

```

Les deux vues pourront partager les mêmes identifiants d'entités et une partie du même backend.

---

# 9. Backend

Le backend est composé de services aux responsabilités distinctes.

```text
                       PostGIS
                          │
          ┌───────────────┼────────────────┐
          │               │                │
        Martin         pygeoapi          FastAPI
          │               │                │
       Tiles          OGC APIs         Kristal logic

```

---

# 10. PostgreSQL / PostGIS

PostGIS constitue la base opérationnelle principale.

## Responsabilités

- géométries;
- attributs;
- relations;
- requêtes spatiales;
- index spatiaux;
- recherche par proximité;
- intersections;
- buffers;
- agrégations;
- filtrage;
- données temporelles;
- relations de provenance;
- scénarios enregistrés.

---

# 11. Schémas PostgreSQL proposés

```text
raw
staging
core
research
scenario
publish
system

```

## `raw`

Import fidèle des sources.

Peu ou pas de transformations.

## `staging`

Normalisation temporaire et transformations ETL.

## `core`

Objets canoniques validés.

## `research`

Evidence, observations, sources et éléments encore incomplets.

## `scenario`

Hypothèses et scénarios Kristal.

## `publish`

Vues préparées pour API, tuiles et exports.

## `system`

Catalogue, configuration, versions et métadonnées internes.

---

# 12. Modèle conceptuel

```text
SOURCE
   │
   ▼
EVIDENCE
   │
   ├───────────────┐
   ▼               ▼
OBSERVATION      ENTITY
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        PLACE    ASSET    PROJECT
                   │
                   ▼
                SCENARIO
                   │
                   ▼
               ASSUMPTION

```

---

# 13. Entités principales

## `core.place`

Un lieu ou territoire identifiable.

Exemples :

- communauté;
- port;
- région;
- site;
- zone d'étude.

Champs indicatifs :

```text
id
name
place_type
geometry
jurisdiction
status
metadata
created_at
updated_at

```

---

## `core.asset`

Infrastructure physique existante ou confirmée.

Exemples :

- centrale;
- ligne;
- route;
- port;
- fibre;
- sous-station.

```text
id
name
asset_type
technology
geometry
operator
operational_status
commissioned_date
capacity_value
capacity_unit
metadata

```

---

## `core.project`

Projet connu, en développement ou de référence.

```text
id
name
project_type
role
status
geometry
developer
operator
technology
capacity_mw
metadata

```

Valeurs possibles :

```text
role:
  external_reference
  kristal_candidate
  kristal_project

```

---

## `core.corridor`

Infrastructure linéaire ou corridor conceptuel.

```text
id
corridor_type
status
geometry
operator
metadata

```

Types possibles :

```text
road
marine
transmission
distribution
fibre
conceptual

```

---

# 14. Evidence

## `research.evidence`

Une evidence représente une affirmation documentée.

Elle n'a pas nécessairement de géométrie.

```text
id
evidence_type
claim
status
confidence
valid_from
valid_to
metadata

```

Statuts proposés :

```text
verified
supported
scoped
unverified
conflicting
unknown

```

---

# 15. Sources

## `research.source`

```text
id
title
publisher
source_type
url
publication_date
retrieved_at
document_reference
license
metadata

```

Types :

```text
government
utility
regulator
community
academic
consultant
company
news
other

```

---

# 16. Relations evidence ↔ entités

Une table générique relie les preuves aux objets.

```text
research.evidence_relation

```

```text
evidence_id
entity_type
entity_id
relation_type

```

Exemples :

```text
supports
describes
contradicts
constrains
references

```

Cela permet :

```text
Evidence #91
  supports
Project Innavik

```

sans copier l'evidence dans la géométrie du projet.

---

# 17. Observations

Une observation représente une valeur mesurée, publiée ou transcrite.

Exemple :

```text
community = Akulivik
metric = planning_margin
period = 2028-2029
value = 351
unit = kW

```

Schéma :

```text
research.observation

id
subject_type
subject_id
metric
value_numeric
value_text
unit
valid_from
valid_to
source_evidence_id
metadata

```

---

# 18. Données temporelles

La plateforme doit supporter deux notions distinctes :

## Temps réel de l'objet

```text
valid_from
valid_to

```

## Temps de connaissance

```text
observed_at
published_at
retrieved_at

```

Cela évite de confondre :

> une donnée valide en 2027

avec :

> une donnée découverte par Kristal en 2029.

---

# 19. Scénarios

Les scénarios sont explicitement séparés des données observées.

## `scenario.scenario`

```text
id
name
description
owner
status
created_at
updated_at
base_dataset_version
geometry
metadata

```

Statuts :

```text
draft
working
shared
archived

```

---

# 20. Hypothèses

## `scenario.assumption`

```text
id
scenario_id
parameter
value
unit
source_type
evidence_id
notes

```

`source_type` peut être :

```text
user_input
engineering_assumption
derived
evidence
default

```

L'interface doit rendre visibles les hypothèses importantes.

---

# 21. Architecture énergétique d'un scénario

Le modèle doit pouvoir représenter :

```text
GENERATION
    │
    ▼
COMMUNITY INTERFACE
    │
    ├────────► PRIORITY COMMUNITY LOAD
    │
    ├────────► STORAGE
    │
    └────────► FLEXIBLE COMPUTE
                    │
                    ▼
                   HEAT
                    │
                    ▼
                OPTIONAL USE

```

Paramètres futurs possibles :

```text
generation_mw
capacity_factor
seasonality
community_priority_mw
reserve_mw
storage_mwh
compute_min_mw
compute_max_mw
compute_ramp_rate
curtailment
heat_recovery_fraction
fibre_capacity
fibre_redundancy

```

---

# 22. Catalogue de couches

Le frontend doit être piloté par un catalogue.

Exemple conceptuel :

```yaml
id: renewable_projects
title: Renewable Projects

source:
  type: vector_tiles
  collection: renewable_projects

geometry:
  types:
    - Point
    - Polygon

display:
  renderer: maplibre
  layer_type: symbol
  min_zoom: 2
  max_zoom: 18

classification:
  field: technology

evidence:
  enabled: true

filters:
  - technology
  - status
  - capacity_mw

timeline:
  enabled: true
  start_field: valid_from
  end_field: valid_to

permissions:
  public: true

```

---

# 23. Configuration pilotée par les données

Le catalogue doit pouvoir contrôler automatiquement :

- nom de couche;
- groupe;
- source;
- style;
- légende;
- attributs visibles;
- recherche;
- filtres;
- timeline;
- popup;
- Evidence Panel;
- export;
- permissions;
- zoom minimum;
- représentation 2D/3D.

L'ajout d'une couche standard doit normalement être possible sans modifier l'application React.

---

# 24. Types de couches

Classification proposée :

```text
BASE
REFERENCE
ENERGY
TELECOM
LOGISTICS
ENVIRONMENT
COMMUNITY
REGULATORY
RESEARCH
SCENARIO
ANALYSIS

```

---

# 25. Statuts visuels

La symbologie doit représenter principalement :

- nature de l'objet;
- état de validation;
- rôle;
- temporalité.

Pas son « mérite ».

Exemple :

```text
● community
◆ energy asset
▲ reference project
━ infrastructure
┄ conceptual corridor
◌ Kristal scenario
? insufficient evidence

```

Les hypothèses doivent être visuellement distinguables des infrastructures réelles.

---

# 26. Timeline

Le moteur temporel doit pouvoir filtrer ou modifier les couches selon une date ou période.

Exemple :

```text
2025 ━━━━━━━━━━━━━●━━━━━━━━━━━━━━━━━━━━ 2032

```

Applications :

- marges réseau;
- mise en service de projets;
- contrats;
- réglementation;
- scénarios;
- évolution de la demande;
- planification d'infrastructure.

---

# 27. Evidence Panel

Le panneau Evidence est l'un des composants UX fondamentaux.

Pour un objet sélectionné :

```text
INNAVIK

Type
External renewable reference

Technology
Run-of-river hydro

Capacity
7.5 MW

STATUS
Verified

EVIDENCE
────────────────────
Source A
Source B
Source C

OPEN QUESTIONS
────────────────────
...

```

Les éléments suivants doivent être distingués :

```text
FACT
OBSERVATION
DERIVED VALUE
ASSUMPTION
UNKNOWN

```

---

# 28. Evidence matrix

Pour les zones encore en screening :

| DomaineÉtat    |                   |
| -------------- | ----------------- |
| Hydro          | Unknown           |
| Grid           | Verified          |
| Fibre          | Research required |
| Port/logistics | Partial           |
| Environment    | Research required |
| Governance     | Research required |
| Economics      | Not evaluated     |

Cette matrice remplace un score de site prématuré.

---

# 29. Services de tuiles — Martin

Martin sert les vector tiles provenant de PostGIS.

```text
PostGIS
   │
   ▼
Martin
   │
   ▼
MVT
   │
   ▼
MapLibre

```

Le navigateur ne récupère que les données nécessaires au viewport et au niveau de zoom.

Les objets volumineux doivent être généralisés en fonction du zoom.

---

# 30. API géospatiale — pygeoapi

Les données professionnelles doivent être accessibles par des standards ouverts.

API cible :

```text
OGC API – Features

```

Exemples conceptuels :

```text
/collections

/collections/communities

/collections/communities/items

/collections/energy-projects/items

/collections/corridors/items

```

Cette API doit permettre à des clients externes de consommer les données sans connaître l'implémentation interne Kristal.

---

# 31. API métier — FastAPI

Une API Kristal séparée gère les fonctions qui ne correspondent pas naturellement à une API géospatiale standard.

Exemples :

```text
POST /scenarios
POST /scenarios/{id}/evaluate
POST /scenarios/{id}/compare
GET  /entities/{id}/evidence
GET  /search
GET  /catalog

```

Cette API pourra également exécuter des modèles Python.

---

# 32. Python

Python est utilisé principalement pour :

- ETL;
- QA;
- analyse géospatiale;
- modèles énergétiques;
- simulation;
- statistiques;
- hydrologie;
- coûts;
- génération de releases;
- imports;
- validation scientifique.

Librairies possibles :

```text
Pydantic
GeoPandas
Shapely
Rasterio
PyArrow
Polars/Pandas
SQLAlchemy

```

Les choix précis peuvent évoluer sans modifier l'architecture générale.

---

# 33. QGIS

QGIS constitue l'interface professionnelle SIG de référence.

Les utilisateurs autorisés peuvent se connecter directement à PostGIS.

Cela permet :

- édition;
- inspection;
- géotraitement;
- production de cartes;
- QA;
- analyse avancée;
- import/export;
- collaboration avec consultants.

La plateforme Web et QGIS doivent utiliser les mêmes identifiants canoniques.

---

# 34. Données publiques statiques

Le site promotionnel ne doit pas dépendre de la disponibilité d'une base de données pour afficher les couches fondamentales.

Lors d'une release :

```text
PostGIS
   ↓
publish pipeline
   ↓
PMTiles
   ↓
object storage
   ↓
CDN
   ↓
public MapLibre client

```

Avantages :

- rapidité;
- mise en cache mondiale;
- coûts faibles;
- très haute scalabilité;
- release reproductible;
- stabilité du site public.

---

# 35. Données live vs release

Deux modes de données sont distingués.

## Public release

```text
version = 2026.08.30
immutable = true

```

Destiné au Showcase et aux visiteurs publics.

## Live research

```text
current working dataset

```

Destiné aux utilisateurs autorisés.

L'interface doit toujours pouvoir identifier la version des données affichées.

---

# 36. Formats

| UsageFormat          |                         |
| -------------------- | ----------------------- |
| Base opérationnelle  | PostGIS                 |
| Petit échange        | GeoJSON                 |
| Analyse volumineuse  | GeoParquet              |
| Web map              | MVT                     |
| Release Web statique | PMTiles                 |
| Raster               | Cloud Optimized GeoTIFF |
| Échange SIG          | GeoPackage / PostGIS    |
| Futur 3D massif      | 3D Tiles                |

---

# 37. Raster

Les futurs datasets raster peuvent inclure :

- DEM;
- pentes;
- hydrologie;
- potentiel éolien;
- couverture terrestre;
- contraintes environnementales;
- imagerie;
- climat.

Le format privilégié est :

```text
Cloud Optimized GeoTIFF

```

Les rasters ne doivent pas être convertis arbitrairement en milliers de polygones uniquement pour faciliter le frontend.

---

# 38. Structure de repository proposée

```text
kristal-platform/
│
├── apps/
│   └── web/
│       ├── app/
│       ├── components/
│       ├── map/
│       ├── showcase/
│       ├── explorer/
│       └── scenario/
│
├── services/
│   ├── kristal-api/
│   ├── ogc-api/
│   └── tiles/
│
├── packages/
│   ├── schemas/
│   ├── catalog/
│   ├── map-style/
│   ├── ui/
│   └── shared/
│
├── pipelines/
│   ├── ingest/
│   ├── transform/
│   ├── validate/
│   └── publish/
│
├── database/
│   ├── migrations/
│   ├── functions/
│   ├── views/
│   └── seeds/
│
├── data/
│   ├── fixtures/
│   └── examples/
│
├── infra/
│   ├── docker/
│   ├── dev/
│   ├── staging/
│   └── production/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DATA_MODEL.md
│   ├── EVIDENCE_MODEL.md
│   ├── API.md
│   ├── CARTOGRAPHY.md
│   ├── SCENARIO_ENGINE.md
│   └── ADR/
│
└── README.md

```

---

# 39. Architecture frontend proposée

```text
App Shell
│
├── Showcase
│   ├── StoryDirector
│   ├── CameraDirector
│   ├── NarrativePanel
│   └── ShowcaseMap
│
├── Explorer
│   ├── MapWorkspace
│   ├── LayerCatalog
│   ├── Legend
│   ├── FilterPanel
│   ├── Timeline
│   ├── EvidencePanel
│   ├── Search
│   └── DataDrawer
│
└── Scenario
    ├── ScenarioEditor
    ├── EnergyDiagram
    ├── AssumptionPanel
    ├── ResultsPanel
    └── ComparePanel

```

---

# 40. État de l'application

Il faut distinguer :

## URL state

Éléments partageables :

```text
camera
selected entity
visible layers
timeline
filters
mode

```

Un utilisateur doit pouvoir envoyer un lien reproduisant sa vue.

## Server state

Données venant des API.

## Local UI state

Panneaux ouverts, préférences temporaires, etc.

---

# 41. Performance

Objectifs :

- aucune dépendance à un téléchargement massif de GeoJSON;
- clustering ou généralisation lorsque requis;
- vector tiles pour grands datasets;
- chargement différé;
- cache navigateur/CDN;
- simplification par zoom;
- séparation données publiques/live;
- rendu GPU pour les visualisations lourdes.

Le système doit rester fluide avec plusieurs centaines de milliers d'objets lorsque la visualisation est correctement tuilée.

---

# 42. Design visuel

L'identité cartographique doit être conçue spécifiquement pour Kristal.

Le basemap ne doit pas concurrencer les données métier.

Principes :

- relief nordique lisible;
- palette sombre ou neutre;
- contrastes élevés sur infrastructures;
- très peu de couleurs décoratives;
- animations fonctionnelles;
- typographie éditoriale forte;
- panneaux avec densité technique contrôlée.

Le « wow » doit principalement provenir de la compréhension du système.

---

# 43. Animation des flux

Les flux énergétiques peuvent être représentés graphiquement :

```text
HYDRO
  │
  ▼
COMMUNITY BUS
  ├────────► COMMUNITY
  │
  ▼
COMPUTE
  │
  ▼
FIBRE ═══════════════════► INTERNET

```

La vitesse ou intensité visuelle pourra éventuellement dépendre de données calculées.

Cependant, aucune animation ne doit laisser entendre une précision non présente dans les données.

---

# 44. Sécurité des données

Toutes les données ne seront pas nécessairement publiques.

Niveaux proposés :

```text
PUBLIC
PARTNER
INTERNAL
RESTRICTED

```

Le catalogue doit pouvoir filtrer les couches selon les permissions.

Une release PMTiles publique ne doit jamais contenir de données privées simplement cachées par le frontend.

La séparation doit avoir lieu lors du pipeline de publication.

---

# 45. Authentification

Le Showcase reste public.

L'Explorer pourra comporter :

```text
public mode
authenticated mode

```

Les fonctions suivantes pourront nécessiter une authentification :

- datasets non publics;
- scénarios sauvegardés;
- annotations;
- exports avancés;
- édition;
- commentaires;
- workflows internes.

Une solution OIDC standard est préférable à un système d'identité propriétaire.

---

# 46. Audit et traçabilité

Les modifications sensibles doivent pouvoir être retracées :

```text
who
what
when
why
source

```

Particulièrement pour :

- statut d'un projet;
- modification d'une capacité;
- ajout/retrait de preuve;
- changement de géométrie;
- décision de screening;
- classement futur.

---

# 47. Pipeline d'ingestion

Flux général :

```text
SOURCE
  ↓
RAW
  ↓
NORMALIZE
  ↓
VALIDATE
  ↓
CORE / RESEARCH
  ↓
QA
  ↓
PUBLISH

```

Une erreur dans le pipeline ne doit jamais écraser automatiquement une donnée validée sans possibilité de contrôle.

---

# 48. QA

Contrôles automatisés minimum :

```text
valid geometry
valid CRS
unique IDs
required fields
valid units
valid dates
valid relations
orphan evidence
orphan sources
duplicate entities
public/private leakage

```

Contrôles Kristal particuliers :

```text
planning_margin != hosting_capacity
external_reference != kristal_candidate
scenario assumptions explicitly tagged
ranking prohibited when ranking_allowed=false

```

---

# 49. Migration du Pass 8

Les fichiers du Pass 8 constituent une première source de recherche à intégrer.

## Layers 28–33

Les objets `status_record_no_geometry` doivent principalement être traités comme :

```text
evidence
observations
reference records

```

et non comme des marqueurs géographiques fictifs.

Une géométrie pourra être reliée ultérieurement lorsqu'elle est obtenue d'une source adéquate.

---

## Hydro-Québec planning margins

Le fichier :

```text
hq_autonomous_grid_power_margin_2025.csv

```

doit devenir une série d'observations temporelles.

Exemple :

```text
metric = autonomous_grid_planning_margin
unit = kW

```

Il doit être accompagné d'une règle d'affichage claire :

```text
Planning margin — not validated compute hosting capacity.

```

---

## Screening override

`SCREENING_STATE_OVERRIDE.csv` doit être intégré comme état de gouvernance.

```text
ranking_allowed = false
screening_mode = unranked

```

Cette règle doit influencer directement le frontend.

---

# 50. Recherche et screening

La plateforme doit pouvoir évoluer vers un processus de screening par dimensions.

Exemples :

```text
energy
hydrology
environment
rights_governance
telecom
logistics
community
regulation
economics
engineering

```

Chaque dimension possède :

```text
status
evidence completeness
open questions
last reviewed

```

et non nécessairement une note numérique.

---

# 51. Futur système de scoring

Un éventuel scoring ne pourra être activé que si :

```text
ranking_allowed = true

```

et qu'une méthodologie formelle existe.

Chaque score devra être décomposable :

```text
score
  ↓
criteria
  ↓
inputs
  ↓
evidence

```

Il doit être impossible d'obtenir un classement « magique » dont la justification n'est pas accessible.

---

# 52. Moteur de scénarios — évolution prévue

Le moteur de scénarios devra pouvoir fonctionner indépendamment du frontend.

Entrée :

```json
{
  "generation_mw": 18,
  "community_priority_mw": 2.5,
  "reserve_mw": 1,
  "compute_max_mw": 14
}

```

Sortie conceptuelle :

```text
annual_generation
community_energy
compute_energy
curtailment
storage_cycles
heat_available
utilization

```

La logique métier doit vivre dans un package ou service testable, et non dans les composants React.

---

# 53. Reproductibilité

Un scénario doit enregistrer :

```text
scenario definition
dataset version
model version
assumptions
timestamp

```

afin qu'un résultat présenté dans un dossier puisse être reproduit ultérieurement.

---

# 54. Interopérabilité

Objectif : permettre à d'autres professionnels d'utiliser les données Kristal.

Interfaces prévues :

```text
QGIS ↔ PostGIS
QGIS ↔ OGC API
Python ↔ PostGIS
Python ↔ GeoParquet
Web ↔ MVT
Web ↔ OGC API
External software ↔ OGC API

```

Le système ne doit pas nécessiter le frontend Kristal pour exploiter les données.

---

# 55. Déploiement

Environnements :

```text
development
staging
production

```

Services conteneurisés :

```text
web
kristal-api
pygeoapi
martin
postgres/postgis

```

Les artefacts statiques publics peuvent être distribués indépendamment :

```text
PMTiles
COG
images
metadata

```

via object storage + CDN.

---

# 56. Déploiement MVP possible

```text
Browser
   │
   ├──────────► CDN ─────► Next.js static assets
   │
   ├──────────► CDN ─────► PMTiles
   │
   └──────────► API
                    │
            ┌───────┼────────┐
            ▼       ▼        ▼
         FastAPI pygeoapi  Martin
            │       │        │
            └───────┴────────┘
                    │
                 PostGIS

```

---

# 57. Observabilité

À terme :

- logs structurés;
- erreurs frontend;
- disponibilité des services;
- temps de requête;
- cache hit rate;
- performance tuiles;
- erreurs ETL;
- historique des releases.

---

# 58. Tests

## Unit tests

- modèles;
- conversions d'unités;
- règles Kristal;
- scénarios.

## Integration tests

- PostGIS;
- API;
- catalogue;
- tuiles.

## Data tests

- QA géospatial;
- provenance;
- cohérence.

## UI tests

- sélection;
- filtres;
- timeline;
- partage;
- permissions.

## Visual regression tests

Particulièrement utiles pour le Showcase et la cartographie.

---

# 59. Ce qui ne doit PAS être fait

## Ne pas utiliser GeoJSON comme base principale permanente

GeoJSON reste utile, mais ne doit pas devenir la base de données.

---

## Ne pas mettre toute la logique dans le frontend

Calculs, relations scientifiques et règles doivent vivre côté modèle/backend.

---

## Ne pas exposer directement PostGIS au navigateur

Le navigateur utilise :

- tiles;
- API;
- exports.

---

## Ne pas créer une classe React par dataset

Les couches standards doivent être générées par catalogue.

---

## Ne pas coder un classement implicite

Aucune convention graphique ne doit simuler un ranking actuellement interdit.

---

## Ne pas confondre absence de géométrie et absence de preuve

Une evidence peut être parfaitement valide sans coordonnées.

---

## Ne pas inventer de précision spatiale

Une région approximative ne doit pas devenir un point précis simplement parce qu'une carte exige une géométrie.

---

## Ne pas mélanger données publiques et privées dans un même artefact public

Le contrôle d'accès frontend seul n'est pas suffisant.

---

# 60. Architecture Decision Records

Les décisions structurantes doivent être documentées dans :

```text
docs/ADR/

```

Exemples :

```text
ADR-001-maplibre-primary-renderer.md
ADR-002-postgis-source-of-truth.md
ADR-003-evidence-separated-from-geometry.md
ADR-004-ogc-api-interoperability.md
ADR-005-pmtiles-public-releases.md
ADR-006-no-ranking-until-governance.md
ADR-007-cesium-deferred.md

```

Chaque ADR contient :

```text
Context
Decision
Alternatives
Consequences
Status

```

---

# 61. Roadmap proposée

## Phase 0 — Foundation

Objectif : obtenir une architecture reproductible.

Construire :

- repository;
- Docker;
- PostGIS;
- migrations;
- modèles;
- catalogue;
- import Pass 8;
- IDs canoniques;
- provenance;
- QA.

---

## Phase 1 — Showcase MVP

Objectif : obtenir rapidement la valeur promotionnelle.

Construire :

- landing;
- MapLibre;
- basemap Kristal;
- globe/terrain;
- communautés;
- projets de référence;
- story transitions;
- energy architecture animation;
- fiches;
- Evidence Panel simplifié;
- PMTiles release.

---

## Phase 2 — Explorer

Ajouter :

- catalogue complet;
- filtres;
- timeline;
- recherche;
- Evidence Matrix;
- partage URL;
- metadata;
- exports;
- OGC API;
- QGIS access.

---

## Phase 3 — Scenario Builder

Ajouter :

- création de site;
- génération;
- community interface;
- compute;
- stockage;
- fibre;
- heat;
- hypothèses;
- résultats;
- comparaison.

---

## Phase 4 — Screening géospatial

Ajouter :

- hydrologie;
- DEM;
- ports;
- routes;
- fibre;
- environnement;
- contraintes;
- proximité;
- analyses PostGIS;
- datasets candidats.

Toujours sans ranking automatique tant que sa méthodologie n'est pas approuvée.

---

## Phase 5 — Engineering / 3D

Si les données le justifient :

- Cesium;
- LiDAR;
- 3D Tiles;
- CAD/BIM;
- barrages;
- conduites;
- lignes;
- visualisation détaillée des sites.

---

# 62. MVP recommandé

Le premier MVP ne doit pas tenter de construire toute la plateforme.

Il doit cependant utiliser les bonnes fondations.

## Données

- communautés nordiques;
- projets renouvelables de référence;
- planning margins;
- éléments réglementaires;
- corridors documentés;
- preuves Pass 8.

## UX

- Showcase;
- Explorer simple;
- Evidence Panel;
- timeline 2025–2032;
- distinction reference/hypothesis;
- navigation vers les sources.

## Infrastructure

- PostGIS;
- catalog;
- MapLibre;
- PMTiles;
- import pipeline.

Martin, pygeoapi et FastAPI peuvent être introduits progressivement lorsque leurs fonctions deviennent nécessaires.

---

# 63. Critères de réussite du MVP

Le MVP est réussi si un visiteur peut comprendre en moins de quelques minutes :

1. pourquoi les réseaux isolés existants ne sont pas simplement considérés comme des sources de plusieurs MW disponibles;
2. pourquoi Kristal s'intéresse à de nouvelles productions renouvelables;
3. pourquoi le calcul flexible peut devenir une charge locale;
4. pourquoi la fibre change l'économie du transport de valeur;
5. quelles informations sont vérifiées;
6. quelles informations sont encore inconnues;
7. que la plateforme repose sur de vraies données géospatiales et une méthodologie technique.

Un professionnel doit également constater que :

- les données sont structurées;
- les sources sont identifiables;
- les standards SIG sont supportés;
- les données sont exportables;
- le système n'est pas une simple animation marketing.

---

# 64. Vision produit

À court terme :

```text
technical promotional map

```

À moyen terme :

```text
evidence-driven geospatial explorer

```

À long terme :

```text
spatial decision-support and scenario platform

```

La même fondation doit pouvoir supporter les trois.

---

# 65. Architecture cible résumée

```text
                          USERS
             ┌──────────────┴──────────────┐
             │                             │
          PUBLIC                       PROFESSIONAL
             │                             │
             └──────────────┬──────────────┘
                            ▼
                 KRISTAL WEB PLATFORM
                  Next.js / React / TS
                            │
               ┌────────────┴─────────────┐
               │                          │
           MapLibre                    deck.gl
               │                          │
               └────────────┬─────────────┘
                            │
            ┌───────────────┼─────────────────┐
            │               │                 │
            ▼               ▼                 ▼
          Martin         pygeoapi          FastAPI
            │               │                 │
            │               │          Scenario engine
            │               │                 │
            └───────────────┼─────────────────┘
                            ▼
                     PostgreSQL/PostGIS
                            │
       ┌────────────────────┼─────────────────────┐
       │                    │                     │
       ▼                    ▼                     ▼
     QGIS              ETL / Python          Publication
 professionals             │                     │
                            ▼                     ▼
                     GeoParquet / COG          PMTiles
                                                  │
                                                  ▼
                                             CDN / Public

```

---

# 66. Décision architecturale principale

**Kristal Geospatial Platform sera construite comme une plateforme géospatiale ouverte et data-driven, avec PostGIS comme source de vérité et MapLibre/deck.gl comme expérience Web principale.**

La plateforme exposera progressivement ses données par standards géospatiaux ouverts et conservera la compatibilité avec les workflows professionnels QGIS.

L'expérience publique privilégiera une présentation visuelle forte et narrative.

L'expérience professionnelle privilégiera la provenance, les données, les filtres et l'analyse.

Les scénarios et simulations seront explicitement séparés des observations et des faits documentés.

La conception doit permettre à Kristal de passer d'un outil promotionnel à une plateforme d'analyse sans remplacement de son architecture fondamentale.
