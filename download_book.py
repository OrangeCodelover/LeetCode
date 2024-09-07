import os
import requests
from bs4 import BeautifulSoup

# URL to download the main text from
url = "https://www.piaotia.com/html/7/7197/4370699.html"

# Directory and file name to save the text
save_directory = r"C:\Users\K\Desktop"
file_name = "page_4370699.txt"
file_path = os.path.join(save_directory, file_name)

# Ensure the save directory exists
os.makedirs(save_directory, exist_ok=True)

def fetch_page_content(url):
    """Fetch the content of the page."""
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return response.content

def extract_main_text(html_content):
    """Extract the main text from the HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    # Example selector, adjust based on the actual page structure
    main_text = soup.find('div', {'class': 'content'})  # Update this based on actual HTML structure
    return main_text.get_text(strip=True) if main_text else ""

def save_text_to_file(text, file_path):
    """Save the text to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

try:
    html_content = fetch_page_content(url)
    main_text = extract_main_text(html_content)
    if main_text:
        save_text_to_file(main_text, file_path)
        print(f"Saved content of {url} to {file_path}")
    else:
        print(f"No main text found for {url}")
except Exception as e:
    print(f"Failed to process {url}: {e}")
