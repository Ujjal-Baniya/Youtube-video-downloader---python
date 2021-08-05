import tkinter as tk
import tkinter.messagebox
def download():
    URL = url.get()
    aud = var.get()
    try:
        if aud == 1:
            ls = YouTube(URL).streams.filter(adaptive=True, only_audio=True)
            ans = 'Audio'
            path = ls[len(ls)-1].download()
        elif aud == 2:
            ls = YouTube(URL).streams.filter(adaptive=True)
            ans = 'Video'
            path = ls[0].download()
        msg = "Badhai xa !! "+ ans + " downloaded sucessfully \n location: "+ path
        tk.messagebox.showinfo("YO done", msg)
    except:
        tk.messagebox.showerror("ERROR!!", "Sorry, We got Error!! Please Try with different URL")

root = tk.Tk()
root.geometry("240x180")
root.title("uTHUB")

url = tk.StringVar()
url_label = tk.Label(root, text = 'URL: ', font=('Comic Sans MS',12, 'italic'))
url_entry = tk.Entry(root, textvariable = url, font=('calibre',10,'normal'), bd=4, width=25, fg='green')

var = tk.IntVar()
Audio_only = tk.Label(root, text='Audio Only', font=('Comic Sans MS',12,'italic'))
R1 = tk.Radiobutton(root, text="Yes",value=1, variable=var, font=('Comic Sans MS',10,'bold'))
R2 = tk.Radiobutton(root, text="No", value=2, variable=var, font=('Comic Sans MS',10,'bold'))

url_label.grid(row = 1, column = 1)
url_entry.grid(row = 1, column = 2)
Audio_only.grid(row=2, column = 2)
R1.grid(row = 3, column = 2)
R2.grid(row = 4, column = 2)

B = tk.Button(text = "Download", command = download)
B.grid(row = 6, column = 2)
root.resizable(False, False) 

root.mainloop()