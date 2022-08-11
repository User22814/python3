import json

import psycopg2
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
content = response.content
json_data = content.decode()
posts = json.loads(json_data)


class Record:
    def __init__(self, row: dict):
        self.userId = row['userId']
        self.id = row['id']
        self.title = row['title']
        self.body = row['body']


conn = psycopg2.connect("dbname=new1_postgres_db user=postgres password=qwerty228")
cur = conn.cursor()
for row in posts:
    obj = Record(row=row)
    try:
        query_string = f"""
            INSERT INTO public.new1_postgres_tb (user_id, id_post, title, body)
            VALUES ('{obj.userId}', '{obj.id}', '{obj.title}', '{obj.body}')
            """
        cur.execute(query_string)
        conn.commit()
    except Exception as error:
        print(error)
        print(row)
conn.close()
