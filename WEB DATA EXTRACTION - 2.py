from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

scraped_data = []

def scrape():

    bright_star_table = soup.find("table",attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        #print(table_cols)

        temp_list = []

        for col_data in table_cols:
            #print(col_data.text)
            data = col_data.text.strip()
            #print(data)
            temp_list.apeend(data)

        scraped_data.append(temp_list) 

        stars_data = []
         

        for i in range(0,len(scraped_data)):
            Star_names = scraped_data[i][1]
            Distance = scraped_data[i][3]
            Mass = scraped_data[i][5]
            Radius = scraped_data[i][6]
            Lum = scraped_data[i][7] 

            required_data = [Star_names,Distance,Mass,Radius,Lum]
            stars_data.append(required_data)

            headers = ['Star_name','Distance','Mass','Radius','Luminosity']

            star_df_1 = pd.DataFrame(stars_data, columns=headers)

            star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")

new_stars_data = []
def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")  
        temp_list = []
        for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tags = tr_tag.find_all ("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_stars_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

stars_df_1 = pd.read_csv("updated_scraped_data.csv")          

for index, row in stars_df_1.iterrows():
    print(row['hyperlink'])
    scrape_more_data(row['hyperlink'])
    print(f"Data Scraping at hyperlink {index+1}completed")
print(new_stars_data[0:10])

scraped_data = []

for row in new_stars_data:
    replaced = []
    for el in row:
        el = el.replace("\n","")
    scraped_data.append(replaced)

print(scraped_data)        