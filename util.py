import csv


def salva_csv(id_user, id_message, text, date, likes, location):
    print(id_message, text, date, likes, location)
    with open('coleta.csv', 'a+', encoding='utf-8', newline='') as file:
        try:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([id_user, id_message, text, date, likes, location])
            file.close()
        except Exception:
            pass


def tokens(message):
    tw = ""
    for token in message.split():
        tw = tw + " " + token
    return tw
