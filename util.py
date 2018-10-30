import csv
import re
import unicodedata

from nltk import TweetTokenizer


def salva_csv(id_user, id_message, text, date, likes, location):
    print(id_message, text, date, likes, location)
    with open('coleta1.csv', 'a+', encoding='utf-8', newline='') as file:
        try:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([id_user, id_message, text, date, likes, location])
            file.close()
        except Exception:
            pass


def ler_csv(csv_file):
    base = list()
    with open(csv_file, 'r', encoding='utf-8') as csv_file:
        try:
            reader = csv.reader(csv_file, delimiter='|')

            for row in reader:
                texto = TweetTokenizer().tokenize(row[4])

                for t in texto:
                    if 'https' in t:
                        texto.remove(t)
                    if '#' in t:
                        texto.remove(t)
                    if '@' in t:
                        texto.remove(t)
                    t = t.lower()

                for i in range(len(texto)):
                    t = remove_acento(texto[i])
                    texto[i] = t
                base.append(tuple([texto, str(row[0]).replace('\ufeff', '')]))

        except IOError:
            pass
    return base


def remove_acento(palavra):
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavra = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavra)



def tokens(message):
    tw = ""
    for token in message.split():
        tw = tw + " " + token
    return tw
