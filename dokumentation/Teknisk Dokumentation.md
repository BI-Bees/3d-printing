# Teknisk Dokument

Vi valgte at lave en hjemmeside som vores business gruppe kunne tilgå for at se hvilke data vi havde fundet, og diverse grafer som er lavet udfra dette.

## Server

Vi har brugt python og frameworket "flask" til at lave en web app. Den app har vi så deployet på DigitalOcean som kan ses her: http://167.99.131.56:5000/
Da denne app er meget simpel og vi vil have, så lille et "overhead" som muligt når det kommer til diverse frameworks og sikkerheds opsætninger, kører vi denne app via en python kommando på serveren. Vi har dog sat et cron-job op som tjekker om denne app kører og i tilfælde af at den ikke gør det, genstarter cron-jobbet serveren. Dette cron-job er sat op til at eksekvere hvert 15. minut.   

## Data Scraping

Vi har lavet et python script som downloadede html koden fra sider vi gerne ville have data fra. Derefter gemte vi det data vi ville have i diverse csv filer, sådan vi senere kunne bruge pandas til at behandle denne data.

## Data Behandling

Vi har brugt python og pandas til behandle dataen og brugt "Pygal" til at visualisere dette i diverse grafer
