import requests
from bs4 import BeautifulSoup

def check_pwned(email):
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("section", class_="pwnedCompany")
    for result in results:
        title = result.find("h2").text.strip()
        breaches = result.find_all("a")
        for breach in breaches:
            print(f"{title}: {breach.text.strip()}")

email = "exemplo@gmail.com"
check_pwned(email)
