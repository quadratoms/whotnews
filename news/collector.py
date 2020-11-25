from newspaper import Article

from bs4 import BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

from news.models import Newsmodel
import pickle


def main():
	
	f=open('forbidenlist.pkl', 'rb')
	a=pickle.load(f)
	all=[]
	sitelist= [
		"https://www.vanguardngr.com/news",
		"https://edition.cnn.com/africa",
		"https://edition.cnn.com/world",
		"https://edition.cnn.com/entertainment",
		"https://edition.cnn.com/style",
		"https://thenationonlineng.net/category/news/"
	]
	
	while True:
    		
		

    	
		for site in sitelist:	
			html = urlopen( site ) # Insert your URL to extrac
			page = BeautifulSoup(html.read())
			for link in page.find_all('a'):
				b=link.get('href')
				
				if b not in a:
					if b not in all:
						all.append(b)
						'''if 'https://www.vanguardngr.com/category/' in b:
							all.pop()
						elif 'https://www.vanguardngr.com/author/' in b:
							all.pop()'''
			
			print(len(all))
			for each in all:
				
				try:
					url = each
					article = Article(url)
					article.download()
					article.parse()
					
					print(article.title)
					n = Newsmodel()
					n.author=article.authors
					n.article_img=article.top_img
					n.heading=article.title
					n.content=article.text
					n.source_url=each
					n.save()
				
				except:
					print('url error')
			a.extend(all)
			all.clear()
			
			
			
				
			
			with open('forbidenlist.pkl', 'wb') as f:
				pickle.dump(a, f)
			
main()	
		
