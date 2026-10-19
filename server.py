import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Weather API Wrapper Server")

# Global cache for the required resource
LAST_WEATHER_CACHE = "No weather data fetched yet."

# --- 2 TOOLS ---

@mcp.tool()
def get_current_weather(city: str) -> str:
    """Get the current weather conditions for a given city.
    
    Args:
        city: The name of the city (e.g., 'London', 'Tokyo', 'New York').
    """
    global LAST_WEATHER_CACHE
    if not city.strip():
        raise ValueError("City name cannot be empty.")
    
    url = f"https://wttr.in/{city}?format=3"
    
    try:
        response = httpx.get(url, timeout=10.0)
        if response.status_code == 200:
            result = response.text.strip()
            LAST_WEATHER_CACHE = f"Cached Weather for {city}: {result}"
            return result
        else:
            return f"Could not fetch weather for {city}. Status code: {response.status_code}"
    except httpx.RequestError as e:
        return f"Network error occurred while reaching weather service: {str(e)}"

@mcp.tool()
def get_weather_forecast(city: str, days: int = 3) -> str:
    """Get a multi-day weather forecast for a city.
    
    Args:
        city: The name of the city.
        days: Number of days for the forecast (between 1 and 3).
    """
    if not city.strip():
        raise ValueError("City name cannot be empty.")
    if not (1 <= days <= 3):
        raise ValueError("Days must be between 1 and 3 for this free API tier.")
        
    url = f"https://wttr.in/{city}?0-{days}"
    
    try:
        response = httpx.get(url, timeout=10.0)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Could not fetch forecast. Status code: {response.status_code}"
    except httpx.RequestError as e:
        return f"Network error occurred: {str(e)}"

# --- 1 RESOURCE ---

@mcp.resource("weather://last-result")
def get_cached_weather() -> str:
    """Provides the cached result of the last fetched weather query."""
    return LAST_WEATHER_CACHE

# --- 1 PROMPT ---

@mcp.prompt()
def daily_briefing(city: str = "London") -> str:
    """A prompt template to generate a complete morning weather brief and packing/outfit recommendation."""
    return (
        f"Please check the current weather for {city} using your tools, "
        "review the cached weather resource, and provide a helpful morning briefing. "
        "Include outfit recommendations and whether I need an umbrella."
    )

if __name__ == "__main__":
    mcp.run()