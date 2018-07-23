from splinter import Browser

browser = Browser('chrome')
browser.visit('http://www.jdyfy.com:8888/login/Login.jsp')
# browser.fill('loginid','010255')
# browser.fill('userpassword','608518')
browser.find_by_id('loginid').fill('010255')
browser.find_by_id('userpassword').fill('608518')
browser.find_by_id('login').click()
browser.find_by_xpath('//*[@id="leftBlock_HrmDiv"]/div/div[2]').click()

browser.find_by_css('.zd_btn_cancle btn_submit').click()

print(browser.html)


