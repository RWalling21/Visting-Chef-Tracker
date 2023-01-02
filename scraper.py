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
    result = soup.find(id="103")
    menu = result.find("div", class_="ds-loc-title")

    # Print the menu
    print(menu.prettify())

def main():
    scrape(url)

if __name__ == "__main__":
    main()

# This code currently does not work because no dining locations are open
# https://stackoverflow.com/questions/53459163/scraping-from-dropdown-option-value-python-beautifulsoup
# I need to change the dropdown value to get to a day where there actually is something on the menu