from flask import request, jsonify

from utils import is_isbn_or_key
from yushu_book import YuShuBook
from .blueprint import web
from ..forms.book import SearchForm


@web.route('/book/search/')
def search():
    q = request.args['q']
    page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data.strip()
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyboard(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)