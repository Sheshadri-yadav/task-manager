from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/taskmanager')

metadata = MetaData()
metadata.reflect(bind=engine)




