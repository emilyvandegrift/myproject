 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

dat = pd.read_csv('data/gapminder_gdp_europe.csv')
oceania = pd.read_csv('data/gapminder_gdp_oceania.csv' , index_col = 'country')
asia = pd.read_csv('data/gapminder_gdp_asia.csv')

