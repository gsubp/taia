import util
import requests


def start(id_post):
    ACCESS_TOKEN = "EAAE4pgrzWasBAFJH7Ct4ZCdBZApOAsAknEPcT9ucFNxxrhGhUBZBq5gA9idxT452kkRzgdQYoeZAPpoqqaXuLzICR3hbsDLgXV17PFY3vIHtXiZCpjB5qJTzsoWZAAbaNJHRl0b9bt1191IpAMBJgBZBhSG7X1GkeCPZBeyZCuJdSSAiMxXbWN4k7cAbuW4M4SHQZD"
    BASE_URL = "https://graph.facebook.com/v3.1/"

    url = BASE_URL + id_post + "?fields=comments.limit(100){id,message,like_count,created_time}&access_token=" + ACCESS_TOKEN
    try:
        post = requests.get(url).json()
        comments = post.get('comments').get('data')

        for c in comments:

            util.salva_csv('NULL', c.get('id'), util.tokens(c.get('message')), c.get('created_time'), c.get('like_count'),
                           'NULL')

        if post.get('comments').get('paging') is not None:
            next_page(post.get('comments').get('paging').get('next'))
    except Exception:
        pass


def next_page(url):
    try:
        next = requests.get(url).json()
        for c in next.get('data'):
            util.salva_csv('NULL', c.get('id'), util.tokens(c.get('message')), c.get('created_time'), c.get('like_count'),
                           'NULL', 'NULL', 'NULL')

        if next.get('paging') is not None:
            next_page(next.get('paging').get('next'))
    except Exception:
        pass


