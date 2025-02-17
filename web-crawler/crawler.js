const { chromium } = require('playwright');
const cheerio = require('cheerio');
const fs = require('fs');

const urls = [
    // Add your URLs here
    'https://www.semrush.com/contentshake/content-marketing-blog/ai-seo-tools/',
    'https://www.semrush.com/contentshake/ai-article-writer/',
    'https://www.semrush.com/contentshake/ai-content-marketing-report/',

];

async function crawlPage(url) {
    try {
        const browser = await chromium.launch();
        const page = await browser.newPage();
        await page.goto(url, { waitUntil: 'networkidle' }); // Corrected line
        const content = await page.content();
        console.log("Page Content Length:", content.length);

        const $ = cheerio.load(content);

        const title = $('title').text();
        console.log("Title:", title);

        const h1Text = $('h2.entry-title').text(); // Or the correct selector
        console.log("H1 Text:", h1Text);

        const bodyText = $('body').text();
        console.log("Body Text Length:", bodyText.length);

        await browser.close();
        return { url, title, h1Text };
    } catch (error) {
        console.error(`Error crawling ${url}:`, error);
        return { url, error: error.message, stack: error.stack };
    } finally {
        // No need to close the browser here; it's done within the try block.
    }

} // <--- END OF REPLACEMENT FUNCTION

async function crawlWebsite() {
    let pages = [];
    for (const url of urls) {
        await new Promise(resolve => setTimeout(resolve, 500)); // Rate limiting
        const page = await crawlPage(url); // Call the improved crawlPage function
        pages.push(page);
    }

    fs.writeFileSync('website_data.json', JSON.stringify(pages, null, 2));
    console.log('Crawling complete, data saved in website_data.json');
}

crawlWebsite();


 
     
     