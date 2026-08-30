---
source_file: "Kristal Farms_ Economic Cost Advantage and Savings Model.docx"
repository_status: "working source / requires validation"
extraction_method: "pandoc"
extracted_on: "2026-08-17"
---

> **Repository note:** This Markdown is a searchable extraction of the supplied DOCX. It is not automatically authoritative. Validate claims and citations before promotion into partner-facing material.

# Kristal Farms: Economic Cost Advantage and Savings Model

### 1. Executive Thesis

Kristal Farms is designed to deliver sovereign AI compute at a structurally lower cost than a conventional data center because it removes or reduces several major cost drivers at once: long-distance transmission, major road construction, mechanical cooling, heat rejection, urban real estate, heavy security infrastructure, and repeated compute waste.

The core model is simple: locate modular compute containers near cold hydro and local heat users, export computation by fiber instead of exporting electricity, and recycle server heat into buildings, domestic hot water, and greenhouses. This turns energy, climate, and remoteness into economic advantages rather than constraints. The existing Kristal Farms concept already defines this stack: short medium-voltage power feed, natural cold, heat reuse, port-based logistics, lower land/security cost, modular phasing, and measurable savings through PUE, WUE, HUF, diesel avoided, pad occupancy, uptime, and compute avoided.

## 2. Primary Economic Drivers

### 2.1 Low-Cost Hydro Power

