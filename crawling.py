import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constant2 as cons
import re 

# This code is to scrape the mobile phone data from Flipkart.

# Create a Chrome options object and set the "detach" flag to True.
# This will allow the browser window to be closed automatically after the script finishes running.
def crawl():
     opt = Options()
     opt.add_experimental_option("detach", True)
     
     path = 'C:/Users/DELL/Documents/chromedriver-win64/chromedriver.exe'
     
     
     # Create a Chrome driver object and set the implicit wait time to 5 seconds.
     driver = webdriver.Chrome(path)
     driver.implicitly_wait(5)
     driver.maximize_window()
     
     # Navigate to the Flipkart website.
     driver.get("https://www.flipkart.com/")
     
     # Try to click the OTP overlay. If it is not present, then skip.
     try:
         otpEscape = WebDriverWait(driver, 5, ignored_exceptions= [Exception, TimeoutError ])
         otpEscape.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/button'))).click()
     except:
         pass
     
     # Find the search input field and enter the keyword "mobiles".
     search = driver.find_element(By.XPATH, "//input[@name='q']")
    #  search.send_keys("smartphone under {cons.BUDGET}")
     
     # Submit the search form.
     search.submit()
     
     # Initialize the variables to store the mobile name, price, features, and rating.
     products=[]                                            
     prices=[]                                            
     ratings=[]                                           
     storages = []                                                          
     screens = []                                           
     cameras = []                                            
     batterys = []                                            
     processors = []  
     count = 0
     
     # The loop will run 42 times, which is the maximum number of pages of results that Flipkart shows.
     while True:
         count += 1
     
         # Get the current page number.
         page_number = count
     
         # Navigate to the specified page.
         driver.get(f"https://www.flipkart.com/search?q=smartphone+under+{cons.BUDGET}&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=smartphone+under+{cons.BUDGET}%7CMobiles&requestId=789ab008-0680-46ee-b8cb-62580e263c2f&as-backfill=on&page={page_number}")
     
         # Get the page source.
         page_source = driver.page_source
     
         # Parse the page source using BeautifulSoup.
         soup = BeautifulSoup(page_source, 'html.parser')
     
        #  # Find all the mobile names, prices, features, and ratings on the page.
        #  name_ = soup.find_all("div", class_ ="_4rR01T")
        #  price_ = soup.find_all("div", class_ ="_30jeq3 _1_WHN1")
        #  features_ = soup.find_all("div", class_="fMghEO")
        #  rating_ = soup.find_all("div", class_="_3LWZlK")
     
        #  # Append the mobile name, price, features, and rating to the corresponding lists.
        #  for i, j, k, l in zip(name_, price_, features_, rating_):
        #      name.append(i.text)
        #      price.append(j.text)
        #      features.append(k.text)
        #      rating.append(l.text)
         
         for data in soup.findAll('div',class_='_3pLy-c row'):
            names=data.find('div', attrs={'class':'_4rR01T'})
            price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
            rating=data.find('div', attrs={'class':'_3LWZlK'})
            specification = data.find('div', attrs={'class':'fMghEO'})
        
            for each in specification:
                col=each.find_all('li', attrs={'class':'rgWa7D'})
                storage =getattr(col[0], 'text', '')
                screen = getattr(col[1], 'text', '')
                camera = getattr(col[2], 'text', '')
                battery = getattr(col[3], 'text', '')
                processor = getattr(col[4], 'text', '')

            products.append(names.text)                                                      
            prices.append(getattr(price, 'text', 0))                                                        
            storages.append(storage)                                                         
            screens.append(screen)                                                            
            cameras.append(camera)                                                           
            batterys.append(battery)                                                          
            processors.append(processor)                                                      
            ratings.append(getattr(rating, 'text', 0.0))                                                     
         
              # Check if the current page is the last page.
         if count == 5:
            break

     best_rat =[]
     max = 0.0
     for i in range (1,23):
         rat = float(ratings[i])
         if rat > max:
             max = rat
     
     for it in range (1,23):
         if float(ratings[it]) == max:
             best_rat.append(it)
     
     
     print("\nMost rated Mobile phones -> \n")
     for it in range(len(best_rat)) :
         print(products[best_rat[it]],"\t\t",storages[best_rat[it]],"\t\t",prices[best_rat[it]])  
     
     
     best_storage = []
     max_ram = 0
     max_rom = 0
     for i in range (len(best_rat)):
         ram  = re.findall("\d",storages[best_rat[i]])
         rom  = re.findall("[0-9]{2,3}",storages[best_rat[i]])
         ram = int(ram[0])
         rom = int(rom[0])
         if(max_ram < ram or max_rom < rom):
             max_ram = ram
             max_rom = rom
         
     for i in range (len(best_rat)):
         ram  = re.findall("\d",storages[best_rat[i]])
         rom  = re.findall("[0-9]{2,3}",storages[best_rat[i]])
         if(int(ram[0]) == max_ram and int(rom[0]) == max_rom):
             best_storage.append(best_rat[i])
     
     print("\n\nBest Storages Phones among most rated mobiles are :- ")
     for i in range (len(best_storage)):
         print(products[best_storage[i]])
     
     
     best_battery = []
     max_bat = 0
     for i in range(len(best_storage)):
         bat = re.findall("[0-9]{4}",batterys[best_storage[i]])
         bat = int(bat[0])
         if( max_bat < bat):
            max_bat = bat
     
     for i in range (len(best_storage)):
         bat = re.findall("[0-9]{4}",batterys[best_storage[i]])
         if(int(bat[0]) == max_bat):
             best_battery.append(best_storage[i])
     
     
     print("\n\nBest Battery Mobiles among selected mobiles are :- ")
     for i in range (len(best_battery)):
         print(products[best_battery[i]])
     
     best= []
     min_prc = 100000
     for i in range(len(best_battery)):
            res = re.findall("[0-9]{1,3}",prices[best_battery[i]])
            res = ''.join(res)
            #print(res)
            prc = int(res)
            if prc < min_prc:
               min_prc= prc
     
     for i in range (len(best_battery)):
         res = re.findall("[0-9]{1,3}",prices[best_battery[i]])
         res = ''.join(res)
         if(int(res) == min_prc):
             best.append(best_battery[i])
      
     print("\n\nBest Mobioles among alll mobile is :-\n ")
     for i in range (len(best)):
        print("Name     :-",  products[best[i]])
        print("Ratings  :-",  ratings[best[i]])
        print("Storage  :-",  storages[best[i]])
        print("Camera   :-",  cameras[best[i]])
        print("Screen   :-",  screens[best[i]])
        print("Battery  :-",  batterys[best[i]])
        print("Processor:-",  processors[best[i]])
        print("Prices   :-",  prices[best[i]])
        print("\n")   

     str =""
     str = str +  "Name     :-"+  products[best[0]] + "\n"
     str = str +  "Ratings  :-"+  ratings[best[0]] + "\n"
     str = str +  "Storage  :-"+  storages[best[0]] + "\n"
     str = str +  "Camera   :-"+  cameras[best[0]] + "\n"
     str = str +  "Screen   :-"+  screens[best[0]] + "\n"
     str = str +  "Battery  :-"+  batterys[best[0]] + "\n"
     str = str +  "Processor:-"+  processors[best[0]] + "\n"
     str = str +  "Prices   :-"+  prices[best[0]]+ "\n"

      


         
    #  # Create a Pandas DataFrame and store the mobile name, price, features, and rating.
    #  df = pd.DataFrame({"moble": name, "price": price, "features": features, "rating": rating})
     
    #  # Save the DataFrame to a CSV file.
    #  df.to_csv("mobiles_data.csv")
     return str
     