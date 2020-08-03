#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="disfactory_data", user="postgres",
                        password="postgres", host="127.0.0.1", port="5433")

print("Opened database successfully")

cur = conn.cursor()

lat = 24.9582182
lng = 121.4069907

sql = """
select id, distance
from (
    select id, 
    name, 
    ( 3959 * acos( cos( radians({target_lat}) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians({target_lng}) ) + sin( radians({target_lat}) ) * sin( radians( lat) ) ) ) 
    as distance
    from api_factory 
) as dt
where distance < 1.0 
order by distance asc
limit 100
""".format(target_lat=lat, target_lng=lng)

print(sql)

cur.execute(sql)
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
