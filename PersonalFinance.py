import json
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog


# Global dictionary to store transactions
transactions = {}


# File handling transactions 
def load_transactions():
    global transactions # Use global keyword to access the global variable transactions
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file) # Load transactions from file
    except FileNotFoundError:
                print("No transaction data found") # Display error that no transaction data was found
    except json.decoder.JSONDecodeError: # Display message if a JSON code indicate an error
        print("Json decode error") 
        transactions = {}  # Initialize an empty dictionary 

# Function to save transactions  
def save_transactions(transactions):
    with open ("transactions.json", "w") as file:
        json.dump(transactions, file) # Writing the transactions to the file in JSON format

# Function to read bulk transactions from the file 
def read_bulk_transactions_from_file(filename):
    with open(filename, "r") as file:
        for line in file:
            entry = json.loads(line)
            category = entry["category"]# Checks if category exists in transactions dictionary
            if category not in transactions:
                transactions[category] = [] # If category does not exist, initialize an empty list for it
                transactions[category].append({"amount": entry["amount"], "date": entry["date"]}) # Append a new dictionary containing the amount and date to the list

# Function to add a new transaction 
def add_transaction(transactions):
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: ")) 
    except ValueError: # If user eneters invalid inputs other than the numeric value dipaly the message 
        print("Ïnvalid Input amount. Enter a valid input ")
        return
    date = input("Enter date YYYY-MM-DD : ")
     # Creating a dictionary
    transaction = {
        "amount": amount,
        "date": date
    }
    if category not in transactions:
        transactions[category] = []
    transactions[category].append(transaction)# Appending the new transaction to the list in transactions dictionary
    save_transactions(transactions) # calling the save function to save the details 
    print("Transaction added successfully")

# Function to view transactions 
def view_transactions(transactions):
    if not transactions:   # Checking if there are no transactions
        print("No transactions to display")
        return
    for category, transactions_list in transactions.items():
        print(f"Category: {category}")
        for transaction in transactions_list:  # Iterate over each transaction in the category
            amount = transaction['amount']  
            date = transaction['date']  
            print(f" Amount: {amount} , Date:{date}")     
        

# Updating function of transactions 
def update_transaction():
    if not transactions: # Checking if there are no transactions
        print("No transactions to update")
        return
    print("Current transaction records")
    view_transactions(transactions)
    category=input("Enter the category to update: ")
    if category in transactions:    # Checking if category already exists
        transactions_list = transactions[category]
        index = int(input("Enter the index of the transactions to update: "))
        if 0<= index <len(transactions_list):# Checking if the index is valid
            try:
                amount=float(input("Enter new amount: "))
                date=input("Enter new date YYYY-MM-DD: ")
            except ValueError: # If user eneters invalid inputs other than the numeric value dipaly the message
                print("Ïnvalid Input amount. Enter a valid input ")
                return
            # Update amount and date of the transaction
            transactions_list[index]["amount"] = amount
            transactions_list[index]["date"] = date
            print("Transaction upated successfully")
            save_transactions(transactions) # calling the save function to sace details 
        else:
            print("Invalid index")
    else:
        print("Invalid category")
            
      
   
# Deleting function of transactions 
def delete_transaction():
    if not transactions:
        print("There are no transactions to delete") # Printing a message that there are no transactions to delete
        return
    print("Current transaction records")
    view_transactions(transactions) # Display the current transaction records
    category = input("Enter the category to delete the transaction: ")
    if category in transactions:
        transactions_list = transactions[category]
        index = int(input("Enter the index of the transaction to delete: "))
        if 0<= index <len(transactions_list):
            del transactions_list[index]
            save_transactions(transactions)# Delete the transaction from the transactions list
            print("Transaction deleted successfuly")
            
        else:
            print("Inavlid transaction index please enter a valid index")
        
    
  
# Displaying summary functions 
def display_summary():
     total_expenses = {}# Initialize an empty dictionary to store total expenses for each category
     for category, transactions_list in transactions.items():  # Iterate over each category and transactions
        total_expense = sum(transaction['amount'] for transaction in transactions_list)
        total_expenses[category] = total_expense
        print(f"{category}: Total Expense = {total_expense}")# Print the category and total expense
        
