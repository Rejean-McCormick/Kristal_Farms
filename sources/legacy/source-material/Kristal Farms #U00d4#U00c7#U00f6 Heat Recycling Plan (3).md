# **Kristal Farms — Heat Recycling Plan**

**Scope.** Heat-first design for Kristal Farms. Servers in the village. Heat to radiators and DHW first. Greenhouse in warm months. Export compute by fiber, not electricity. Keep focus on heat, not balance-of-plant.

---

## **1\) Purpose and non‑negotiables**

**Purpose.** Replace local diesel heat with server waste heat. Deliver stable, low‑cost heat to public buildings and homes. Use a greenhouse as the summer sink.

**Rules.**

* **Reuse → Store → Reject.** Always in this order.

* **Two sealed circuits.** IT loop and building loop are separate. No fluid mixing.

* **Non‑contact with the environment.** All heat exchange via plate exchangers.

* **Village‑first siting.** Data containers near heat users. Not at the dam.

* **No long high‑voltage lines.** Short medium‑voltage feed from the hydro to the village.

---

## **2\) Architecture at a glance**

**Heat path (text diagram).**

IT servers (DLC / rear-door) → 45–60 °C → Plate HX → \[ optional Heat Pump booster → 65–75 °C \]  
→ Building loop (radiators \+ DHW) and Greenhouse → Return cooler → Plate HX → IT return 30–45 °C

**Cold source (for IT cooling).**

* Primary: seawater/bay at the port, **non‑contact** via titanium plate HX.

* Backup/shoulder: dry coolers.

* Do **not** depend on a small river as the main sink.

**Two loops.**

* **IT loop.** Treated water or water‑glycol. Inlet 30–45 °C. Outlet 45–60 °C. Pumps with VFDs.

* **Building loop.** Water only. Supply temperature set by demand and outside air temp.

**Distribution.**

* Pre‑insulated twin pipes. Short runs. Substations per building (plate HX, valves, meter).

* Balance by design. Use differential pressure control valves.

---

## **3\) Capture options at the racks**

**Direct Liquid Cooling (DLC).** Warm‑water plates on CPUs/GPUs. Highest thermal quality.

**Rear‑Door Heat Exchangers (RDHx).** Water coil behind the rack. Lower integration cost.

**Choice.** Use DLC when available. RDHx acceptable where integration speed matters.

---

## **4\) Temperatures and heat delivery**

**Low‑temperature service (no booster).**

* If buildings accept 50–60 °C supply, inject directly from the plate HX.

* Good for retrofits with oversized radiators, fan‑coils, or new emitters.

**High‑temperature service (with booster).**

* If legacy radiators require 65–75 °C, add a central **heat‑pump booster**.

* Booster sized to peak winter load of priority buildings.

**Domestic Hot Water (DHW).**

* Preheat through the building substation. Keep Legionella safeguards (final lift if needed).

---

## **5\) Heat sinks and seasonal plan**

**Winter (priority).** Public buildings (clinic, school, town hall), then nearby housing.

**Shoulder seasons.** Mix buildings \+ greenhouse. Use storage to clip morning/evening peaks.

**Summer.** Greenhouse as main sink. Reject only if storage and greenhouse are full.

---

## **6\) Storage**

**Thermal tanks (stratified).** 2–12 h of average thermal load. Start with \~6 h.

**Why.** Smooth diurnal peaks. Allow IT scheduling to align with heat value.

**Later option.** Borehole (BTES) or pit (PTES) for multi‑week smoothing if needed.

---

## **7\) Controls and operating mode**

**Heat‑aware scheduling.**

* Run batch/AI jobs harder when tanks are low and heat demand is high.

* Throttle or shift when tanks are full and greenhouse demand is low.

**Control loops.**

* Outdoor‑reset “heat curve” for building supply.

* ΔT caps on any environmental reject. Alarms on ΔT, flow, temperature.

---

