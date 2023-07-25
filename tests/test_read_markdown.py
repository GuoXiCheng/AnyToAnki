import markdown
from bs4 import BeautifulSoup


def test_read_markdown():
    with open('example.md', 'r', encoding='utf-8') as file:
        markdown_text = file.read()
        html = markdown.markdown(markdown_text)
        print(html.split('<hr />')[0])
        first = html.split('<hr />')[0]

        soup = BeautifulSoup(first, 'html.parser')
        # print(soup.find_all('h4')[0].text)
        # print(soup.find('blockquote').find_next('p').text)
        # paragraphs = soup.find_all('h2')

        # for paragraph in paragraphs:
        #     print(paragraph.text)
