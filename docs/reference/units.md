# Units

## Principle

Store a numeric value with an explicit unit. Do not infer units from field names alone for generic observations.

## Preferred units

Use SI units by default unless domain convention or source fidelity requires otherwise.

Common canonical units:

```text
Power: kW, MW
Energy: kWh, MWh, GWh
Distance: m, km
Volume: L, m3
Mass: kg, t
Emissions: kgCO2e, tCO2e
Currency: explicit ISO currency + basis year when material
Data rate: Mbps, Gbps, Tbps
```

## Source fidelity

Preserve original source unit in import metadata when conversion occurs. Record conversion method and avoid false precision.

## Percentages

Store/display conventions must be explicit: `80%` should not ambiguously appear as numeric `80` in one system and `0.8` in another without schema definition.
