class SortedSet:
    def __init__(self, items = None):
        self._items = sorted(set(items)) if items is not None else []
    
    """
    dunder contain is the most fundamental of the collection protocols and simply allows us to determine whether a particular item is present in the collection
    dunder contains accept a single argument, which is the item to test for and returns a Boolean
    Our dunder contains implementation will just use the membership test on the enclosed list object
    """
    def __contains__(self, item):
        return item in self._items
    
    """To obtain the len of items use dunder len method
    The sized protocol allows us to determine how many items are in a collection by passing it to the len built- in function
    """
    def __len__(self):
        return len(self._items)
    
    """ Iterable protocol allows us obtain an iterator over the series of items with iter(iterable)
    we use dunder iter
    """
    def __iter__(self):
        return iter(self._items)
        #We can return generators, but list iterator is likely to be faster
        """
        for item in self._items:
            yield item
        """
    
    """The sequence protocol allows us
    - Retrieve slices by slicing 
	    item = seq[index]
	    item = seq[start: stop]
    - Find items by value
	    index = seq.index(item)
    - Count items
	    num = seq.count(item)
    - Produce a reversed sequence
	    r = reversed(seq)
    - Suport concatenation with + operator and repetition with * operator
    """
    def __getitem__(self, index):
        """This is a more sophisticate version of dunder getitem, which detects wheter it's being called with an index or a slice and acts accordingly""" 
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result



