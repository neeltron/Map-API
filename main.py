from flask import Flask, render_template, request, make_response, redirect, url_for
from opencage.geocoder import OpenCageGeocode
import folium as f
import os

ocapi = os.environ['ocapi']
geocoder = OpenCageGeocode(ocapi)

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == "POST":
    title = request.form.get('title')
    query = title
    results = geocoder.geocode(query)
    return str(results[0]['geometry']['lat'])
  return render_template('index.html')



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
