xpath_selectors = {
    'name' : [
    ],
    'publishedAt' : [
        '//meta[@property="article:published"]/@content'
    ],
    'modifiedAt' : [
        '//meta[@property="article:modified"]/@content'
    ],
    'title' : [
        '//h1/text()',
        '//meta[@property="og:title"]/@content',
    ],
    'title_detail' : [
        '//meta[@property="og:description"]/@content',
        '//meta[@name="description"]/@content',
    ],
    'urlToImg' : [
        '//meta[@property="og:image"]/@content',
    ],
    'author' : [
        '//meta[@name="byl"]/@content',
    ],
    # 'content' : [
    #     '//div[@itemprop = "articleBody"]/descendant::text()[not(ancestor::script)]',
    # ],
    'section' : [
        '//meta[@property="article:section"]/@content',
    ],
    'tags': [
        '//meta[@name="news_keywords"]/@content',
    ],
    'type': [
        '//meta[@property="og:type"]/@content',
    ],
}

schema_handling = {
    'index': 0, # what script should we looked at
    'list_check': False, # True if many schemas are in a list
    'list_index': None, # if it's a list this should be an int()
    'fixed_type': 'NEWSARTICLE', # accepted type
}