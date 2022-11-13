import pickle,json
import numpy as np
try:
    import config
except:
    pass

class titanic():
    def __init__(self,Pclass,Age,Sibsp,Parch,Fare,Gender_male,Embarked):
        self.Pclass=Pclass
        self.Age=Age
        self.Sibsp=Sibsp
        self.Parch=Parch
        self.Fare=Fare
        self.Gender_male=Gender_male
        self.Embarked='Embarked_'+Embarked

    def load_model(self):

        try:
            
            with open(config.MODEL_PATH,"rb") as f:
                self.random_model=pickle.load(f)
                
            with open(config.JSON_PATH,"r") as m:
                self.column_data=json.load(m)
         
        except:
            
            with open ('random_model.pkl','rb') as f:
                self.random_model=pickle.load(f)
   
            with open ('column_data.json','r') as m:
                self.column_data=json.load(m)
    
    def prediction(self):
        self.load_model()
        Embarked_index=self.column_data['columns'].index(self.Embarked)
        array=np.zeros(len(self.column_data['columns']))
        array[0]=self.Pclass
        array[1]=self.Age
        array[2]=self.Sibsp
        array[3]=self.Parch
        array[4]=self.Fare
        array[5]=self.column_data['Gender_male'].get(self.Gender_male)
        array[Embarked_index]=1

        print('test_array',array)
        result=self.random_model.predict([array])
        print(result)
        return result
if __name__=="__main__":
    pred=titanic(1,49,1,0,7.17,'female',"Q")
    pred.prediction()


