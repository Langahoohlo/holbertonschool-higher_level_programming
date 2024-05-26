class VerboseList(list):
    """A subclass of list that provides notifications for list operations."""

    def append(self, item):
        """Append an item to the list and print a notification.

        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        """Extend the list with items and print a notification.

        Args:
            items: The iterable of items to add to the list.
        """
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """Remove the first occurrence of an item from the list and print a notification.

        Args:
            item: The item to be removed from the list.
        
        Raises:
            ValueError: If the item is not found in the list.
        """
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """Remove and return an item at the given index and print a notification.

        Args:
            index (int, optional): The index of the item to be removed. Defaults to -1 (the last item).

        Returns:
            The item that was removed from the list.
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
