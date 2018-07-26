import requests
import json

class Registrar:

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

cookie_str = r'__RequestVerificationToken=64TGmcVMXnI--UxgGh5mK4QCmxsRlh7TBPjoeaIXlllknmbY916toJW5NRwkpRWN9H8Kn4xtP-4cu-FSpYRe5YbpiiUOsMB6CcPhnhEkZfo1; ASP.NET_SessionId=drnw1myaweyjaf4j1tudmxbm; ' \
             r'User=UserName=lh8229238&Password=lh301415926; ' \
             r'HBHOSPITALCODE=0018'
#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

# data = {'DoctorId': '6101000210003001', 'registType': '1'}

#得到该医生的挂号ID和日期
def get_registrar_id(doctor_id):
    registrar = {}
    data = {'DoctorId': doctor_id ,
            'registType':'1'}
    response = requests.post('http://www.dyyy120.com/Clinic/GHGetClinicRegistList',data=data,headers=headers)
    jsonResult = json.loads(response.text)
    for registModel in jsonResult['RegistModelList']:
        if registModel['Status'] == 1:
            registrar = registModel
            break
    return registrar

# 6101000210003322
# print(get_registrar_id('6101000210003001'))

#准备挂号的数据：医生、时间、病人
def construction_registration_data(doctor_id,patienter):
    # registrar = {'ClinicDate': '2018-07-30', 'TimePartType': 0, 'Status': 1, 'ClinicLabelId': '6101000210003322', 'ClinicLabelType': 1, 'RsvModel': 1, 'BookedNums': 15, 'CountLimit': 30}
    registrar = get_registrar_id(doctor_id)

    if(any(registrar) == False):
        print("还没开始construction_registration_data")
        return {}

    form_data = {'clinicLabelId':registrar.get('ClinicLabelId'),
                 'timePartType':registrar.get('TimePartType'),
                 'clinicDate': registrar.get('ClinicDate')}
    response = requests.post('http://www.dyyy120.com/Clinic/GetBookSureModel', data=form_data, headers=headers,cookies = cookies)
    jsonResult = response.json()
    patientCards = json.loads(jsonResult['PatientCardJsons'])

    for personTmp in patientCards:
        if(personTmp['TrueName'] == patienter):
            person = personTmp
            break

    registration_data = {
                'param':'orderAPI',
                'hospitalId':'61010002',
                'patientId':person['PersonId'],
                'clinicLabelId':jsonResult['ClinicLabelId'],
                'clinicDate':jsonResult['ClinicDate'],
                'timePartType':str(jsonResult['TimePartType']),
                'timePart':jsonResult['TimePartList'][-1]['TimePart'],
                'channcelType':str(jsonResult['ChannelTypeId']),
                'rsvmodel':str(jsonResult['RsvModel']),
                'returnVisitId':'2',
                'symptom':' ',
                'cardnum':person['CardList'][-1]['CardNum'],
                'payChanel':'2'
                }
    return registration_data

print(construction_registration_data('6101000210027013','刘辉'))

# print(construction_registration_data('6101000210011004','刘辉'))

def start_registration(doctor_id,patienter):
    from_data = construction_registration_data(doctor_id, patienter)
    print(from_data)
    if(any(from_data) == False):
        print("还没开始start_registration")
        return
    response = requests.post('http://www.dyyy120.com/ajax.aspx', data=from_data, headers=headers,
                             cookies=cookies)
    print(response.json())

# start_registration('6101000210011004', '刘辉')


