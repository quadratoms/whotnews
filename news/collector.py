from newspaper import Article

from bs4 import BeautifulSoup
from urllib.request import urlopen

from news.models import Newsmodel, cartegory
import pickle


def main():
	
	f=open('forbidenlist.pkl', 'rb')
	a=pickle.load(f)
	all=[]
	sitelist= [
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
			html = urlopen( site ) # Insert your URL to extrac
			page = BeautifulSoup(html.read(), 'lxml')
			for link in page.find_all('a'):
				b=link.get('href')
				
				if b not in a:
					if b not in all:
						all.append(b)

						if all.count(b)== 2:
							all.remove(b)
							
			
			print(len(all))
			for each in all:
				l=['vanguard', 'nation', 'cnn', 'theguardian', '127', 'dailytimes', 'dailytrust',
				'tribune']
				'''
				the purpose of this is to fetch the image corespond with the model
				e.g {source}.jpg in template
				'''
				source=None
				for s in l:
					if s in each:
						source= s
						break
					else:
						pass

				try:
					url = each
					article = Article(url)
					article.download()
					article.parse()
					
					print(article.title)
					n = Newsmodel()
					n.newscat= cartegory.objects.get(cat=News)
					n.author=article.authors
					n.article_img=article.top_img
					n.heading=article.title
					n.content=article.text
					n.source_url=each
					n.source=source+'.png'
					n.save()
				
				except:
					print('url error')
			a.extend(all)
			all.clear()
			
			
			
				
			
			with open('forbidenlist.pkl', 'wb') as f:
				pickle.dump(a, f)
		badtit=['News', 'Latest Nigeria News, Nigerian Newspapers, Politics', '',
		'Vanguard News', 'Vanguard News, Sports and Business from vanguard Newspapers -',
		'Page'
		]
		for i in badtit:
			Newsmodel.objects.filter(heading=i).delete()

main()