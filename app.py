from bs4 import BeautifulSoup
import requests
import csv

tech_page_to_scrape = requests.get("https://www.bbc.co.uk/news/technology")
soup = BeautifulSoup(tech_page_to_scrape.text, "html.parser")

world_page_to_scrape = requests.get("https://www.bbc.co.uk/news/world")
soup2 = BeautifulSoup(world_page_to_scrape.text, "html.parser")

uk_page_to_scrape = requests.get("https://www.bbc.co.uk/news/uk")
soup3 = BeautifulSoup(uk_page_to_scrape.text, "html.parser")

tech_headings = soup.select('a[href*="/news/"] span[aria-hidden="false"]')
world_headings = soup2.select('a[href*="/news/"] span[aria-hidden="false"]')
uk_headings = soup3.select('a[href*="/news/"] span[aria-hidden="false"]')

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["Technology News", "World News", "UK News"])

for tech, world, uk in zip(tech_headings[:7], world_headings[:7], uk_headings[:7]):
    print(tech.text)
    print(world.text)
    print(uk.text)
    writer.writerow([tech.text, world.text, uk.text])
file.close()