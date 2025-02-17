CREATE TABLE pages (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    cluster INTEGER,
    CONSTRAINT fk_cluster FOREIGN KEY (cluster) REFERENCES clusters(id) ON DELETE SET NULL
);

CREATE TABLE internal_links (
    id SERIAL PRIMARY KEY,
    from_url TEXT NOT NULL,
    to_url TEXT NOT NULL,
    anchor_text TEXT,
    CONSTRAINT fk_from_url FOREIGN KEY (from_url) REFERENCES pages(url) ON DELETE CASCADE,
    CONSTRAINT fk_to_url FOREIGN KEY (to_url) REFERENCES pages(url) ON DELETE CASCADE
);

CREATE TABLE clusters (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Example query to insert a page:
INSERT INTO internal_links (from_url, to_url) VALUES 
    ('https://www.semrush.com/contentshake/content-marketing-blog/ai-seo-tools/', 'https://www.semrush.com/contentshake/ai-article-writer/'),
    ('https://www.semrush.com/contentshake/content-marketing-blog/ai-seo-tools/', 'https://www.semrush.com/contentshake/ai-content-marketing-report/');
 
