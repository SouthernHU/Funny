from selenium import webdriver
import time


chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'  #chromedriver的文件位置
driver = webdriver.Chrome( executable_path = chrome_driver )
driver.get( 'http://jkrb.xjtu.edu.cn/EIP/user/index.htm' )
username = driver.find_element_by_name( 'username' )
password = driver.find_element_by_name( 'pwd' )
username.send_keys( "username" )    # 引号里填写学号
password.send_keys('password')      # 引号里填写密码
button1 = driver.find_element_by_css_selector("#account_login")
driver.execute_script("arguments[0].click();", button1)
# 点击研究生健康每日报
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div[2]/div/table/tbody/tr/td[2]/div[2]/div/iframe"))
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/table/tbody/tr/td/div[1]/div/div[2]/div[2]/iframe"))
button2 =  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul[1]/li[1]/div/a/div/div")
driver.execute_script("arguments[0].click();", button2)
# 点击每日健康填报
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div[2]/div/table/tbody/tr/td[2]/div[2]/div[2]/iframe"))
button3 = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]/span[1]")
driver.execute_script("arguments[0].click();", button3)
# 点击否
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div[2]/div/table/tbody/tr/td[2]/div[2]/div[3]/iframe"))
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/div/iframe"))
button4 = driver.find_element_by_xpath("/html/body/div/div/p[11]/strong/span[2]/div/table/tbody/tr/td/div[1]/div[2]/input")
driver.execute_script("arguments[0].click();", button4)
# 填写体温
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div[2]/div/table/tbody/tr/td[2]/div[2]/div[3]/iframe"))
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/div/iframe"))
driver.find_element_by_xpath("/html/body/div/div/table/tbody/tr[13]/td[2]/span/span/input").send_keys("36.5")
# 点击提交
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div[2]/div/table/tbody/tr/td[2]/div[2]/div[3]/iframe"))
button5 = driver.find_element_by_id("sendBtn")
driver.execute_script("arguments[0].click();", button5)
# 点击确认
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div[2]/div/table/tbody/tr/td[2]/div[2]/div[3]/iframe"))
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div[2]/a[1]/span").click()

driver.quit()
