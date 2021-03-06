from urllib.request import urlopen
from bs4 import BeautifulSoup

urls = [
          # Links da Alicia
          'https://coronavirus.jhu.edu/',
          'https://noticias.unb.br/',
          'http://coronavirus.df.gov.br/',
          'https://www.gov.br/pt-br',
          'https://www.paho.org/pt',
          'https://www.saude.df.gov.br/',
          'https://www.unasus.gov.br/',
          'https://unbciencia.unb.br/',
          'https://pt.wikipedia.org/wiki/COVID-19',
          'https://pt.wikipedia.org/wiki/Coronav%C3%ADrus',
          # Links do Caio
          'https://pt.wikipedia.org/wiki/Matrix',
          'https://pt.wikipedia.org/wiki/Star_Wars',
          'https://pt.wikipedia.org/wiki/Indiana_Jones',
          'https://pt.wikipedia.org/wiki/Back_to_the_Future',
          'https://pt.wikipedia.org/wiki/The_Terminator',
          'https://pt.wikipedia.org/wiki/O_Senhor_dos_An%C3%A9is',
          'https://pt.wikipedia.org/wiki/Harry_Potter',
          'https://pt.wikipedia.org/wiki/The_Shining',
          'https://pt.wikipedia.org/wiki/The_Dark_Knight',
          'https://pt.wikipedia.org/wiki/It_(2017)'
					# Links da Bebe
					'https://www.tencent.com/en-us',
					'https://www.samsung.com/br/',
					'https://www.cisco.com/c/pt_br/about.html',
					'https://www.microsoft.com/pt-br/',
					'https://corporate.delltechnologies.com/en-us/about-us/who-we-are.htm',
					'https://www.apple.com/br/',
					'https://www.intel.com/content/www/us/en/homepage.html',
					'https://abc.xyz/',
					'https://www.ibm.com/br-pt',
					'https://www.oracle.com/br/index.html'
       ]

# Abrir arquivo
f = open('seeds.rb', 'w')

f.write("Document.destroy_all\n")

for url in urls:
  html = urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')

  # Recuperar titulo
  for title in soup.find_all('title'):
    title = title.get_text()

  # Retirar conteudo desnecessario
  for script in soup(["script", "style"]):
    script.extract()

  # Recuperar conteudo da pagina
  text = soup.get_text()

  # Quebrar conteudo em linhas e tirar espaco desnecessario
  lines = (line.strip() for line in text.splitlines())

  # Quebrar em blocos
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

  # Retirar linhas vazias
  text = '\n'.join(chunk for chunk in chunks if chunk)

  # retirar aspas duplas e simples
  text = text.replace("'", "")
  text = text.replace('"', '')

  string = f"Document.create!(url: '{url}', title: '{title}', body: '{text}');\n"
  f.write(string)

f.close()
