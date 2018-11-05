from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_gwyneth_paltrows_roles():
    actor_object = session.query(Actor).filter(Actor.name == 'Gwyneth Paltrow')
    for x in actor_object:
        new_list = x.roles
    return list(map(lambda x: x.character, new_list))

def return_tom_hanks_2nd_role():
    actor_object = session.query(Actor).filter(Actor.name == 'Tom Hanks')
    for x in actor_object:
        new_list = x.roles
    new_list = list(map(lambda x: x.character, new_list))
    return new_list[1]
