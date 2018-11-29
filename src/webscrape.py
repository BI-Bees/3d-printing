from requests import get
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv
import codecs

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

if __name__ == '__main__':

    table_content = []

    myFile = open('3d_printers_senvol.csv', 'w')

    raw_html = codecs.open("2A_Machine Search Results Table.html", 'r')
    html = BeautifulSoup(raw_html, 'html.parser')
    for table in html.select('table'):
        if table.get('id') == 'cbTable_500db065861ec6':
            th_list = []
            for th in table.select('th'):
                for a in th.select('a'):
                    print(a)
                    th_list.append(a.text)
            table_content.append(th_list)
            for tr in table.select('tr'):
                tr_list = []
                for td in tr.select('td'):
                    tr_list.append(td.text)
                table_content.append(tr_list)
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(table_content)
    myFile.close()

    # myFile = open('3d_printers.csv', 'w')
    #
    # raw_html = simple_get('https://www.3ders.org/pricecompare/3dprinters/')
    # html = BeautifulSoup(raw_html, 'html.parser')
    # for span in html.select('span'):
    #     if span.get('id') == 'Label_Products':
    #             for tr in span.select('tr'):
    #                 tr_list = []
    #                 for td in tr.select('td'):
    #                     tr_list.append(td.text)
    #                 table_content.append(tr_list)
    # print(table_content)
    # with myFile:
    #     writer = csv.writer(myFile)
    #     writer.writerows(table_content)
    # myFile.close()
    #
    # table_content = []
    # myFile = open('countries.csv', 'w')
    # countries_raw_html = simple_get('https://developers.google.com/public-data/docs/canonical/countries_csv')
    # countries_html = BeautifulSoup(countries_raw_html, 'html.parser')
    # div = countries_html.find("div", {"class": "devsite-article-body"})
    # th_list = []
    # for th in div.select('th'):
    #     th_list.append(th.text)
    # table_content.append(th_list)
    # for tr in div.select('tr'):
    #     tr_list = []
    #     for td in tr.select('td'):
    #         tr_list.append(td.text)
    #     table_content.append(tr_list)
    # print(table_content)
    # with myFile:
    #     writer = csv.writer(myFile)
    #     writer.writerows(table_content)
    # myFile.close()
