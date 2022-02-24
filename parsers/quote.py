# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-24 08:26:36
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-24 08:40:12

from locators.quote_locators import QuoteLocators

class QuoteParser:
    """
    Given one of the specific quote divs, find out the data
    about the quote (quote content, author and tag)

    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"Quote {self.content} by {self.author}"

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS_LOCATOR
        return self.parent.select_one(locator).string
