from fastmcp import FastMCP
import requests
import os

mcp = FastMCP("Transport Info Server")

HERE_API_KEY = os.getenv("HERE_API_KEY")

@mcp.tool()
def get_transit_route(origin: str, destination: str):
    """
    Get public transport route between two locations.
    Example:
    origin="Delhi"
    destination="Gurgaon"
    """
    url = f"https://transit.router.hereapi.com/v8/routes?origin={origin}&destination={destination}&return=summary,actions&apikey={HERE_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error fetching data: {response.text}"

    return response.json()


@mcp.tool()
def get_nearby_stops(location: str):
    """
    Get nearby public transport stops for a location.
    Example:
    location="28.6139,77.2090" (Delhi Coordinates)
    """
    url = f"https://transit.router.hereapi.com/v8/stations?in={location}&apikey={HERE_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: {response.text}"

    return response.json()

if __name__ == "__main__":
    mcp.run()
