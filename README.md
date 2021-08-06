# Michael-Patterson.com

A full featured Django website.

## Implemented Features

-   General
    -   Using NPM to bring in third party static assets.
        -   Bootstrap 5
        -   Animate.css
        -   Hamburgers
    -   Third party assets are compiled with SASS using only the parts that are needed and minifying the output files.
-   Pages App
    -   Static pages with views, templates, and urls.
-   Contact App
    -   Twilio SendGrid email API integration.
    -   Google ReCaptcha.
    -   Store message data to the database.
-   Blog App
    -   Rich-text editing with CKEditor.
    -   Images served with custom Cloudinary integration.
    -   Unique slug generator in the event posts have the same title.
    -   Blog post search feature.
-   Settings
    -   Settings file broken out into smaller files.
    -   Settings files unique to development and production:
        -   manage.py
        -   wsgi.py
-   SEO
    -   Load speed
    -   Semantic HTML
    -   Structured data / JSON-LD
    -   Keywords
    -   Good content
-   Security
    -   Custom middleware to handle HTTP headers:
        -   Strict Transport Security
        -   Content Security Policy
        -   Cache Control
    -   Site has HTTPS implemented.
    -   No inline code in the HTML.
    -   Serve third party files, or CDN links with subresource integrity or nonce.
    -   Environment variables.
-   Production
    -   Google Analytics.
    -   Cloudflare DNS.
    -   Deployed to Heroku.
