import web

db = web.database(dbn='mysql', user='acousticpants', pw='some_pass', db='todo')

def get_todo():
    return db.select('todo', order = 'id')

def new_todo(text):
    db.insert('todo', title = text)

def del_todo(id):
    db.delete('todo', where = "id=$id", vars=locals())
