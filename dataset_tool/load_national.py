#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd
import definitions

dfmg = pd.read_csv(definitions.BRASILIO_MG)
dfnt = pd.read_csv(definitions.BRASILIO_NT)

national = pd.concat([dfmg, dfnt]).reset_index().iloc[:, 1:]

# save
now = pd.Timestamp.now().strftime('update_%Y_%m_%d')

filename_pattern = f'blueteam_national_{now}.'
national.to_csv(filename_pattern + 'csv')
national.to_json(filename_pattern + 'json')

conn = sqlite3.connect(filename_pattern + 'db')
national.to_sql(name = 'blueteam_national', con = conn)
