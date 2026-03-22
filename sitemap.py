import feedparser
import datetime

FEED_URL = "https://www.digitnaut.com/feeds/posts/default?alt=rss"
BLOG_NAME = "Digitnaut Technical Resources"

def generate_files():
    feed = feedparser.parse(FEED_URL)
    
    # Generate sitemap.xml
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Generate index.html
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{BLOG_NAME}</title>
    <style>
        :root {{ --g-blue: #1a73e8; --g-gray: #f8f9fa; --text: #202124; }}
        body {{ font-family: 'Segoe UI', Roboto, Arial, sans-serif; background: var(--g-gray); color: var(--text); margin: 0; padding: 20px; }}
        .container {{ max-width: 800px; margin: auto; background: white; padding: 40px; border-radius: 8px; border: 1px solid #dadce0; }}
        h1 {{ font-size: 24px; font-weight: 500; margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 15px; }}
        .post-card {{ padding: 20px 0; border-bottom: 1px solid #f1f1f1; text-decoration: none; display: block; transition: 0.2s; }}
        .post-card:hover {{ background: #fdfdfd; padding-left: 10px; border-left: 4px solid var(--g-blue); }}
        .post-title {{ color: var(--g-blue); font-size: 18px; font-weight: 500; text-decoration: none; }}
        .post-meta {{ font-size: 12px; color: #5f6368; margin-top: 5px; }}
        footer {{ margin-top: 40px; font-size: 12px; color: #70757a; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{BLOG_NAME}</h1>
"""

    for entry in feed.entries[:10]:
        date_obj = datetime.datetime(*entry.published_parsed[:3])
        date_str = date_obj.strftime('%Y-%m-%d')
        readable_date = date_obj.strftime('%d %b %Y')

        sitemap_content += f'  <url>\n    <loc>{entry.link}</loc>\n    <lastmod>{date_str}</lastmod>\n  </url>\n'

        html_content += f"""        <a href="{entry.link}" class="post-card">
            <div class="post-title">{entry.title}</div>
            <div class="post-meta">Technical Report • Published {readable_date}</div>
        </a>\n"""

    sitemap_content += '</urlset>'
    html_content += f"""        <footer>Updated on {datetime.date.today()}</footer>
    </div>
</body>
</html>"""
    
    with open("sitemap.xml", "w") as f: f.write(sitemap_content)
    with open("index.html", "w") as f: f.write(html_content)

if __name__ == "__main__":
    generate_files()
