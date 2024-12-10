from selenium import webdriver
import selenium
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
    return changedUrl

def scroll_and_wait(driver, xpath, timeout=10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Elementin erişilebilir olup olmadığını kontrol et
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    print(f"Element bulundu: {xpath}")
    

def NefisYemekTarifleri(driver, ingreditiendsList, desiredRecipeNumber):
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

def Yemek(driver, ingreditiendsList, desiredRecipeNumber):
    # 9 21 45 57 81 105 129 141 177 189 213 237
    for i in range(0,len(ingreditiendsList)):
        newUrl = changeUrl(websiteUrl=url[1], ingredients=ingreditiendsList[i], queryLinkNumber=1)
        driver.get(newUrl)
        iteration = desiredRecipeNumber // 24
        if iteration > 0:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[3]/main/section[2]/div[3]")))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            for i in range(0,iteration):
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # recipes = driver.find_element(by=By.CLASS_NAME, value="py-0").text.split("\n")
        recipes = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[3]/main/section[2]/div[3]").text.split("\n")
        for i in range(0,3):
            recipeName = recipes[i*5+3]
            # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f"/html/body/div/div/div[3]/main/section[2]/div[3]/div[{i}]")))
            recipeLink = driver.find_element(by=By.XPATH, value=f"/html/body/div/div/div[3]/main/section[2]/div[3]/div[{i+1}]/div/a").get_attribute("href")
            driver.switch_to.parent_frame()
            time.sleep(0.5)
            try:
                # //*[@id="__next"]/div/div[3]/main/section[2]/div[3]/div[1]/div/a/div/div[1]/div/span/img
                recipeImageLink = driver.find_element(by=By.XPATH, value=f"//*[@id='__next']/div/div[3]/main/section[2]/div[3]/div[{i+1}]/div/a/div/div[1]/div/span/img").get_attribute("src")
            except selenium.common.exceptions.NoSuchElementException:
                print(f"Öğe bulunamadı: {recipeName}")
                recipeImageLink =  ''
                pass
            # recipeImageLink = driver.find_element(by=By.XPATH, value=f"/html/body/div/div/div[3]/main/section[2]/div[3]/div[{i+1}]/div/a/div/div[1]/div/span/img").get_attribute("src")
            # recipeImageLink = WebDriverWait(driver, 10).until(EC.element_located_to_be_selected((By.XPATH, f"/html/body/div/div/div[3]/main/section[2]/div[3]/div[{i+1}]/div/a/div/div[1]/div/span/img"))).get_attribute("src")        
            driver.switch_to.parent_frame()
            driver.execute_script("window.open('');")  # Yeni sekme aç
            driver.switch_to.window(driver.window_handles[1])  # Yeni sekmeye geçiş yap
            driver.get(recipeLink)
            recipeIngredients = driver.find_element(by=By.CLASS_NAME, value = "Ingredients_ingredientList__DhBO1").text.split("\n")
            numberOfIngreditiens = len(recipeIngredients) // 3
            # ingreditiends = []
            # ingreditiendsDetails = []
            # for j in range(0,numberOfIngreditiens):
            #     ingreditiends.append(recipeIngredients[j*3+2])
            #     ingreditiendsDetails.append(recipeIngredients[j*3]+ ' ' + recipeIngredients[j*3+1])

            ingreditiends = []
            ingreditiendsDetails = []

            recipeIngredients = driver.find_element(by=By.CLASS_NAME, value = "Ingredients_ingredientList__DhBO1")
            numberOfIngreditiens  = len(recipeIngredients.find_elements(By.TAG_NAME, "li"))
            ing = driver.find_element(by=By.XPATH, value=f"//*[@id='__next']/div/div[3]/main/section[2]/div/div[1]/section/div[3]/div/div[2]/ul") #Düzelt
            ingredient_elements = ing.find_elements(By.CLASS_NAME, "fw-normal")  # Liste döner

            for j in range(0,numberOfIngreditiens):
                ingreditiends.append(ingredient_elements[j].text)
                ingDetail = driver.find_element(by=By.XPATH, value=f"//*[@id='__next']/div/div[3]/main/section[2]/div/div[1]/section/div[3]/div/div[2]/ul/li[{j+1}]").text.split('\n') #Düzelt
                ingDetail.remove(ingredient_elements[j].text)
                ingreditiendsDetails.append(' '.join(ingDetail))
                driver.switch_to.parent_frame()

            print(recipeName)
            print(recipeLink)
            print(recipeImageLink)
            print(ingreditiends)
            print(ingreditiendsDetails)
            print("*******************************************")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        recipes = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[3]/main/section[2]/div[4]").text.split("\n")
        numberOfRecipes = len(recipes) // 5
        for i in range(0,numberOfRecipes):
            # recipeName = recipes[i*5+3]
            recipeName = driver.find_element(by=By.XPATH, value=f"/html/body/div/div/div[3]/main/section[2]/div[4]/div/div[1]/div[{i+1}]/div/div/h4/a").text
            driver.switch_to.parent_frame()

            recipeLink = driver.find_element(by=By.XPATH, value=f"/html/body/div/div/div[3]/main/section[2]/div[4]/div/div[1]/div[{i+1}]/div/a").get_attribute("href")
            driver.switch_to.parent_frame()
            time.sleep(0.5)

            try:
                # //*[@id="__next"]/div/div[3]/main/section[2]/div[4]/div/div[1]/div[1]/div/a/div/div[1]/div/span/img
                # //*[@id="__next"]/div/div[3]/main/section[2]/div[4]/div/div[1]/div[2]/div/a/div/div[1]/div/span/img
                recipeImageLink = driver.find_element(by=By.XPATH, value=f"//*[@id='__next']/div/div[3]/main/section[2]/div[4]/div/div[1]/div[{i+1}]/div/a/div/div[1]/div/span/img").get_attribute("src")
            except selenium.common.exceptions.NoSuchElementException:
                print(f"Öğe bulunamadı: {recipeName}")
                recipeImageLink =  ''
                pass
            # recipeImageLink = driver.find_element(by=By.XPATH, value=f"/html/body/div/div/div[3]/main/section[2]/div[4]/div/div[{i+1}]/div/a/div/div[1]/div/span/img").get_attribute("src")
            driver.switch_to.parent_frame()
            driver.execute_script("window.open('');")  # Yeni sekme aç
            driver.switch_to.window(driver.window_handles[1])  # Yeni sekmeye geçiş yap
            driver.get(recipeLink)
            ingreditiends = []
            ingreditiendsDetails = []

            recipeIngredients = driver.find_element(by=By.CLASS_NAME, value = "Ingredients_ingredientList__DhBO1")
            numberOfIngreditiens  = len(recipeIngredients.find_elements(By.TAG_NAME, "li"))
            ing = driver.find_element(by=By.XPATH, value=f"//*[@id='__next']/div/div[3]/main/section[2]/div/div[1]/section/div[3]/div/div[2]/ul") #Düzelt
            ingredient_elements = ing.find_elements(By.CLASS_NAME, "fw-normal")  # Liste döner

            for j in range(0,numberOfIngreditiens):
                ingreditiends.append(ingredient_elements[j].text)
                ingDetail = driver.find_element(by=By.XPATH, value=f"//*[@id='__next']/div/div[3]/main/section[2]/div/div[1]/section/div[3]/div/div[2]/ul/li[{j+1}]").text.split('\n') #Düzelt
                ingDetail.remove(ingredient_elements[j].text)
                ingreditiendsDetails.append(' '.join(ingDetail))
                driver.switch_to.parent_frame()
        
            print(recipeName)
            print(recipeLink)
            print(recipeImageLink)
            print(ingreditiends)
            print(ingreditiendsDetails)
            print("*******************************************")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        # print(recipes)

if __name__ == "__main__":
    ingreditiendsList = ['Domates','Yumurta','Un','Pirinç','Makarna','Tavuk','Kıyma','Patates','Soğan','Sarımsak']
    ingreditiendsListTest = ['Domates']
    Yemek(driver, ingreditiendsListTest, 105)
    # NefisYemekTarifleri(driver, ingreditiendsList, 25)