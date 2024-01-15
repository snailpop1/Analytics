import urllib.request
urllib.request.urlretrieve("https://data.cdc.gov/api/views/9j2v-jamp/rows.csv?accessType=DOWNLOAD", "/Users/deepak/deathrates/data/raw/deathrates.csv")
urllib.request.urlretrieve("https://data.cdc.gov/api/views/9j2v-jamp/rows.json?accessType=DOWNLOAD", "/Users/deepak/deathrates/data/raw/metadata.json")