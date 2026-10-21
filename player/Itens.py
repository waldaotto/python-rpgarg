from core.Model import Model

class Itens(Model):
    """Access all itens"""

    def __init__(self):

        super().__init__()
        self.TABLE = 'item'
        self.COLUMNS = (
            'item',
            'desc',
            'item_type',
            'value',
            'price',
        )

        self._constructor([
            "TEXT NOT NULL",
            "TEXT NOT NULL",
            "INT NOT NULL",
            "INTEGER NOT NULL",
            "INTEGER NOT NULL",
        ])
        self._loader()
        self.types = Item_types()

    def _loader(self):
        """Load all records into database"""

        itens_to_load = self._itens()

        if len(self.find_all()) == len(itens_to_load):
            return

        try:
            self.add_many(itens_to_load)
            return True

        except Exception as e:
            raise Exception(e)

    def _itens(self):
        """Return all itens from database"""

        # WARNING : TAKE SURE ALL ITENS TYPES IDS ARE IN ITEM TYPES DB
        # item, desc, item_type, value, price
        # value = attack / defense / healing power, depending on the type
        return [
            # Weapons (value = attack)
            ("Little Sword",  "Small and metallic",                            1, 5,  10),
            ("Sword",         "Big and metallic",                              1, 15,  50),
            ("Dagger",        "Small, light and quick to strike",              1,  8,  25),
            ("War Axe",       "Heavy blade that splits shields in two",        1, 22,  90),
            ("Oak Staff",     "Carved wood that channels weak magic",          1, 12,  60),
            ("Longbow",       "Silent and deadly from a distance",             1, 18,  80),
            ("Flameblade",    "A sword wrapped in a living flame",             1, 35, 400),

            # Armors (value = defense)
            ("Leather Vest",  "Cheap, flexible and better than nothing",       2,  5,  30),
            ("Chainmail",     "Thousands of iron rings linked together",       2, 12, 120),
            ("Plate Armor",   "Full steel protection, but very heavy",         2, 25, 350),

            # Helmets (value = defense)
            ("Iron Helm",     "Dented from many battles",                      3,  4,  40),
            ("Knight's Helm", "Polished steel with a feathered crest",         3,  9, 150),

            # Shields (value = defense)
            ("Wooden Shield", "Splinters fast, but it saves lives",            4,  3,  20),
            ("Tower Shield",  "A wall you can carry in one arm",               4, 14, 180),

            # Potions (value = HP restored)
            ("Health Potion", "A red liquid that closes small wounds",         5, 30,  15),
            ("Elixir",        "Restores a large amount of health",             5, 80,  60),

            # Accessories (value = bonus)
            ("Lucky Charm",   "A rabbit's foot that brings good fortune",      6,  2,  45),
            ("Ring of Honor", "Worn by the guards of an ancient kingdom",      6,  5, 200),
        ]

class Item_types(Model):
    """Type of itens"""

    def __init__(self):
        super().__init__()
        self.TABLE = 'item_type'
        self.COLUMNS = ("type",)

        self._constructor(["TEXT NOT NULL"])
        self._loader()

    def _loader(self):
        """Load all records into database"""

        types_to_load = self._itens_types()

        if len(self.find_all()) == len(types_to_load):

            return

        try:
            self.add_many(types_to_load)
            return True

        except Exception as e:
            raise Exception(e)

    def _itens_types(self):
        """Return all itens types from databse"""

         # item_type (id, type)
        return [
            ("weapon",),     # id 1
            ("armor",),      # id 2
            ("helmet",),     # id 3
            ("shield",),     # id 4
            ("potion",),     # id 5
            ("accessory",),  # id 6
        ]

                

                
