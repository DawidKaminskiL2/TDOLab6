import os

name = os.getenv("NAME", "unknown user")
print(f"Hello {name}")
