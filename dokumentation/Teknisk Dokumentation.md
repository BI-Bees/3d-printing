# Teknisk Dokument

Vi har valgt at lave en hjemmeside vores business gruppe kan tilgå for at se hvilke data vi har fundet, samt de grafer der er lavet udfra dette.

## Server

Vi har brugt python og frameworket "flask" til at lave en web app. Den app har vi deployet på DigitalOcean som kan ses her: http://167.99.131.56:5000/

Da denne app er meget simpel og vi vil have, så lille et "overhead" som muligt når det kommer til diverse frameworks og sikkerheds opsætninger, kører vi denne app via en python kommando på serveren. Vi har dog sat et cron-job op som tjekker om denne app kører og i tilfælde af at den ikke gør det, genstarter cron-jobbet appen. Dette cron-job er sat op til at eksekvere hvert 15. minut.
De vi arbejder med en simpel opsætning skal vi manuelt ind på serveren, opdatere filerne, og genstarte web appen.  

## Data Sources

Vi har lavet et python script som downloader html koden fra de sider vi gerne ville have data fra. Derefter gemmer vi dette data vi skal bruge, i diverse csv filer, så vi kan bruge python og pandas til at behandle denne data.

De sider som vi har brugt data fra kan ses herunder:

* [Senvol.com](http://senvol.com/machine-search/)

* [3ders.org](https://www.3ders.org/pricecompare/3dprinters/)

* [developers.google.com](https://developers.google.com/public-data/docs/canonical/countries_csv)

Derudover kan alle CSV filer vi har genereret findes i mappen [dataset.](https://github.com/BI-Bees/3d-printing/tree/master/dataset)

## Data Behandling

Vi har brugt python og pandas til behandle dataen og brugt "Pygal" til at visualisere dette i diverse grafer
