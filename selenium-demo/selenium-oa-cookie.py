from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
browser = webdriver.Chrome()


# testBanCookie=test; JSESSIONID=abc9TQuUhrTgWd6iZGptw;


browser.add_cookie({'name':'JSESSIONID','value':'abc9TQuUhrTgWd6iZGptw'})

browser.get('http://www.jdyfy.com:8888/wui/main.jsp')

# browser.get('http://www.jdyfy.com:8888/login/Login.jsp')
# print(browser.current_url)
# browser.find_element_by_id('loginid').send_keys('010255')
# browser.find_element_by_id('userpassword').send_keys('608518')
# browser.find_element_by_id('login').click()
#
# browser.find_element_by_xpath('//*[@id="leftBlock_HrmDiv"]/div/div[2]').click()
# browser.implicitly_wait(30)

#切换iframe
browser.switch_to.frame('mainFrame')
browser.find_element_by_xpath('//*[@id="li_a_4"]').click()

browser.switch_to.frame('tabcontentframe')

# #从frame中切回主文档
# #browser.switch_to.default_content()

print('扣款：' + browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[29]/td[4]').text)
print('实发：' + browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[30]/td[2]').text)
