from flask import Flask,render_template,request
from Model.utils import titanic
import config

app=Flask(__name__)
@app.route('/')
def sachin():
    return render_template("home.html")

@app.route('/api',methods=["POST"])
def sms():
    Input=request.form.get
    Pclass=float(Input('Pclass'))
    Age=int(Input('Age'))
    Sibsp=Input('Sibsp')
    Parch=float(Input('Parch'))
    Fare=float(Input('Fare'))
    Gender_male=Input('Gender_male')
    Embarked=Input('Embarked')
    
    ans=titanic(Pclass,Age,Sibsp,Parch,Fare,Gender_male,Embarked)
    action=ans.prediction()
    
    return render_template("home.html",predict=action)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)
