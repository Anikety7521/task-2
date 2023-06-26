import requests
import pytest

def test_website_loading():
    url = "https://www.atg.world"

    response = requests.get(url)

    status_code = response.status_code
    print(f"Response Status Code: {status_code}")
    assert status_code == 200, "Website failed to load"

