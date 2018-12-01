from flask import Flask, request, render_template, session, redirect
import pandas as pd
import pygal

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
    map = create_data_map(df, df_country)
    return render_template("map.html", data=map.render_data_uri())

# Route that shows all bar graphs we have
@app.route('/bar')
def bar_page():
    df = get_data_frame()
    df_combined_tech = get_combined_tech()
    df_country = get_countries()
    df_combined_price = get_combined_price()
    bar = create_data_bar(df, df_country)
    tech_bar = create_tech_bar(df_combined_tech)
    price_bar = create_price_bar(df_combined_price)
    return render_template("bar.html", data=bar.render_data_uri(), tech_data=tech_bar.render_data_uri(), price_data=price_bar.render_data_uri())

# Route that shows the combined data we have worked with
@app.route('/data')
def data_page():
    df = get_data_frame()
    df_country = get_countries()
    return render_template("data.html", printers_data=df.to_html(classes=['table-sm', 'table-striped', 'table-dark']))

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

# Creating a map graph that displays how many 3-printers a country produces
def create_data_map(df, df_country):
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Produced 3D-Printers per Country'

    df_map = df.Country.unique()
    for countries in df_map:
        worldmap_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]), {
            countries.lower(): df.Country.value_counts()[countries]
        })

    return worldmap_chart

# Creating a bar graph that shows how many 3d-printers a country produces
def create_data_bar(df, df_country):
    line_chart = pygal.Bar()
    line_chart.title = '3D-Printers per country'

    df_map = df.Country.unique()
    for countries in df_map:
        line_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]),
                       df.Country.value_counts()[countries])
    return line_chart

# Creating a bar graph that shows what technology is used by how many 3d-printers
def create_tech_bar(df_combined_techs):
    line_chart = pygal.Bar()
    line_chart.title = 'Technology used by 995 3D-Printers'
    for tech in df_combined_techs.Technology.unique():
        line_chart.add(tech,
                       df_combined_techs.Technology.value_counts()[tech])
    return line_chart

# Creating a bar graph that shows how many 3d-printers are in what price range
def create_price_bar(df_combined_price):
    prices = df_combined_price.groupby(['Price'])['Price'].count()

    line_chart = pygal.Bar()
    line_chart.title = '3D-Printers prices'
    line_chart.add('Price not reported', prices['Price not reported'])
    line_chart.add('< 49000', prices['Less than $49.999'])
    line_chart.add('50000 - 99999', prices['$50.000 - $99.999'])
    line_chart.add('100000 - 249999', prices['$100.000 - $249.999'])
    line_chart.add('250000 - 499999', prices['$250.000 - $499.999'])
    line_chart.add('500000 - 999999', prices['$500.000 - $999.999'])
    return line_chart



if __name__ == "__main__":
    app.run(host='0.0.0.0')
