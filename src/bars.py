import pygal
import pandas as pd

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

# Creating a bar graph that shows what technology is used by how many 3d-printers
def create_tech_bar(df_combined_techs):
    line_chart = pygal.Bar()
    line_chart.title = 'Technology used by 995 3D-Printers'
    for tech in df_combined_techs.Technology.unique():
        line_chart.add(tech,
                       df_combined_techs.Technology.value_counts()[tech])
    return line_chart

# Creating a bar graph that shows how many 3d-printers a country produces
def create_data_bar(df, df_country):
    line_chart = pygal.Bar()
    line_chart.title = '3D-Printers per country'

    df_map = df.Country.unique()
    for countries in df_map:
        line_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]),
                       df.Country.value_counts()[countries])
    return line_chart
