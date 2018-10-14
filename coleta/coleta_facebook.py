import requests

ACCESS_TOKEN = "EAAcbblZCvP80BAMuw7b3RYAJj9eeN3EWqpr24AMi3CpZBQw4JVomYuNZAFjgGCAvhOj4IBbfRT6JgUwxADxPZCo6VGLZAVpgIx9om05uYxTP3JzkKKCSZBBV5VzTiAV6qeuUA0yvGntZBATqCoaJcXUTGZCGdl836bQwYSZATVv7KiSNKXw62kVc2nEoP7BuFRa4ZD"
BASE_URL = "https://graph.facebook.com/v3.0/"

url = BASE_URL + "" + "?fields=comments.limit(100){id,message,like_count}&access_token=" + ACCESS_TOKEN
post = requests.get(url).json()
comments = post['comments']
for comment in comments['data']:
    print(comment)
    id_comm = comment['id']
    message = comment['message']
    tokens = message.split()
    tw = ""
    for token in tokens:
        tw = tw + " " + token
    message = tw
    like_count = comment['like_count']
    #salva_csv(id_comm, message, like_count)