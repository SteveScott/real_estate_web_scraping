import psycopg2
from dotenv import load_dotenv
import os
import sqlalchemy 

load_dotenv(verbose=True)

PASSWORD = os.getenv("DB_PASSWORD")
def insert_df(df):
	engine = sqlalchemy.create_engine('postgresql://stevo517:' + PASSWORD + '@localhost/stevo517')
	connection = engine.connect()
	print("engine: " + str(engine))
	sqlalchemy.sql.expression.text("TRUNCATE TABLE web_scraping_table;")
	#result = connection.execute("INSERT INTO web_scraping_table (address, bedroom, price) VALUES('foo', 1, 500);")
	for index, row in df.iterrows():
		connection.execute("INSERT INTO web_scraping_table(address, bedroom, price) VALUES (" + "'" + row['Address'] + "'" + ", " + str(row['Bed']) + ", "  + "'" + str(row['Price'])+"'"+");")
	connection.close()
	#sqlalchemy.sql.expression.insert(web_scraping_table, values=["foo", "bar", 1]
	
