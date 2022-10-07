from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd 
import pyautogui
import time

#Ler o Arquivo 
nome_do_arquivo = 'TestePrograma.xlsx'
df = pd.read_excel("TestePrograma.xlsx")
url_do_forms = "https://esaj.tjsp.jus.br/sco/abrirCadastro.do"


for index,row in df.iterrows():
    print("index: " + str(index) + " o nome é " + row ["Nome"])
    chrome = webdriver.Chrome()
    chrome.get(url_do_forms)
    time.sleep(3) 

    #Selecionar documento 
    pyautogui.press(['down'])

    #
    elemento_texto_Nome = chrome.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
    elemento_texto_Rg = chrome.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
    elemento_texto_Cpf = chrome.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
    
    elemento_texto_Nome.send_keys(row["Nome"])
    elemento_texto_Rg.send_keys(row["Rg"])
    elemento_texto_Cpf.send_keys(row["Cpf"])

    if row["Sexo"] == "M":
     elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[1]/label/input').click()
    else:
     elemento_texto_Sexo = chrome.find_element(By.XPATH,'/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[8]/td[2]/table/tbody/tr/td/fieldset/span[2]/label/input').click()
     
chrome.quit
    



#documento 2 
