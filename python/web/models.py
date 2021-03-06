from web import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    # Получает список всех пользователей
    @staticmethod
    def get_all():
        return User.query.all()