#%%
import glassdorscrape as gs
import pandas as pd
#%%
path = "C:/Users/fibia/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
df = gs.get_jobs('data scientist', 15, False, path, 15 )