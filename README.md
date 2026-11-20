# JobInsight – Python Job Listings Scraper

**A Python-based Web Scraping Project**

## 1. Project Description

JobInsight is a Python-based web scraping project designed to collect job listing information from a sample job website.

The project uses Python libraries such as Requests and BeautifulSoup to extract job-related information from web pages and store the collected data in a CSV file.

This project demonstrates the basic concepts of web scraping, HTML parsing, data extraction, and CSV file handling using Python.

## 2. Problem Statement

Searching and collecting job information from websites manually can be time-consuming.

JobInsight provides a simple automated approach to extracting job listing information from a sample website and organizing the collected records into a structured CSV file.

## 3. Project Objectives

- To understand the fundamentals of web scraping.
- To extract job listing information automatically.
- To collect job titles and company names.
- To retrieve job locations and other available listing details.
- To understand HTML parsing using BeautifulSoup.
- To store extracted information in CSV format.
- To develop practical Python programming skills.

## 4. Data Source

**Website:** [Fake Python Jobs – Real Python](https://realpython.github.io/fake-jobs/)

This project uses the Fake Python Jobs website provided by Real Python as its sample data source.

The website is used for educational and practical web scraping purposes.

## 5. Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Sending HTTP requests to the website |
| BeautifulSoup | Extracting information from HTML |
| CSV | Storing collected job information |
| VS Code / Jupyter Notebook | Writing and executing Python code |

## 6. Project Features

- Automated extraction of job listings.
- Collection of available job-related information.
- HTML parsing using BeautifulSoup.
- Website access using the Requests library.
- Storage of extracted records in a CSV file.
- Organized output for future use and analysis.

## 7. Project Folder Structure

```text
JobInsight/
│
├── scraper.py
├── jobs.csv
└── README.md
```

**File Description:**

- `scraper.py` – Contains the Python web scraping code.
- `jobs.csv` – Stores the extracted job listing information.
- `README.md` – Contains project documentation.

## 8. Installation Requirements

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install requests beautifulsoup4
```

## 9. How the Project Works

The project follows these basic steps:

1. Send a request to the sample job website.
2. Receive the webpage HTML content.
3. Parse the HTML using BeautifulSoup.
4. Locate and extract the required job listing information.
5. Organize the extracted information.
6. Save the collected records into a CSV file.

## 10. How to Run the Project

**Step 1:** Download or clone the GitHub repository.

```bash
git clone https://github.com/YOUR-USERNAME/JobInsight.git
```

**Step 2:** Open the project folder.

```bash
cd JobInsight
```

**Step 3:** Install the required libraries.

```bash
pip install requests beautifulsoup4
```

**Step 4:** Run the Python scraper.

```bash
python scraper.py
```

**Step 5:** Open `jobs.csv` to view the collected job listing information.

## 11. Output

The scraper generates a CSV file named:

`jobs.csv`

The file contains the job listing information extracted from the sample website.

The CSV file can be opened using Microsoft Excel, Google Sheets, or any text editor that supports CSV files.

## 12. Project Limitations

- The project currently uses a sample job listing website.
- It focuses on basic web scraping and CSV storage.
- It does not currently provide advanced data analysis.
- It does not include a graphical user interface or frontend.
- The extracted information depends on the structure and availability of the source website.

## 13. Future Improvements

The project can be extended with the following features:

- Add job filtering by location and company.
- Add keyword-based job searching.
- Perform data cleaning and analysis.
- Create interactive data visualizations.
- Develop a web-based user interface.
- Store job information in a database.
- Add more supported job data sources where permitted.

## 14. Learning Outcomes

Through this project, I learned:

- Basic concepts of web scraping.
- How HTTP requests work using Python.
- HTML parsing using BeautifulSoup.
- Extracting structured information from websites.
- Writing data into CSV files.
- Organizing a Python project.
- Using GitHub for project sharing and documentation.

## 15. Project Repository

**GitHub Repository:**  
[https://github.com/kedarhatte24/python-job-scraper-projec]


## 16. Author

**Project Name:** JobInsight

**Developed By:** Kedar Hatte

**Department:** Data Science

**Project Type:** Python Web Scraping

**Academic Level:** Second Year Engineering

---

## Acknowledgement

This project uses the Fake Python Jobs sample website provided by Real Python for educational web scraping practice.

**Data Source:** https://realpython.github.io/fake-jobs/

