import time
from contextlib import contextmanager

class DatabaseError(Exception):
    pass

query_count = 0  # Track total queries


@contextmanager
def database_connection():
    """
    Context manager that simulates:
    - Opening database connection
    - Tracking query time
    - Handling errors
    - Properly closing connection
    - Tracking number of queries
    
    Should print:
    - Connection status
    - Query execution time
    - Connection closing status
    - Total queries executed
    """

@contextmanager
def database_connection():
    global query_count
    error = None

    try:
        # Connection opening
        print("Opening database connection...")
        start_time = time.time()
        
        yield
        
    except DatabaseError as e:
        error = f"Database Error: {e}"
    except Exception as e:
        error = f"General Error: {e}"

    finally:
        # Connection closing
        elapsed = time.time() - start_time
        query_count += 2  # Count our simulated queries
        
        print(f"\nConnection Summary:")
        print(f"- Queries executed: {query_count}")
        print(f"- Total time: {elapsed:.2f} seconds")
        
        if error:
            print(f"- Error occurred: {error}")
        
        print("Closing database connection...")

# Test it
with database_connection():
    # Simulate successful query
    time.sleep(1)
    print("Executing query 1...")
    
    # Simulate another query
    time.sleep(0.5)
    print("Executing query 2...")
    
    # Simulate error
    raise DatabaseError("Connection lost!")