from sqlalchemy import (create_engine, Table, MetaData, Column, Integer,
                        String, tuple_)

from sqlalchemy import select, asc, and_
from consts import DB_URI

eng = create_engine(DB_URI)

meta = MetaData(eng)
users = Table('Users',meta,
    Column('Id', Integer, primary_key=True, autoincrement=True),
    Column('Name', String(50), nullable=False),
)

def execute(s):
    print '-' * 20
    rs = con.execute(s)
    for row in rs:
        print row['Id'], row['Name']

with eng.connect() as con:

    if users.exists() == False:
        users.create()

    for username in ('xiaoming', 'zhangsan','hanmei'):
        user = users.insert().values(Name=username)
        con.execute(user)

    stm = select([users]).limit(1)
    execute(stm)
    
    k = [(2,)]
    stm = select([users]).where(tuple_(users.c.Id).in_(k))
    execute(stm)

    stm = select([users]).where(and_(users.c.Id > 2, users.c.Id < 4))
    execute(stm)

    stm = select([users]).order_by(asc(users.c.Name))
    execute(stm)

    stm = select([users]).where(users.c.Name.like('%mei%'))
    execute(stm)
    
    
