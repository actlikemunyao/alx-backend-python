import sqlite3
import functools

query_cache = {}

def with_db_connection(func):
    """Decorator that opens a DB connection, passes it to the function, then closes it."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    """Decorator that caches query results based on the SQL query string."""
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            # Return cached result
            return query_cache[query]
        # Run the function and cache its result
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Example usage:
if __name__ == '__main__':
    # First call will cache the result
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call will use the cached result
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
