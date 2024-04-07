import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  input_features = [int(x) for x in request.form.values()]
  features_value = [np.array(input_features)]

  features_name = ['Pregnancies', 'BloodPressure','Glucose' 'SkinThickness',
       'insulin', 'BMI', 'DiabetesPedigreeFunction',
       'age']

  df = pd.DataFrame(features_value, columns=features_name)
  output = model.predict(df)

  if output == 4:
      res_val = "Has Breast Lump  and It is Cancerous (Malignant)"
  else:
      res_val = "Does not Have Breat Lump (Benign)"


  return render_template('index.html', prediction_text='Patient  {}'.format(res_val))

if __name__ == "__main__":
  app.run()
