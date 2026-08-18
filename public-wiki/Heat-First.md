# Heat First

Nearly all electricity consumed by servers ultimately becomes heat. Kristal Farms treats this heat as a second product.

The operating hierarchy is:

> **Reuse → Store → Reject**

## Reuse

Useful heat can serve, where technically appropriate:

- clinics, schools and public buildings;
- nearby homes;
- domestic hot-water preheat;
- greenhouses;
- other validated local thermal users.

## Store

Thermal storage can smooth the mismatch between constant compute heat and variable building demand. The baseline design describes stratified hot-water storage for short-term balancing.

## Reject

Only when useful sinks and storage cannot absorb the heat should the system reject it through the environmental cold-source loop or backup dry coolers, within environmental limits.

## Temperature levels

The detailed architecture anticipates server heat in approximately the **45–60°C** range. Some legacy buildings may need higher temperatures, in which case a central heat-pump booster can raise supply temperatures toward roughly **65–75°C**.

## Expansion discipline

Compute capacity should not grow independently of heat capacity. The baseline architecture stages new pads so that local heat sinks, storage and rejection capacity remain adequate.
