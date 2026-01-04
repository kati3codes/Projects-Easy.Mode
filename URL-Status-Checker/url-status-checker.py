import requests

def check_status(url):
    if not url.startswith("http"):
        url = f"https://{url}"

    try:
        response = requests.get(url, timeout=3)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("success (200 OK)!")
        else:
            print("Failed or Redirected.")
    except requests.exceptions.RequestException:
        print("Not connect or request timed out.")

target_url = input("Enter a website URL:")
check_status(target_url)