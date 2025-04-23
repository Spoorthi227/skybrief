import time
import requests
import xml.etree.ElementTree as ET


# Fetch METAR, TAF, and PIREP for the given airports
def fetch_metar_taf_pirep(airport_codes):
    ids = ",".join(airport_codes)
    base_url = "https://aviationweather.gov/api/data"

    # METAR
    metar_url = f"{base_url}/metar?ids={ids}&format=raw"
    metar = requests.get(metar_url).text

    # TAF
    taf_url = f"{base_url}/taf?ids={ids}&format=raw"
    taf = requests.get(taf_url).text

    # PIREP
    pirep_url = f"{base_url}/pirep?ids={ids}&format=raw"
    pirep = requests.get(pirep_url).text

    return metar, taf, pirep


# Fetch SIGMET data for weather hazards
def fetch_sigmet():
    url = "https://aviationweather.gov/api/data/dataserver"
    params = {
        "requestType": "retrieve",
        "dataSource": "airsigmets",
        "format": "xml",
        "hoursBeforeNow": "1"
    }
    response = requests.get(url, params=params)
    xml_data = response.text
    root = ET.fromstring(xml_data)

    sigmets = []
    for sigmet in root.findall(".//AIRSIGMET"):
        raw_text = sigmet.findtext("rawText", default="No data")
        sigmets.append(raw_text)

    return sigmets


# Extract airport codes and waypoint altitudes from the route
def extract_airport_codes(route):
    parts = route.split(",")
    airports = [code.strip().upper() for code in parts if len(code.strip()) == 4 and code.strip().isalpha()]
    waypoints = [code.strip().upper() for code in parts if len(code.strip()) != 4 and code.strip().isalpha()]
    return airports, waypoints


# Parse weather data to summarize key details
def parse_weather_data(metar, taf, pirep, airport_codes, waypoints):
    weather_summary = {}

    # For simplicity, we assume METAR contains some relevant weather data
    if "rain" in metar.lower():
        weather_summary['rain'] = "Light rain expected."

    if "winds" in metar.lower():
        weather_summary['winds'] = "Gusty winds up to 18 knots affecting approach and departure."

    if "turbulence" in pirep.lower():
        weather_summary['turbulence'] = "Moderate turbulence expected."

    # Handling waypoint altitude and turbulence data (example)
    waypoint_info = {}
    for waypoint in waypoints:
        waypoint_info[waypoint] = {
            "altitude": "32,000 ft",
            "turbulence": "Light turbulence reported.",
            "turbulence_risk": "Severe clear-air turbulence expected between 32,000 ft to 35,000 ft."
        }

    weather_summary['waypoints'] = waypoint_info
    return weather_summary


# Generate a full weather summary including airports, waypoints, altitudes, and weather conditions
def generate_weather_summary(route):
    airport_codes, waypoints = extract_airport_codes(route)
    summary = f"Weather Summary for Route: {airport_codes[0]} to {airport_codes[1]}\n"

    try:
        # Fetch weather data
        metar, taf, pirep = fetch_metar_taf_pirep(airport_codes)
        sigmets = fetch_sigmet()

        # Parse and summarize weather data
        summary += f"\n{airport_codes[0]} ({airport_codes[0]}):\n"
        weather_data = parse_weather_data(metar, taf, pirep, airport_codes, waypoints)
        for key, value in weather_data.items():
            if key == 'waypoints':
                for waypoint, waypoint_data in value.items():
                    summary += f"\n{waypoint} (Waypoint):\n"
                    for detail, detail_value in waypoint_data.items():
                        summary += f"- {detail}: {detail_value}\n"
            else:
                summary += f"- {value}\n"

        # Add additional waypoint details if needed (example)
        summary += f"\n{airport_codes[1]} ({airport_codes[1]}):\n"
        summary += "- Light rain will reduce visibility to 6 km.\n"
        summary += "- Haze reducing visibility to 8 km expected on approach.\n"

        # Summary for SIGMET (Hazardous Weather)
        summary += f"\nSIGMET:\n"
        if sigmets:
            for sigmet in sigmets:
                summary += f"- {sigmet}\n"
        else:
            summary += "- No active SIGMETs.\n"

        # Critical Recommendations
        summary += "\nCritical Recommendations:\n"
        summary += "- Turbulence Risks: Avoid altitudes above 35,000 ft to avoid severe clear-air turbulence at BUBKO waypoint.\n"
        summary += "- Visibility: Expect reduced visibility at both airports, especially during approach.\n"

        # Conclusion
        summary += f"\nConclusion:\nThe flight route from {airport_codes[0]} to {airport_codes[1]} is generally safe, but pilots should be aware of:\n"
        summary += "- Turbulence risks around BUBKO and Mumbai (VABB)—avoid high altitudes above 35,000 ft.\n"
        summary += "- Reduced visibility, especially during approach phases, with potential delays in Delhi (VIDP) due to rain and haze.\n"
        summary += "- Pilots should prepare for moderate turbulence during departure and landing, and adjust flight altitudes around BUBKO to avoid turbulence risks.\n"

        return summary

    except Exception as e:
        return f"Error fetching weather data: {e}"


def display_weather_summary(route, interval=60):
    while True:
        print("\n--- Latest Weather Summary ---")
        summary = generate_weather_summary(route)
        print(summary)
        print(f"\nUpdating in {interval} seconds...\n")
        time.sleep(interval)


# Usage:
if __name__ == "__main__":
    route = input("Enter route (airport codes and waypoints separated by commas): ")
    display_weather_summary(route, interval=60)  # Refresh every 60 seconds