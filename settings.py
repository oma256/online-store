from os import environ


POSTGRES = {
    'user': environ.get('POSTGRES_USER'),
    'pw': environ.get('POSTGRES_PASSWORD'),
    'db': environ.get('POSTGRES_DB'),
    'host': environ.get('POSTGRES_HOST'),
    'port': environ.get('POSTGRES_PORT'),
}

SQLALCHEMY_DATABASE_URI = (
    'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
)
