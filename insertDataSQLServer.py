"""
Create Time: 2020/3/27 9:56
Author: FengkaiXiao
"""

import pymssql
import random
NUM = 0
db = pymssql.connect(server='192.168.125.135', user='sa', password='xfk@626526', database='xfk_mssql_2', port=1433, charset='utf8')
cursor = db.cursor()

for i in range(100):
	Ageint = 20 + random.randint(0, 40)
	IMCONME = 10000 + random.randint(0, 1000)
	NUM += 1
	NAME ='name'+str(NUM)
	Nation ='CHINA', 'JAPAN', 'UK', 'USA', 'GERMAN', 'FRANCE', 'KOREA', 'BRAZIL'
	Lastname = 'SMTH','KOBE', 'MICHEAEL', 'JASON', 'FUCK', 'STUPID'
	Hobby = 'FOOTBALL', 'BASKETBALL', 'VOLLEBALL'
	COME = random.choice(Nation)
	LASTNAME = random.choice(Lastname)
	HOBBY = random.choice(Hobby)
	sql ="INSERT INTO xfk02 (id, first_name, middle_name, last_name, come_from, age, income, hobby) VALUES ('%d', '%s','%s','%s', '%s', '%d', '%d' ,'%s')"% (NUM, NAME, COME, LASTNAME, COME, Ageint, IMCONME,HOBBY)
	cursor.execute(sql)
	db.commit()
cursor.close()
db.close()

