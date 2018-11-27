
# coding: utf-8

# In[179]:


import requests
import selenium.webdriver
import re
import time
from bs4 import BeautifulSoup
import urllib


# In[188]:


driver = selenium.webdriver.Firefox()
driver.get('http://www.baidu.com/')
driver.find_element_by_class_name('s_ipt').send_keys('天气')
driver.find_element_by_id('su').click()
time.sleep(2)
cookies = driver.get_cookies()
cookies1={}
for cookie in cookies:
    cookies1[cookie['name']]=cookie['value']
driver.quit()

# In[189]:


def search(key):
    key = urllib.request.quote(key)
    find = 'http://www.baidu.com/s?wd=' + key
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) "                           "Chrome/55.0.2883.95 Safari/537.36 "
    headers = {'User-Agent': user_agent}
    return BeautifulSoup(requests.get(find,headers=headers, cookies=cookies1 ).text, 'lxml')


# In[190]:


def answering(num):
    tempquestion = question[num].find('div', class_='div_title_question').text
    tempanswer = question[num].find('div', class_='div_table_radio_question').find_all('li')
    sheet = search(tempquestion)
    answersheet = {}
    templist = []
    for i, item in enumerate(tempanswer):
        templist.append(tempanswer[i].text[2:])
        answersheet[tempanswer[i].text[2:]] = len(re.findall(tempanswer[i].text[2:], sheet.decode('utf8')))
    # sorted(answersheet.items(), key=lambda v: v[1], reverse=True)
    print(answersheet)
    for i,item in enumerate(templist):
        if item == max(answersheet,key=answersheet.get):
            return(i)


# In[192]:


if __name__ == '__main__':
    url = 'https://ks.wjx.top/jq/24386487.aspx'
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_id('txtExt').send_keys('电子信息学院刘恒宇')
    driver.find_element_by_id('txtpwd').send_keys('2018261681')
    time.sleep(3)
    driver.find_element_by_id('btnContinue').click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    question = soup.find_all('div', class_='div_question')
    for i in range(10):
        driver.find_elements_by_class_name('div_question')[i].find_elements_by_xpath('div/ul/li/a')[answering(i)].click()

