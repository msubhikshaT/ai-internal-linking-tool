function crawlWebsite() {
    const url = document.getElementById("urlInput").value;
    
    if (!url) {
        alert("Please enter a URL!");
        return;
    }

    fetch("http://127.0.0.1:5000/crawl", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("results").textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error("Error:", error));
}
