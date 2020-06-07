"""
Create Time: 2020/3/27 9:56
Author: FengkaiXiao
"""
import datetime
import pymysql
import random

db = pymysql.connect(host='192.168.125.135', user='root', passwd='root123456', db='party_dev', port=3306, charset='utf8')
cursor = db.cursor()

for i in range(10000):
	# 共用参数
	id = i + 1
	def isPassed(learn_fraction):
		if(learn_fraction<60):
			is_passed = 0
		else:
			is_passed = 1
		return is_passed
	org_ids = ('OrgId-0001','OrgId-0002','OrgId-0003')
	org_nos = ('OrgNo-0001','OrgNo-0002','OrgNo-0003')
	org_names = ('成都高新区中和街道党委','中和街道东寺社区党总支部','东寺社区第一党支部')
	org_infos = [org_ids,org_nos,org_names]
	index = random.randint(0,2)
	print(index)
	org_id = org_infos[0][index]
	org_no = org_infos[1][index]
	org_name = org_infos[2][index]
	print(org_id,org_no,org_name)
	is_deleteds = [0,1]
	is_deleted = random.choice(is_deleteds)

	time_interval = random.randint(1,10)
	now = datetime.datetime.now()
	delta1 = datetime.timedelta(minutes=-time_interval)
	delta2 = datetime.timedelta(minutes=time_interval)
	create_time = now + delta1
	update_time = now + delta2
	create_time = create_time.strftime('%Y-%m-%d %H:%M:%S')
	update_time = update_time.strftime('%Y-%m-%d %H:%M:%S')
	fourID = random.randint(1000, 9000)

	# basic_party_org
	# id = i + 1
	# pid = ''
	# # org_id = 'OrgId-0001'
	# # org_no = 'OrgNo-0001'
	# # org_name = '成都高新区中和街道党委'
	# org_contact_name = '组织联系名称-' + str(id)
	# org_contact_phone = '1880000' + str(fourID)
	# org_types = [0,1,2,3,4,5,6,7,8,9,10]
	# org_statuss = [1,2]
	# org_build_situation = 'perfect-' + str(id)
	# org_desc = '描述-' + str(id)
	# unit_name = '单位名称-' + str(id)
	# unit_category = '非公有经济控制'
	# uniform_social_credit_code = '代码-' + str(id)
	# party_secretary = 'PartySecretary-' + str(id)
	# update_time = update_time
	# create_time = create_time
	# org_type = random.choice(org_types)
	# org_status = random.choice(org_statuss)

	# basic_party_org
	# id = i + 1
	party_org_id = id
	# party_org_id = 'OrgId-15579'
	archives_no = 'archivesNo-' + str(id)
	name = 'Kevin-' + str(id)
	age = random.randint(18, 100)
	age = age
	genders = [0,1]
	delta3 = datetime.timedelta(weeks=-age*52)
	birthday = now + delta3
	birthday = birthday.strftime('%Y-%m-%d %H:%M:%S')
	birthday = birthday
	nation = '参照民族代码表'
	identity_no = '22222222200000' + str(fourID)
	education_code = '参照学历代码'
	college = '成都理工学'
	party_statuss = [1,2]
	personnel_categorys = [1,2]
	address = '四川成都'
	is_lost_contacts = [0,1]
	# is_deleteds = [0,1]
	update_time = update_time
	create_time = create_time
	# org_no = 'OrgNo-15579'
	# org_name = 'OrgName-15579'
	delta4 = datetime.timedelta(weeks=-3*52)
	accession_time = now + delta4
	accession_time = accession_time.strftime('%Y-%m-%d %H:%M:%S')
	accession_time = accession_time
	join_party_time = accession_time
	delta5 = datetime.timedelta(weeks=1*52)
	accession_time = datetime.datetime.strptime(accession_time, '%Y-%m-%d %H:%M:%S')
	correction_time = accession_time + delta5
	correction_time = correction_time.strftime('%Y-%m-%d %H:%M:%S')
	correction_time = correction_time
	post = '参照岗位代码表'
	social_stratum = '参照新的社会阶层表'
	is_farmers = [0,1]
	phone = '1315012' + str(fourID)
	domicile_location = '四川成都'
	lost_times = create_time
	gender = random.choice(genders)
	party_status = random.choice(party_statuss)
	personnel_category = random.choice(personnel_categorys)
	is_lost_contact = random.choice(is_lost_contacts)
	# is_deleted = random.choice(is_deleteds)
	is_farmer = random.choice(is_farmers)
	lost_time = lost_times

	# record_party_activity
	# id = i + 1
	# org_no = 'OrgNo-10'
	# org_name = 'OrgName-10'
	# archives_no = 'archivesNo-' + str(id)
	# name = '萧氏之-' + str(i)
	party_member_id = id
	activity_theme = '学习强国-' + str(i)
	activity_time = create_time
	activity_address = '四川成都'
	apply_time = create_time
	is_summarys = [0,1]
	# is_deleteds = [0,1]
	# update_time = update_time
	# create_time = create_time
	is_summary = random.choice(is_summarys)
	# is_deleted = random.choice(is_deleteds)

	# record_party_fee
	# id = i + 1
	# party_member_id = id
	# party_org_id = 15757742658616
	pay_time = create_time
	pay_need_amount = 1234.00
	pay_amount = 1234.00
	is_extensions = [0,1]
	operator_name = '习大大-' + str(i)
	# is_deleteds = [0,1]
	update_time = update_time
	create_time = create_time
	# name = '萧氏之-' + str(i)
	# archives_no = 'archivesNo-' + str(id)
	# org_no = 'OrgNo-10'
	# org_name = 'OrgName-10'
	is_extension = random.choice(is_extensions)
	# is_deleted = random.choice(is_deleteds)

	# record_party_learn
	# id = i + 1
	# party_member_id = id
	# org_no = 'OrgNo-10'
	# org_name = 'OrgName-10'
	# archives_no = 'archivesNo-' + str(id)
	# name = '萧氏之-' + str(i)
	learn_channel = id
	learn_theme = '学习强国-' + str(i)
	learn_time = 66.6
	learn_fraction = float(random.randint(1, 100))
	# is_deleteds = [0,1]
	# is_deleted = random.choice(is_deleteds)
	update_time = update_time
	create_time = create_time
	is_passed = isPassed(learn_fraction)

	# sql_1 = "INSERT INTO `party_dev`.`basic_party_org`(`id`, `pid`, `org_id`, `org_no`, `org_name`, `org_contact_name`, `org_contact_phone`, `org_type`, `org_status`, `org_build_situation`, `org_desc`, `unit_name`, `unit_category`, `uniform_social_credit_code`, `party_secretary`, `is_deleted`, `update_time`, `create_time`) VALUES ('%d', '%s','%s','%s', '%s','%s','%s','%d', '%d', '%s','%s','%s', '%s', '%s', '%s' ,'%d','%s', '%s')"% (id, pid, org_id, org_no, org_name, org_contact_name, org_contact_phone, org_type, org_status, org_build_situation, org_desc, unit_name, unit_category, uniform_social_credit_code, party_secretary, is_deleted, update_time, create_time)
	sql_2 = "INSERT INTO `party_dev`.`basic_party_member`(`id`, `party_org_id`, `archives_no`, `name`, `age`, `gender`, `birthday`, `nation`, `identity_no`, `education_code`, `college`, `party_status`, `personnel_category`, `address`, `is_lost_contact`, `is_deleted`, `update_time`, `create_time`, `org_no`, `org_name`, `accession_time`, `join_party_time`, `correction_time`, `post`, `social_stratum`, `is_farmer`, `phone`, `domicile_location`, `lost_time`)  VALUES ( '%d', '%d','%s','%s', '%d','%d','%s','%s', '%s', '%s','%s','%d', '%d', '%s', '%d' ,'%d','%s', '%s','%s', '%s','%s','%s', '%s','%s','%s','%d', '%s', '%s','%s')"% (id, party_org_id, archives_no, name, age, gender, birthday, nation, identity_no, education_code, college, party_status, personnel_category, address, is_lost_contact, is_deleted, update_time, create_time, org_no, org_name, accession_time, join_party_time, correction_time, post, social_stratum, is_farmer, phone, domicile_location, lost_time)
	sql_3 = "INSERT INTO `party_dev`.`record_party_activity`(`id`, `org_no`, `org_name`, `archives_no`, `name`, `party_member_id`, `activity_theme`, `activity_time`, `activity_address`, `apply_time`, `is_summary`, `is_deleted`, `update_time`, `create_time`) VALUES ( '%d','%s','%s','%s','%s','%d','%s','%s','%s','%s','%d','%d','%s','%s')"% (id, org_no, org_name, archives_no, name, party_member_id, activity_theme, activity_time, activity_address, apply_time, is_summary, is_deleted, update_time, create_time)
	sql_4 = "INSERT INTO `party_dev`.`record_party_fee`(`id`, `party_member_id`, `party_org_id`, `pay_time`, `pay_need_amount`, `pay_amount`, `is_extension`, `operator_name`, `is_deleted`, `update_time`, `create_time`, `name`, `archives_no`, `org_no`, `org_name`) VALUES ( '%d','%d','%d','%s','%.2f','%.2f','%d','%s','%d','%s','%s','%s','%s','%s','%s')"% (id,party_member_id,party_org_id,pay_time,pay_need_amount,pay_amount,is_extension,operator_name,is_deleted,update_time,create_time,name,archives_no,org_no,org_name)
	sql_5 = "INSERT INTO `party_dev`.`record_party_learn`(`id`, `party_member_id`, `org_no`, `org_name`, `archives_no`, `name`, `learn_channel`, `learn_theme`, `learn_time`, `learn_fraction`, `is_deleted`, `update_time`, `create_time`,`is_passed`)  VALUES ( '%d','%d','%s','%s','%s','%s','%d','%s','%.1f','%.1f','%d','%s','%s','%d')"% (id, party_member_id, org_no, org_name, archives_no, name, learn_channel, learn_theme, learn_time, learn_fraction, is_deleted, update_time, create_time,is_passed)

	# cursor.execute(sql_1)
	cursor.execute(sql_2)
	cursor.execute(sql_3)
	cursor.execute(sql_4)
	cursor.execute(sql_5)
	db.commit()
cursor.close()
db.close()