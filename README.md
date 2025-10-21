

# pykit: A Pragmatic Utility Library for Modern Python Development

`pykit` is a pure-Python, zero-dependency utility library designed to solve the small, recurring frustrations—the "paper cuts"—of day-to-day Python development. It provides a curated set of simple, reliable, and intuitive tools to reduce boilerplate, encapsulate best practices, and lower the friction of turning ideas into code.

Inspired by excellent libraries like `boltons` and `ubelt`, `pykit` focuses on pragmatism and ease of use, allowing developers to focus on their application logic instead of reinventing common helper functions. [1, 2, 3, 4, 5, 6, 7]

## Key Features

  * **Zero Dependencies:** Pure Python with no third-party requirements. Just drop it into your project or install it with pip.
  * **Intuitive API:** Clean, self-explanatory function names that are easy to remember and use.
  * **Safety by Default:** Functions like `atomic_write` prevent common pitfalls like data corruption. [8]
  * **Pragmatic Solutions:** A curated collection of helpers for the most common, real-world tasks.

## Installation

Once the package is published, you can install `pykit` directly from PyPI:bash
pip install pykit

````

You can also install directly from this GitHub repository:

```bash
pip install git+[https://github.com/YOUR_USERNAME/pykit.git](https://github.com/YOUR_USERNAME/pykit.git)
````

## Quickstart

Let's say you have a messy, nested list of product tags and you need a clean, ordered list of unique tags.

**Before `pykit`:**

```python
messy_tags = ["new", "featured", ["sale", "clearance"], "new", "featured"]

# 1. Flatten the list manually
flat_tags =
for item in messy_tags:
    if isinstance(item, list):
        flat_tags.extend(item)
    else:
        flat_tags.append(item)

# 2. Get unique tags while preserving order
unique_tags =
seen = set()
for tag in flat_tags:
    if tag not in seen:
        unique_tags.append(tag)
        seen.add(tag)

print(unique_tags)
# Output: ['new', 'featured', 'sale', 'clearance']
```

**After `pykit`:**

```python
from pykit import collections

messy_tags = ["new", "featured", ["sale", "clearance"], "new", "featured"]

flat_tags = collections.flatten(messy_tags)
unique_tags = collections.unique(flat_tags)

print(unique_tags)
# Output: ['new', 'featured', 'sale', 'clearance']
```

## Usage Examples

### Safely Manage Nested Configuration

Safely read a nested value from a JSON file and write an update back atomically, preventing data loss even if the program crashes. [9, 8, 10]

```python
from pykit import io, collections
import json

# config.json: {"db": {"prod": {"host": "localhost"}}}

try:
    config = io.read_json('config.json')
except FileNotFoundError:
    config = {}

# Safely get a nested key, providing a default if it's missing
port = collections.get_nested(config, 'db.prod.port', default=3306)
print(f"Using database port: {port}")

# Update the config
config['last_run'] = '2024-10-25T15:00:00Z'

# Write the file back safely
updated_config_string = json.dumps(config, indent=4)
io.atomic_write('config.json', updated_config_string, overwrite=True)
print("Config file updated safely.")
```

### Build a Resilient API Client

Automatically retry a function that might fail due to transient network errors, using exponential backoff. [11, 12]

```python
import requests
from pykit.decorators import retry

@retry(tries=3, delay=2, backoff=2)
def fetch_user_data(user_id):
    """Fetches user data from a potentially unreliable API."""
    print(f"Attempting to fetch data for user {user_id}...")
    response = requests.get(f"[https://api.example.com/users/](https://api.example.com/users/){user_id}")
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

try:
    # This function will be attempted up to 3 times
    user = fetch_user_data(123)
    print("Successfully fetched user data:", user)
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch user data after multiple retries: {e}")
```

### Optimize a Slow Function

Cache the results of an expensive function (memoization) to avoid re-computing them for the same inputs, and time its execution. [13, 14, 15, 16]

```python
import time
from pykit.decorators import memoize, timer

@timer
@memoize
def calculate_complex_metric(param1, param2):
    """A slow, computationally intensive function."""
    time.sleep(2)  # Simulate a long calculation
    return (param1 ** 2) * param2

# First call is slow and the result is cached
print("First call...")
result1 = calculate_complex_metric(10, 5)
# Output: Finished 'calculate_complex_metric' in 2.00... secs

# Second call with the same arguments is instantaneous
print("\nSecond call...")
result2 = calculate_complex_metric(10, 5)
# Output: Finished 'calculate_complex_metric' in 0.00... secs
```

## API Overview

### `pykit.collections`

  * `flatten(nested_list)`: Flattens a list of arbitrarily nested lists. [17, 18]
  * `unique(items)`: Removes duplicates from a list while preserving order. [19, 20]
  * `chunk(items, size)`: Yields successive n-sized chunks from a list. [21, 22]
  * `get_nested(data, key_path, default=None)`: Safely retrieves a value from a nested dictionary using a dot-separated path. [23, 24]
  * `invert_dict(data)`: Inverts a dictionary, handling duplicate values by creating lists of keys. [25, 26]

### `pykit.io`

  * `read_json(filepath)`: Reads and parses a JSON file in one line. [10, 27]
  * `write_json(filepath, data)`: Writes data to a JSON file with pretty-printing. [10, 27]
  * `atomic_write(filepath, content, overwrite=False)`: Writes to a file atomically to prevent data corruption. [9, 8]
  * `read_lines(filepath, strip_whitespace=True)`: Reads a text file into a list of lines, with optional whitespace stripping. [28, 29]

### `pykit.strings`

  * `slugify(text)`: Converts a string into a URL-friendly "slug". [30, 31]
  * `truncate(text, length, placeholder='...')`: Truncates a string to a specified length without breaking words. [32]
  * `is_palindrome(text, case_sensitive=False)`: Checks if a string is a palindrome, ignoring punctuation and whitespace. [33, 34]

### `pykit.time`

  * `parse_date(date_str)`: Parses a date string from a variety of common formats. [35, 36]
  * `humanize_delta(delta)`: Converts a `timedelta` object into a simple, human-readable string (e.g., "2 days"). [37, 38]

### `pykit.decorators`

  * `@memoize`: A simple decorator to cache function results. [13, 14]
  * `@retry(tries, delay, backoff)`: A decorator to retry a function call upon failure with exponential backoff. [11, 12]
  * `@timer`: A decorator that prints the execution time of a function. [15, 16]

## Contributing

Contributions are welcome\! If you find a bug, have a feature request, or want to add a new utility, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.

```
```
