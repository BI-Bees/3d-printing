import pygal
import pandas as pd

# Creating a bar graph that shows what technology is used by how many 3d-printers
def create_tech_bar(df_combined_techs):
    line_chart = pygal.Bar()
    line_chart.title = 'Teknologier brugt af 3D-printere'
    for tech in df_combined_techs.Technology.unique():
        line_chart.add(tech,
                       df_combined_techs.Technology.value_counts()[tech])
    return line_chart

# Creating a bar graph that shows how many 3d-printer manufacturers there are in each country
def create_data_bar(df, df_country):
    line_chart = pygal.Bar()
    line_chart.title = '3D-Printer producenter per land'

    df_map = df.Country.unique()
    for countries in df_map:
        line_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]),
                       df.Country.value_counts()[countries])
    return line_chart

# Creating a bar graph that shows how many 3d-printers are in what price range
def create_price_bar(df_combined_price):
    prices = df_combined_price.groupby(['Price'])['Price'].count()

    line_chart = pygal.Bar()
    line_chart.title = 'Prisfordeling for 3D-printere'
    line_chart.add('Price not reported', prices['Price not reported'])
    line_chart.add('< 49000', prices['Less than $49.999'])
    line_chart.add('50000 - 99999', prices['$50.000 - $99.999'])
    line_chart.add('100000 - 249999', prices['$100.000 - $249.999'])
    line_chart.add('250000 - 499999', prices['$250.000 - $499.999'])
    line_chart.add('500000 - 999999', prices['$500.000 - $999.999'])
    return line_chart

def create_price_country_bar(df_combined_price):
    priceCountry = df_combined_price.groupby(['Country', 'Price'])['Price'].count()
    c_unique = df_combined_price.Country.unique()

    line_chart = pygal.Bar()
    line_chart.title = 'Prisfordelingen for 3D-printere per land'
    line_chart.x_labels = ['Price not reported', '< 49000', '50000-99999', '100000-249999', '250000-499999', '500000-999999']
    for c in c_unique:
        c_values = [None,None,None,None,None,None]
        for country in priceCountry.index:
            if c == country[0]:
                if country[1] == 'Price not reported':
                    c_values[0] = priceCountry.get(country)
                if country[1] == 'Less than $49.999':
                    c_values[1] = priceCountry.get(country)
                if country[1] == '$50.000 - $99.999':
                    c_values[2] = priceCountry.get(country)
                if country[1] == '$100.000 - $249.999':
                    c_values[3] = priceCountry.get(country)
                if country[1] == '$250.000 - $499.999':
                    c_values[4] = priceCountry.get(country)
                if country[1] == '$500.000 - $999.999':
                    c_values[5] = priceCountry.get(country)
        line_chart.add(c, c_values)
    return line_chart
