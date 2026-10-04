class Backpack:
    """Player backpack object"""

    def __init__(self):

        self._space = 10
        """How much you you can carry"""
        self._itens = [{}] * 10
        """Itens on your backpack"""

    @property
    def space(self):
        """Returns:
            int: backpack space
            """
        return self._space

    @property
    def itens(self)->list:
        """
        Returns:
            dict: an array thats contain X dicts representing itens
        """
        return self._itens

    @property.setter
    def space(self,space: int):
        """
        Args:
            space(int): new space size
        """
        
        self._space = space

    @property.setter
    def itens(self,slot:int,item:dict)->None:
        """
        Args:
            slot(int): item slot;
            item(dict): item dict
        Raises:
            ValueError: if slot already has a item  
        """
        
        if self._itens[slot]:
            raise ValueError(f"Slot {slot} already has a item!")

        self._itens[slot] = item
    
    def drop(self,slot:int)->int:
        """
        Args:
            slot(int): item's slot to drop
        Returns:
            int: dropped item slot
        Raises:
            ValueError: if slot does not have a item
        """

        if not self._itens[slot]:
            raise ValueError(f"Slot {slot} does not have a item to drop! ")
        
        self.itens(slot,{})
        return slot

        


    
