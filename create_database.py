from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
from playsound import playsound
import sqlite3 as sql
import requests as http

vt = sql.connect('C:/Users/circi/Desktop/Masaüstü/Projects/yemek_app/recipeDatabase.sqlite')
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS 'recipes' (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, link TEXT)")
im.execute("INSERT INTO recipes(name,ingredients,link) VALUES(\'deneme\',\'[asd,asd,asda,asd]\',\'1231231asd\' )")
im.execute("INSERT INTO recipes(name,ingredients,link) VALUES(\'deneme1213123\',\'[asd,asd,asda,aqqqsd]\',\'1231231a22sd\' )")
vt.commit()
vt.close()

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.tabs.remote.useCrossOriginEmbedderPolicy", False)
profile.set_preference("security.csp.enable", False)
profile.set_preference("security.external_protocol_requires_permission", False)
profile.set_preference("security.fileuri.strict_origin_policy", False)
profile.set_preference("browser.tabs.remote.useCrossOriginOpenerPolicy", False)
profile.set_preference("network.http.referer.disallowCrossSiteRelaxingDefault.pbmode", False)
profile.set_preference("dom.block_external_protocol_in_iframes", False)
profile.set_preference("dom.block_download_in_sandboxed_iframes", False)
profile.set_preference("dom.delay.block_external_protocol_in_iframes.enabled", False)
profile.set_preference("dom.block_download_in_sandboxed_iframes", False)
profile.set_preference("privacy.trackingprotection.enabled", False)
options = Options()
options.profile = profile

service = Service(options=options,executable_path='./geckodriver.exe')
driver =  webdriver.Firefox(service=service)
url = ["https://www.nefisyemektarifleri.com/","https://www.yemek.com/"]

def changeUrl(websiteUrl,ingredients,queryLinkNumber):
    queryLinks = ['ara/?s=','tarif/?q=']
    changedUrl = websiteUrl + queryLinks[queryLinkNumber] + ingredients
    print(changedUrl)
    return changedUrl

def scroll_and_wait(driver, xpath, timeout=10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Elementin erişilebilir olup olmadığını kontrol et
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    print(f"Element bulundu: {xpath}")
    

def NefisYemekTarifleri(driver,desiredRecipeNumber):
    newUrl = changeUrl(websiteUrl=url[0], ingredients="Domates", queryLinkNumber=0)
    driver.get(newUrl)
    iteration = desiredRecipeNumber // 12
    if iteration > 0:
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for i in range(0,iteration):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            scroll_and_wait(driver, f"/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[{i+2}]")
    # scroll_and_wait(driver, "/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[3]")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # scroll_and_wait(driver, "/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[4]")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# /html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[2]


    # # Sayfanın sonuna kaydır
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[3]")))
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[4]")))
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# /html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[3]
    asd = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[1]")
    print(asd.text.split("\n"))
    a= asd.text.split("\n")
    print(len(a))

    #/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[1]/div[1]
    #/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/div
    #/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[2]
    #/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/div/figure/a/img image

    asda1 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/div/figure/a")
    driver.switch_to.parent_frame()
    asda2 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/div/figure/a/img")
    driver.switch_to.parent_frame()
    # asda3 = driver.find_element(by=By.CLASS_NAME, value="attachment-medium size-medium wp-post-image")
    bca1 = asda1.get_attribute("href")
    bca2 = asda2.get_attribute("src")
    print(bca1)
    print(bca2)
    driver.execute_script("window.open('');")  # Yeni sekme aç
    driver.switch_to.window(driver.window_handles[1])  # Yeni sekmeye geçiş yap
    driver.get(bca1)
    ings = driver.find_element(by=By.CLASS_NAME, value="recipe-materials").text.split("\n")
    print(ings)
    driver.close()
    # asd333 = http.get(bca1)
    # print(asd333.text)
    # print(asda3.get_attribute("src"))

def Yemek(driver, desiredRecipeNumber):
    # 9 21 45 57 81 105 129 141 177 189 213 237
    newUrl = changeUrl(websiteUrl=url[1], ingredients="Domates", queryLinkNumber=1)
    driver.get(newUrl)
    iteration = desiredRecipeNumber // 24
    if iteration > 0:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[3]/main/section[2]/div[3]")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for i in range(0,iteration):
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # recipes = driver.find_element(by=By.CLASS_NAME, value="py-0").text.split("\n")
    recipes = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[3]/main/section[2]/div[3]").text.split("\n")
    print(recipes)
Yemek(driver, 105)
# NefisYemekTarifleri(driver,25)