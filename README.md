# PythonProgramMyself
介绍自己的python小编程

## 用selenium+Beautifulsoup爬取数据
``` python

ccbsite=[]
adr = []
url = "http://tool.ccb.com/outlet/frontOprNodeQuery.gsp"
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('//*[@id="province"]').click()
browser.find_element_by_xpath('//*[@id="province"]/option[25]').click()
browser.find_element_by_xpath('//*[@id="button"]').click()
for p in range(1,20):
    curr_html = browser.page_source
    bs = BeautifulSoup(curr_html,"html.parser")
    tables = bs.select('table tbody tr')
    for i in [0,1,2]:
        tables.pop(0)
    for i in range(0,len(tables)):
        ccbsite.append(tables[i].text.split('\n')[1])
        adr.append(tables[i].text.split('\n')[3].split('\xa0')[0].strip())
    try:
        browser.find_element_by_link_text('下一页').click()    #这一步很关键，不能用xpath定位，试了很多次才意识到
    except:
        print("结束")
        

browser.close()

```
