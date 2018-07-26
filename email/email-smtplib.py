import  smtplib
from email.mime.text import MIMEText

def send_mail(mail_recv_list, subject, content):
    #邮箱用户名
    mail_send_user = "18629005576@163.com"
    #邮箱密码：需要授权码
    mail_send_pass = "lh608518"
    msg = MIMEText(content, _charset='utf-8') #邮件内容
    msg['Subject'] = subject
    msg['From'] = mail_send_user
    msg['To'] = mail_recv_list
    try:
        s = smtplib.SMTP_SSL('smtp.163.com') #连接邮箱服务器，默认端口号是25
        s.login(mail_send_user, mail_send_pass)
        s.sendmail(mail_send_user,mail_recv_list,msg.as_string())
        s.quit()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == '__main__':
    mail_recv_list = 'liuh2018@xjtu.edu.cn'
    subject = '这是python自动发送的邮件'
    content = '这是邮件的测试内容'
    if send_mail(mail_recv_list,subject,content):
        print('success')
    else:
        print('fail')
