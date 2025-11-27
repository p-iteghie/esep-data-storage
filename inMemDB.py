class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.cur_data = None
        self.in_transaction = False
    
    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("Only one transaction can be active at a time.")
        self.in_transaction = True
        self.cur_data = {}
 
    def put(self, key, val):
        if not self.in_transaction:
            raise Exception("Cannot use put outside of a transaction.")
        self.cur_data[key] = val
           
    def get(self, key):
        return self.data.get(key, None)
    
    def commit(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress.")
        self.data.update(self.cur_data)

        self.cur_data = None
        self.in_transaction = False
    
    def rollback(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress.")
        self.cur_data = None
        self.in_transaction = False

if __name__ == "__main__":
    inmemoryDB = InMemoryDB()
    print("Running Tests from Figure 2!")
    
    print("\nTest 1: Get non-existent key")
    result = inmemoryDB.get("A")
    print(f"get('A') = {result}")
    assert result is None, "Expected None"
    
    print("\nTest 2: Put without transaction (should throw error)")
    try:
        inmemoryDB.put("A", 5)
        print("ERROR: Should have thrown an exception")
    except Exception as e:
        print(f"Correctly threw exception: {e}")
    
    print("\nTest 3: Begin transaction and put")
    inmemoryDB.begin_transaction()
    inmemoryDB.put("A", 5)
    print("put('A', 5) in transaction")
    
    print("\nTest 4: Get uncommitted value")
    result = inmemoryDB.get("A")
    print(f"get('A') = {result}")
    assert result is None, "Expected None (not committed yet)"
    
    print("\nTest 5: Update value in transaction")
    inmemoryDB.put("A", 6)
    print("put('A', 6) in transaction")
    
    print("\nTest 6: Commit transaction")
    inmemoryDB.commit()
    print("commit()")
    
    print("\nTest 7: Get committed value")
    result = inmemoryDB.get("A")
    print(f"get('A') = {result}")
    assert result == 6, "Expected 6"
    
    print("\nTest 8: Commit without transaction (should throw error)")
    try:
        inmemoryDB.commit()
        print("ERROR: Should have thrown an exception")
    except Exception as e:
        print(f"Correctly threw exception: {e}")
    
    print("\nTest 9: Rollback without transaction (should throw error)")
    try:
        inmemoryDB.rollback()
        print("ERROR: Should have thrown an exception")
    except Exception as e:
        print(f"Correctly threw exception: {e}")
    
    print("\nTest 10: Get non-existent key B")
    result = inmemoryDB.get("B")
    print(f"get('B') = {result}")
    assert result is None, "Expected None"
    
    print("\nTest 11: Transaction with rollback")
    inmemoryDB.begin_transaction()
    inmemoryDB.put("B", 10)
    print("put('B', 10) in transaction")
    
    print("\nTest 12: Rollback transaction")
    inmemoryDB.rollback()
    print("rollback()")
    
    print("\nTest 13: Get rolled-back value")
    result = inmemoryDB.get("B")
    print(f"get('B') = {result}")
    assert result is None, "Expected None (rolled back)"
    
    print("\nAll tests passed!")