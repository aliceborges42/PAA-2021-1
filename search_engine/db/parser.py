from urllib.request import urlopen
from bs4 import BeautifulSoup

urls = [
          # Links da Alícia
          'https://coronavirus.jhu.edu/',
          'https://noticias.unb.br/',
          'http://coronavirus.df.gov.br/',
          'https://www.gov.br/pt-br',
          'https://www.paho.org/pt',
          'https://www.saude.df.gov.br/',
          'https://www.unasus.gov.br/',
          'https://unbciencia.unb.br/',
          'https://pt.wikipedia.org/wiki/COVID-19',
          'https://pt.wikipedia.org/wiki/Coronav%C3%ADrus'
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

  # Retirar conteudo desnecessário
  for script in soup(["script", "style"]):
    script.extract()

  # Recuperar conteudo da pagina
  text = soup.get_text()

  # Quebrar conteúdo em linhas e tirar espaço desnecessário
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