The first economic advantage is access to low-cost hydroelectricity. For benchmarking, Hydro-Québec’s 2026 Rate L energy price is listed at **3.821¢/kWh**, while Newfoundland and Labrador Hydro lists the Labrador Interconnected System rate at **3.154¢/kWh**. These figures are not yet a final Kristal Farms tariff, but they establish the strategic price range that makes hydro-based AI compute compelling. ([<u>Hydro Quebec</u>](https://www.hydroquebec.com/data/documents-donnees/pdf/rates-chart.pdf))

At this price level, power becomes a strategic advantage. A conventional AI data center in a higher-cost electricity market may pay two to four times more per kWh before even accounting for cooling, water, transmission, or heat waste. Kristal Farms should therefore present electricity cost not as a standalone number, but as the foundation of a full-stack cost reduction model.

### 2.2 Transmission Infrastructure Avoided

Conventional remote energy development often requires long high-voltage transmission lines, substations, rights-of-way, permitting, clearing, and long-term maintenance. Kristal Farms avoids this by using local hydro near the compute site and relying on a short medium-voltage feed from the hydro plant to a village or port substation.

A useful Canadian benchmark is the Wataynikaneyap Transmission Project in northern Ontario, described as a **C\$1.9 billion** project for a **1,744 km** transmission system. That implies an average cost of approximately **C\$1.09 million per km**, before adjusting for site-specific geography, permitting, substations, climate, and escalation. ([<u>Torys LLP</u>](https://www.torys.com/work/2018/12/wataynikaneyap-transmission-project))

**Illustrative avoided transmission cost**

| **Transmission distance avoided** | **Indicative avoided cost** |
|-----------------------------------|-----------------------------|
| 25 km                             | C\$27 million               |
| 50 km                             | C\$55 million               |
| 100 km                            | C\$109 million              |
| 200 km                            | C\$218 million              |

This is one of the strongest economic arguments: Kristal Farms does not need to move electricity over long distances. It moves compute results by fiber.

### 2.3 Road Construction Avoided

Remote data center construction can require large all-season roads for heavy equipment, maintenance access, fuel, construction materials, and long-term logistics. Kristal Farms reduces this requirement by using coastal or port-adjacent siting, marine delivery, standard 40-foot containers, and short lifts from quay to pad.

A northern road cost benchmark from Northern Policy Institute identifies the cost of all-season roads in the Far North at approximately **C\$3 million per km on average**. ([<u>Northern Policy Institute</u>](https://www.northernpolicy.ca/upload/documents/publications/reports-new/smart-roads-2022-10-12-ac.pdf))

**Illustrative avoided road cost**

| **Road distance avoided** | **Indicative avoided cost** |
|---------------------------|-----------------------------|
| 10 km                     | C\$30 million               |
| 20 km                     | C\$60 million               |
| 50 km                     | C\$150 million              |
| 100 km                    | C\$300 million              |

This should be shown visually in the proposal because it makes the “port + modular containers” model immediately understandable.

## 3. Cooling Cost Advantage

### 3.1 Natural Cold Replaces Mechanical Cooling

Conventional data centers spend significant capital and operating costs on chillers, cooling towers, pumps, water treatment, air handling, and redundancy. Kristal Farms replaces much of that cost with cold-climate design, liquid cooling, water-to-water heat exchange, seawater or bay-water heat rejection through non-contact plate exchangers, and dry coolers as backup.

Uptime Institute’s 2025 data center survey reports that facilities commissioned in the last five years achieved an average **PUE of 1.48**, while larger data centers of 20 MW and above averaged **1.44** globally. ([<u>Uptime Institute</u>](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2025.Annual.Survey.Report.pdf?mkt_tok=NzExLVJJQS0xNDUAAAGcNPnjzIRtJDlpo9-Khi9n18G0DO03Sio3lnUg39J2C4NwajSneDRbDbQS68NjcylaxC-tv-Wxs8gNe8yLCsRPInSsJBBujdGUMIQQZ66IJcvg&version=0))

Kristal Farms should model a target PUE range of **1.10–1.20**, subject to engineering validation. This is not only an energy saving. It is a cost saving, a cooling-infrastructure saving, and a water-saving story.

### 3.2 PUE Savings Per 1 MW of IT Load

For every **1 MW of IT load** running continuously:

| **Item**                    | **Formula**        | **Result**      |
|-----------------------------|--------------------|-----------------|
| IT energy per year          | 1 MW × 8,760 hours | 8,760 MWh/year  |
| Facility energy at PUE 1.48 | 8,760 × 1.48       | 12,965 MWh/year |
| Facility energy at PUE 1.15 | 8,760 × 1.15       | 10,074 MWh/year |
| Annual energy saved         | Difference         | 2,891 MWh/year  |

**Annual PUE-related operating savings per 1 MW IT**

| **Electricity price** | **Savings from lower PUE** |
|-----------------------|----------------------------|
| 3.154¢/kWh            | ~C\$91,000/year            |
| 3.821¢/kWh            | ~C\$110,000/year           |
| 10¢/kWh               | ~C\$289,000/year           |

At **20 MW IT**, the same PUE improvement represents approximately:

| **Electricity price** | **Annual savings**   |
|-----------------------|----------------------|
| 3.154¢/kWh            | ~C\$1.8 million/year |
| 3.821¢/kWh            | ~C\$2.2 million/year |
| 10¢/kWh               | ~C\$5.8 million/year |

This excludes capital savings from smaller chiller plants, lower cooling maintenance, lower water treatment, and reduced cooling redundancy.

## 4. Heat Recycling Value

### 4.1 Heat Becomes a Product

Almost all electricity consumed by servers ultimately becomes heat. In a conventional data center, this heat is treated as a waste stream. Kristal Farms treats it as a product.

The heat recycling plan prioritizes useful heat in this order: **reuse, store, reject**. Heat is sent first to radiators and domestic hot water, then to a greenhouse in warm months, then to storage, and only rejected when other sinks are full.

For every **1 MW IT** running continuously:

| **Item**                       | **Result**        |
|--------------------------------|-------------------|
| IT energy consumed             | 8,760 MWh/year    |
| Potential waste heat available | ~8,760 MWhth/year |
| Useful heat at 50% HUF         | 4,380 MWhth/year  |
| Useful heat at 70% HUF         | 6,132 MWhth/year  |
| Useful heat at 90% HUF         | 7,884 MWhth/year  |

The economic value can be counted three ways:

1.  avoided diesel or heating oil purchases;

2.  heat revenue from buildings, public facilities, or greenhouse users;

3.  social value from lower heating costs and improved energy resilience.

### 4.2 Diesel and Emissions Avoided

For proposal modelling, Kristal Farms should track diesel avoided in both **litres** and **tonnes of CO₂e**. Environment and Climate Change Canada’s 2026 refined petroleum product factors list diesel at **2,681 g CO₂/L**, and light fuel oil at **2,753 g CO₂/L** for common heating categories. ([<u>Canada</u>](https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/emission-factors-reference-values.html))

Using a conservative working assumption of **10 kWh of useful heat per litre equivalent** until local boiler efficiency and fuel data are confirmed:

| **IT load** | **Useful heat at 70% HUF** | **Fuel equivalent avoided** | **CO₂ avoided using diesel factor** |
|-------------|----------------------------|-----------------------------|-------------------------------------|
| 1 MW        | 6,132 MWhth/year           | ~613,000 L/year             | ~1,644 tCO₂/year                    |
| 10 MW       | 61,320 MWhth/year          | ~6.1 million L/year         | ~16,440 tCO₂/year                   |
| 20 MW       | 122,640 MWhth/year         | ~12.3 million L/year        | ~32,880 tCO₂/year                   |

These numbers should be refined later with actual local fuel type, delivered fuel price, boiler efficiency, heat network losses, and seasonal HUF.

## 5. Security and Real Estate Savings

Kristal Farms reduces security and real estate costs by avoiding expensive urban or suburban data center land. The model uses a fenced container yard at or near the port, controlled access, fewer neighbors, and a shorter logistics chain from quay to pad.

This produces several economic effects:

| **Cost factor**     | **Conventional data center**        | **Kristal Farms**                    |
|---------------------|-------------------------------------|--------------------------------------|
| Land                | Urban or suburban premium           | Remote/port-adjacent industrial land |
| Physical security   | Large urban perimeter and personnel | Controlled isolated yard             |
| Neighbor mitigation | Noise, traffic, visual impact       | Fewer direct neighbors               |
| Logistics           | Road freight and repeated trucking  | Marine delivery and short pad lifts  |
| Expansion           | Large campus upfront                | Modular pad-by-pad growth            |

This category should be quantified as a range once site data are known. For now, it should be presented as a defensible OPEX and CAPEX reduction category, not as a fixed number.

## 6. Logistics Savings

Kristal Farms uses modular compute pads and marine delivery. This reduces the need for repeated long-haul trucking, large road upgrades, and complex remote construction staging. The project documentation identifies standard 40-foot containers, marine delivery to the port, short lifts to pads, and seasonal windows as the preferred logistics model.

Economic benefits include:

- fewer road kilometres to build or maintain;

- fewer heavy transport movements;

- faster pad deployment;

- easier replacement or removal of containers;

- lower stranded-asset risk;

- phased expansion instead of a single large upfront build.

The economic message is that Kristal Farms does not need to build a full remote industrial campus before revenue begins. It can start with a smaller number of pads and expand as power, heat demand, tenants, and community support grow.

## 7. Modularity and Financing Risk Reduction

Large conventional data centers often require major upfront capital before the first dollar of revenue. Kristal Farms lowers this risk by adding pads in phases. The first pad funds and de-risks the next, allowing the project to match compute capacity with confirmed heat demand, confirmed tenants, and available hydro capacity.

This improves the financial profile in four ways:

1.  lower initial capital requirement;

2.  faster first revenue;

3.  better alignment between capacity and demand;

4.  reduced risk of overbuilding.

For funders, this matters because the project can be evaluated as a replicable infrastructure platform, not a single one-off megaproject.

## 8. Data Boundary and Tenant Trust as Economic Value

The black-box tenancy model is also an economic advantage. The host provides power, cooling, heat export, fiber, and physical security, but does not access tenant data, models, logs, or application content. Monitoring is limited to physical metrics such as energy, temperatures, flows, uptime, bandwidth usage, and alarms.

This matters economically because it makes the site more attractive to universities, AI companies, public-sector users, and sensitive compute tenants. It also reduces governance complexity: the operator sells infrastructure, not access to tenant data.

## 9. Summary of Quantified Economic Advantages

| **Category**         | **Economic mechanism**                    | **Current quantification method** |
|----------------------|-------------------------------------------|-----------------------------------|
| Low-cost power       | Hydro electricity at strategic rates      | ¢/kWh benchmark                   |
| Transmission avoided | No long HV corridor                       | C\$/km avoided                    |
| Road avoided         | Port delivery and short site access       | C\$/km avoided                    |
| Cooling savings      | Lower PUE from climate and liquid cooling | MWh saved/year                    |
| Water savings        | WUE near zero through closed-loop cooling | L/kWh avoided                     |
| Heat value           | Waste heat reused locally                 | MWhth delivered/year              |
| Diesel avoided       | Recovered heat replaces fuel              | Litres/year and tCO₂/year         |
| Security savings     | Isolation and controlled access           | OPEX range                        |
| Logistics savings    | Marine delivery, modular pads             | CAPEX/OPEX range                  |
| Financing risk       | Phased deployment                         | Lower upfront capital             |
| Compute avoided      | Reuse of validated “Kristals”             | kWh-IT avoided                    |

## 10. Proposed Economic Dashboard

Kristal Farms should publish a monthly economic dashboard with a small set of indicators:

| **Metric**            | **Unit**      | **Purpose**                     |
|-----------------------|---------------|---------------------------------|
| Power price           | ¢/kWh         | Shows base energy advantage     |
| IT energy consumed    | MWh           | Measures compute scale          |
| PUE                   | ratio         | Measures facility efficiency    |
| WUE                   | L/kWh         | Measures water advantage        |
| Useful heat delivered | MWhth         | Measures heat value             |
| HUF                   | %             | Measures share of heat reused   |
| Diesel avoided        | L/year        | Measures fuel displacement      |
| CO₂e avoided          | tCO₂e/year    | Measures climate value          |
| Transmission avoided  | km / C\$      | Measures infrastructure savings |
| Road avoided          | km / C\$      | Measures infrastructure savings |
| Pad occupancy         | %             | Measures revenue utilization    |
| Uptime                | %             | Measures reliability            |
| Local revenues        | C\$           | Measures community value        |
| Local jobs/training   | count / hours | Measures economic development   |

These are consistent with the project’s existing scorecard approach, which already identifies PUE, WUE, HUF, MWhth delivered, diesel avoided, local revenues, OPEX, ROI, jobs, training, local purchasing, greenhouse production, Kristals published, and kWh-IT avoided.

## 11. Initial Scenario Model

### Scenario: 20 MW IT Phase

| **Economic factor**         | **Working estimate** |
|-----------------------------|----------------------|
| IT energy per year          | 175,200 MWh          |
| Facility energy at PUE 1.48 | 259,296 MWh          |
| Facility energy at PUE 1.15 | 201,480 MWh          |
| PUE energy saved            | 57,816 MWh/year      |
| PUE savings at 3.821¢/kWh   | ~C\$2.2 million/year |
| Heat available              | 175,200 MWhth/year   |
| Useful heat at 70% HUF      | 122,640 MWhth/year   |
| Fuel equivalent avoided     | ~12.3 million L/year |
| CO₂ avoided                 | ~32,880 tCO₂/year    |
| 50 km transmission avoided  | ~C\$55 million       |
| 20 km road avoided          | ~C\$60 million       |

This scenario should be treated as an illustrative pre-engineering model. Final values must be validated through site selection, utility tariffs, hydrology, heat demand study, civil engineering, road access assessment, fiber design, and tenant load profile.

## 12. Investor and Government Message

Kristal Farms is not merely a cheaper data center. It is a cost-avoidance infrastructure model.

It reduces the cost of AI compute by stacking several advantages: low-cost hydro, short electrical interconnection, avoided transmission, avoided road construction, cold-climate cooling, heat reuse, near-zero water consumption, modular deployment, lower real estate cost, lower security complexity, and measurable community benefits.

The result is a platform where the cost of compute is reduced not by one factor, but by the combined effect of energy, climate, geography, infrastructure design, and local heat demand.
