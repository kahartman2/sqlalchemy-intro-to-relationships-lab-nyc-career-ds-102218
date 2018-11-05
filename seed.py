from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below

tom_hanks = Actor(name = 'Tom Hanks')
gwyneth_paltrow = Actor(name = 'Gwyneth Paltrow')
jennifer_anniston = Actor(name = 'Jennifer Anniston')

tom_hanks.roles = [Role(character = 'Forrest Gump'), Role(character = 'Jim Lovell'), Role(character = 'Woody'), Role(character = 'Robert Langdon')]
gwyneth_paltrow.roles = [Role(character = 'Pepper Potts'), Role(character = 'Margot Tenenbaum')]
jennifer_anniston.roles = [Role(character = 'Rachel Green')]

# forest_gump = Role(character = 'Forest Gump', actor = tom_hanks)
# jim_lovell = Role(character = 'Jim Lovell', actor = tom_hanks)
# woody = Role(character = 'Woody', actor = tom_hanks)
# robert_langdon = Role(character = 'Robert Langdon', actor = tom_hanks)

# pepper_potts = Role(character = 'Pepper Potts', actor = gwyneth_paltrow)
# margot_tenenbaum = Role(character = 'Margot Tenenbaum', actor = gwyneth_paltrow)
#
# rachel_green = Role(character = 'Rachel Green')

# session.add_all([tom_hanks, gwyneth_paltrow, jennifer_anniston, forest_gump, jim_lovell, woody, robert_langdon, pepper_potts, margot_tenenbaum, rachel_green])
# session.commit()

session.add_all([tom_hanks, gwyneth_paltrow, jennifer_anniston])
session.commit()
