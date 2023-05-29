from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from session import engine

Base = declarative_base(bind=engine)


class User(Base):
    __table__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    second_name = Column(String(50))
    nickname = Column(String(50), unique=True, nullable=False)

    def __str__(self):
        return self.id


class Post(Base):
    __table__ = 'post'

    id = Column(Integer, primary_key=True, autoincremet=True)
    title = Column(String(50))
    content = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))

    def __str__(self):
        return f'Title: {self.title}, User: {self.user_id}'


class Keyword(Base):
    __table__ = 'keyword'

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String(500), nullabel=False)

    def __str__(self):
        return self.word


class PostKeywords(Base):
    __table__ = 'post keywords'

    post_id = Column(Integer, ForeignKey('post.id'))
    keyword_id = Column(Integer, ForeignKey('keyword.id'))

