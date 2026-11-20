import requests
from bs4 import BeautifulSoup
import pandas as pd

#website url
url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url,timeout=20)
response.raise_for_status()

#convert htmml into redable structure
soup = BeautifulSoup(response.content,"html.parser")

#find all  job title
job_cards = soup.find_all("div",class_="card-content")

jobs = []

#extract job information
for job in job_cards:

    title = job.find("h2",class_="title").text.strip()

    company = job.find("h3",class_="company").text.strip()

    location = job.find("p",class_="location").text.strip()

    #find job detail link
    card = job.parent
    links = card.find_all("a",class_="card-footer-item")
    job_url = links[1]["href"]

    #store information in dictionary
    jobs.append({"job Title": title,"company":company,"Location":location,"job url ":job_url})

#convert list into data frame

df = pd.DataFrame(jobs)

#save data into CSV
df.to_csv("Job.csv", index=False)

#display result
print("Total jobs collected : ",len(df))
print("CSV file created successfully!")

print(df.head())

