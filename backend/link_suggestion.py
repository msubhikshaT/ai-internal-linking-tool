import json

def generate_internal_links(pages):
    """
    Generate internal links based on topic clusters.
    :param pages: List of page dictionaries
    :return: List of internal linking suggestions
    """
    links = []
    for page in pages:
        cluster_pages = [p for p in pages if p['cluster'] == page['cluster'] and p['url'] != page['url']]
        for cluster_page in cluster_pages:
            links.append({
                'from_url': page['url'],
                'to_url': cluster_page['url'],
                'anchor_text': f"Learn more about {cluster_page['title']}"
            })
    return links

if __name__ == "__main__":
    with open("clustered_pages.json", "r") as f:
        pages = json.load(f)
    internal_links = generate_internal_links(pages)
    with open("internal_links.json", "w") as f:
        json.dump(internal_links, f)
