#!/usr/bin/python3


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        length = len(self)
        super().extend(iterable)
        nitems_add = len(self) - length
        print(f"Extended the list with {nitems_add} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        try:
            item = self[index]
        except IndexError:
            raise
        print(f"Popped {item} from the list.")
        return super().pop(index)
