import csv
import decimal
import psycopg2

username = 'Danylevych93'
password = 'qwerty228'
database = 'postgres'
host = 'localhost'
port = 5555

INPUT_CSV_FILE = '2016.csv'

query_0 = '''
CREATE TABLE data_new
(
    country_id INT NOT NULL,
    country character(100)  NOT NULL,
    region  character(100)  NOT NULL,
    position INT NOT NULL,
    points decimal NOT NULL,
    CONSTRAINT pk_data_new PRIMARY KEY (country_id)
)
'''

query_1 = '''
DELETE FROM data_new
'''

query_2 = '''
INSERT INTO data_new (country_id, country, region, position, points) VALUES (%s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
counter=0
with conn:
    cur = conn.cursor()
    cur.execute(query_0)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
#           price = float(row['Product_Price'].lstrip('$')) - incorrect handling of money value
            counter=counter+1
            values = (counter,row['Country'], row['Region'], row['Happiness Rank'], row['Happiness Score'])
            cur.execute(query_2, values)

    conn.commit()