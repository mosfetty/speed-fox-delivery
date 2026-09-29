import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    shipment = {
        "company_name": "Speed Fox Delivery",
        "tracking_number": "SFX-98342104",
        "status": "In Transit - International Hub",
        "origin": "USA, Manhattan",
        "destination": "Nigeria, Lagos",
        "carrier": "Speed Fox Global Freight",
        "estimated_delivery": "October 6, 2026"
    }
    return render_template('index.html', parcel=shipment)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
