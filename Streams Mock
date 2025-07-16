class Stream:
    def __init__(self, iterable):
        print(f"iterable: received {iterable}")
        self.iterable = iterable

    def map(self, func):
        def generator():
            for item in self.iterable:
                print(f"map: received {item}")
                yield func(item)
        return Stream(generator())

    def filter(self, predicate):
        def generator():
            for item in self.iterable:
                print(f"filter: received {item}")
                if predicate(item):
                    yield item
        return Stream(generator())

    def sort(self, key=None, reverse=False):
        def generator():
            items = list(self.iterable)
            print(f"sort: received all items: {items}")
            items.sort(key=key, reverse=reverse)
            for item in items:
                print(f"sort: yielding {item}")
                yield item
        return Stream(generator())

    def for_each(self, consumer):
        for item in self.iterable:
            print(f"for_each: received {item}")
            consumer(item)

# 📦 Example usage
data = [1, 2, 3, 4, 5]

Stream(data)\
    .map(lambda x: x * 3)\
    .filter(lambda x: x > 5)\
    .sort(reverse=True)\
    .for_each(print)
