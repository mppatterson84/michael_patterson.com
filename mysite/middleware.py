import base64
import hashlib
import random
import urllib.request

def get_sri(file_url):
    f = ''
    for line in urllib.request.urlopen(file_url):
        f = f + line.decode('utf-8')
    f = f.encode()

    h = hashlib.sha384(f).digest()
    hash_base64 = base64.b64encode(h).decode()
    return 'sha384-{}'.format(hash_base64)


def GetCspNonce(len=16):
    """Return a random nonce."""
    return hex(random.getrandbits(128))


class ExtraHttpHeaders(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        self.nonce_str = GetCspNonce()

        response = self.get_response(request)
        response['Strict-Transport-Security'] = 'max-age=63072000'

        csp_sse_urls = [
            "https://stats.g.doubleclick.net",
            "https://www.google-analytics.com",
            "https://ssl.google-analytics.com",
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
            "default-src 'none'",
            "img-src *",
            f"script-src 'self' 'nonce-{self.nonce_str}' {csp_sse}",
            f"script-src-elem 'self' {csp_sse}",
            "style-src * 'unsafe-inline'",
            "font-src *",
            "connect-src 'self' https://www.google-analytics.com https://stats.g.doubleclick.net",
            "frame-src 'self' https://www.google.com/",
            "frame-ancestors 'none'",
            "base-uri 'none'",
            "form-action 'self'"
        ]

        response['Content-Security-Policy'] = "; ".join(csp)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_template_response(self, request, response):
        response.context_data['nonce'] = self.nonce_str
        return response