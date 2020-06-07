"""
Create Time: 2020/4/9 17:57
Author: FengkaiXiao
"""
import datetime
#
# now = datetime.datetime.now()
# now.strftime('%Y-%m-%d %H:%M:%S')
#
# print(now)
import random

# import time
#
# #获取当前时间
# time_now = int(time.time())
# #转换成localtime
# time_local = time.localtime(time_now)
# #转换成新的时间格式(2016-05-09 18:59:20)
# dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
# print(dt)
#
# # now = datetime.datetime.now()
# # delta = datetime.timedelta(days=3)
# # n_days = now + delta
# # print(n_days.strftime('%Y-%m-%d %H:%M:%S'))
#
# now = datetime.datetime.now()
# delta = datetime.timedelta(minutes=1)
# n_seconds = now + delta
# print(n_seconds.strftime('%Y-%m-%d %H:%M:%S'))
#
# age = random.randint(18, 100)
# print(age)

org_ids = ('OrgId-0001','OrgId-0002','OrgId-0003')
org_nos = ('OrgNo-0001','OrgNo-0002','OrgNo-0003')
org_names = ('成都高新区中和街道党委','中和街道东寺社区党总支部','东寺社区第一党支部')
org_infos = [org_ids,org_nos,org_names]

for i in range(10):
	index = random.randint(0,2)
	print(index)
	org_ids = org_infos[0][index]
	org_nos = org_infos[1][index]
	org_names = org_infos[2][index]
	print(org_ids)

