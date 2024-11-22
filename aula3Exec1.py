from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

navegador = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
navegador.get(url)

sleep(3)

dicth1 = navegador.find_element(By.TAG_NAME,'h1')


nomeDict = {}
ps = navegador.find_elements(By.TAG_NAME,'p')


for elem in range(len(ps)):
    atributo = ps[elem].get_attribute('atributo')
    nomeDict[atributo] = ps[elem].text
    
print(nomeDict)

navegador.quit()