from databasecloud import engine

try:
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("Connection successful! Result:", result.fetchone())
except Exception as e:
    print("Connection failed:", e)