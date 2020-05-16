import requests
import time
import random
import sys
headers = {
    #AUTH = get it from any portal
    'Authorization': 'Basic AUTH',
    'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G925F Build/KOT49H)',
    'Host': 'yocket.in',
}

params = (
    ('page', '3'),
)

data = {
  'user_id': '',
  'applications': '',
  'gre_score': '',
  'term': '',
  'year': '',
  'gre_date[year]': '',
  'gre_date[month]': '',
  'gre_date[day]': '',
  'en_exam_key': '',
  'en_exam_score': '',
  'ug_score': '',
  'ug_score_key': '',
  'work_experience_months': '0',
  'tpp_key': '',
  'visa_status': '',
  'interested_course_group_id': '',
  'application_status': '0'
}
proxy = {'https': 'https://ncUdx7:FC0pYy@186.65.114.108:9794/'}
with open('datajson.txt','a') as jp:
    for i in range(5146,6220):
        try:
            response = requests.post('https://yocket.in/user-profiles/find/matching-profiles.json?page='+str(i),timeout=5, headers=headers,proxies=proxy, data=data)
            ptxt = response.text
            jp.write(ptxt+",")
            print(i)
            time.sleep(random.randint(1,4))
        except:
            print(sys.exc_info()[1])








