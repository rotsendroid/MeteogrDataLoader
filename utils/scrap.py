import os

# $ pip install requests
# API: http://docs.python-requests.org/en/master/api/
import requests


class Scraping:
    """
    Download the corresponding txt files
    """

    MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    DATA_DIR = "data"

    def __init__(self, area, start, stop):
        self.area = area
        self.start_year = start
        self.stop_year = stop

    def download(self):
        # traverse the years
        for i in range(self.start_year, self.stop_year+1):
            test_area_req = requests.get("http://meteosearch.meteo.gr/data/{}".format(self.area))
            if test_area_req.status_code == 404:
                print("Area name invalid!")
                break
            elif test_area_req.status_code == 403:
                for j in Scraping.MONTHS:
                    BASIC_URL = "http://meteosearch.meteo.gr/data/{}/{}-{}.txt".format(self.area, i, j)
                    r = requests.get(BASIC_URL)
                    if r.status_code != 404:
                        if not os.path.exists('{}/{}'.format(Scraping.DATA_DIR, self.area)):
                            os.makedirs("{}/{}".format(Scraping.DATA_DIR, self.area))
                        else:
                            pass
                        # write the txt files
                        with open('{}/{}/{}_{}.txt'.format( Scraping.DATA_DIR, self.area, i, j), 'wb') as f:
                            f.write(r.content)
                        