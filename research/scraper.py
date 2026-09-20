"""
Web scraper for B2B strategic account management research.
Scrapes Sodexo, SAMA, HBR, FM industry, competitor sites.
Saves raw text to scrapes/ directory and builds RAG DB entries.
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
import hashlib
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

SCRAPE_DIR = os.path.join(os.path.dirname(__file__), "scrapes")
RAG_DIR = os.path.join(os.path.dirname(__file__), "rag_db")

TARGET_URLS = [
    # Sodexo corporate
    ("sodexo", "https://www.sodexo.com/home/our-expertise/corporate-services.html"),
    ("sodexo", "https://www.sodexo.com/home/our-expertise/integrated-facilities-management.html"),
    ("sodexo", "https://www.sodexo.com/home/our-expertise/workplace-experience.html"),
    ("sodexo", "https://www.sodexo.com/home/media/media-library/press-releases.html"),
    # SAMA - Strategic Account Management Association
    ("sama", "https://www.strategicaccountmgmt.com/resources/research-studies/"),
    ("sama", "https://www.strategicaccountmgmt.com/resources/articles/"),
    # FM industry
    ("fm_industry", "https://www.facilitiesnet.com/businessmanagement/"),
    ("fm_industry", "https://www.fmj.co.uk/business-management/"),
    ("fm_industry", "https://www.ifma.org/research/"),
    # Compass Group (competitor)
    ("competitor", "https://www.compass-group.com/en/what-we-do/our-businesses.html"),
    ("competitor", "https://www.compass-group.com/en/investors.html"),
    # ISS World (competitor)
    ("competitor", "https://www.issworld.com/en/solutions/corporate-facilities-services"),
    # B2B sales / strategic accounts
    ("b2b_frameworks", "https://www.salesforce.com/resources/articles/strategic-account-management/"),
    ("b2b_frameworks", "https://blog.hubspot.com/sales/strategic-account-management"),
    ("b2b_frameworks", "https://www.richardson.com/sales-resources/strategic-account-management/"),
    # HBR on strategic accounts
    ("hbr", "https://hbr.org/2012/09/the-end-of-solution-sales"),
    ("hbr", "https://hbr.org/2014/07/the-key-to-winning-large-strategic-customers"),
    # Gartner / analyst
    ("analyst", "https://www.gartner.com/en/sales/insights/account-management"),
    # McKinsey on B2B growth
    ("mckinsey", "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/b2b-customer-experience"),
    ("mckinsey", "https://www.mckinsey.com/industries/real-estate/our-insights/facilities-management"),
    # Forrester on account management
    ("analyst", "https://www.forrester.com/blogs/category/account-management/"),
]

def scrape_url(url: str, timeout: int = 15) -> str:
    """Fetch URL and return cleaned text content."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout, verify=False)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        # Remove nav, footer, scripts, styles
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "noscript"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        # Clean up whitespace
        lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 40]
        return "\n".join(lines[:300])  # cap at 300 meaningful lines
    except Exception as e:
        return f"SCRAPE_ERROR: {str(e)}"


def url_to_filename(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:12]


def scrape_all(verbose: bool = True) -> list[dict]:
    """Scrape all target URLs, save to disk, return list of RAG entries."""
    entries = []
    os.makedirs(SCRAPE_DIR, exist_ok=True)
    os.makedirs(RAG_DIR, exist_ok=True)

    for i, (category, url) in enumerate(TARGET_URLS):
        if verbose:
            print(f"[{i+1}/{len(TARGET_URLS)}] Scraping {category}: {url[:60]}...")

        fname = url_to_filename(url)
        fpath = os.path.join(SCRAPE_DIR, f"{category}_{fname}.txt")

        # Use cached if exists
        if os.path.exists(fpath):
            with open(fpath) as f:
                content = f.read()
            if verbose:
                print(f"  -> cached ({len(content)} chars)")
        else:
            content = scrape_url(url)
            with open(fpath, "w") as f:
                f.write(content)
            if verbose:
                status = "ok" if not content.startswith("SCRAPE_ERROR") else "ERROR"
                print(f"  -> {status} ({len(content)} chars)")
            time.sleep(1.5)  # polite delay

        if not content.startswith("SCRAPE_ERROR") and len(content) > 100:
            entries.append({
                "id": fname,
                "category": category,
                "url": url,
                "content": content[:3000],  # cap per entry for RAG
                "scraped_at": datetime.now().isoformat(),
            })

    # Save RAG DB
    rag_path = os.path.join(RAG_DIR, "rag_entries.json")
    with open(rag_path, "w") as f:
        json.dump(entries, f, indent=2)

    print(f"\nRAG DB: {len(entries)} entries saved to {rag_path}")
    return entries


def load_rag_db() -> list[dict]:
    rag_path = os.path.join(RAG_DIR, "rag_entries.json")
    if not os.path.exists(rag_path):
        return []
    with open(rag_path) as f:
        return json.load(f)


def search_rag(query: str, entries: list[dict], top_k: int = 5) -> list[dict]:
    """Simple keyword-based RAG search."""
    query_words = set(query.lower().split())
    scored = []
    for entry in entries:
        text = (entry.get("content", "") + " " + entry.get("url", "")).lower()
        score = sum(1 for w in query_words if w in text)
        if score > 0:
            scored.append((score, entry))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in scored[:top_k]]


if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings()
    entries = scrape_all(verbose=True)
    print(f"\nTotal entries in RAG: {len(entries)}")
