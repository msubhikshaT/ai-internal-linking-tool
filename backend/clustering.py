from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json

def cluster_pages(pages, n_clusters=5):
    """
    Cluster pages into topics based on content.
    :param pages: List of page dictionaries with content
    :param n_clusters: Number of clusters to form
    :return: List of clusters
    """
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_df=0.85, min_df=2)
    X = vectorizer.fit_transform([page['content'] for page in pages])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    clusters = kmeans.predict(X)
    for i, page in enumerate(pages):
        page['cluster'] = clusters[i]
    return pages

if __name__ == "__main__":
    with open("website_data.json", "r") as f:
        pages = json.load(f)
    clustered_pages = cluster_pages(pages, n_clusters=3)
    with open("clustered_pages.json", "w") as f:
        json.dump(clustered_pages, f)

