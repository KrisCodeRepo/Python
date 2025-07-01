import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
from datetime import datetime, timedelta
import pytz
from newspaper import Article

# Target companies and their keywords (can add more)
companies = {
    "CRED": ["cred"],
    "Dream11": ["dream11"],
    "Swiggy": ["swiggy"],
    "Zomato": ["zomato"],
    "Flipkart": ["flipkart"],
    "Paytm": ["paytm"],
    "Razorpay": ["razorpay"],
    "Oyo Rooms": ["oyo"],
    "PolicyBazaar": ["policybazaar"],
    "PhonePe": ["phonepe"],
    "Lenskart": ["lenskart"],
    "Urban Company": ["urban company"],
    "BYJU'S": ["byjus", "byju's"],
    "Freshworks": ["freshworks"],
    "Meesho": ["meesho"],
    "Pine Labs": ["pine labs"],
    "Hike Messenger": ["hike"],
    "Grofers": ["grofers", "blinkit"],
    "BigBasket": ["bigbasket"],
    "Infosys": ["infosys"],
    "TCS": ["tata consultancy services", "tcs"],
    "Wipro": ["wipro"],
    "HDFC Bank": ["hdfc bank"],
    "Payoneer": ["payoneer"],
    "Google India": ["google india", "google"],
    "Microsoft India": ["microsoft india", "microsoft"],
    "OpenAI": ["openai"],
    "IBM": ["ibm"],
    "CTS": ["cognizant technology solutions","cts"],
    "Google": ["google", "android", "youtube"],
    "Microsoft": ["microsoft", "azure", "office"],
    "Apple": ["apple", "ios", "mac"],
    "Amazon": ["amazon", "aws", "alexa"],
    "Meta": ["facebook", "meta", "oculus"],
    "Adobe": ["adobe", "creative cloud"],
    "Salesforce": ["salesforce", "crm"],
    "Oracle": ["oracle", "database"],
    "Intel": ["intel", "semiconductor"],
    "Nvidia": ["nvidia", "gpu"],
    "IBM": ["ibm"],
    "Cisco": ["cisco"],
    "SAP": ["sap"],
    "ServiceNow": ["servicenow"],
    "Zoom": ["zoom"],
    "Dropbox": ["dropbox"],
    "Atlassian": ["atlassian", "jira", "confluence"],
    "Spotify": ["spotify"],
    "Twitter": ["twitter", "x"],
    "Slack": ["slack", "salesforce"],
    # Indian product companies
    "Freshworks": ["freshworks"],
    "Zoho": ["zoho"],
    "BrowserStack": ["browserstack"],
    "Druva": ["druva"],
    "Postman": ["postman"],
}
# Trend keywords to highlight
trend_keywords = [
    "AI", "artificial intelligence", "machine learning", "cloud", "automation",
    "blockchain", "data", "future", "innovation", "technology", "ML", "5G",
    "edge computing", "metaverse", "IoT", "cybersecurity"
]

# Google News RSS base URL template (search for "CTO + company")
GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q=CTO+{}+when:7d&hl=en-IN&gl=IN&ceid=IN:en"

# IST timezone
IST = pytz.timezone('Asia/Kolkata')

def get_article_summary(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary
    except Exception as e:
        print(f"Error summarizing {url}: {e}")
        return ""

def fetch_news_for_company(company_name, keywords):
    """Fetch news items from Google News RSS for the given company."""
    url = GOOGLE_NEWS_RSS.format("+".join(keywords))
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch news for {company_name}")
        return []

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")

    news_list = []
    for item in items:
        title = item.title.text
        link = item.link.text
        pub_date = item.pubDate.text  # Example: Wed, 29 May 2025 22:05:00 GMT
        pub_dt = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %Z')
        pub_dt_ist = pub_dt.replace(tzinfo=pytz.utc).astimezone(IST)

        summary = get_article_summary(link) if link else ''

        # Check if company name appears in title or link as fallback
        if company_name.lower() not in title.lower() and company_name.lower() not in link.lower():
            continue

        news_list.append({
            "Title": title,
            "Company": company_name,
            "URL": link,
            "Posting Date": pub_dt_ist,
            "Trend Tag": tag_trends(title),
            "summary": summary
        })
    return news_list

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
    for company, keywords in companies.items():
        news = fetch_news_for_company(company, keywords)
        all_news.extend(news)
    return all_news

def run_task():
    print(f"\nRunning CTO news fetch at {datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S %Z')}")

    news_data = fetch_all_news()
    if not news_data:
        print("No news postings found in the last 7 days.")
        return

    df = pd.DataFrame(news_data)
    df.sort_values(by="Posting Date", ascending=False, inplace=True)

    # Display table in console
    print(df.to_string(index=False))

    # Save as CSV and HTML
    timestamp = datetime.now(IST).strftime("%Y%m%d_%H%M%S")
    csv_filename = f"cto_news_{timestamp}.csv"
    html_filename = f"cto_news_{timestamp}.html"
    df.to_csv(csv_filename, index=False)
    df.to_html(html_filename, index=False)

    print(f"\nResults saved as {csv_filename} and {html_filename}")

# Scheduling for Monday, Wednesday, Friday at 09:00 IST
def schedule_task():
    # Convert IST 09:00 to UTC for scheduler (since schedule runs in local time)
    # If you run on an IST machine, just schedule directly at 09:00
    schedule.every().monday.at("09:00").do(run_task)
    schedule.every().wednesday.at("09:00").do(run_task)
    schedule.every().friday.at("09:00").do(run_task)

    print("Scheduler started - Waiting for scheduled runs...")
    while True:
        schedule.run_pending()
        time.sleep(30)  # wait 30 sec between checks

if __name__ == "__main__":
    # Uncomment to run once immediately:
    run_task()

    # Start scheduler
    #schedule_task()
