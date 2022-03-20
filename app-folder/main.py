from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('new-quote') == 'Quote':

            df = pd.read_csv('app-folder/assets/billionaire-quotes.csv', header=None)
            row = df.sample()

            billionaire = row.iat[0,0]
            quote = row.iat[0,1]

            return render_template('home.html', billionaire=billionaire, quote=quote)

    # Upon opening webpage for the first time
    df = pd.read_csv('assets/billionaire-quotes.csv', header=None)
    row = df.sample()

    billionaire = row.iat[0,0]
    quote = row.iat[0,1]

    return render_template('home.html', billionaire=billionaire, quote=quote)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080) 