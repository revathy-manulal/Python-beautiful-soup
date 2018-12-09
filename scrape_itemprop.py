import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.myntra.com/dupatta/indya/indya-sea-green-solid-dupatta/5505196/buy")
		
		res.raise_for_status()
		recipeSoup = BeautifulSoup(res.text, "html.parser")
		type(recipeSoup)
		instructions = recipeSoup.find_all(itemtype=re.compile(r"/Product$"))

		# print 'length of instructions'+str(len(instructions))

		product = {}


		for product_values in instructions:
	
			recipeSoup = BeautifulSoup(str(product_values), "html.parser")
			valueable_tags = recipeSoup.find_all(itemprop=re.compile(r"\w$"))


			product = {}

			for tag in valueable_tags:
				contents = tag.contents
				if '\n' in contents:
					contents.remove('\n')
				
				print tag.get('itemprop'), tag.contents, contents
				product[tag.get('itemprop')] = contents[0] if len(contents) >0 else ''

			print product
