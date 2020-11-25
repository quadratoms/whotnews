
from newspaper import Article

from bs4 import BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

y=['#content',
		'https://www.vanguardngr.com/', 
		'https://www.vanguardngr.com/about/',
		'https://www.vanguardngr.com/advertise-with-us/',
		'https://www.vanguardngr.com/contactus/', 
		'https://www.vanguardngr.com/about/mobile-app-privacy-policy/',
		'https://twitter.com/vanguardngrnews',
		'https://www.vanguardngr.com/',
		'https://www.vanguardngr.com/category/national-news/',
		'https://www.vanguardngr.com/category/headlines/',
		'https://www.vanguardngr.com/category/sports/',
		'https://www.vanguardngr.com/category/politics/',
		'https://www.vanguardngr.com/category/business/',
		'https://www.vanguardngr.com/category/money-market/',
		'https://www.vanguardngr.com/category/capital-market/',
		'https://www.vanguardngr.com/category/business/insurance-and-you/',
		'https://www.vanguardngr.com/category/business/energy/',
		'https://www.vanguardngr.com/category/business/maritime-report/',
		'https://www.vanguardngr.com/category/business/vanguard-money-digest/',
		'https://www.vanguardngr.com/category/public-finance/',
		'https://www.vanguardngr.com/category/economy/',
		'https://digitalpaper.vanguardngr.com/',
		'https://www.vanguardngr.com/category/entertainment/',
		'http://allure.vanguardngr.com/',
		'https://www.vanguardngr.com/videos/',
		'https://www.vanguardngr.com/category/videos/vanguard-live/',
		'https://www.vanguardngr.com/category/editorial/',
		'https://www.vanguardngr.com/category/viewpoints/',
		'http://community.vanguardngr.com/forum',
		'https://www.vanguardngr.com/category/jobs/',
		'https://www.vanguardngr.com/category/columns/',
		'https://www.vanguardngr.com/category/columns/people-politics/',
		'https://www.vanguardngr.com/category/columns/rational-perspectives/',
		'https://www.vanguardngr.com/category/columns/article-of-faith/',
		'https://www.vanguardngr.com/category/columns/talking-point/',
		'https://www.vanguardngr.com/category/columns/people-politics/',
		'https://www.vanguardngr.com/category/columns/the-hub/',
		'https://www.vanguardngr.com/category/columns/sweet-and-sour/',
		'https://www.vanguardngr.com/category/columns/onochie-anibeze/',
		'https://www.vanguardngr.com/category/columns/sunday-perspectives/',
		'https://www.vanguardngr.com/category/columns/my-world/',
		'https://www.vanguardngr.com/category/columns/frankly-speaking/',
		'https://www.vanguardngr.com/category/columns/the-orbit/',
		'https://www.vanguardngr.com/category/columns/nigeria-today/',
		'https://www.vanguardngr.com/category/columns/vista-woman/',
		'https://www.vanguardngr.com/category/romance-an-relationships/',
		'https://www.vanguardngr.com/author/polycarp/',
		'https://www.vanguardngr.com/news/page/2/', 'https://www.vanguardngr.com/news/page/3/', 'https://www.vanguardngr.com/news/page/48894/', 'https://www.vanguardngr.com/news/page/2/',
		'https://www.vanguardngr.com/2020/08/sell-now-on-habari-shop/',
		'https://digitalpaper.vanguardngr.com/', 'https://play.google.com/store/apps/details?id=com.goodbarber.vanguardngrnews&hl=en', 'https://www.vanguardngr.com/2020/01/acknowledgements-and-gratitude-1/', 'https://www.vanguardngr.com/category/more/education/', 'https://www.vanguardngr.com/category/more/environment/', 'https://www.vanguardngr.com/category/motoring/', 'https://www.vanguardngr.com/category/more/metro/', 'https://www.vanguardngr.com/category/more/interview/', 'https://www.vanguardngr.com/category/more/labour/', 'https://www.vanguardngr.com/category/more/law-and-human-rights/', 'https://www.vanguardngr.com/category/more/bus-stop-parliament/', 'https://www.vanguardngr.com/category/more/crime-guard/', 'https://www.vanguardngr.com/category/more/crime-alert/', 'https://www.vanguardngr.com/category/homes-property/', 'https://www.vanguardngr.com/category/business/investors-forum/', 'https://www.vanguardngr.com/category/business/insurance-and-you/', 'https://www.vanguardngr.com/category/features/', 'https://www.vanguardngr.com/category/worship-2/', 'https://www.vanguardngr.com/category/conference-hall/', 'https://www.vanguardngr.com/category/health/', 'https://www.vanguardngr.com/category/travel-and-tourism/', 'https://www.vanguardngr.com/category/columns/human-angle/', 'https://www.vanguardngr.com/category/romance-an-relationships/is-it-beyond-pardon/', 'https://www.vanguardngr.com/category/thearts/', 'https://www.vanguardngr.com/category/tummy-talk/', 'https://www.vanguardngr.com/category/woman-2/', 'https://www.vanguardngr.com/#', 'https://www.vanguardngr.com/category/columns/sports-bassey/', 'https://www.vanguardngr.com/category/columns/people-politics/', 'https://www.vanguardngr.com/category/columns/rational-perspectives/', 'https://www.vanguardngr.com/category/sobowale-on-business/', 'https://www.vanguardngr.com/category/columns/broken-links/', 'https://www.vanguardngr.com/category/columns/owei-lakemfa/', 'https://www.vanguardngr.com/#', 'https://www.vanguardngr.com/category/columns/femi-aribisala/', 'https://www.vanguardngr.com/category/columns/dispatches-from-america', 'https://www.vanguardngr.com/#', 'https://www.vanguardngr.com/category/columns/talking-point/', 'https://www.vanguardngr.com/category/columns/for-crying-out-loud/', 'https://www.vanguardngr.com/category/columns/tip-of-a-new-dawn/', 'https://www.vanguardngr.com/#', 'https://www.vanguardngr.com/category/columns/people-politics/', 'https://www.vanguardngr.com/category/columns/ishaq-modibbo-kawu/', 'https://www.vanguardngr.com/category/columns/the-hub/', 'https://www.vanguardngr.com/#', 'https://www.vanguardngr.com/category/columns/sweet-and-sour/', 'https://www.vanguardngr.com/category/woman-2/lipstick/', 'https://www.vanguardngr.com/category/columns/owei-lakemfa/', 'https://www.vanguardngr.com/#', 'https://www.vanguardngr.com/category/columns/the-passing-scene/', 'https://www.vanguardngr.com/category/columns/my-world/', 'https://www.vanguardngr.com/category/columns/frank-fair/', 'https://www.vanguardngr.com/category/columns/marriage-and-family/', 'https://www.vanguardngr.com/category/columns/oil-gas-summiteer/', 'https://www.vanguardngr.com/category/columns/bits-and-pieces/', 'https://www.vanguardngr.com/#', 'https://www.vanguardngr.com/category/columns/frankly-speaking/', 'https://www.vanguardngr.com/category/columns/sunday-perspectives/', 'https://www.vanguardngr.com/category/columns/nigeria-today/', 'https://www.vanguardngr.com/category/columns/the-orbit/', 'https://www.vanguardngr.com/category/columns/outside-looking-in/', 'https://www.vanguardngr.com/category/columns/joyful-homes/', 'https://www.vanguardngr.com/category/columns/article-of-faith/', 'https://www.vanguardngr.com', 'https://www.vanguardngr.com/', 'https://www.vanguardngr.com/about/',
		]


'''with open('forbidenlist.txt', 'r') as f:
	print(f.readlines())'''


	
def main():
	
	a=open('forbidenlist.txt', 'r')
	a= a.readlines()
	
	al=[]
	sitelist=[
		"https://www.vanguardngr.com/news"
		
	]

	
	for site in sitelist:

		html = urlopen(site) # Insert your URL to extrac
		page = BeautifulSoup(html.read())
		for link in page.find_all('a'):
			b=link.get('href')
			for i in a:
				print(i)
				if b not in i:
					if b not in al:
						al.append(b)
						if 'https://www.vanguardngr.com/category/' in b:
							al.pop()
						elif 'https://www.vanguardngr.com/author/' in b:
							al.pop()
		
		print(len(al))

		for each in al:
			#print(each)
			
			url = each
			article = Article(url)
			article.download()
			article.parse()
			print(article.title)

		for i in al:
			with open('forbidenlist.txt', 'a+') as f:
				print(i)
				f.write(i+'\n')
			f.close()
		al.clear()
main()

'''
					n = Newsmodel()
					n.author=article.authors
					n.article_img=article.top_img
					n.heading=article.title
					n.content=article.text
					n.source_url=each
					n.save()
				except:
					print('url error')
			
'''