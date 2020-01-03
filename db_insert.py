import os
import sqlalchemy
PASSWORD = os.getenv("DB_PASSWORD")
def insert_df(df):
	engine = sqlalchemy.create_engine('postgresql://stevo517:' + DB_PASSWORD + '@localhost/stevo517')
	sqlalchemy.sql.expression.text("TRUNCATE TABLE web_scraping_table")
	sqlalchemy.sql.expression.insert(web_scraping_table, values=["foo", "bar", 1]
)	
