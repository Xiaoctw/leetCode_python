from bs4 import BeautifulSoup
from bs4 import BeautifulStoneSoup
markup='<p class="title"><b>The Little Prince</b></p>'
soup=BeautifulSoup(markup,"lxml")
print(soup.b)