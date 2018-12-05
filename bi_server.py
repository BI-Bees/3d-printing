from flask import Flask, request, render_template, session, redirect, send_file
import pandas as pd
import pygal
import sys
sys.path.insert(0, 'src/')
import bars
import maps

app = Flask(__name__)

# Used as main page
@app.route('/')
def home_page():
    return render_template("index.html")

# Route that shows all map graphs we have
@app.route('/map')
def map_page():
    df = get_data_frame()
    df_country = get_countries()
    map = maps.create_data_map(df, df_country)
    return render_template("map.html", data=map.render_data_uri())

# Route that shows all bar graphs we have
@app.route('/bar')
def bar_page():
    df = get_data_frame()
    df_combined_tech = get_combined_tech()
    df_country = get_countries()
    df_combined_price = get_combined_price()
    bar = bars.create_data_bar(df, df_country)
    tech_bar = bars.create_tech_bar(df_combined_tech)
    price_bar = bars.create_price_bar(df_combined_price)
    price_country_bar = bars.create_price_country_bar(df_combined_price)
    return render_template("bar.html", data=bar.render_data_uri(), tech_data=tech_bar.render_data_uri(), price_data=price_bar.render_data_uri(), price_country_data=price_country_bar.render_data_uri())

# Route that shows the combined data we have worked with
@app.route('/data')
def data_page():
    df = get_data_frame()
    df_country = get_countries()
    return render_template("data.html", printers_data=df.to_html(classes=['table-sm', 'table-striped', 'table-dark']))

@app.route("/data/<path>")
def DownloadLogFile (path = None):
    return send_file('dataset/' + path, as_attachment=True)

# Returning csv file
def get_data_frame():
    return pd.read_csv('dataset/printers_unique_country.csv')

# Returning csv file
def get_countries():
    return pd.read_csv('dataset/countries.csv')

# Returning csv file
def get_combined_tech():
    return pd.read_csv('dataset/printers_combined_tech.csv')

# Returning csv file
def get_combined_price():
    return pd.read_csv('dataset/printers_combined_price.csv')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
