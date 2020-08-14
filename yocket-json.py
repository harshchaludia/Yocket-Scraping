import requests
import time
import random
import sys
headers = {
    #AUTH = get it from any proxy portal for testing purpose
    'Authorization': 'Basic AUTH',
    'User-Agent': '<user-agent>',
    'Host': '<website-name>',
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

#proxyData = get it from any proxy portal for testing purpose
proxy = {'https': proxyData}
with open('datajson.txt','a') as jp:
    for i in range(5146,6220):
        try:
            response = requests.post('https://<website-name>/user-profiles/find/matching-profiles.json?page='+str(i),timeout=5, headers=headers,proxies=proxy, data=data)
            ptxt = response.text
            jp.write(ptxt+",")
            print(i)
            time.sleep(random.randint(1,4))
        except:
            print(sys.exc_info()[1])








