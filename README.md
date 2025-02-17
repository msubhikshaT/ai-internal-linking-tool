# AI-Powered Internal Linking Tool

## Overview
This tool helps improve website SEO by identifying internal linking opportunities based on content relevance. It crawls a website, clusters pages based on content, and generates suggestions for internal links to boost SEO.

## Features
- Crawls a website's sitemap to extract URLs.
- Uses NLP to cluster pages into topics.
- Suggests internal links between related pages.
- Generates a detailed report of suggested links.
- Optionally stores data in a PostgreSQL database.

## Setup

### Python Backend
1. Install Python and virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   .\venv\Scripts\activate  # For Windows
