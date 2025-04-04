def gas():
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.common.by import By 
  import os
  
  options = Options()
  options.set_capability('browserless:token', os.environ['BROWSER_TOKEN'])
  options.add_argument("--headless=new") #Headless = No GUI
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")

  driver = webdriver.Remote(os.environ['BROWSER_WEBDRIVER_ENDPOINT'],options=options)
  driver.get("https://www.sootoday.com/gas-prices")

  items = driver.find_element(By.TAG_NAME, "table")
  gasdata = items.text
  gasdata = items.text.replace("\n\n\n",",")
  driver.quit()

  #add commas bw cells in a CSV
  headings = {'Station','Address','City'}
  cities = {'Echo Bay','Sault Ste Marie','Bruce Mines','Thessalon','Desbarats'}
  stations = {'Heyden Fuels','Esso',"Mac's",'Circle K',"Canadian Tire","Shell",'Petro-Canada','Flying J','Pit Stop','Tunnel Lake Trading Post','Airways General Store'}

  for heading in headings:
    gasdata = gasdata.replace(f"{heading}",f",{heading}")
  for station in stations:
    gasdata = gasdata.replace(f"{station}",f",{station} ")
  for city in cities:
    gasdata = gasdata.replace(f"{city}",f",{city}")

  gasdata = gasdata.replace("Thessalon ,Esso","Thessalon Esso")

  print(gasdata)
  
  #Copies Gas Station Data to CSV
  text_file = open("ssmgas.csv", "w")
  n = text_file.write(gasdata)
  text_file.close()

  return gasdata
