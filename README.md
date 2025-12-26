# SaaS Review Scraper – Pulse Coding Assignment 4
This project is a Python-based script to scrape SaaS product reviews from G2 and Capterra based on company name and date range.
A third source (Trustpilot) is integrated for bonus points.

Due to bot protection on review platforms, the script includes a fallback mechanism that returns sample review data when automated scraping is blocked.

# Features
- Command-line input support
- Multiple review sources (G2, Capterra, Trustpilot)
- Date validation
- Graceful error handling
- JSON output
- Fallback review data when scraping is blocked

# Tech Stack
- Python 3
- requests
- BeautifulSoup
- argparse
- JSON

# Installation
bash : pip install -r requirements.txt

# Third Source (Bonus): Trustpilot
In addition to G2 and Capterra, this project integrates Trustpilot as a third review source.
Trustpilot pages are heavily protected and often load content dynamically.
If automated scraping is blocked, the script automatically falls back to sample review data.
This ensures consistent output while demonstrating multi-source integration.

# Usage
Run the scraper.py file using the command line:
python scraper.py --company <company name> --start <yyyy-mm-dd> --end <yyyy-mm-dd> --source <source>
bash : "python scraper.py --company slack --start 2024-01-01 --end 2024-12-31 --source g2"

To scrape reviews from Trustpilot, run the script with the "trustpilot" source option:
bash : "python scraper.py --company slack --start 2024-01-01 --end 2024-12-31 --source trustpilot"

# Sample Output
The script generates an output.json file with the following structure:
output.json:
{
  "company": "slack",
  "source": "g2",
  "start_date": "2024-01-01",
  "end_date": "2024-12-31",
  "reviews":
  [
    {
      "title": "Excellent product",
      "review": "Very useful for improving productivity and collaboration.",
      "rating": "5",
      "reviewer": "Verified User",
      "date": "2024-06-12",
      "source": "g2"
    }
  ]
}
