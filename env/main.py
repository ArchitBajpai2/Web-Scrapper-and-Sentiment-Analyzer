import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

df = pd.read_excel('Input.xlsx') # can also index sheet by name or fetch all sheets
urlname = df['URL'].tolist()
urlid = df['URL_ID'].tolist()
for i in range(len(urlname)):
    driver = webdriver.Chrome(r'C:\Users\ARCHIT\PycharmProjects\webscraper\chromedriver.exe')
    try:
        driver.get(urlname[i])
    # url_id=str(urlid[i])
        file = open("{}.txt".format(urlid[i]),"w")
        results = []
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

       
        for element in soup.findAll('div', class_="td-post-content"):
            if element not in results:
                results.append(element.text)
                body = ""
                for i in results:
                    body += i + '. '
                file.write(body)

    except Exception as e:
        print(e)
   






