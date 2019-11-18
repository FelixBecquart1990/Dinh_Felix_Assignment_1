from flask import Flask, render_template
import json
app = Flask(__name__)

# import the data from the JSON file
products = []
products = json.load(open("./products.json"))

@app.route('/')
def index():
  # render template with the data
  return render_template('index.html', products=products)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 