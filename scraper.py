import requests
from bs4 import BeautifulSoup

# URL to the RIT dining services page
url = "https://www.rit.edu/fa/diningservices/daily-specials"

def scrape(url):
    # Get the HTML
    page = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the menu for Brick City (Listed as 103)
    results = soup.find(id="103")

    try:
        # Get the menu for the day
        menu = results.find("div", class_="menu-item").prettify()
    except AttributeError:
        # If the menu returns a NoneType, then there is no menu for that day
        menu = "No menu available today"

    # Print the menu
    print(menu)

def main():
    scrape(url)

if __name__ == "__main__":
    main()