import requests
from bs4 import BeautifulSoup

def scrape_static_page(url):
    try:
        # Fetch the HTML content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract relevant information
        # Example: Extract all links
        links = soup.find_all("a")
        for link in links:
            print(f"Link: {link['href']}")

        # Example: Extract all text
        paragraphs = soup.find_all("p")
        for p in paragraphs:
            print(f"Text: {p.text}")

        # Example: Extract all images
        images = soup.find_all("img")
        for img in images:
            print(f"Image Source: {img['src']}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if _name_ == "_main_":
    target_url = "https://example.com"  # Replace with the desired URL
    scrape_static_page(target_url)


