import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

titles = []
companies = []
locations = []
links = []

for job in jobs:

    title = job.find("h2", class_="title").text.strip()

    company = job.find("h3", class_="company").text.strip()

    location = job.find("p", class_="location").text.strip()

    link = job.find("a")["href"]

    titles.append(title)
    companies.append(company)
    locations.append(location)
    links.append(link)

df = pd.DataFrame({
    "Job Title": titles,
    "Company": companies,
    "Location": locations,
    "Application Link": links
})

df.to_excel("jobs.xlsx", index=False)

print("Job data exported to Excel!")