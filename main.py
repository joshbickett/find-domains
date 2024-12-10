import requests

# Replace with your WhoisXML API key
API_KEY = "your_api_key_here"

# Base URL for the Domain Availability API
API_URL = "https://domain-availability.whoisxmlapi.com/api/v1"

# List of domains you want to check (populate this array with your domains)
domains_to_check = []

def check_domain_availability(domain):
    """Check the availability of a single domain."""
    params = {
        "apiKey": API_KEY,
        "domainName": domain,
        "outputFormat": "JSON"
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error checking domain {domain}: {e}")
        return None

if __name__ == "__main__":
    if not domains_to_check:
        print("Please populate the 'domains_to_check' list with domains you want to query.")
    else:
        for domain in domains_to_check:
            result = check_domain_availability(domain)
            if result:
                availability = result.get("DomainInfo", {}).get("domainAvailability", "Unknown")
                print(f"Domain: {domain}, Availability: {availability}")
