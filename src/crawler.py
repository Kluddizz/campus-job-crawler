import requests
from bs4 import BeautifulSoup
from adapters import hsflensburg_adapter, caukiel_adapter

institutions = {
    'Hochschule Flensburg': {
        'url': 'https://hs-flensburg.de/hochschule/organisation/zentrale-verwaltung/personaldienstleistungen/stellenangebote',
        'adapter': hsflensburg_adapter
    },

    'Christian-Albrechts-Universität zu Kiel': {
        'url': 'https://www.uni-kiel.de/personal/de/stellen/extern/wiss',
        'adapter': caukiel_adapter
    }
}

for institution in institutions.keys():
    request_url = institutions[institution]['url']
    request_adapter = institutions[institution]['adapter']

    response = requests.get(request_url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = request_adapter(soup)
    print(institution)
    print(jobs)