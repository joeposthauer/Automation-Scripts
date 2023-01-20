from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag
import time



def main():
    # url of LinkedIn
    url = "http://linkedin.com/"
    # url of LinkedIn network page
    network_url = "http://linkedin.com/in/joeposthauer/"
    # path to browser web driver
    driver = webdriver.Chrome('/Users/joeposthauer/Downloads/chromedriver_mac64/chromedriver.exe')
    driver.get(url)


    username = driver.find_element("id","session_key")
    # Sending the keys for username
    username.send_keys("posthauerjoe@gmail.com")
    # Getting the password element

    password = driver.find_element("id","session_password")
    # Sending the keys for password
    password.send_keys("daiss1008")
    # Getting the tag for submit button
    # driver.find_element_by_id("login-submit").click()
    driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()


    #search for person
    searchCriteria = driver.find_element(By.CLASS_NAME,"search-global-typeahead__input")
    searchCriteria.send_keys("Western Digital Recruiter")
    searchCriteria.send_keys(Keys.ENTER)
    #wait for page to load
    time.sleep(3)

    #click on first profile
    driver.find_element(By.CLASS_NAME,"mb1").click()
    time.sleep(3)

    #click on 'more' button
    button = driver.find_elements(By.CSS_SELECTOR,"button.artdeco-dropdown__trigger")[2]
    x,y = pag.position()
    print(x,y)
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()

    button2 = driver.find_elements(By.CSS_SELECTOR,"div.artdeco-dropdown__item--is-dropdown")[3]
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button2).click(button2).perform()
    time.sleep(3)









def login(driver):
    # Getting the login element
    print("h")

if __name__ == "__main__":
    main()
