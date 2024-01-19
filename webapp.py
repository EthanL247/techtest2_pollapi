from flask import Flask, render_template
import requests
import json

app = Flask("App")


@app.route('/voting')
def hello():
    response = requests.get('http://localhost:5000/voting')
    data = json.loads(response.text)
    return render_template('voting.html',data=data)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)