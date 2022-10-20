import requests
import bs4 as bs
import re

class camphub_parser:

    def __init__(self, source=None):
        self.source = source
        self.info = self.all_camp_info()
        # request and pass the source to BeautifulSoup

    def get_soup(self, url):
        r = requests.get(url)
        soup = bs.BeautifulSoup(r.text, 'html.parser')
        return soup

    def all_camp_article(self, link):
        # get all article tag
        articles = self.get_soup(link).find_all('article')
        return articles
    
    def camp_info(self, article):
        # get title and link and description
        def get_title_link_desc(article):
            title = article.find('a')['title']
            link = article.find('a')['href']
            desc = article.find('p').text
            return title, link, desc

        # get all information in camp
        def get_info(inside_pages):
            def description_stripper(text):
                text = text.replace(u'\u200b', '')
                text = re.sub(r'\n', '', text)
                return text
            full_description = [description_stripper(x.text) for x in inside_pages.find('div', {'class':'entry-content'}).find_all('p')]
            full_description = ' '.join(full_description)

            info = []
            for i in inside_pages.find_all('h4'):
                info.append(i.get_text(separator=" ").strip())
            mapping = {'type':info[0], 'organize_date':info[1], 'register_deadline':info[2], 'max_paticipants':info[3], 'costs':info[4], 'paticipants_requirements':info[5], 'organizer':info[6], 'full_description':full_description}
            return mapping
        
        def info_parser(article):
            title, link, small_description = get_title_link_desc(article)
            info = {'title':title, 'link':link, 'small_description':small_description}
            inside_pages = self.get_soup(link)
            info.update(get_info(inside_pages))
            return info
        
        return info_parser(article)

    # get all article camp info
    def all_camp_info(self, source=None):
        if source is None:
            source = self.source
        articles = self.all_camp_article(source)
        camp_info_list = []
        for article in articles:
            camp_info_list.append(self.camp_info(article))
        return camp_info_list
