# Job Listing Scraper

This project is a Python web scraping script that collects job postings from a webpage and exports them into an Excel file.

The project demonstrates how web scraping can be used to collect structured job market data for research, recruitment, or analysis.

## Features

* Scrapes job titles
* Extracts company names
* Collects job locations
* Extracts application links
* Exports the results into an Excel spreadsheet

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* OpenPyXL

## Installation

Clone the repository:

```
git clone https://github.com/ExcelsKennedy2/Job-Listing-Scraper.git
```

Navigate to the project directory:

```
cd job-listing-scraper
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the script:

```
python scraper.py
```

After execution, the script generates:

```
jobs.xlsx
```

This Excel file contains all scraped job listings.

## Example Output

| Job Title        | Company  | Location | Application Link |
| ---------------- | -------- | -------- | ---------------- |
| Python Developer | ABC Tech | Remote   | job link         |

## Learning Objectives

This project demonstrates:

* Sending HTTP requests to a webpage
* Parsing HTML content
* Extracting structured data
* Exporting scraped data to Excel

## Disclaimer

This project is for educational purposes. Always ensure you respect the terms of service of websites when scraping data.
