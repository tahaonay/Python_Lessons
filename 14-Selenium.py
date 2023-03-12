from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#import time


url = "https://www.youtube.com/"

chr_options = Options()
chr_options.add_experimental_option("detach",True)
driver = webdriver.Chrome("chromedriver",options=chr_options)
driver.get(url)


""" 2sn aç kapat
time.sleep(2)

print(driver.title)
time.sleep(2)
driver.close()
"""
"""
driver.maximize_window()   #tam ekran yapar
#driver.save_screenshot("ss.png")  # ekran görüntüsü alır

if "YouTube" in driver.title:
    driver.save_screenshot("youtube.png")

driver.close()
"""



