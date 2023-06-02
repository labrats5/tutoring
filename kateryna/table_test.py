import tkinter as tk
 
 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        tk.Label(root, text="test", image=tk.PhotoImage(), compound=tk.CENTER,
              width=200, height=166, fg='white', borderwidth=2, relief='ridge',
              font=('Arial', 16,'bold')).grid(row=0, column=0, rowspan=5)
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = tk.Label(root, fg='white', borderwidth=2, relief='ridge',
                                  font=('Arial',16,'bold'), text=lst[i][j],
                                  image=tk.PhotoImage(), compound=tk.CENTER,
                                  width=200, height=30)
                 
                self.e.grid(row=i, column=j+1)
                # self.e.config(text=lst[i][j])
 
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = tk.Tk()
t = Table(root)
root.mainloop()