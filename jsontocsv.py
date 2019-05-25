import ujson
file = open("sample.csv","w")
kd = {}
ka = {}
usrl = []
def extrd(d,kd,n=''):
    if type(d) is dict:
        for k in d:
            if(k=="posts" or k=="application_statuses" or k=="related_university_courses"):
                pass
            else:
                extrd(d[k],kd,n+k+"_")
    elif type(d) is list:
        i=0
        for k in d:
            extrd(k,kd,n + str(i) + '_')
            i+=1
    else:
        if(n[:-1]=="user_profile_gre_verbal_score" or n[:-1]=="user_profile_gre_verbal_score" or n[:-1]=="user_profile_gre_quant_score"
or n[:-1]=="user_profile_gre_awa_score"
or n[:-1]=="user_profile_en_exam_score"
or n[:-1]=="user_profile_en_exam_reading_score"
or n[:-1]=="user_profile_en_exam_writing_score"	
or n[:-1]=="user_profile_en_exam_listening_score"	
or n[:-1]=="user_profile_en_exam_speaking_score"
or n[:-1]=="user_profile_ug_score"	
or n[:-1]=="user_profile_work_experience_months"	
or n[:-1]=="user_profile_gre_score"	
or n[:-1]=="user_profile_en_exam_format"
or n[:-1]=="user_profile_ug_score_format"
or n[:-1]=="user_profile_undergrad_details"	
or n[:-1]=="application_statuses_university_course_university_url_alias"	
or n[:-1]=="application_statuses_university_course_university_name"	
or n[:-1]=="application_statuses_university_course_university_abbreviation"	
or n[:-1]=="application_statuses_status_text"	
or n[:-1]=="user_profile_visa_consulate_country"	
or n[:-1]=="user_profile_final_university_course_university_id"	
or n[:-1]=="user_profile_final_university_course_university_url_alias"	
or n[:-1]=="user_profile_final_university_course_university_name"	
or n[:-1]=="user_profile_final_university_course_university_abbreviation"):
            kd[n[:-1]]=str(d)
        
with open('datajson.txt','r') as jp:
    st = str(jp.read())
    y = ujson.loads(st)
    for i in range(0,len(y)):
        try:
            for li in kd:
                kd[li]="None"
            if len(y[i]["user"]["application_statuses"])!=0:
                usrst=""
                extrd(y[i]["user"],kd,'')
                for li in kd:
                    #print(li)
                    usrst = usrst + '"'+kd[li].replace("\n","").replace("\r","")+'",'
                #fw = '","'.join(kd.values())
                #file.write('"'+fw+'"'+"\n")
                for j in range(0,len(y[i]["user"]["application_statuses"])):
                    for li in ka:
                        ka[li]="None"
                    extrd(y[i]["user"]["application_statuses"][j],ka,"application_statuses_")  
                    for li in ka:
                        kd[li]=ka[li]
                    for li in kd:
                        file.write('"'+kd[li].replace("\n","").replace("\r","")+'",')
                    file.write("\n")             
        except:
            pass
    file.write('"'+'","'.join(kd.keys())+'"')  
    #file.write(',"'+'","'.join(ka.keys())+'"')
file.close()               
