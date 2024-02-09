from model import clean_data,rfc
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample

app = Flask(__name__)

# Your existing route for rendering the form
@app.route('/')
def home():
    return render_template('index.html')


# Your existing route for handling form submission
@app.route('/submit',methods=['POST'])
def submit():
    title = request.form.get('title')
    norating1 = request.form.get('norating1')
    noreviews1 = request.form.get('noreviews1')
    rating = request.form.get('rating')
    star_1f = request.form.get('star_1f')
    star_2f = request.form.get('star_2f')
    star_3f = request.form.get('star_3f')
    star_4f = request.form.get('star_4f')
    star_5f = request.form.get('star_5f')
    maincateg = request.form.get('maincateg')
    platform = request.form.get('platform')
    price1 = request.form.get('price1')
    actprice = request.form.get('actprice')




    # Preprocess the form data
    user_input_df = pd.DataFrame({
        'title': [title],
        'Rating': [rating],
        'maincateg':[maincateg],
        'platform':[platform],
        'price1':[price1],
        'actprice1':[actprice],
        'norating1': [norating1],
        'noreviews1': [noreviews1],
        'star_5f': [star_5f],
        'star_4f': [star_4f],
        'star_3f' : [star_3f],
        'star_2f': [star_2f],
        'star_1f': [star_1f],
    })

    
    data = user_input_df.copy()
    data.drop(['title'],axis=1,inplace=True)
    data = clean_data(data)
    print(data)
    pred = rfc.predict(data)
    if pred ==0 :
        result = f"Users are not statified with {user_input_df.at[0,'title']}"
    else:
       result = f"Users are statified with {user_input_df.at[0,'title']}"

    return render_template('result.html',result_text=result)

if __name__=='__main__':
    app.run(debug=True)
