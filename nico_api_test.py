#Nico Dou Custom Search
import requests, json, datetime


def fetch_from_nico():
    #公式ガイド https://site.nicovideo.jp/search-api-docs/search.html

    #setting
    keyword = '艦これMMD' # search word(tag)
    view = 5000 #threshold of viewCount

    date_gte = (datetime.datetime.today() + datetime.timedelta(days=-30) ).strftime("%Y-%m-%d") # date of 30 days ago
    date_lte = datetime.datetime.today().strftime("%Y-%m-%d") # today's date

    url ="http://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search" # endpoint
    query = {
        'q' : keyword,
        'targets': 'tags',
        'fields' : 'contentId,title,viewCounter,commentCounter,startTime',
        '_sort' : '+startTime',
        'filters[viewCounter][gte]' : view,
        'filters[startTime][gte]' : date_gte + 'T00:00:00+09:00',
        'filters[startTime][lte]' : date_lte + 'T00:00:00+09:00',
        '_limit' : 50,
        '_context': 'test_api'
    }

    r = requests.get(url, params=query)
    api_data = r.json()['data']
    print(r.headers)

    #output
    print("{}件の動画が見つかりました。".format(len(api_data)), end="\n\n")
    for data in api_data:
        print("{} ({}): http://nico.ms/{}".format(data['title'], data['startTime'][:10], data['contentId']))
        print("\t再生数: {}  コメント数: {}".format(data['viewCounter'], data['commentCounter']), end="\n\n")

if __name__ == "__main__":
    fetch_from_nico()