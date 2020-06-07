"""
Create Time: 2020/3/27 9:56
Author: FengkaiXiao
"""

import pymysql
import random
NUM = 0
db = pymysql.connect(host='192.168.125.135', user='root', passwd='root123456', db='raybass15', port=3306, charset='utf8')
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
	sql ="INSERT INTO test15(id, firstname, middlename, lastname, comefrom, age, income, hobby) VALUES ('%d', '%s','%s','%s', '%s', '%d', '%d' ,'%s')"% (NUM, NAME, COME, LASTNAME, COME, Ageint, IMCONME,HOBBY)
	cursor.execute(sql)
	db.commit()
cursor.close()
db.close()

