import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """scrape information from linkedin profiles,
    Manually scrape the information from the linkedin profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/nicolau-rodrigues/bf2b3364aad3392134cca82c22a9db6c/raw/964a476a384b043f8f6204eb19751410e63a979d/nicolau-rodrigues.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10)

    else:
        api_key = os.environ.get('PROXYCURL_API_KEY')
        header_dic = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'url': linkedin_profile_url
        }
        response = requests.get(api_endpoint,
                                params=params,
                                headers=header_dic,
                                timeout=10)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/helio-cola/", mock=True)
    )