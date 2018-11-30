from flask import Flask, request, render_template, session, redirect
import pandas as pd
import pygal

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/map')
def map_page():
    df = get_data_frame()
    df_country = get_countries()
    map = create_data_map(df, df_country)
    return render_template("map.html", data=map.render_data_uri())

@app.route('/bar')
def bar_page():
    df = get_data_frame()
    df_combined_tech = get_combined_tech()
    df_country = get_countries()
    bar = create_data_bar(df, df_country)
    tech_bar = create_tech_bar(df_combined_tech)
    return render_template("bar.html", data=bar.render_data_uri(), tech_data=tech_bar.render_data_uri())

@app.route('/data')
def data_page():
    df = get_data_frame()
    df_country = get_countries()
    return render_template("data.html", printers_data=df.to_html(classes=['table-sm', 'table-striped', 'table-dark']))


def get_data_frame():
    return pd.read_csv('dataset/printers_unique_country.csv')

def get_countries():
    complete_data = 'dataset/countries.csv'
    return pd.read_csv(complete_data)

def get_combined_tech():
    return pd.read_csv('dataset/printers_combined_tech.csv')

def create_data_map(df, df_country):
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Produced printers per country'

    df_map = df.Country.unique()
    for countries in df_map:
        worldmap_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]), {
            countries.lower(): df.Country.value_counts()[countries]
        })

    return worldmap_chart

def create_data_bar(df, df_country):
    line_chart = pygal.Bar()
    line_chart.title = 'Printers per country'

    df_map = df.Country.unique()
    for countries in df_map:
        line_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]),
                       df.Country.value_counts()[countries])
    return line_chart

def create_tech_bar(df_combined_techs):
    line_chart = pygal.Bar()
    line_chart.title = 'Techs used by 995 printers'
    for tech in df_combined_techs.Technology.unique():
        line_chart.add(tech,
                       df_combined_techs.Technology.value_counts()[tech])
    return line_chart
