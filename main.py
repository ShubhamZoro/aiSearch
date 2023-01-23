from tkinter import *
import mysql.connector

# main.py
from secret import secrets
import datetime
import calendar
from datetime import date, datetime


 


db_user = secrets.get("DATABASE_USER")
db_password = secrets.get("DATABASE_PASSWORD")

print("Starting.")


mydb = mysql.connector.connect(
    host="localhost", user=db_user, password=db_password, database="mydatabase"
)
mycursor = mydb.cursor()




date= datetime.utcnow() 
seconds =(date.total_seconds())
milliseconds = round(seconds*1000)

print()

mycursor.execute("SELECT * FROM search")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

def get_value():
   e_text=edit.get()
   print(e_text)
   sql = "INSERT INTO search (SEARCHKEY, TIME) VALUES (%s, %s)"
   val = (e_text, milliseconds)
   mycursor.execute(sql, val)

   mydb.commit()

   print(mycursor.rowcount, "record inserted.")


# mycursor.execute("SHOW DATABASES")

# creating table
# searchRecord = """ALTER TABLE search (
# 				   ID INT AUTO_INCREMENT PRIMARY KEY,
#                    SEARCHKEY  VARCHAR(20) NOT NULL,
#                    TIME VARCHAR(50)
#                    )"""

# mycursor.execute(searchRecord)

# for x in mycursor:
#     print(x)



# Python Program to search string in text using Tkinter


#to create a window
window = Tk()

#root window is the parent window
root_window = Frame(window)

#adding label to search box
Label(root_window,text='Text to find:').pack(side=LEFT)

#adding of single line text box
edit = Entry(root_window)

#positioning of text box
edit.pack(side=LEFT, fill=BOTH, expand=1)

#setting focus
edit.focus_set()

#adding of search button
butt = Button(root_window, text='Find')
butt.pack(side=RIGHT)
root_window.pack(side=TOP)

#text box in root window
text = Text(window)

#text input area at index 1 in text window
text.insert('1.0','''Type your text here''')
text.pack(side=BOTTOM)






#function to search string in text
def find():
	
	#remove tag 'found' from index 1 to END
	text.tag_remove('found', '1.0', END)
	
	#returns to widget currently in focus
	s = edit.get()
	if s:
		idx = '1.0'
		while 1:
			#searches for desired string from index 1
			idx = text.search(s, idx, nocase=1,
							stopindex=END)
			if not idx: break
			
			#last index sum of current index and
			#length of text
			lastidx = '%s+%dc' % (idx, len(s))
			
			#overwrite 'Found' at idx
			text.tag_add('found', idx, lastidx)
			idx = lastidx
		
		#mark located string as red
		text.tag_config('found', foreground='red')
	edit.focus_set()
butt.config(command=get_value)

find();




#mainloop function calls the endless loop of the window,
#so the window will wait for any
#user interaction till we close it
window.mainloop()

