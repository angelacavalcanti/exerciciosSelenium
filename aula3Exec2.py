from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html#'
navegador = Firefox()
navegador.get(url)

sleep(1)

while True:
    a = navegador.find_element(By.TAG_NAME,'a')
    ps = navegador.find_elements(By.TAG_NAME,'p')
    if "Você" in ps[-1].text:
        break
    a.click()
