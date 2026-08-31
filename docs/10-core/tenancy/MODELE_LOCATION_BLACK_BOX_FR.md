# Kristal Farms — Environnement chiffré sous contrôle du locataire

**Statut :** Modèle commercial/sécurité de référence actuel (C1)  
**Raccourci commercial :** location « black box »

## Modèle

Kristal Farms peut louer des sites ou pads de calcul viabilisés tout en laissant au locataire la souveraineté numérique sur les systèmes placés derrière l'interface de service.

Kristal Farms peut fournir :

- alimentation électrique et comptage;
- interface de refroidissement;
- raccordement fibre/réseau;
- sécurité physique et accès contrôlé;
- accès logistique et maintenance;
- télémétrie des services/infrastructures et mesure des SLA.

Le locataire peut garder le contrôle de :

- la configuration matérielle et des accélérateurs;
- systèmes d'exploitation et orchestration;
- modèles, jeux de données et applications;
- identités, justificatifs d'accès et journaux internes;
- clés cryptographiques et secrets.

## Engagement de confidentialité

Le fonctionnement normal est **aveugle au contenu par conception** (*content-blind by design*). Kristal Farms n'exige pas d'accès de routine aux modèles privés, jeux de données, prompts, sorties ou trafic applicatif déchiffré pour louer l'infrastructure.

L'admissibilité de la contrepartie est établie avant l'accès par une diligence raisonnable portant sur la juridiction, l'organisation, la propriété effective et le contrôle. Pendant la location, la conformité repose sur le contrat, les faits externes vérifiables et les procédures légales applicables, et non sur l'inspection cachée des charges de calcul chiffrées.

## Limites

La location black box n'élimine pas :

- le comptage;
- la télémétrie des installations;
- les contrôles de sécurité physique;
- la protection du réseau partagé;
- les obligations liées aux sanctions et contrôles à l'exportation;
- les procédures légales valides;
- la responsabilité du locataire pour ses propres systèmes.

La formulation de référence est :

> **Kristal Farms exploite l'infrastructure. Le locataire contrôle le calcul.**

Voir :

- `docs/00-control/INTERNATIONAL_TENANT_GOVERNANCE.md`
- `docs/security/TENANT_CONFIDENTIALITY_BOUNDARY.md`
- ADR-0021 et ADR-0022
