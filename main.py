from dotenv import load_dotenv
import scrape
import db_insert

load_dotenv()

my_scrape = scrape.Scrape()
df = my_scrape.scrape()
#print(df.info())
db_insert.insert_df(df)
