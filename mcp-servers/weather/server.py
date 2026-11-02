import httpx
from fastmcp import FastMCP

mcp = FastMCP("AgentK Weather")

@mcp.tool()
async def get_current_weather(city: str) -> dict:
    """Return current weather for a city using Open-Meteo."""
    if not city.strip():
        raise ValueError("city must not be empty")
    async with httpx.AsyncClient(timeout=8.0) as client:
        geo = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1, "language": "en", "format": "json"},
        )
        geo.raise_for_status()
        places = geo.json().get("results", [])
        if not places:
            return {"error": f"No location found for {city}"}
        place = places[0]
        weather = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
            },
        )
        weather.raise_for_status()
        return {
            "location": place.get("name"),
            "country": place.get("country"),
            "current": weather.json().get("current", {}),
        }

if __name__ == "__main__":
    mcp.run()
