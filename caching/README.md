![Caching System](https://www.logical-inc.com/wp-content/uploads/LogicalBlog-ClearCache.webp)
# Caching System :sparkles:

This week in Holberton we will be exploring the cachin system, and the following replacement policies:

  - First in first out - [FIFO]("https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29")
  - Last in first out - [LIFO]("https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29")
  - Least recently used [LRU]("https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29")
  - Most recently used [MRU]("https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29")
  - Least frequently used [LFU]("https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29")

## Given Parent class, `BaseCaching`:

```
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Contributors:

**Lindsey Thomas** :sparkles: [timidgeek]("github.com/timidgeek")