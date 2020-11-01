from app.libs.myHttp import HTTP


class YuShuBook:
    per_page = 15
    id_url = 'https://api.jisuapi.com/isbn/query?appkey=3c6815bcd9872d60&isbn={}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.id_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, page)
        result = HTTP.get(url)
        return result