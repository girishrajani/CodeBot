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
"""num1 = 5 
num2 = 10 
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)""",
"""num1 = 5 
num2 = 10 
num3  = 22
sum = num1 + num2 + num3
print("The sum of", num1, ",",num3 ,"and", num2, "is", sum)""",
"""Hi! I am c0deb0t, I am here to help you write code.""",
"""print("I am learning")""",
"""To install Python:
To download Python, you need to visit www.python.org, which is the official Python website.
""",

"""Commenting:
Comments start with a #, and Python will render the rest of the line as a comment.""",

"""Data Types: 
Python has the following data types built-in:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType""",

"""Lists are used to store multiple items in a single variable.
Lists are created using square brackets.
Try,
thislist = ["apple", "banana", "cherry"]
print(thislist)""",

"""Tuples are used to store multiple items in single variable. 
Tuples are created using round brackets.
Try,
thistuple = ("apple", "banana", "cherry")
print(thistuple)""",

"""Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable, and unindexed.
Sets are created using curly brackets.
Try,
thisset = {"apple", "banana", "cherry"}
print(thisset)""",

"""Dictionaries are used to store data values in key:value pairs.
Dictionaries are written with curly brackets, and have keys and values.
Try,
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)""",

"""An "if statement" is written by using the if keyword.
Try,
a = 33
b = 200
if b > a:
  print("b is greater than a")""",

"""The else keyword catches anything which isn't caught by the preceding conditions.
Try,
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
""",

"""With the while loop we can execute a set of statements as long as a condition is true.
Try,
Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1""",

"""A for loop is used for iterating over a sequence.
Try,
Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)""",

"""
A function is a block of code which only runs when it is called.
In Python a function is defined using the def keyword.
Try,
def my_function():
  print("Hello from a function")
To call a function, use the function name followed 
by parenthesis:
def my_function():
  print("Hello from a function")
my_function()""",

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
# print(data)
max = data.indices
# print(max[0])

# print(code_corpus[max[0]])


import tkinter as tk
from tkinter import *

print("c0deb0t execution in progress....")


root = tk.Tk()
root.geometry("500x720")
root.title("c0deb0t")
root.iconbitmap("icon.ico")
canvas1 = tk.Canvas(root, width=1000, bg="#14192b", height=1000)
canvas1.pack()

label1 = tk.Label(
    root, text="welcome to c0deb0t", fg="#FFFFFF", bg="#14192b", font=("Helvetica", 18, "bold")
)
label1.place(x=140, y=50)

my_list = tk.Text(root, fg="#c792ea", bg="#292d3e", font=("Dubai", 17, "bold"))
my_list.pack(pady=20)
canvas1.create_window(250, 355, width=398, height=500, window=my_list)

my_text = tk.Text(root, fg="#14192b", font=("Dubai", 15))
my_text.pack(pady=20)
canvas1.create_window(200, 640, width=300, height=50, window=my_text)
    
def gethelp():
    output = ""
    temp = ""
    nl_query = my_text.get(1.0, tk.END)
    temp += "you: " + nl_query
    # nl_query  = 'What is List?'
    nlq_emb = get_embeddings(nl_query)
    nlq_emb
    cos_scores = util.cos_sim(nlq_emb, vector_database)[0]
    top_results = torch.topk(cos_scores, k=2)
    type(torch.return_types.topk(top_results))
    data = torch.return_types.topk(top_results)
    # print(data)
    max = data.indices
    # print(max[0])
    # print(code_corpus[max[0]])
    temp2 = ""
    temp2 += temp
    temp2 += "\n"
    temp2 += "c0deb0t: " + code_corpus[max[0]]
    temp2 += "\n\n"
    my_list.insert(tk.END, temp2)



var = "hello! i'm here to help you write code.\n\n" 

my_list.insert(tk.END, var)

button1 = tk.Button(
    text="Enter", bg="#292d3e", fg="#FFFFFF", font=("SansSerif", 12), command= gethelp 
    )
canvas1.create_window(400, 641, width=100, height=52, window=button1)

root.mainloop()
