from flask import Flask,render_template,request
import pandas
from geopy.geocoders import ArcGIS
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/templates", methods=['POST'])
def success():
    if request.method=='POST':
        file=request.files["file"]
        file.save(file.filename)
        df=pandas.read_csv(file.filename)
        print(df['address'][0])
        nom=ArcGIS()
        n=nom.geocode(df['address'][0])
        lon=n.longitude
        lat=n.latitude
        return render_template("index.html", lon=lon,lat=lat,df=df.to_html())

if __name__=="__main__":
    app.run(debug=True)
