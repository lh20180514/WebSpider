import requests
import json
import time
import schedule
import datetime

class Registrar:
    headers = {
        'Connection': 'keep-alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        }

    def __init__(self, doctorId, patienter, cookieStr):
        self.doctorId = doctorId
        self.patienter = patienter
        self.cookies = self.transCookie(cookieStr)

    # 字符串cookie转换为字典类型
    def transCookie(self, cookieStr):
        cookies = {}
        for line in cookieStr.split(';'):
            # split 1表示分隔的次数为1次，
            # 存在User=UserName=lh8229238，分隔1次为(User,UserName=lh8229238)
            key, value = line.split('=', 1)
            cookies[key] = value
        return cookies

    # 得到该医生的挂号ID和日期，对于抢号来说默认取一个即可
    def getRegistrarId(self):
        registrar = {}
        formData = {'DoctorId': self.doctorId, 'registType': '1'}

        start = time.clock()
        response = requests.post('http://www.dyyy120.com/Clinic/GHGetClinicRegistList',
                                 data=formData, headers=self.headers)
        end = time.clock()
        print('GHGetClinicRegistList Running time: %s Seconds' % (end - start))

        if response.status_code == 200:
            # json.dumps  将Python对象编码成JSON字符串
            # json.loads  将已编码的JSON字符串解码为Python对象
            # json.loads(response.text)等同 response.json()
            jsonResult = json.loads(response.text)
            for registModel in jsonResult['RegistModelList']:
                if registModel['Status'] == 1:
                    registrar = registModel
                    break
        else:
            print('getRegistrarId 请求错误: ' + response.text)
        return registrar

    # 准备挂号的数据：医生、时间、病人
    def constructionRegistrationData(self):
        print(str(datetime.datetime.now()))
        # registrar = {'ClinicDate': '2018-07-30', 'TimePartType': 0, 'Status': 1, 'ClinicLabelId': '6101000210003322', 'ClinicLabelType': 1, 'RsvModel': 1, 'BookedNums': 15, 'CountLimit': 30}
        registrationData = {}
        registrar = self.getRegistrarId()

        if any(registrar) == False:
            print("没有获取到医生的挂号ID，可能还没有放号！")
            return registrationData

        formData = {'clinicLabelId': registrar.get('ClinicLabelId'),
                     'timePartType': registrar.get('TimePartType'),
                     'clinicDate': registrar.get('ClinicDate')}

        start = time.clock()
        response = requests.post('http://www.dyyy120.com/Clinic/GetBookSureModel', data=formData, headers=self.headers,
                                 cookies=self.cookies)
        end = time.clock()
        print('GetBookSureModel Running time: %s Seconds' % (end - start))

        if response.status_code == 200:
            # json.dumps  将Python对象编码成JSON字符串
            # json.loads  将已编码的JSON字符串解码为Python对象
            # json.loads(response.text)等同 response.json()
            jsonResult = json.loads(response.text)

            if jsonResult['ReturnInfo']['Result'] == 2:
                print('constructionRegistrationData :' + jsonResult['ReturnInfo']['ResultMsg'])
                return registrationData

            patientCards = json.loads(jsonResult['PatientCardJsons'])

            # 得到挂号病人的详细信息
            for personTmp in patientCards:
                if personTmp['TrueName'] == self.patienter:
                    person = personTmp
                    break

            if any(person):
                registrationData = {'param': 'orderAPI',
                                    'hospitalId': '61010002',
                                    'patientId': person['PersonId'],
                                    'clinicLabelId': jsonResult['ClinicLabelId'],
                                    'clinicDate': jsonResult['ClinicDate'],
                                    'timePartType': str(jsonResult['TimePartType']),
                                    # 'timePart': jsonResult['TimePartList'][-1]['TimePart'],
                                    'TimePartList': jsonResult['TimePartList'],
                                    'channcelType': str(jsonResult['ChannelTypeId']),
                                    'rsvmodel': str(jsonResult['RsvModel']),
                                    'returnVisitId': '2',
                                    'symptom': ' ',
                                    'cardnum': person['CardList'][-1]['CardNum'],
                                    'payChanel': '2'}
            else:
                print("没有找到挂号的病人")
        else:
            print('constructionRegistrationData 请求错误: ' + response.text)
        print(registrationData)
        return registrationData

    #开始发起挂号请求
    def startRegistration(slef):
        formData = slef.constructionRegistrationData()
        # 构造挂号数据为空
        if any(formData) == False:
            print("构造的挂号数据为空！")
        else:
            timePartList = copy.deepcopy(formData['TimePartList'])
            # 挂号时间采用优先逆序
            for timePart in timePartList[::-1]:
                formData['TimePart'] = timePart['TimePart']
                if 'TimePartList' in formData.keys():
                    formData.pop('TimePartList')

                start = time.clock()
                response = requests.post('http://www.dyyy120.com/ajax.aspx', data=formData,
                                         headers=slef.headers, cookies=slef.cookies)
                end = time.clock()
                print('ajax.aspx Running time: %s Seconds' % (end - start))

                if response.status_code == 200:
                    jsonResult = json.loads(response.text)
                    if jsonResult['ReturnCode'] == 0:
                        print(jsonResult['Message'])
                    else:
                        print(jsonResult['Message'])
                    break
                else:
                    print('startRegistration 请求错误: ' + response.text)

if __name__ == '__main__':
    start = time.clock()

    doctorId = r'6101000210003003'
    patienter = r'刘若熙'
    cookieStr = r'__RequestVerificationToken=64TGmcVMXnI--UxgGh5mK4QCmxsRlh7TBPjoeaIXlllknmbY916toJW5NRwkpRWN9H8Kn4xtP-4cu-FSpYRe5YbpiiUOsMB6CcPhnhEkZfo1;' \
                r' ASP.NET_SessionId=drnw1myaweyjaf4j1tudmxbm;' \
                r' User=UserName=lh8229238&Password=lh301415926;' \
                r' HBHOSPITALCODE=8016'
    registrar = Registrar(doctorId, patienter, cookieStr)
    # print(registrar.getRegistrarId())

    schedule.every(90).seconds.do(registrar.constructionRegistrationData)
    while True:
        schedule.run_pending()

    # print(registrar.constructionRegistrationData())
    # registrar.startRegistration()

    # end = time.clock()
    # print('main Running time: %s Seconds' % (end - start))


