from core import db as models

class Item(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(50))
    price = models.Column(models.Integer)
    description = models.Column(models.Text)

    def __repr__(self):
        return f'<Item {self.title}>'