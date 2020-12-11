from flask import Flask, render_template, request  #request object to get value of zip
import requests

app = Flask(__name__)



@app.route('/temperature' , methods = ["POST"] )
def temperature() :
    # Request ZIP code from user 
    zipcode = request.form["zip"]
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',in&appid=####################################')
    json_object = r.json()
    temperature = json_object["main"]["temp"]
    temperature_f =temperature - 273.15
    return render_template("temperature.html" , temp = temperature_f)

@app.route('/')
def indexx():
    return render_template("form_template.html")

if __name__ == '__main__' :
    app.run(debug=False)






