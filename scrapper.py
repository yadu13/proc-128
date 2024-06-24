from bs4 import BeautifulSoup
import requests
import pandas as pd


new_stars_data=[]
def scrap_more_data(hyperlink):
    page=requests.get(hyperlink)
    soup=BeautifulSoup(page.content,"html.parser")
    temp_list=[]
    information_to_extract=["Star_name", "Distance", "Mass", "Radius","Luminosity"]
    for info_name in information_to_extract:
        try:
         value=soup.find("div",text=info_name).find_next("span").text.strip()
         print(value)
         temp_list.append(value)
        except:
         temp_list.append("Unknown")
         new_stars_data.append(temp_list)
stars_df_1 =pd.read_csv(r"C:\Users\chitr\Downloads\PROC-128 Web Detection-2\scrapped_data.csv")
for index,row in stars_df_1.iterrows():
       print(row["hyperlink"])
       scrap_more_data(row["hyperlink"])
       print(f"Data scraping at hyperlink {index+1} completed")
headers=["Star_name", "Distance", "Mass", "Radius","Luminosity"]
new_stars_df_1 = pd.DataFrame(new_stars_data,columns = headers)
new_stars_df_1.to_csv('updated_scraped_data.csv',index=True, index_label="id")
