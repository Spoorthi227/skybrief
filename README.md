# ✈️ SkyBrief - Smart Pre-Flight Weather Briefing System

> **Weather conditions are critical for safe and efficient flight operations.**  
> SkyBrief simplifies complex aviation weather data into intelligent, real-time briefings with route-based visualizations.

---

## 🧠 Problem Statement

Modern pilots must interpret weather from multiple coded formats like METAR, TAF, SIGMET, and PIREPs before every flight. This task is:

- **Time-consuming**
- **Complex**
- **Error-prone**

There’s a pressing need for a smart assistant that can:
- Decode and summarize weather reports
- Highlight only **relevant** and **critical** weather conditions
- Present insights in a **visual and natural language format**

---

## 🚀 Project Overview

**SkyBrief** is a web-based tool designed to:
- Fetch **live aviation weather data** in real-time
- Parse **flight plans** with multiple waypoints and altitudes
- Analyze data for **risk levels** and **flight safety**
- Present results as **summaries, alerts, and interactive maps**

---

## 🔍 Innovative Features

| Feature | Description |
|--------|-------------|
| 💬 Natural Language Briefing | Converts METAR/TAF into simple, readable summaries |
| 🚨 Critical Alert Detection | Flags hazards from SIGMETs and PIREPs |
| 📶 Altitude-Based Filtering | Filters weather reports based on planned flight levels |
| 🔴🟡🟢 Risk Tagging | Tags each waypoint with a color-coded risk level |
| 🗺️ Route Map | Visualizes the entire flight path on a map |
| 📈 Weather Overlay (Planned) | Future feature for dynamic weather overlays on the route |

---

## 🧪 Preliminary Solution

- Provide a **real-time textual summary** and **visual map**
- Decode and format:
  - **METAR** – Current observations
  - **TAF** – Forecasts
  - **SIGMET** – Hazard alerts
  - **PIREP** – Pilot reports
- Present it all in a **pilot-friendly UI** and **map visualization**

---

## 🧰 Technology Stack

### Frontend:
- HTML + CSS + JS
- Leaflet.js for map visualization

### Backend:
- Python + Flask
- REST API to handle route parsing, weather summarization, and data delivery

### APIs Used:
- [aviationweather.gov](https://aviationweather.gov/)


---

## 🛠️ Methodology

1. **Parse Flight Plan**
   - Input: List of ICAO/IATA airport codes with optional altitudes
   - Output: Structured list of waypoints and flight levels

2. **Fetch Weather Data**
   - Live pull of METAR, TAF, SIGMET, and PIREPs via API

3. **Filter & Analyze**
   - Filter by location and cruising altitude
   - Detect IFR/VFR conditions
   - Highlight weather hazards

4. **Summarize & Display**
   - Textual weather summary
   - Interactive map showing flight route and risk points

---

## 📦 How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/skybrief.git
   cd skybrief
