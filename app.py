from flask import Flask, render_template, request
import pandas as pd
from keras.models import load_model
from get_date import get_input_date
from predict_sales import predict_sales
from sklearn.model_selection import train_test_split

app = Flask(__name__, static_url_path='/static')

model = load_model('model/model.h5')

df = pd.read_csv('dataset/penjualan_mobil_toyota.csv',index_col='Bulan',parse_dates=True)
df.index.freq='MS'

train, test = train_test_split(df, test_size=0.1, shuffle=False)
print(f"Train set length: {len(train)}")
print(f"Test set length: {len(test)}")

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        start_month = int(request.form['start_month'])
        end_month = int(request.form['end_month'])
        year = int(request.form['year'])
    
        start_date, end_date = get_input_date(start_month, end_month, year)

        result_prediction = predict_sales(model, train, start_date, end_date)
        result_prediction['Penjualan'] = result_prediction['Penjualan'].apply(lambda x: f'{x} unit')

        return render_template("predict.html", start_date=start_date, end_date=end_date, tables=[result_prediction.to_html(classes='data', index=False)], titles=result_prediction.columns.values)
    
    return render_template("predict.html", start_date='', end_date='', tables='', titles='')

if __name__=="__main__":
    app.run(debug=True)