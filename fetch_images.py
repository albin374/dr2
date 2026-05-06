import urllib.request, re; html = urllib.request.urlopen('https://drnoushad.vercel.app/').read().decode('utf-8'); print(re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html))
