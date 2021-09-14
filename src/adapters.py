def hsflensburg_adapter(soup):
    content = soup.select('#block-hsfl-content ul li article a')
    jobs = [{'title': link.select('span')[0].text, 'url': link["href"]} for link in content]
    return jobs

def caukiel_adapter(soup):
    content = soup.select('#content-core article h1')
    jobs = [{'title': link.text, 'url': ''} for link in content]
    return jobs