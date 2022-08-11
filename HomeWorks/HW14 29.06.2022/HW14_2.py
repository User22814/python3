import psycopg2


# CREATE (INSERT)
############################################################################
conn = psycopg2.connect("dbname=new_postgres_db_hw14_29.06.2022 user=postgres password=qwerty228")
cur = conn.cursor()

# (28, False, 'Michael')

new_arr = [
    [27, False, 'Daniel'],
    [29, False, 'Azamat'],
    [22, True, 'Assel'],
    [18, False, 'Inkar'],
    [16, True, 'Amir'],
    [17, False, 'Annabel'],
    [19, True, 'Adrean'],
]

# print(new_arr)

# query_string = f"""
#     INSERT INTO public.new_postges_tb (age, is_have_money, name)
#     VALUES ({new_arr[0]}, {new_arr[1]}, '{new_arr[2]}')
#     """

# create data
for i in new_arr:
    query_string = f"""
    INSERT INTO public.new_postges_tb (age, is_have_money, name)
    VALUES ({i[0]}, {i[1]}, '{i[2]}')
    """

    cur.execute(query_string)
    conn.commit()  # применение данных после изменений

conn.close()
