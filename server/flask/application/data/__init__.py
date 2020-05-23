from .. import db

def base_insert(data, model):
    for item in data:
        db.session.add(model(item))

    db.session.commit()