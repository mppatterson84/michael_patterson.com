class ExtraHttpHeaders:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        response['Strict-Transport-Security'] = 'max-age=63072000'

        csp_sse_urls = [
            "https://stats.g.doubleclick.net",
            "https://www.google-analytics.com",
            "https://code.jquery.com",
            "https://www.googletagmanager.com",
            "https://cdn.jsdelivr.net",
            "https://cdnjs.cloudflare.com",
            "https://www.google.com",
            "https://www.gstatic.com",
            "https://media-library.cloudinary.com/global/all.js"
        ]

        csp_sse = ' '.join([str(u) for u in csp_sse_urls])

        csp = [
            "default-src 'self';",
            "img-src *;",
            f"script-src-elem 'self' {csp_sse};",
            "style-src * 'unsafe-inline';",
            "font-src *;",
            "connect-src 'self' https://www.google-analytics.com https://stats.g.doubleclick.net;",
            "frame-src 'self' https://www.google.com/"
        ]

        response['Content-Security-Policy'] = "".join(csp)
        # Code to be executed for each request/response after
        # the view is called.

        return response
