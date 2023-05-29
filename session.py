from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from getpass import getpass


password = getpass(input('Your password: '))

engine = create_engine(
    f'mysql+pymysql://root:{password}@localhost:3306/blog'
)
Session = sessionmaker(bind=engine)
session = Session()