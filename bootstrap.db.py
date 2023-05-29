from models import Base


def main():
    # create all tables
    Base.metadata.create_all()


if __name__ == '__main__':
    main()
