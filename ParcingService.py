from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


mark = "Chevrolet"
model = "Corvette"
year = "2012"
def parce_the_image(mark, model, year):
    query = f'{mark}+{model}+{year}'
    query = query.replace(' ', '+')
    url = f'https://google.com/search?tbm=isch&q={query}'
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    #headers = {"user-agent": USER_AGENT}
    #resp = get(url, headers=headers)
    #if resp.status_code == 200:
    #    soup = BeautifulSoup(resp.content, "html.parser")
    #alldivs = soup.findAll('div', class_='bRMDJf')
    print(url)
    driver = webdriver.Chrome()
    driver.set_window_size(300, 300)
    driver.get(url)
    action =ActionChains(driver)
    elems = driver.find_elements("class name", "wXeWr.islib.nfEiy")
    big_picture = ""
    for elem in elems:
        action.move_to_element(elem).click().perform()
        big_picture = driver.find_element("class name", "Du2c7e")
        #нужно вытащить ссылку на полную картинку как-то
    driver.close()
    return big_picture



if __name__ == "__main__":
    big_picture = parce_the_image(mark,model,year)


#https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQL3fu7VFyrZyP1-_jivxnFSm58uXdpnCheGtiYsbeC2X8u93J3YVT0mWByIUKAsS4rYQ&usqp=CAU
#GET
#https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQL3fu7VFyrZyP1-_jivxnFSm58uXdpnCheGtiYsbeC2X8u93J3YVT0mWByIUKAsS4rYQ&usqp=CAU