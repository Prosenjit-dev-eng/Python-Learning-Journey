Type	Syntax Example
List	myList = [1, 2, 3]
Tuple	myTuple = (1, 2, 3)

🧠 2. Mutability
Feature	List	Tuple
Mutable	✅ Yes	❌ No
Can change elements?	✅ Yes	❌ No

python
Copy
Edit
# List
l = [1, 2, 3]
l[0] = 99  # OK

# Tuple
t = (1, 2, 3)
t[0] = 99  # ❌ Error: 'tuple' object does not support item assignment
📚 3. Methods Available
Feature	List	Tuple
Has many built-in methods (e.g., append(), pop())	✅ Yes	❌ Limited (count(), index() only)

⚙️ 4. Performance
Tuples are slightly faster than lists (due to immutability).

Useful when you need fixed, read-only data.

🔐 5. Use Cases
Use Case	List	Tuple
Data that changes over time	✅ List is better	❌ Not recommended
Fixed data structure (e.g., x, y coordinates, RGB values)	❌ Not ideal	✅ Tuple preferred
Dictionary key (must be immutable)	❌ Not allowed	✅ Allowed

python
Copy
Edit
# Tuple as dictionary key — OK
coordinates = {(0, 0): "origin"}

# List as dictionary key — ❌ Error
# coordinates = {[0, 0]: "origin"}  # Invalid
🧪 6. Nesting & Mixed Types
Both can contain mixed types and be nested:

python
Copy
Edit
[1, 'two', (3, 4)]   # List with a tuple
(1, [2, 3], 'four')  # Tuple with a list
✅ Summary Table
Feature	List ([])	Tuple (())
Mutable	✅ Yes	❌ No
Ordered	✅ Yes	✅ Yes
Indexable	✅ Yes	✅ Yes
Methods	Many	Few
Performance	Slower	Faster
Used as dict key	❌ No	✅ Yes

