import scrape
import db_insert

my_scrape = scrape.Scrape()
df =my_scrape.scrape()
#print(df.info())

db_insert.insert_df(df)
