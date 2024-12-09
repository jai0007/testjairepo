from flask import Flask
from dash import Dash, html

# Flask instance
server = Flask(__name__)

# Dash instance
app = Dash(__name__, server=server)
app.layout = html.Div("Hello, Vercel! Jai here")

# Ensure the app runs on port 8080 for local testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
