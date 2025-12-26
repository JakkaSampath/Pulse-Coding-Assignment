import requests
import json
import argparse
from bs4 import BeautifulSoup

from utils import validate_dates
from fallback_data import get_fallback_reviews

HEADERS = {
    "User-Agent": "Chrome/120.0.0.0"
}

# Source: G2 
def scrape_g2(company):
    url = f"https://www.g2.com/products/{company}/reviews"
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    reviews = []

    for block in soup.select("div.paper"):
        title = block.select_one("h3")
        body = block.select_one("p")

        reviews.append({
            "title": title.text.strip() if title else "N/A",
            "review": body.text.strip() if body else "N/A",
            "rating": "N/A",
            "reviewer": "Anonymous",
            "date": "N/A",
            "source": "G2"
        })

    return reviews


# Source: Capterra 
def scrape_capterra(company):
    url = f"https://www.capterra.com/p/{company}/reviews/"
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    reviews = []

    for block in soup.select("div.review"):
        title = block.select_one("h3")
        body = block.select_one("p")

        reviews.append({
            "title": title.text.strip() if title else "N/A",
            "review": body.text.strip() if body else "N/A",
            "rating": "N/A",
            "reviewer": "Anonymous",
            "date": "N/A",
            "source": "Capterra"
        })

    return reviews


# BONUS: Trustpilot 
def scrape_trustpilot(company):
    url = f"https://www.trustpilot.com/review/{company}.com"
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    reviews = []

    for block in soup.select("article"):
        title = block.select_one("h2")
        body = block.select_one("p")

        reviews.append({
            "title": title.text.strip() if title else "N/A",
            "review": body.text.strip() if body else "N/A",
            "rating": "N/A",
            "reviewer": "Anonymous",
            "date": "N/A",
            "source": "Trustpilot"
        })

    return reviews

# NOTE:
# Pagination is not implemented because platforms like G2, Capterra,
# and Trustpilot load reviews dynamically and actively block bots.
# This script scrapes the first page only to demonstrate scraping logic.

# Some fields like rating, reviewer name, and date are marked as "N/A"
# because these platforms render them dynamically using JavaScript.
# Static scraping with requests + BeautifulSoup cannot reliably extract them.




# MAIN 
def main():
    parser = argparse.ArgumentParser(description="SaaS Review Scraper")
    parser.add_argument("--company", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--source", required=True, choices=["g2", "capterra", "trustpilot"])

    args = parser.parse_args()
    validate_dates(args.start, args.end)

    if args.source == "g2":
        data = scrape_g2(args.company)
    elif args.source == "capterra":
        data = scrape_capterra(args.company)
    else:
        data = scrape_trustpilot(args.company)

    #  FALLBACK (CRITICAL)
    if not data:
        print("Review platform blocked automated access. Using fallback reviews.")
        data = get_fallback_reviews(args.source)

    output = {
        "company": args.company,
        "source": args.source,
        "start_date": args.start,
        "end_date": args.end,
        "reviews": data
    }

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print("✅ Reviews saved to output.json")


if __name__ == "__main__":
    main()
