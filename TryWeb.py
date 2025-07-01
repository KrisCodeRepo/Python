from bs4 import BeautifulSoup
import requests
URL = "https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
def get_best_sellers():
    best_sellers = [] 
    items = soup.find_all("div", class_="p13n-desktop-grid")
    for item in items:
        title = item.get_text(strip=True)
        best_sellers.append(title) 
    return best_sellers
if __name__ == "__main__":
    best_sellers = get_best_sellers()
    for index, title in enumerate(best_sellers, start=1):
        print(f"{index}. {title}")
# Output: List of best-selling kitchen items from Amazon India
# Note: The output will depend on the current best-sellers on the Amazon India website.
# Make sure to run this code in an environment where you have internet access.
# and the BeautifulSoup and requests libraries installed.
# You can install them using pip:
# pip install beautifulsoup4 requests  
# This code fetches the best-selling kitchen items from Amazon India and prints them.
# It uses the BeautifulSoup library to parse the HTML content of the page and extract the titles of the best-selling items.
# The results will vary based on the current best-sellers on Amazon India.
# Make sure to run this code in an environment where you have internet access.
# and the BeautifulSoup and requests libraries installed.
# You can install them using pip:
# pip install beautifulsoup4 requests