from newspaper import Article

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from news.models import Newsmodel, cartegory
import pickle
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main():

    f = open('forbidenlist.pkl', 'rb')
    a = pickle.load(f)
    all = []
    sitelist = [
        "https://dailytimes.ng/category/news/",
        "https://tribuneonlineng.com/category/latest-news/",
        "https://twmagazine.net/category/beauty/",
        "https://twmagazine.net/category/fashion/",
        "https://twmagazine.net/category/living/",
        "https://twmagazine.net/category/love/",
        "https://guardian.ng/latest/",
        "https://www.vanguardngr.com/news",
        "https://edition.cnn.com/africa",
        "https://edition.cnn.com/world",
        "https://edition.cnn.com/entertainment",
        "https://edition.cnn.com",
        "https://thenationonlineng.net/category/news/"
    ]

    while True:

        for site in sitelist:
            req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})

            html = urlopen(req)  # Insert your URL to extrac
            page = BeautifulSoup(html.read(), 'lxml')
            for link in page.find_all('a'):
                b = link.get('href')

                if b not in a:
                    if b not in all:
                        all.append(b)

                        if all.count(b) == 2:
                            all.remove(b)

            print(len(all))
            for each in all:
                l = ['vanguard', 'nation', 'cnn', 'theguardian', '127', 'dailytimes', 'dailytrust',
                     'tribune']
                '''
				the purpose of this is to fetch the image corespond with the model
				e.g {source}.jpg in template
				'''
                source = None
                if each==None:
                    continue
                for s in l:
                    if s in each:
                        source = s
                        break
                    else:
                        pass

                try:
                    url = each
                    article = Article(url)
                    article.download()
                    article.parse()

                    n = Newsmodel()
                    print(article.title)
                    n.author = article.authors
                    n.article_img = article.top_img
                    n.heading = article.title
                    n.content = article.text
                    n.source_url = each
                    n.source = source+'.png'
                    n.save()
                    print("saved")
                    n.newscat.add(cartegory.objects.get(cat="News"))
                    n.save()

                except:

                    print('url error')
            a.extend(all)
            all.clear()

            with open('forbidenlist.pkl', 'wb') as f:
                pickle.dump(a, f)
        badtit = ['News', 'Latest Nigeria News, Nigerian Newspapers, Politics', '',
                  'Vanguard News', 'Vanguard News, Sports and Business from vanguard Newspapers -',
                  'Page'
                  ]
        for i in badtit:
            Newsmodel.objects.filter(heading=i).delete()

# main()
# import pickle
# from concurrent.futures import ThreadPoolExecutor
# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup
# from newspaper import Article
# from news.models import Newsmodel, cartegory
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# def scrape_site(site):
#     forbidden_list = pickle.load(open('forbidenlist.pkl', 'rb'))
#     news_links = []
#     source = None
#     l = ['vanguard', 'nation', 'cnn', 'theguardian',
#          '127', 'dailytimes', 'dailytrust', 'tribune']
#     req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
#     with urlopen(req) as html:
#         page = BeautifulSoup(html, 'lxml')
#         for link in page.find_all('a'):
#             url = link.get('href')
#             if url and url not in forbidden_list and url not in news_links:
#                 news_links.append(url)

#         for link in news_links:
#             if any(s in link for s in l):
#                 for s in l:
#                     if s in link:
#                         source = s + '.png'
#                         break
#                 break

#         news = []
#         # with ThreadPoolExecutor() as executor:
#         for link in news_links:
#             print(link)
#             if link not in forbidden_list:
#                 news.append(scrape_news(link, source))

#         for n in news:
#             try:
#                 data = n.result()
#                 if data:
#                     Newsmodel.objects.create(
#                         newscat=cartegory.objects.get(cat='News'),
#                         author=data['author'],
#                         article_img=data['image_url'],
#                         heading=data['title'],
#                         content=data['text'],
#                         source_url=data['source_url'],
#                         source=source
#                     )
#             except Exception as e:
#                 print(f"Error processing news: {e}")
#     forbidden_list.extend(news_links)
#     with open('forbidenlist.pkl', 'wb') as f:
#         pickle.dump(forbidden_list, f)


# def scrape_news(link, source):
#     try:
#         article = Article(link)
#         article.download()
#         article.parse()
#         return {
#             'author': article.authors,
#             'image_url': article.top_img,
#             'title': article.title,
#             'text': article.text,
#             'source_url': link,
#             'source': source,
#         }
#     except Exception as e:
#         print(f"Error downloading news: {e}")
#         return None


# def main():
#     site_list = [
#         # "https://dailytimes.ng/category/news/",
#         "https://tribuneonlineng.com/category/latest-news/",
#         "https://twmagazine.net/category/beauty/",
#         "https://twmagazine.net/category/fashion/",
#         "https://twmagazine.net/category/living/",
#         "https://twmagazine.net/category/love/",
#         "https://guardian.ng/latest/",
#         "https://www.vanguardngr.com/news",
#         "https://edition.cnn.com/africa",
#         "https://edition.cnn.com/world",
#         "https://edition.cnn.com/entertainment",
#         "https://edition.cnn.com",
#         "https://thenationonlineng.net/category/news/"
#     ]
#     for site in site_list:
#         scrape_site(site)

#     # delete news with bad titles
#     bad_titles = ['News', 'Latest Nigeria News, Nigerian Newspapers, Politics', '',
#                   'Vanguard News', 'Vanguard News, Sports and Business from vanguard Newspapers -', 'Page']
#     Newsmodel.objects.filter(heading__in=bad_titles).delete()


# if __name__ == "__main__":
#     main()
