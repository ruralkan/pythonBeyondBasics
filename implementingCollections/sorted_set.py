
# importing "bisect" for bisection operations 
from bisect import bisect_left
#from collections.abc import Sequence
#we dont use collection.abc, because we've overrdiden all of the methodsinherited from collection.abc sequence
#except dunder reverse, but  we dont need to override that because there's alredy fallback in the reversed implemetation to a dunder getitem and dunder len

from itertools import chain

class SortedSet():
    def __init__(self, items = None):
        self._items = sorted(set(items)) if items is not None else []
    
    """
    dunder contain is the most fundamental of the collection protocols and simply allows us to determine whether a particular item is present in the collection
    dunder contains accept a single argument, which is the item to test for and returns a Boolean
    Our dunder contains implementation will just use the membership test on the enclosed list object
    """
    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False
            
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

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    #We know that the list inside our set is always sorted, we try to improve index search
    #We implement dindex method
    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and (self._items[index] == item):
            return index
        raise ValueError("{} not found".format(repr(item)))
    

    #We know that the list inside our set is always sorted, we try to improve count method
    #We override the count implementation
    # so we should be able to perform a  binary search for the element in a time proportional to log n 
    def count(self, item):
        return int(item in self) 
    
    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))
    
    def __mult__(self, rhs):
        """Note: the only reason wecan return simpy self is because our SortedSet object are immutable,
        If or when they are made mutable, it would be necessary to return a copy of the self object
        This could be achieved either by passing self to the SortedSet constructuro or perhaps
        by implementing a more efficient copy method"""
        return self if rhs > 0 else SortedSet()


