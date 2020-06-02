


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        cur = self.head

        # walk the linked list
        while cur is not None:
            if cur.value == value:
                # Found it!
                return cur

            cur = cur.next

        return None

    def delete(self, value):
        cur = self.head

        # Special case of deleting the head of the list

        if cur.value == value:
            self.head = self.head.next
            return cur

        # General case

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:  # Delete this one
                prev.next = cur.next   # Cuts out the old node
                return cur
            else:
                prev = prev.next
                cur = cur.next

        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.entries = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        loadFactor = self.entries / self.capacity
        return loadFactor

    def fnv1_64(self, string, seed=0):
        """
        Returns: The FNV-1 hash of a given string. 
        """
        # Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        # FNV-1a Hash Function
        hash = offset_basis + seed
        for char in string:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, s):
        hash = 5381
        for x in s:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def get_slot(self, s):
        hash_val = self.djb2(s)
        return hash_val % len(self.data)

    def put(self, key, value):
        slot = self.get_slot(key)
        
        # print(f'[{value}] Slot deemed to be:', slot)
        if self.data[slot] == None:
            self.data[slot] = HashTableEntry(key, value)
            self.entries +=1
        elif self.data[slot].key == key:
            self.data[slot].value = value
        elif self.data[slot].key != key:
            cur = self.data[slot]
            while cur.next is not None:
                cur = cur.next
            cur.next = HashTableEntry(key, value)
            self.entries +=1
            

    def get(self, key):
        slot = self.get_slot(key)
        hash_entry = self.data[slot]
        cur = hash_entry
        if cur: 
            while cur.next != None:
                if cur.key == key:
                    return cur.value
                else:
                    cur = cur.next
            return cur.value
        return None 


    def delete(self, key):
        self.put(key, None)
        self.entries -=1
        

    def resize(self, new_capacity):

        self.capacity = new_capacity

        newData = [None] * new_capacity
        # print('New data:', newData)

        for i in range(len(self.data)):
            newData[i] = self.data[i]

        print('NewData', newData)

        self.data = newData
        
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing

    # ht.delete("line_5")
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

    for i in ht.data:
        print('[]',i.value)


    print(ht.get_load_factor())
