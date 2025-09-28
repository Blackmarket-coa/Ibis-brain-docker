from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def index():
    # Create a map object centered on Ferndale, MI
    # Coordinates are [Latitude, Longitude]
    start_coords = (42.4609, -83.1349)
    folium_map = folium.Map(location=start_coords, zoom_start=13)

    # Add a marker to the map for Ferndale
    folium.Marker(
        location=start_coords,
        popup="Ferndale, MI",
        tooltip="Click me!"
    ).add_to(folium_map)

    # Return the HTML representation of the map object
    return folium_map._repr_html_()

if __name__ == "__main__":
    # The host must be '0.0.0.0' to be accessible from outside the container
    app.run(host="0.0.0.0", port=8080)
