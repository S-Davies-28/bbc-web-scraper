from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.bbc.co.uk/news/technology")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

tech_headings = soup.select('a[href*="/news/"] span[aria-hidden="false"]')

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["Technology News"])

for tech in tech_headings[:7]:
    print(tech.text)
    writer.writerow([tech.text])
file.close()