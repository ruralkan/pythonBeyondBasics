class SortedSet:
    def __init__(self, items = None):
        self._items = sorted(items) if items is not None else []
    
    """
    dunder contain is the most fundamental of the collection protocols and simply allows us to determine whether a particular item is present in the collection
    dunder contains accept a single argument, which is the item to test for and returns a Boolean
    Our dunder contains implementation will just use the membership test on the enclosed list object
    """
    def __contains__(self, item):
        return item in self._items