from app import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.String(10), default="Media")

    def __init__(self, title, text, priority="Media"):
        self.title = title
        self.text = text
        self.priority = priority

    def __repr__(self):
        return f"<Post {self.title}>"