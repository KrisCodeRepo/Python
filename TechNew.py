import requests
from bs4 import BeautifulSoup
from newspaper import Article
from datetime import datetime
import time
import pandas as pd
import urllib.parse

# --- CONFIGURATION ---

companies = {
    "CRED": ["cred"],
    "Dream11": ["dream11"],
    "Swiggy": ["swiggy"],
    "Zomato": ["zomato"],
    "Flipkart": ["flipkart"],
    # "Paytm": ["paytm"],
    # "Razorpay": ["razorpay"],
    # "Oyo Rooms": ["oyo"],
    # "PolicyBazaar": ["policybazaar"],
    # "PhonePe": ["phonepe"],
    # "Lenskart": ["lenskart"],
    # "Urban Company": ["urban company"],
    # "BYJU'S": ["byjus", "byju's"],
    # "Freshworks": ["freshworks"],
    # "Meesho": ["meesho"],
    # "Pine Labs": ["pine labs"],
    # "Hike Messenger": ["hike"],
    # "Grofers": ["grofers", "blinkit"],
    # "BigBasket": ["bigbasket"],
    # "Infosys": ["infosys"],
    # "TCS": ["tata consultancy services", "tcs"],
    # "Wipro": ["wipro"],
    # "HDFC Bank": ["hdfc bank"],
    # "Payoneer": ["payoneer"],
    # "Google India": ["google india", "google"],
    # "Microsoft India": ["microsoft india", "microsoft"],
    # "OpenAI": ["openai"],
    # "IBM": ["ibm"],
    # "CTS": ["cognizant technology solutions","cts"],
    # "Google": ["google", "android", "youtube"],
    # "Microsoft": ["microsoft", "azure", "office"],
    # "Apple": ["apple", "ios", "mac"],
    # "Amazon": ["amazon", "aws", "alexa"],
    # "Meta": ["facebook", "meta", "oculus"],
    # "Adobe": ["adobe", "creative cloud"],
    # "Salesforce": ["salesforce", "crm"],
    # "Oracle": ["oracle", "database"],
    # "Intel": ["intel", "semiconductor"],
    # "Nvidia": ["nvidia", "gpu"],
    # "IBM": ["ibm"],
    # "Cisco": ["cisco"],
    # "SAP": ["sap"],
    # "ServiceNow": ["servicenow"],
    # "Zoom": ["zoom"],
    # "Dropbox": ["dropbox"],
    # "Atlassian": ["atlassian", "jira", "confluence"],
    # "Spotify": ["spotify"],
    # "Twitter": ["twitter", "x"],
    # "Slack": ["slack", "salesforce"],
    # # Indian product companies
    # "Freshworks": ["freshworks"],
    # "Zoho": ["zoho"],
    # "BrowserStack": ["browserstack"],
    # "Druva": ["druva"],
    # "Postman": ["postman"],
}

# Trend keywords to highlight
trend_keywords = [
    "AI", "artificial intelligence", "machine learning", "cloud", "automation",
    "blockchain", "data", "future", "innovation", "technology", "ML", "5G",
    "edge computing", "metaverse", "IoT", "cybersecurity"
]

HEADERS = {"User-Agent": "Mozilla/5.0"}
MAX_RESULTS_PER_COMPANY = 2


# --- UTILITIES ---

def clean_google_news_link(link):
    if "news.google.com" in link and "url=" in link:
        parsed = urllib.parse.urlparse(link)
        qs = urllib.parse.parse_qs(parsed.query)
        return qs.get("url", [link])[0]
        
    return link


def get_article_summary(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary.strip()
    except Exception as e:
        print(f"[!] Summary Error ({url}): {e}")
        return ""


def fetch_news_for_company(company_name, keywords):
    search_query = '+OR+'.join(keywords + ['CTO', 'Chief+Technology+Officer', 'technology+update'])
    feed_url = f"https://news.google.com/rss/search?q={search_query}"

    try:
        response = requests.get(feed_url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, "xml")
    except Exception as e:
        print(f"[!] Error fetching news for {company_name}: {e}")
        return []

    news_items = []
    for item in soup.find_all('item')[:MAX_RESULTS_PER_COMPANY]:
        title = item.title.text if item.title else ''
        link = item.link.text if item.link else ''
        description = item.description.text if item.description else ''
        pub_date_raw = item.pubDate.text if item.pubDate else ''
        pub_date = datetime.strptime(pub_date_raw, "%a, %d %b %Y %H:%M:%S %Z") if pub_date_raw else datetime.now()

        actual_link = clean_google_news_link(link)

        # Get summary from actual link
        summary = get_article_summary(actual_link)
        if not summary:
            summary = BeautifulSoup(description, "html.parser").get_text(strip=True)  # clean HTML

        news_items.append({
            "Company": company_name,
            "Title": title,
            "Link": actual_link,
            "Date": pub_date.strftime('%Y-%m-%d %H:%M'),
            "Trend Tag": tag_trends(title),
            "Summary": summary
        })

        time.sleep(3)  # Respectful delay to avoid rate limiting

    return news_items

def tag_trends(text):
    """Tag trends found in the text."""
    tags_found = []
    text_lower = text.lower()
    for keyword in trend_keywords:
        if keyword.lower() in text_lower:
            tags_found.append(keyword)
    return ", ".join(tags_found) if tags_found else "-"

def fetch_all_news():
    all_news = []
    print("[*] Fetching CTO news from companies...\n")
    for company, keywords in companies.items():
        print(f"→ {company}")
        news = fetch_news_for_company(company, keywords)
        all_news.extend(news)
    return sorted(all_news, key=lambda x: x["Date"], reverse=True)


def save_results_to_csv(news_data):
    today = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"CTO_News_{today}.csv"
    df = pd.DataFrame(news_data)
    df.to_csv(filename, index=False)
    print(f"\n[✓] Saved results to {filename}")


def run_task():
    news_data = fetch_all_news()
    if news_data:
        save_results_to_csv(news_data)
        save_results_to_html(news_data)
        print("\n[✓] Task completed successfully.")
    else:
        print("No news postings found.")

def save_results_to_html(news_data):
    today = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"CTO_News_{today}.html"

    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h2>CTO News Summary Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}</h2>
        <table>
            <tr>
                <th>Company</th>
                <th>Title</th>
                <th>Date</th>
                <th>Summary</th>
                <th>Link</th>
            </tr>
    """

    for item in news_data:
        html += f"""
            <tr>
                <td>{item['Company']}</td>
                <td>{item['Title']}</td>
                <td>{item['Date']}</td>
                <td>{item['Summary']}</td>
                <td><a href="{item['Link']}" target="_blank">View</a></td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[✓] Saved HTML report to {filename}")



# --- MAIN ---

if __name__ == "__main__":
    run_task()
