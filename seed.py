from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below

tom_hanks = Actor(name = 'Tom Hanks')
gwyneth_paltrow = Actor(name = 'Gwyneth Paltrow')
jennifer_anniston = Actor(name = 'Jennifer Anniston')

forest_gump = Role(character = 'Forest Gump', actors = tom_hanks)
jim_lovell = Role(character = 'Jim Lovell', actors = tom_hanks)
woody = Role(character = 'Woody', actors = tom_hanks)
robert_langdon = Role(character = 'Robert Langdon', actors = tom_hanks)

pepper_potts = Role(character = 'Pepper Potts', actors = gwyneth_paltrow)
margot_tenenbaum = Role(character = 'Margot Tenenbaum', actors = gwyneth_paltrow)

rachel_green = Role(character = 'Rachel Green')

session.add_all([tom_hanks, gwyneth_paltrow, jennifer_anniston, forest_gump, jim_lovell, woody, robert_langdon, pepper_potts, margot_tenenbaum, rachel_green])
session.commit()
