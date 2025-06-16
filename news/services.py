from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))




def get_posts():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM news_post""")
        posts = dictfetchall(cursor)
        return posts



def get_author():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT news_author.id, news_author.fname,
        news_author.fname,
        news_author.lname,
        news_author.age
        FROM news_author""")
        author = dictfetchall(cursor)
        return author


def get_user():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT news_user.id, news_user.fname, 
        news_user.lname, 
        news_user.age, 
        news_user.image AS image  FROM news_user""")
        user = dictfetchall(cursor)
        return user
