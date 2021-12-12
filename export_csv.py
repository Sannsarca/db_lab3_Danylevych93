import csv
import psycopg2

username = 'Danylevych93'
password = 'qwerty228'
database = 'postgres'
host = 'localhost'
port = 5555

OUTPUT_FILE_T = 'Danylevych93_DB_{}.csv'

TABLES = [
    'country',
    'data_new',
    'years',
    'information'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])