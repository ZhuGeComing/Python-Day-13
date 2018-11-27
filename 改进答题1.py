
# coding: utf-8

# In[198]:


import requests
import selenium.webdriver
import re
import time
from bs4 import BeautifulSoup
import urllib
import docx


# In[188]:


# driver = selenium.webdriver.Firefox()
# driver.get('http://www.baidu.com/')
# driver.find_element_by_class_name('s_ipt').send_keys('天气')
# driver.find_element_by_id('su').click()
# time.sleep(2)
# cookies = driver.get_cookies()
# cookies1={}
# for cookie in cookies:
#     cookies1[cookie['name']]=cookie['value']
# driver.quit()

cookies1 = {'BAIDUID': '0C973E1CB092F3299E040E6A2F6F7EBE:FG=1',
 'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
 'BDSVRTM': '181',
 'BD_CK_SAM': '1',
 'BD_HOME': '0',
 'BD_LAST_QID': '16348314965184109764',
 'BD_UPN': '13314352',
 'BIDUPSID': '0C973E1CB092F3299E040E6A2F6F7EBE',
 'H_PS_645EC': '85ae5zPCwmuK3yQhbGOSThMtE%2B57ZdhdE5sptnNE%2FTLuo4rW4NfFjVP4%2BYo',
 'H_PS_PSSID': '1431_25809_21082_18560_26350_20929',
 'PSINO': '1',
 'PSTM': '1536292947',
 'delPer': '0'}

# In[189]:


def search(key):
    key = urllib.request.quote(key)
    find = 'http://www.baidu.com/s?wd=' + key
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) "                           "Chrome/55.0.2883.95 Safari/537.36 "
    headers = {'User-Agent': user_agent}
    return BeautifulSoup(requests.get(find,headers=headers, cookies=cookies1 ).text, 'lxml')


# In[230]:


def answering(num):
    tempquestion = question[num].find('div', class_='div_title_question').text
    tempanswer = question[num].find('div', class_='div_table_radio_question').find_all('li')
    print(pipei(tempquestion[:8]))
    sheet = search(tempquestion)
    answersheet = {}
    templist = []
    for i, item in enumerate(tempanswer):
        templist.append(tempanswer[i].text[2:])
        answersheet[tempanswer[i].text[2:]] = len(re.findall(tempanswer[i].text[2:], sheet.decode('utf8')))
    # sorted(answersheet.items(), key=lambda v: v[1], reverse=True)
    print(answersheet)
    print('')
    print('----------')
    for i,item in enumerate(templist):
        if item == max(answersheet,key=answersheet.get):
            return(i)

def read_docx(file_name):
    doc = docx.Document(file_name)
    content = '\n'.join([para.text for para in doc.paragraphs])
    return content


# In[227]:


def pipei(qqq):
    raw = read_docx('demo.docx')
    qqq = qqq.replace('(', '').replace(')', '')
    try:
        print(re.findall( qqq + '.*?\n.*?\n.*?\n.*?\n.*?\n', raw, re.S)[0])
    except IndexError:
        print(re.findall(qqq + '.*?\n.*?\n.*?\n.*?\n.*?\n', raw, re.S))

# In[231]:


if __name__ == '__main__':
    url = 'https://ks.wjx.top/jq/24386487.aspx'
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_id('txtExt').send_keys('电子信息学院管政奎')
    driver.find_element_by_id('txtpwd').send_keys('2018261664')
#     time.sleep(3)
    driver.find_element_by_id('btnContinue').click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    question = soup.find_all('div', class_='div_question')
    for i in range(100):
        print('---%d---' % (i+1))
        driver.find_elements_by_class_name('div_question')[i].find_elements_by_xpath('div/ul/li/a')[answering(i)].click()


# In[199]:



