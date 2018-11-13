import json
from download import download, get_url_from_config_file
import os
import pandas as pd

with open('links.json') as fp:
    amazon_uk = json.load(fp)['UK']
    #amazon_us = json.load(fp)['US']
    #amazon_fr = json.load(fp)['FR']
    #amazon_jp = json.load(fp)['JP']
    #amazon_de = json.load(fp)['DE']
#download(amazon_uk)
#download(amazon_us)
#download(amazon_fr)
#download(amazon_jp)
#download(amazon_de)

file_name = os.path.basename(amazon_uk)
df = pd.read_csv(file_name, compression='gzip', error_bad_lines=False, sep='\t')
print(df.head())
