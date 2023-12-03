import json
import re


class Olx():
    HTML_TAGS = {
        'titles': ['h6', 'css-16v5mdi er34gjf0'],
        'prices': ['p', 'css-10b0gli er34gjf0'],
        'urls': ['a', 'css-rc5s2u'],
        'max_page': ['a', "css-1mi714g"],
        }
    NAME = 'Olx'


    def __init__(
            self, searched_phrase: str, min_price: int, max_price: int, 
            only_new: bool, by_date: bool
            ) -> None:
        
        self.base_url = 'https://www.olx.pl'
        self.searched_phrase = searched_phrase

        self.min_price = min_price
        self.max_price = max_price
        self.only_new = only_new
        self.by_date = by_date


    def get_url(self, page: str) -> str:
        self.url = self.base_url + f'/oferty/q-{self.searched_phrase}/'
        self.url += '?'

        if page:
            self.url += f'page={page}'

        if self.by_date:
            self.url += f'&search%5Border%5D=created_at:desc'

        if self.min_price:
            self.url += f'&search%5Bfilter_float_price:from%5D={self.min_price}'

        if self.max_price:
            self.url += f'&search%5Bfilter_float_price:to%5D={self.max_price}'

        if self.only_new:
            self.url += f'&search%5Bfilter_enum_state%5D%5B0%5D=new'

        return self.url


    def read_titles(self, soup: object) -> list:
        tags = self.HTML_TAGS['titles']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )
    

    def read_prices(self, soup: object) -> list:
        tags = self.HTML_TAGS['prices']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )


    def read_urls(self, soup: object) -> list:
        tags = self.HTML_TAGS['urls']
        return(
            [a['href'] for a in soup.find_all(tags[0], class_=tags[1])]
               )


    def read_max_page(self, soup: object) -> list:
        tags = self.HTML_TAGS['max_page']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )


    def __str__(self) -> str:
        return self.NAME

        
class AllegroLokalnie():
    HTML_TAGS = {
        'titles': ['h3', 'mlc-itembox__title'],
        'prices': ['span', 'ml-offer-price__dollars'],
        'urls': ['a', 'mlc-card mlc-itembox'],
        'max_page': ['div', 'data-mlc-listing-bottom-pagination', 'pages_count'],
        }
    NAME = 'Allegro Lokalnie'

    def __init__(
            self, searched_phrase: str, min_price: int, max_price: int, 
            only_new: bool, by_date: bool
            ) -> None:
        
        self.base_url = 'https://allegrolokalnie.pl'
        self.searched_phrase = searched_phrase.replace('-', '%20')

        self.min_price = min_price
        self.max_price = max_price
        self.only_new = only_new
        self.by_date = by_date


    def get_url(self, page: int) -> str:
        self.url = self.base_url + f'/oferty/q/{self.searched_phrase}/'
        
        if self.only_new:
            self.url += f'nowe'

        self.url += '?'

        if self.by_date:
            pass

        if self.min_price:
            self.url += f'price_from={self.min_price}'

        if self.max_price:
            self.url += f'&price_to={self.max_price}'

        if page:
            self.url += f'&page={page}'

        return self.url
    

    def read_titles(self, soup: object) -> list:
        tags = self.HTML_TAGS['titles']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )
    

    def read_prices(self, soup: object) -> list:
        tags = self.HTML_TAGS['prices']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )


    def read_urls(self, soup: object) -> list:
        tags = self.HTML_TAGS['urls']
        return(
            [a['href'] for a in soup.find_all(tags[0], class_=tags[1])]
               )


    def read_max_page(self, soup: object) -> list:
        tags = self.HTML_TAGS['max_page']
        return(
            json.loads(soup.find(tags[0], {tags[1]: True})[tags[1]]) [tags[2]]
                )


    def __str__(self) -> str:
        return self.NAME

class Allegro():
    HTML_TAGS = {
        'titles': ['h2', "mgn2_14 m9qz_yp meqh_en mpof_z0 mqu1_16 \
                   m6ax_n4 mp4t_0 m3h2_0 mryx_0 munh_0 mj7a_4"],
        'prices': ['span', "mli8_k4 msa3_z4 mqu1_1 mgmw_qw mp0t_ji \
                   m9qz_yo mgn2_27 mgn2_30_s"],
        'urls': ['h2', "mgn2_14 m9qz_yp meqh_en mpof_z0 mqu1_16 m6ax_n4 \
                 mp4t_0 m3h2_0 mryx_0 munh_0 mj7a_4"],
        'max_page': ['span', "_1h7wt mgmw_wo mh36_8 mvrt_8 _6d89c_wwgPl \
                     _6d89c_oLeFV"]
        }
    NAME = 'Allegro'

    def __init__(
            self, searched_phrase: str, min_price: int, max_price: int, 
            only_new: bool, by_date: bool
            ) -> None:
        
        self.base_url = 'https://allegro.pl'
        self.url = self.base_url + f'/oferty/q/{searched_phrase}/' # TODO

        self.min_price = min_price
        self.max_price = max_price
        self.only_new = only_new
        self.by_date = by_date


    def get_url(self, page: int) -> str:
        self.url = self.base_url + '' # TODO

        if self.only_new:
            self.url += f'nowe'

        self.url += '?'

        if self.by_date: # TODO
            pass

        if self.min_price:
            self.url += f'price_from={self.min_price}'

        if self.max_price:
            self.url += f'&price_to={self.max_price}'

        if page:
            self.url += f'&page={page}'

        return self.url
    

    def read_titles(self, soup: object) -> list:
        tags = self.HTML_TAGS['titles']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )
    

    def read_prices(self, soup: object) -> list:
        tags = self.HTML_TAGS['prices']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )


    def read_urls(self, soup: object) -> list:
        tags = self.HTML_TAGS['urls']
        return(
            [re.split('" href="|" title="', str(a))[1] 
             for a in soup.find_all(tags[0], class_=tags[1])]
            )


    def read_max_page(self, soup: object) -> list:
        tags = self.HTML_TAGS['max_page']
        return(
            [a.get_text() for a in soup.find_all(tags[0], class_=tags[1])]
            )
