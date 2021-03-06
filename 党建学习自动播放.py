import time
from selenium import webdriver
import sys
import math
class AutoPlay():
    def __init__(self):
        chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'  #chromedriver的文件位置
        self.driver = webdriver.Chrome( executable_path=chrome_driver )
        self.id = "输入你的学号"
        self.pwd = "输入你的密码"
        self.loginUrl = "http://xjtudj.edu.cn/login.html"
        # 团课Xpath
        self.tuankeXPath = '//*[@id="learnPlan"]/table/tbody/tr[2]/td[7]'
        # 七一讲话Xpath
        self.qiyiXPath = '//*[@id="learnPlan"]/table/tbody/tr[3]/td[7]'

    def login(self):
        self.driver.get(self.loginUrl)
        loginSwitchButton = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div[1]')
        self.driver.execute_script("arguments[0].click();", loginSwitchButton)
        loginButton1 = self.driver.find_element_by_id('cas_btn')
        self.driver.execute_script("arguments[0].click();", loginButton1)
        username = self.driver.find_element_by_name( 'username' )
        password = self.driver.find_element_by_name( 'pwd' )
        username.send_keys( self.id )
        password.send_keys( self.pwd )
        loginButton2 = self.driver.find_element_by_css_selector( "#account_login" )
        self.driver.execute_script( "arguments[0].click();", loginButton2 )
        time.sleep( 2 )
        # 进入学习空间
        courseButton1 = self.driver.find_element_by_xpath( '/html/body/div/div[2]/div/div[2]/div[2]/a[7]' )  # 点击我的空间
        self.driver.execute_script( "arguments[0].click();", courseButton1 )

    def play(self,startCourse,playSpeed):
        # # 倍速按钮定位，playSpeedList[0]为2倍速，playSpeedList[1]为四倍速
        # playSpeedList = [2,1]
        # playSpeedButton = "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div/div/div[8]/p["+str(playSpeedList[playSpeed])+"]"
        # 登录
        self.login()
        time.sleep(3)
        # 选择团课学习
        self.driver.find_element_by_xpath(self.tuankeXPath).click()#点击团课
        time.sleep(2)
        # 进入习新专题
        # self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/a').click()#点击习新第一集
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/div[1]/div[6]/div[2]/div[1]/a' ).click( )  # 点击青年网络公开课
        # self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/div[1]/div[5]/div[2]/div/a' ).click( )
        time.sleep(2)
        for i in range(startCourse,6):
            self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[3]/a["+str(i)+"]").click()#选集
            time.sleep(2)
            # 获取视频位置
            video = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div/div/video" )
            videoID = video.get_attribute( "id" )
            time.sleep(1)
            # 获取视频时长
            js = "return document.getElementById("+"'"+videoID+"'"+").duration"
            videoTime = self.driver.execute_script( js )
            # 播放视频
            self.driver.execute_script("return arguments[0].play()",video)
            print( "\n---------------------第"+str(i)+"集---------------------" )
            print("正在播放第"+str(i)+"集，预计耗时："+str(videoTime)+"秒")
            # # 倍速选择
            # self.driver.execute_script( "arguments[0].click()", playSpeedButton )
            for remaining in range(math.ceil(videoTime+20),-1,-1):
                sys.stdout.write("\r")
                sys.stdout.write( "本集剩余{:2d}分".format( int( remaining / 60 ) ) +
                                  "{:2d}秒".format( remaining - int( remaining / 60 ) * 60 ) )
                sys.stdout.flush( )
                time.sleep( 1 )

if __name__ == '__main__':
    autoPlay = AutoPlay()
    autoPlay.play(1,1)#从第三个视频开始播放



