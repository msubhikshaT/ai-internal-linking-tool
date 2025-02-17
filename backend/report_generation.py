import json

def generate_report(internal_links):
    """
    Generate a report with internal link suggestions.
    :param internal_links: List of internal linking suggestions
    :return: None
    """
    for link in internal_links:
        print(f"Suggested Link: {link['from_url']} → {link['to_url']}")
        print(f"Anchor Text: {link['anchor_text']}\n")

if __name__ == "__main__":
    with open("internal_links.json", "r") as f:
        internal_links = json.load(f)
    generate_report(internal_links)
