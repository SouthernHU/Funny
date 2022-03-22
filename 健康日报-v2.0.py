from selenium import webdriver
import time

chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'  #chromedriver的文件位置
driver = webdriver.Chrome( executable_path = chrome_driver )
driver.set_window_size(width=780, height=820, windowHandle="current")
driver.set_window_position(x=-10, y=0)
driver.get( 'http://jkrb.xjtu.edu.cn/EIP/user/index.htm' )
username = driver.find_element_by_name( 'username' )
password = driver.find_element_by_name( 'pwd' )
username.send_keys( "studentID" )    # 引号里填写学号
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

# # 点击我已阅知
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/div[2]/div/table/tbody/tr/td[2]/div[2]/div[3]/iframe'))
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/div/iframe"))
button_Ikonwed=driver.find_element_by_xpath('/html/body/div/div/p[11]/span[2]/div/table/tbody/tr/td/div[1]/div/input')
driver.execute_script("arguments[0].click();", button_Ikonwed)
# 填写体温
driver.find_element_by_xpath("/html/body/div/div/p[13]/span[2]/span/span/input").send_keys("36.5")
# 是否做过核酸
button_hesuan_no=driver.find_element_by_xpath('/html/body/div/div/p[15]/div/table/tbody/tr/td/div[1]/div[2]/input')
button_hesuan_yes=driver.find_element_by_xpath('/html/body/div/div/p[15]/div/table/tbody/tr/td/div[1]/div[1]/input')
driver.execute_script("arguments[0].click();", button_hesuan_no)
driver.find_element_by_xpath("/html/body/div[1]/div/p[16]/span/span[2]/span/span[1]/input").send_keys("2022-03-14 10:00")
# 检测结果（阴性）
button_result=driver.find_element_by_xpath('/html/body/div/div/p[17]/span/span[3]/div/table/tbody/tr/td/div[1]/div[2]/input')
driver.execute_script("arguments[0].click();", button_result)
# 隔离情况（未被隔离）
button_status=driver.find_element_by_xpath('/html/body/div/div/p[18]/span[2]/div/table/tbody/tr/td/div[1]/div[1]/input')
driver.execute_script("arguments[0].click();", button_status)
# 一码通颜色（绿色）
button_healthCode=driver.find_element_by_xpath('/html/body/div/div/p[19]/div/table/tbody/tr/td/div[1]/div[3]/input')
driver.execute_script("arguments[0].click();", button_healthCode)
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

time.sleep(5)
driver.quit()