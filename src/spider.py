from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json

# Initialize ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://sxsj.bfsu.edu.cn/index/xwxx.htm")

driver.implicitly_wait(5)  # time.sleep(5)

all_data = []
while True:
    container = driver.find_element(By.CSS_SELECTOR, ".main_conR.main_conRb")
    items = container.find_elements(By.TAG_NAME, 'li')

    for item in items:
        a_tag = item.find_element(By.TAG_NAME,'a')
        title = a_tag.get_attribute('title')
        link = a_tag.get_attribute('href')
        date = a_tag.find_element(By.TAG_NAME, 'span').text
        all_data.append(
            {
            'title':title,
            'link': link,
            'date': date
            }
                         )   

    try:
        next_page = driver.find_element(By.LINK_TEXT, '下页')
        next_page.click()
    except NoSuchElementException:
        print('已经是最后一页了，抓取完成')
        break

with open('bfsu_project.json', 'w', encoding='utf-8')as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

driver.quit()