## **8\) Electrical feeding (kept simple)**

**Medium‑voltage (MV) short feed** from the hydro plant to a village substation at the port.  
 No new long HV corridor. No large switchyards. Keep interconnection local.

---

## **9\) Instrumentation and minimal public metrics**

Publish four numbers monthly. Keep the rest internal.

1. **Useful heat delivered** (MWh‑th), by sink (buildings, greenhouse, storage).

2. **HUF** (Heat Utilization Factor) \= useful heat / total heat available.

3. **PUE** (winter and annual). **WUE ≈ 0** by design.

4. **Diesel avoided** for heat and power (liters, then tCO₂e).

Internal ops add: ΔT hours‑within‑limit, booster COP, pump kWh, pipe losses, uptime.

---

## **10\) Contracts and data boundaries (one page)**

**Heat‑supply contract.** Temperature bands, metering, tariff, curtailment rules, social heat quota.

**Pad lease (black‑box tenancy).** Landlord provides power/cooling/heat export/fiber. No access to tenant data or models. Only physical metrics.

**Governance.** Local committee sets seasonal priorities and approves greenhouse windows.

---

## **11\) Phasing**

**Phase 1 — Public buildings first.**  
 Energy center at the port. Short MV feed. IT loop \+ plate HX. Booster (if required). Two to three substations. One stratified tank. Greenhouse stub.

**Phase 2 — Close‑by housing.**  
 Extend the loop to nearest clusters. Add tank capacity if peaks rise.

**Phase 3 — Greenhouse scale‑up.**  
 Increase surface and integrate summer schedules. Consider LT emitters in new buildings.

---

## **12\) Acceptance gates (simple, measurable)**

* **ΔT compliance**: 100% of hours within environmental limit.

* **HUF**: meets seasonal floor agreed with the community.

* **Booster delivery**: radiators achieve setpoint on design days.

* **PUE/WUE**: winter PUE meets target. WUE ≈ 0 proven.

* **Scorecard live**: public dashboard online with the four metrics.

---

## **13\) Risks and guards**

* **Summer sink not enough** → add greenhouse area, add storage, adjust IT schedules.

* **Legacy radiators underperform** → enable booster, add fan‑coils in problem zones.

* **Cold source outage** → dry coolers in standby, IT throttling policy.

* **Fiber event** → path protection; batch jobs prioritized.

* **Social fit** → publish numbers; run monthly clinic‑school‑greenhouse updates.

---

## **14\) One‑page equipment list (minimum viable)**

* **IT side**: DLC manifolds or RDHx, pumps with VFDs, water treatment skid, isolation valves.

* **HX**: plate heat exchanger (stainless/titanium as needed), differential‑pressure control.

* **Booster**: heat pump (if needed) sized to legacy radiator load, buffer tank.

* **Storage**: stratified tank(s) with internal baffles, level and temperature instrumentation.

* **Distribution**: pre‑insulated twin pipes, building substations (plate HX, meters, controls).

* **Cold source**: seawater intake/outfall HX, corrosion‑resistant materials; dry coolers backup.

* **Controls**: PLC/SCADA, outdoor‑reset curve, HUF calculator, ΔT guard, data export for dashboard.

---

## **15\) Plain‑language FAQs (for the community)**

* **Will this heat my radiators?** Yes. If your building needs high temperature, the booster lifts it.

* **Is river or sea water flowing into my house?** No. Fluids never mix. Heat crosses a metal plate.

* **What happens in summer?** We heat a greenhouse first. Only then do we reject a small remainder.

* **Do you see my data?** No. The operator sees energy, heat, and fiber metrics only.

* **What if something breaks?** Dry coolers and diesel remain as backup. We publish uptime.

---

## **16\) One‑sentence summary**

**Heat first.** Put the servers in the village, move their heat into radiators and DHW, use a greenhouse when homes don’t need it, store a few hours to smooth peaks, and reject only when everything else is full.

