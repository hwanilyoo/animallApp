from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
driver = webdriver.Chrome()
#driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
#elem = driver.find_element_by_name("q")

names = ["박보검", "송중기"]

#  "엑소 백현","워너원 강다니엘", "강동원","엑소 시우민", "워너원 황민현", "이종석", "이준기",
#            "마동석","안재홍","조세호","조진웅","공유","김우빈","육성재","윤두준","이민기","방탄소년단 정국","아이콘 바비","엑소 수호",
#            "워너원 박지훈"]
for name in names:
    print(name)
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)
    try:
        if not os.path.exists('./'+name):
            os.makedirs('./'+name)
    except OSError:
        print ('Error: Creating directory. ' +  name)
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    myPath = name
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(3)
            imgURL = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
            fullfilename = os.path.join(myPath, str(count)+".jpg")
            urllib.request.urlretrieve(imgURL, fullfilename)
            count = count+1
            if(count == 5):
                break
        except:
            pass
        
    driver.find_element_by_name("q").clear()

driver.close()