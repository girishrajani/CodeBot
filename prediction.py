import torch
from unixcoder import UniXcoder
from sentence_transformers import util



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UniXcoder("microsoft/unixcoder-base")


PATH = "model.pt"
model.load_state_dict(torch.load(PATH))
model.eval()
model.to(device)


"""
Extract embeddings from a code snippet or a natural language query.
"""
def get_embeddings(text):
    tokens_ids = model.tokenize([text],max_length=512,mode="<encoder-only>")
    source_ids = torch.tensor(tokens_ids).to(device)
    tokens_embeddings,nl_embedding = model(source_ids)
    norm_nl_embedding = torch.nn.functional.normalize(nl_embedding, p=2, dim=1)
    norm_nl_embedding = norm_nl_embedding.detach().cpu().numpy()[0]
    return norm_nl_embedding

code_corpus = [
"""
num1 = 5 
num2 = 10 
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

""",
"""
num1 = 5 
num2 = 10 
num3  = 22
sum = num1 + num2 + num3
print("The sum of", num1, ",",num3 ,"and", num2, "is", sum)

""",
"""
Hi! I am C0deB0t :0 , I am here to help you write code.
""",
"""
print("I am learning")
""",
"""
To install Python:

To download Python, you need to visit www.python.org, which is the official Python website.
To check if you have python installed on a Windows PC, search in the start bar for Python or run the following on the Command Line (cmd.exe):
python --version
To check if you have python installed on a Linux or Mac, then on linux open the command line or on Mac open the Terminal and type:
python3 --version
""",
"""
Commenting:

Python has commenting capability for the purpose of in-code documentation.
Comments start with a #, and Python will render the rest of the line as a comment.
""",
"""
Data Types:

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
""",
"""

Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets.

Try,
thislist = ["apple", "banana", "cherry"]
print(thislist)
""",
"""
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are created using round brackets.

Try,
thistuple = ("apple", "banana", "cherry")
print(thistuple)
""",
"""
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
Sets are created using curly brackets.

* Note: Set items are unchangeable, but you can remove items and add new items.

Try,
thisset = {"apple", "banana", "cherry"}
print(thisset)
""",
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values.

Try,
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
""",
"""
An "if statement" is written by using the if keyword.

Try,
a = 33
b = 200
if b > a:
  print("b is greater than a")

In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".
""",
"""
The else keyword catches anything which isn't caught by the preceding conditions.

Try,
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".
""",
"""
With the while loop we can execute a set of statements as long as a condition is true.

Try,
Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
""",
"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

Try,
Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
""",
"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
In Python a function is defined using the def keyword.

Try,
def my_function():
  print("Hello from a function")

To call a function, use the function name followed by parenthesis:
def my_function():
  print("Hello from a function")

my_function()
""",
"""
def Average(lst):
    return sum(lst) / len(lst)
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)
print("Average of the list =", average)
""",
"""
numbers = [11, 3, 7, 5, 2]
numbers.sort()
print(numbers)
""",
"""
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
""",
]

vector_database = []
for code in code_corpus:
    vector_database.append(get_embeddings(code))



nl_query  = 'What is List?'
nlq_emb = get_embeddings(nl_query)
nlq_emb

cos_scores = util.cos_sim(nlq_emb, vector_database)[0]
top_results = torch.topk(cos_scores, k=2)

# print(top_results)


type(torch.return_types.topk(top_results))
data = torch.return_types.topk(top_results)
print(data)
max = data.indices
print(max[0])

print(code_corpus[max[0]])