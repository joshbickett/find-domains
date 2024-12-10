import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from .env
API_KEY = os.getenv("API_KEY")

# Base URL for the Domain Availability API
API_URL = "https://domain-availability.whoisxmlapi.com/api/v1"

# List of domains to check
domains_to_check = []


def check_domain_availability(domain):
    """Check the availability of a single domain."""
    params = {"apiKey": API_KEY, "domainName": domain, "outputFormat": "JSON"}
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error checking domain {domain}: {e}")
        return None


def format_domain_info(domain, info):
    """Format and display detailed domain information."""
    domain_info = info.get("DomainInfo", {})
    availability = domain_info.get("domainAvailability", "Unknown")
    registrar = domain_info.get("registrarName", "Unknown")
    create_date = domain_info.get("createDate", "N/A")
    expire_date = domain_info.get("expireDate", "N/A")
    godaddy_link = (
        f"https://www.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={domain}"
    )

    print(f"Domain: {domain}")
    print(f"  - Availability: {availability}")
    print(f"  - Registrar: {registrar}")
    print(f"  - Created On: {create_date}")
    print(f"  - Expires On: {expire_date}")
    if availability == "AVAILABLE":
        print(f"  - Purchase Link: {godaddy_link}")
    print("-" * 40)


if __name__ == "__main__":
    if not API_KEY:
        print("Error: API_KEY not set. Please set it in the .env file.")
    elif not domains_to_check:
        print(
            "Please populate the 'domains_to_check' list with domains you want to query."
        )
    else:
        for domain in domains_to_check:
            result = check_domain_availability(domain)
            if result:
                format_domain_info(domain, result)
