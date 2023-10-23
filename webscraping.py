import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP GET request to the URL
url = "https://example.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Extract data from the HTML
    # Example: Get the title of the page
    title = soup.title.string
    print("Title:", title)

    # Example: Find and print all the links on the page
    links = soup.find_all('a')
    for link in links:
        print("Link:", link.get('href'))

    # You can extract other data based on the HTML structure of the webpage

else:
    print("Failed to retrieve the web page.")

