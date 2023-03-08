from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# URL
URL = 'https://www.londonstockexchange.com/'

# Chrome Options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Instancia de Selenium Web Driver
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(URL)
driver.implicitly_wait(10000)
accept_all = driver.find_element(By.XPATH, "//button[@id='ccc-notify-accept']")
accept_all.click()

page = BeautifulSoup(driver.page_source,'html.parser')


#INDEX (STOCK)
indexs_descriptions = list()
for indexs_names in page.find_all('td', attrs={'class':'index-description'}):
    #Index name
    index_name = indexs_names.find('span',attrs={'class':'ellipsed'})
    #print(index_name.text)
    indexs_descriptions.append(index_name.text)    
#print(indexs_descriptions)


# Index Value
index_values = list()
for indexs_value in page.find_all('td', attrs={'class':'index-value'}):
    #Index value    
    index_value = indexs_value.find('span')
    #print(index_name.text)
    float_value = float(index_value.text.replace(',',''))
    index_values.append(float_value)    
#print(index_values)


# Index Change
indexs_changes = list()
for indexs_change in page.find_all('td', attrs={'class':'index-change'}):
    #Index change
    index_change = indexs_change.find('span')
    #print(index_change.text)
    indexs_changes.append(index_change.text)    
#print(indexs_changes)


# Data Frame
df2 = pd.DataFrame({
    'Index Description': indexs_descriptions,
    'Index Value': index_values,
    'Index Changes': indexs_changes
})

# Sin Ordenar
print(df2)

# Tabla Ordenada
df2.sort_values(by=['Index Value'], inplace=True)
print(df2)

# Excel file
writer = pd.ExcelWriter('challenge_stock_exchanges.xlsx')
df2.to_excel(writer, 'London Stock Exchange', index=False)

# CSV file
df2.to_csv('challenge_stock_exchange.csv', index = False)

# Save xlsx file
writer.save()

print('Datos exportados!')
driver.quit()