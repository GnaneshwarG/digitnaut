import feedparser
import datetime

# Your Blogger RSS Feed URL
FEED_URL = "https://www.digitnaut.com/feeds/posts/default?alt=rss"

def generate_sitemap():
    feed = feedparser.parse(FEED_URL)
    
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Add Homepage
    sitemap_content += '  <url>\n    <loc>https://www.digitnaut.com/</loc>\n'
    sitemap_content += f'    <lastmod>{datetime.date.today()}</lastmod>\n'
    sitemap_content += '    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>\n'

    # Add Posts from Feed
    for entry in feed.entries:
        sitemap_content += '  <url>\n'
        sitemap_content += f'    <loc>{entry.link}</loc>\n'
        # Extract date
        date = datetime.datetime(*entry.published_parsed[:3]).strftime('%Y-%m-%d')
        sitemap_content += f'    <lastmod>{date}</lastmod>\n'
        sitemap_content += '    <changefreq>monthly</changefreq>\n'
        sitemap_content += '    <priority>0.8</priority>\n  </url>\n'

    sitemap_content += '</urlset>'
    
    with open("sitemap.xml", "w") as f:
        f.write(sitemap_content)

if __name__ == "__main__":
    generate_sitemap()
