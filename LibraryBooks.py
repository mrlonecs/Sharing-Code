import tkinter as tk
from tkinter import ttk, messagebox


BOOKS = [
    [101, "The Pragmatic Programmer", "Andrew Hunt", 1999],
    [205, "Clean Code", "Robert C. Martin", 2008],
    [150, "Introduction to Algorithms", "Cormen et al.", 2009],
    [77,  "Automate the Boring Stuff", "Al Sweigart", 2015],
    [305, "Design Patterns", "Erich Gamma et al.", 1994],
    [88,  "Python Crash Course", "Eric Matthes", 2016],
    [412, "Fluent Python", "Luciano Ramalho", 2015],
    [231, "Code Complete", "Steve McConnell", 2004],
    [119, "SICP", "Abelson & Sussman", 1996],
    [264, "Effective Python", "Brett Slatkin", 2015],
]

#working copy we can sort/filter
current_view = [row[:] for row in BOOKS]

# ---------------- Sorting Algorithms ----------------
def bubble_sort(arr, key_index):
    """Bubble Sort on a 2D list, using key_index as the sort key."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if str(arr[j][key_index]).lower() > str(arr[j + 1][key_index]).lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ---------------- Table Operations ----------------
def populate_table(rows):
    tree.delete(*tree.get_children())
    for r in rows:
        tree.insert("", tk.END, values=r)

def sort_by_year():
    bubble_sort(current_view, 3)  # Year is index 3
    populate_table(current_view)

def sort_by_title():
    bubble_sort(current_view, 1)  # Book Name is index 1
    populate_table(current_view)

def search_by_id():
    pass
    
    ##### add code here that takes the value (ID) in the input box and searches for the data in the array
    #### if it is found the book is shown in the table
    #### if it is not then a message should be displayed to say no match

def reset_table():
    current_view.clear()
    current_view.extend([row[:] for row in BOOKS])
    populate_table(current_view)
    entry_var.set("")

# ---------------- UI setup ----------------
root = tk.Tk()
root.title("Book Browser — Search (ID) • Sort Year • Sort Title")
root.geometry("900x520")

# Top row buttons
top = ttk.Frame(root)
top.pack(fill=tk.X, padx=10, pady=(10, 6))

btn_search = ttk.Button(top, text="Search", command=search_by_id)
btn_sort_year = ttk.Button(top, text="Sort Year", command=sort_by_year)
btn_sort_title = ttk.Button(top, text="Sort Title", command=sort_by_title)

btn_search.pack(side=tk.LEFT, padx=(0, 6))
btn_sort_year.pack(side=tk.LEFT, padx=6)
btn_sort_title.pack(side=tk.LEFT, padx=6)

# Entry row
entry_row = ttk.Frame(root)
entry_row.pack(fill=tk.X, padx=10, pady=(0, 10))
ttk.Label(entry_row, text="Enter Book ID:").pack(side=tk.LEFT)
entry_var = tk.StringVar()
entry = ttk.Entry(entry_row, textvariable=entry_var, width=30)
entry.pack(side=tk.LEFT, padx=8)

# Table
table_frame = ttk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=0)

columns = ("Book ID", "Book Name", "Author", "Year")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)

tree.column("Book ID", width=90, anchor=tk.CENTER)
tree.column("Book Name", width=420, anchor=tk.W)
tree.column("Author", width=220, anchor=tk.W)
tree.column("Year", width=80, anchor=tk.CENTER)

ys = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=ys.set)

tree.grid(row=0, column=0, sticky="nsew")
ys.grid(row=0, column=1, sticky="ns")

table_frame.rowconfigure(0, weight=1)
table_frame.columnconfigure(0, weight=1)

# Bottom reset button
bottom = ttk.Frame(root)
bottom.pack(fill=tk.X, padx=10, pady=10)
ttk.Button(bottom, text="Reset (Show All)", command=reset_table).pack(side=tk.RIGHT)

# Populate initial data
populate_table(current_view)

# Convenience: Enter triggers Search
entry.bind("<Return>", lambda e: search_by_id())

root.mainloop()
