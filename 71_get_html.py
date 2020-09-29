
import urllib.request

def get_html(url):

    response = urllib.request.urlopen(url)
    page_resource = response.read()

    return page_resource

print(get_html('http://google.com'))