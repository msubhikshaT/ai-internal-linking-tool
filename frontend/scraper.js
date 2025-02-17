const cheerio = require('cheerio');
const fs = require('fs');

function extractContentFromHTML(html) {
    const $ = cheerio.load(html);
    const title = $('title').text();
    const content = $('body').text();
    return { title: title, content: content };
}

fs.readFile('website_data.json', 'utf-8', (err, data) => {
    if (err) throw err;
    const pages = JSON.parse(data);
    const extractedPages = pages.map(page => {
        return extractContentFromHTML(page.content);
    });
    fs.writeFileSync('extracted_pages.json', JSON.stringify(extractedPages, null, 2));
});
