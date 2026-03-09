"""
Minimal Flask application for the Docker Network Operations Lab.

This app exposes a single route at the root ("/") that returns a
simple HTML page. In a real-world scenario, this could be expanded
into an operations dashboard that reports container status, metrics
or other network information.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """Return a simple HTML page with a heading and description."""
    return (
        "<h2>Docker Network Operations Dashboard</h2>"
        "<p>This Flask application is running inside a Docker container. "
        "It is fronted by an Nginx reverse proxy and connected to a shared volume. "
        "Use this dashboard to verify that your containers are communicating across the Docker network.</p>"
    )


if __name__ == "__main__":
    # Bind to all interfaces so Docker can map the port
    app.run(host="0.0.0.0", port=5000)
