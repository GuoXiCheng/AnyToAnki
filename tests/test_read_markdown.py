import markdown
from bs4 import BeautifulSoup


def test_read_markdown():
    with open('example.md', 'r', encoding='utf-8') as file:
        markdown_text = file.read()
        html = markdown.markdown(markdown_text)
        print(html)

        soup = BeautifulSoup(html, 'html.parser')
        paragraphs = soup.find_all('h2')

        for paragraph in paragraphs:
            print(paragraph.text)
