import requests
import bs4
url = 'https://www.amazon.eg/-/en/b?bbn=21832872031&rh=n%3A18018102031%2Cn%3' \
      'A21832872031%2Cn%3A21832907031&dc&qid=1670526756&rnid=2183' \
      '2872031&ref=lp_21832872031_nr_n_5&node=21832907031'
laptopsprices=[]
laptopsnames=[]
page=requests.get(url)
src=page.content
print(src)
soup = bs4.BeautifulSoup(src, "html.parser")
print(soup)
laptopsnames=soup.find_all("span",{"class":"a-truncate acs-product-block__contributor a-size-base"})
print(laptopsnames)
for i in range(len(laptopsnames)):
    laptopsnames.append(laptopsnames[i].text)
print(laptopsnames)
laptopsprices=soup.find_all("span",{"class":"a-price-whole"})
print(laptopsprices)
for i in range(len(laptopsprices)):
   laptopsprices.append(laptopsprices[i].text)
print(laptopsprices)