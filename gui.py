import dropAlert as alert
import crawling 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Import ttk module for Notebook widget

# Button style
button_style = {'width': 30, 'pady': 7, 'bg': '#57a1f8', 'fg': 'white', 'border': 0, 'font': ('Arial', 12)}

def store():
        uname = username.get()
        flipkart_link = flipkart.get()
        products = product.get()
        wish_price = target.get()
        email = mail.get()
        if(uname=='' or flipkart_link=='' or products=='' or wish_price=='' or email ==''):
            messagebox.showerror('Python Error', 'Error: Fill all with correct info!')
        else:
            pdt_label = Label(frame1, text="Thank you", fg="grey",  font=('Arial', 20, 'bold')).place(x=450, y=435)
            # Format the content using f-strings
            content = f"""USERNAME = '{uname}' \n\nPRODUCT_NAME = '{products}' \n\nFLIPKART_URL = '{flipkart_link}' \n\nWISH_PRICE = {wish_price} \n\nEMAIL_ID = '{email}'
            """

            with open('constant.py', 'w') as file:
                 file.write(content)
            # root.destroy() 
            alert.excute()

def show():
        price = budget.get()

        if(price==''):
            messagebox.showerror('Python Error', 'Error: Fill all with correct info!')
        else:
            content = f"""BUDGET = '{price}'"""

            with open('constant2.py', 'w') as file:
                 file.write(content)
        result=crawling.crawl()
        Label(frame2, text="Best smartphone under your budget", bg="white", font=('Arial', 10, 'bold')).place(x=60, y=180)
        Label(frame2, text=result, bg="white", font=('Arial', 10, 'bold')).place(x=40, y=220)

root = Tk()
root.title('Price Alert')
root.geometry('950x600')
root.configure(bg='#E0E0E0')  # Light gray background
root.resizable(False, False)

# Create a Notebook (Tabbed Widget) for multiple pages
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Page 1
frame1 = Frame(notebook, width=730, height=650, bg='#FFFFFF')  # White background
frame1.place(x=100, y=70)

heading = Label(frame1, text='Price Drop Alert', fg='#DC143C', bg='#FFFFFF', font=('Arial', 23, 'bold'))
heading.place(x=250, y=5)

# Entry field styles
entry_style = {'fg': 'black', 'border': 0, 'font': ('Arial', 11)}
entry_bg_color = '#F0F8FF'  # Light blue

alabel = Label(frame1, text="Name ", bg="white",  font=('Arial', 10, 'bold')).place(x=25, y=80)
username = Entry(frame1, width=69, bg=entry_bg_color, **entry_style)
username.place(x=120, y=80)
Frame(frame1, width=550, height=2, bg='black').place(x=120, y=107)

flabel = Label(frame1, text="Flipkart Link", bg="white",  font=('Arial', 10, 'bold')).place(x=25, y=150)
flipkart = Entry(frame1, width=69, bg=entry_bg_color, **entry_style)
flipkart.place(x=120, y=150)
Frame(frame1, width=550, height=2, bg='black').place(x=120, y=177)

pdt_label = Label(frame1, text="Product", bg="white",  font=('Arial', 10, 'bold')).place(x=25, y=220)
product = Entry(frame1, width=40, bg=entry_bg_color, **entry_style)
product.place(x=120, y=220)
Frame(frame1, width=322, height=2, bg='black').place(x=120, y=245)

tlabel = Label(frame1, text="Wish Price", bg="white",  font=('Arial', 10, 'bold')).place(x=25, y=290)
target = Entry(frame1, width=40, bg='#C1FFC1', **entry_style)  # Light green background
target.place(x=120, y=290)
Frame(frame1, width=320, height=2, bg='black').place(x=120, y=315)

mlabel = Label(frame1, text="E- Mail", bg="white",  font=('Arial', 10, 'bold')).place(x=25, y=360)
mail = Entry(frame1, width=40, bg='#C1FFC1', **entry_style)  # Light green background
mail.place(x=120, y=360)
Frame(frame1, width=320, height=2, bg='black').place(x=120, y=385)

Button(frame1, text='Submit', **button_style, command=store).place(x=150, y=430)

# Page 2
frame2 = Frame(notebook, width=730, height=650, bg='#FFFFFF')  # White background
frame2.place(x=100, y=70)

text_label = Label(frame2, text='Enter your budget to discover best phone under your budget', fg='#DC143C', font=('Arial', 20, 'bold'))
text_label.place(x=50, y=20)

budget_label = Label(frame2, text="Your Budget", bg="white", font=('Arial', 10, 'bold')).place(x=25, y=80)
budget = Entry(frame2, width=69, bg=entry_bg_color, **entry_style)
budget.place(x=120, y=80)
Frame(frame2, width=550, height=2, bg='black').place(x=120, y=107)

Button(frame2, text='Search', **button_style, command=show).place(x=150, y=120)


# output_button.pack()

# Add pages to the Notebook
notebook.add(frame1, text='Price Drop')
notebook.add(frame2, text='Best Smartphone')

root.mainloop()
