# -*- coding: utf-8 -*-

from zope.component import getMultiAdapter
from plone.memoize.view import memoize
from Products.Five.browser import BrowserView
from collective.tablepage.browser.table import TableViewView

class MultipleTablesView(TableViewView):
    """View with multiple tables"""
    
    def is_label(self, row):
        return isinstance(row, basestring) and row or None

    def getHeader(self, col_index):
        return self.headers()[col_index]
