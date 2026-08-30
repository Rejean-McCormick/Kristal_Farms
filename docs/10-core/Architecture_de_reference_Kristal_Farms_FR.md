# Architecture de référence Kristal Farms — état canonique final

## Thèse centrale

Kristal Farms est une architecture d’accès aux ressources énergétiques nordiques. L’inversion centrale est :

> **amener une charge de calcul flexible à l’énergie éloignée et exporter la valeur numérique par fibre, plutôt que dépendre par défaut de longues routes et de longs corridors électriques haute tension.**

La réduction ou l’évitement des longues routes et lignes HV est une proposition de valeur structurelle primaire. Elle n’est pas présumée universellement avantageuse : l’économie doit être démontrée corridor par corridor et site par site.

## Géographie

- Côte-Nord : géographie de pilote/apprentissage.
- Québec nordique et Labrador : territoire de déploiement à long terme où l’éloignement des routes/HV peut créer le contraste structurel le plus fort.
- Nain : cas historique/de référence, **pas premier site actif**.

## Architecture physique

Trois dispositions restent valides : calcul près de la centrale, calcul près du village/port, ou architecture hybride. Le choix dépend de la distance électrique, de la valeur de la chaleur, de la fibre, de la logistique, de l’environnement, de la maintenance, de la sécurité et du choix communautaire.

## Modèle commercial du calcul

Kristal Farms peut offrir des sites/pads de calcul viabilisés plutôt que posséder tous les serveurs. L’infrastructure commune peut fournir alimentation électrique, interface de refroidissement, fibre, sécurité, comptage/télémétrie et accès logistique. Les locataires gardent la souveraineté sur leur matériel, OS, modèles, données, clés et télémétrie interne.

## Priorité énergétique communautaire

Les réseaux villageois existants sont une infrastructure communautaire protégée; ils ne sont pas présumés fournir plusieurs MW disponibles au calcul. L’architecture étudiée est principalement :

> **nouvelle production → interface communautaire protégée → calcul flexible → export par fibre**

Les charges communautaires/critiques ont priorité sur le calcul interruptible.

## Chaleur

La chaleur est un coproduit utile, pas une règle universelle de localisation. Elle est récupérée lorsque sa valeur utile dépasse le coût et la complexité de récupération/distribution.

## Réseau et modularité

Le programme peut utiliser des projets hydro/renouvelables petits, moyens ou plus grands lorsque justifiés, avec une croissance du calcul pad par pad. Des nœuds réussis peuvent former un chapelet côtier/de bassins relié principalement par fibre et logistique maritime, avec des interconnexions électriques plus courtes lorsqu’elles apportent de la résilience.

## Gouvernance et anti-capture

Le capital peut financer l’infrastructure sans acquérir automatiquement le contrôle de la terre, du logement, de l’énergie, du port, de la fibre, de l’emploi et de la gouvernance communautaire.

## État du screening

Il n’existe **aucun classement actif de sites**. Les anciens tiers et le Nain-first sont de la provenance seulement. Toute priorisation future exige des preuves transparentes en hydrologie, terrain/head, environnement, gouvernance communautaire/autochtone, logistique, télécom, architecture électrique et économie actuelle.
