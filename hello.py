from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='chromedriver')
driver = webdriver.Chrome("chromedriver",options=chrome_options)

##make edits here for reading file
urls=pd.read_csv("sources.txt")
##select the column which contains the urls
var=urls.iloc[:,2].values
count=0
tmp=[]
print(var)

print(len(var))
for i in var:
    driver.get(i)
    count+=1
    #time.sleep(10)
    seqs = [ x.text for x in driver.find_elements_by_xpath('//pre')]
    newseq=seqs[0].split("\n")
    tmp.append(newseq[-1])
    print(newseq[-1])
    if count%10==0 or count==len(var):
        print(count)
    

print(tmp)

##add the downloaded data 
urls['Sequence']=tmp
urls.to_csv("Outputall.txt",index=None)

driver.close()
