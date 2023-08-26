from bs4 import BeautifulSoup
from requests import get


mark = "Chevrolet"
model = "Tahoe"
year = "2012"
def parce_the_image(mark, model, year):
    query = f'{mark}+{model}+{year}'
    query = query.replace(' ', '+')
    url = f'https://google.com/search?q={query}'
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = get(url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    print(url)

if __name__ == "__main__":
    parce_the_image(mark,model,year)