# Function for main menu
def main_menu():
    load_transactions()
    while True:
        print("\nPersonal Finance Tracker")
        print ("1. CLI interface")
        print ("2. GUI interface")
        select = input("Enter your selection: ")
        
        if select == '1':
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Update Transaction")
            print("4. Delete Transaction")
            print("5. Load Bulk Trasactiond From File")
            print("6. Display Summary")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                add_transaction(transactions)
            elif choice == '2':
                view_transactions(transactions)
            elif choice == '3':
                update_transaction()
            elif choice == '4':
                delete_transaction()
            elif choice == '5':
                read_bulk_transactions_from_file(filename)
            elif choice == '6':
                display_summary()
            elif choice == '7':
                save_transactions() # Calling the save function 
                print("Exiting program")
                print("Thank you")
                break
            else:
                print("Invalid choice. Please try again")
        elif select == '2':
           class FinanceTrackerApp:
                def __init__(self,root):
                    self.root = root
                    self.root.title("Personal Finance Tracker")
                    
                    # Setting white background color
                    self.root.configure(bg="white")
                    
                    # Define blue colors for the theme
                    self.primary_blue = "#1976D2"  # Primary blue
                    self.light_blue = "#BBDEFB"    # Light blue for highlights
                    self.dark_blue = "#0D47A1"     # Dark blue for accents
                    
                    # Configure ttk styles for themed widgets
                    self.style = ttk.Style()
                    self.style.theme_use('clam')  # Use clam theme as base
                    
                    # Configure styles
                    self.style.configure("TFrame", background="white")
                    self.style.configure("TLabel", background="white", foreground=self.dark_blue)
                    self.style.configure("TButton", background=self.primary_blue, foreground="white")
                    self.style.configure("Treeview", background="white", fieldbackground="white", foreground=self.dark_blue)
                    self.style.configure("Treeview.Heading", background=self.primary_blue, foreground="white", font=("Helvetica", 10, "bold"))
                    self.style.map("Treeview", background=[('selected', self.light_blue)], foreground=[('selected', self.dark_blue)])
                    self.style.map("TButton", background=[('active', self.dark_blue)])
                    
                    # Create custom fonts
                    self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
                    self.header_font = font.Font(family="Helvetica", size=14, weight="bold")
                    
                    self.create_widgets()
                    self.transactions = self.load_transactions("transactions.json")
                    self.display_transactions(self.transactions)
                    
                def create_widgets(self):
                    # Main container frame with padding
                    main_frame = ttk.Frame(self.root, padding=(20, 20, 20, 20))
                    main_frame.pack(fill='both', expand=True)
                    
                    # Header with app title
                    title_label = tk.Label(main_frame, text="Personal Finance Tracker", 
                                          font=self.title_font, bg="white", fg=self.primary_blue)
                    title_label.pack(pady=(0, 20))
                    
                    # Header frame for buttons
                    header_frame = ttk.Frame(main_frame)
                    header_frame.pack(fill='x', pady=(0, 15))
                    
                    # Add transaction button
                    add_button = ttk.Button(header_frame, text='Add Transaction', style="TButton")
                    add_button.pack(side="left", padx=(0, 10))
                    
                    # Open file button
                    open_button = ttk.Button(header_frame, text='Open', command=self.open_file)
                    open_button.pack(side="left")
                    
                    # Summary button on right
                    summary_button = ttk.Button(header_frame, text='View Summary')
                    summary_button.pack(side="right")
                    
                    # Search bar and button with border and rounded corners
                    search_frame = ttk.Frame(main_frame)
                    search_frame.pack(fill="x", pady=(0, 15))
                    
                    search_label = ttk.Label(search_frame, text="Search:")
                    search_label.pack(side="left", padx=(0, 10))
                    
                    self.search_var = tk.StringVar()
                    search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=40)
                    search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
                    
                    search_button = ttk.Button(search_frame, text="Search", command=self.search_transactions)
                    search_button.pack(side="left")
                    
                    # Frame for table with border
                    table_frame = ttk.Frame(main_frame, relief="solid", borderwidth=1)
                    table_frame.pack(fill="both", expand=True)
                    
                    # Table header
                    table_header = ttk.Label(table_frame, text="Transactions", 
                                           font=self.header_font, background=self.primary_blue, foreground="white")
                    table_header.pack(fill="x", padx=1, pady=1)

                    # Treeview for displaying transactions
                    columns = ("Category", "Date", "Amount")
                    self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
                    
                    # Configure column widths and anchors
                    self.tree.column("Category", width=200, anchor="w")
                    self.tree.column("Date", width=150, anchor="center")
                    self.tree.column("Amount", width=150, anchor="e")
                    
                    # Configure column headings
                    self.tree.heading("Category", text="Category", anchor="w")
                    self.tree.heading("Date", text="Date", anchor="center")
                    self.tree.heading("Amount", text="Amount", anchor="e")
                    
                    # Add scrollbars
                    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
                    hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
                    self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
                    
                    # Pack everything
                    vsb.pack(side="right", fill="y")
                    hsb.pack(side="bottom", fill="x")
                    self.tree.pack(side="left", fill="both", expand=True)

                    # Add footer with status
                    status_frame = ttk.Frame(main_frame)
                    status_frame.pack(fill="x", pady=(15, 0))
                    
                    status_label = ttk.Label(status_frame, text="Ready", foreground=self.primary_blue)
                    status_label.pack(side="left")
                    
                    # Set up sorting
                    for col in columns:
                        self.tree.heading(col, text=col, command=lambda _col=col: self.sort_by_column(_col, False))

                def open_file(self):
                    # Opening file dialog to select JSON file
                    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
                    if file_path:
                        self.transactions = self.load_transactions(file_path)
                        self.display_transactions(self.transactions)

                def sort_transactions(self, column, reverse=False):
                    #Get current transactions from treeview
                    transactions = []
                    for item in self.tree.get_children():
                        values = self.tree.item(item, "values")
                        transactions.append((values, item))

                    #sort Transaction
                    transactions.sort(key=lambda x: x[0][column], reverse=reverse)

                    #rearrange the items
                    for index, (values, item) in enumerate(transactions):
                        self.tree.move(item, "", index)

                    #Update the heading
                    self.tree.heading(column, command=lambda: self.sort_transactions(column, not reverse))

                def load_transactions(self, filename):
                    try:
                        with open(filename, "r") as file:
                            transactions = json.load(file)
                        return transactions
                    except FileNotFoundError:
                        return {}

                def display_transactions(self, transactions):
                    # Removing existing entries
                    for item in self.tree.get_children():
                        self.tree.delete(item)

                    # Adding transactions to the treeview
                    for category, transaction_list in transactions.items():
                        for transaction in transaction_list:
                            date = transaction.get("date", transaction.get("Date", ""))
                            amount = transaction.get("amount", transaction.get("Amount", 0))
                            # Format amount to display currency symbol
                            formatted_amount = f"${float(amount):.2f}"
                            values = (
                                category,
                                date,
                                formatted_amount
                            )
                            self.tree.insert("", "end", values=values)

                def search_transactions(self): #searching transactions 
                    search_term = self.search_var.get().lower()
                    matches = []

                    # First clear any existing selection
                    self.tree.selection_remove(self.tree.selection())

                    # If search term is empty, return early
                    if not search_term:
                        return

                    for item in self.tree.get_children():
                        values = [str(value).lower() for value in self.tree.item(item, "values")]
                        if any(search_term in value for value in values):
                            matches.append(item)

                    # Select matching items
                    if matches:
                        self.tree.selection_set(matches)
                        # Ensure the first match is visible
                        self.tree.see(matches[0])

                def sort_by_column(self, col, reverse): #sorting 
                    column_index = self.tree["columns"].index(col)
                    
                    # Get data from treeview
                    data = []
                    for item_id in self.tree.get_children():
                        values = self.tree.item(item_id, "values")
                        # Handle numeric sorting for Amount column
                        if col == "Amount":
                            # Remove currency symbol and convert to float
                            value = float(values[column_index].replace('$', ''))
                        else:
                            value = values[column_index]
                        data.append((value, item_id))
                    
                    # Sort data
                    data.sort(reverse=reverse)
                    
                    # Rearrange items in treeview
                    for idx, (_, item_id) in enumerate(data):
                        self.tree.move(item_id, '', idx)
                    
                    # Reverse sort next time
                    self.tree.heading(col, command=lambda: self.sort_by_column(col, not reverse))


           def main():
               root = tk.Tk()
               # Set window size
               root.geometry("700x600")
               # Center window on screen
               root.eval('tk::PlaceWindow . center')
               app = FinanceTrackerApp(root)
               root.mainloop()

           if __name__ == "__main__":
               main() #calling the GUI function 
            
        else:
            print("Invalid choice. Please try again")
            
if __name__ == "__main__":
    main_menu() #calling the main menu function
