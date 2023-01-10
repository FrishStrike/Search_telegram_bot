import requests
from bs4 import BeautifulSoup


def get_url(str):
    global response
    global headers
    headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    #str = input().replace(' ', '+')
    url_search = f'https://www.google.com/search?q={str}'
    response = requests.get(url_search, headers=headers)


def get_data(response):
    soup = BeautifulSoup(response.text, 'lxml')
    src = soup.find_all('div', class_='MjjYud')

    file = open('google.txt', 'w', encoding='utf-8')
    for i in src:
        try:
            h3 = i.find('h3', class_='LC20lb MBeuO DKV0Md')
            a = i.find('a').get('href')

            if a[0] != 'h':
                print('no')
                continue

            file.write(h3.text)
            file.write(' --- ')
            file.write(a)
            file.write('\n')
            file.write(' --- ')
            file.write('\n')

        except Exception as AttributeError:
            print('')
    file.close


def get_img():
    url = f'https://www.google.com/search?q={str}&sxsrf=ALiCzsYoWZ0P00CAQ_9oDJQyp8I23eG1vw:1672677234558&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjF2I6jqKn8AhXRl4sKHUTbB88Q_AUoAXoECAEQAw'
    response_img = requests.get(url, headers=headers)

    soup = BeautifulSoup(response_img.text, 'lxml')
    src = soup.find_all('div', class_='isv-r PNCib MSM1fd BUooTd')

    a = src[0].find('a', class_='wXeWr islib nfEiy').get('href')
    print(a)


def get_result():
    with open('google.txt', encoding='utf-8') as file:
        data = file.read()
        print(data)


def main():
    get_url()
    get_data(response)
    #get_img()
    get_result()


if __name__ == '__main__':
    main()
