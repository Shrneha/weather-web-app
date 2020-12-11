from flask import Flask, render_template, request  #request object to get value of zip
import requests

app = Flask(__name__)



@app.route('/temperature' , methods = ["POST"] )
def temperature() :
    zipcode = request.form["zip"]
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',in&appid=efa16d818419a7254923390f8c98c1c5')
    #r = requests.get('http://samples.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=cbf40c31dc6e53a5b63069b956572b3a')
    json_object = r.json()
    #temperature = json_object
    temperature = json_object["main"]["temp"]
    temperature_f =temperature - 273.15
    #return str(temperature)
    #return json_object
    return render_template("temperature.html" , temp = temperature_f)

@app.route('/')
def indexx():
    return render_template("form_template.html")

if __name__ == '__main__' :
    app.run(debug=False)






