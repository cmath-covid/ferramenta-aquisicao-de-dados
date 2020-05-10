#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd
import definitions

df = pd.read_csv('data/daily-cases-covid-19.csv')

countries = "|".join(definitions.BLUETEAM_LOCATION_INTERNATIONAL)
countries_blueteam = df[df['Entity'].str.contains(countries, case = False)]

# save
now = pd.Timestamp.now().strftime('update_%Y_%m_%d')

filename_pattern = f'blueteam_international_{now}.'
countries_blueteam.to_csv(filename_pattern + 'csv')
countries_blueteam.to_json(filename_pattern + 'json')

conn = sqlite3.connect(filename_pattern + 'db')
countries_blueteam.to_sql(name = 'blueteam_international', con = conn)
