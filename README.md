# Iteghie Data Processing and Storage Assignment

## Overview
This project implements an in-memory key-value database with transaction support in Python. The database ensures that multiple operations can be grouped into atomic transactions, preventing dirty writes.

## How to Run

### Prerequisites
- Python 3.6 or higher

### Running the Code

1. **Clone or download the repository**

2. **Open terminal and navigate to repo**

3. **Run the main implementation file:**
   ```
   py inMemDB.py
   ```

4. **The script will automatically run all test cases** from the assignment specification (Fig 2) and display the results.

### Expected Output
When you run the script, you should see output for each test case demonstrating:
- Getting non-existent keys (returns None)
- Error handling when operations are called outside transactions
- Transaction isolation (uncommitted changes are not visible)
- Commit functionality (changes become visible after commit)
- Rollback functionality (changes are discarded)

All tests should pass with "All tests passed!" at the end.

## Suggestions for Future Assignment Modifications

This assignment provides good hands-on experience with atomic transaction concepts, but there are some areas that could be improved. First, the expected behavior of `begin_transaction()` should be clarified. I was unsure if calling it during an active transaction should be ignored or throw an exception. Additionally, the assignment might benefit from additional methods like `delete(key)`, `get_all()`, or `pay(key1, key2, value)` to make the database more complete and closer to common interview design questions. Finally, I think grading could be improved by providing a comprehensive test suite that students must pass, with extra credit for hidden edge cases that encourage more critical thinking.