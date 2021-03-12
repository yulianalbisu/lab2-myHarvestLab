############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller, 
                 ):
        """Initialize a melon."""
        self.pairings = [] #empty list always before text?
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        
        
        
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing) #name of object will work with pairing word, returning pairing attribute

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.update_code = new_code

        print(f'Code updated to {new_code}') #ask about this? whats the new code comming from?

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = [] #return a entire list in this empty brackets

    musk = MelonTypes('muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing('mint') #adding the unique atribute for each melon, name, funct, name string
    all_melon_types.append(musk)
    cas = MelonTypes('casaba', 'cas', 2003, 'orange', False, False)
    cas.add_pairing('strawberries and mint')
    all_melon_types.append(cas)
    cren = MelonTypes('crenshaw', 'cren', 1996, 'green', False, False)
    cren.add_pairing('proscuitto, love it!')
    all_melon_types.append(cren)
    yw = MelonTypes('Yellow Watermelon', 'yw', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # I dont get this!!!!!

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    self.new_code = melon_types

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



