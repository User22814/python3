import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=new_postgres_db_hw14_29.06.2022 user=postgres password=qwerty228")  # localhost (127.0.0.1 / 192.168.1.121)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query

# read data
cur.execute("""
SELECT * FROM public.new_postges_tb
WHERE age > 20
ORDER BY age ASC
""")

# Retrieve query results
records = cur.fetchall()

# print(records)
# print(type(records))

for i in records:
    print(i)
    # print(type(i))

conn.close()
