# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-24 08:25:48
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-24 08:25:48

from bs4 import BeautifulSoup

from locators.quote_page_locator import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotePages:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
