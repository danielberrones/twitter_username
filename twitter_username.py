
from twitter_scraper import Profile
impor tkinter as tk 

root = tk.Tk()
root.title("Twitter Handle")
root.iconbitmap("twitterlogo.ico")

instructions = tk.Label(root, text = "Enter your desired handle below: ")
instructions.grid(row = 0, column = 1,)

handle = tk.Entry(root)
handle.grid(row = 1, column = 1)

#for handle
def handle_search(username_):
	#comparing if it avaiable
	a = ""
	background = ""
	padding = 50
	try:
		profile = Profile(str(username_))
		a = "Not Avaiable"
		background = "red"
	except:
		a = "Avaiable"
		background = "green"
		padding = 65

	display = tk.Label(root, text = a, bg = background, padx = padding)
	display.grid(row = 4, column = 1)

submit_button = tk.Button(root, text = "Submit", command = lambda: handle_search(handle.get()))
submit_button.grid(row = 2, column = 1)

avaliability = tk.Label(root, text = "Availiablity: ")
avaliability.grid(row = 3, column = 1)

root.mainloop()
