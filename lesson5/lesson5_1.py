from tkinter import ttk
import tkinter as tk 
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

#自訂class Window並自訂初始化
class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("登入")
        #=================start style=================
        style = ttk.Style(self)
        style.configure("TopFrame.TLabel",font=("Helvetica",20))
        #==================end style==================

        #=================start topframe=================
        topFrame = ttk.Frame(self)
        #若後續ttk.Lable沒有要更改可以直接用pack打包，不需要先指定變數
        ttk.Label(topFrame,text="個人資料輸入: ",style="TopFrame.TLabel").pack()
        topFrame.pack(padx=10,pady=10)
        #==================end topframe==================

        #===============start bottomframe================
        bottomFrame = ttk.Frame(self)

        ttk.Label(bottomFrame,text="UserName: ").grid(column=0,row=0,sticky="E")
        
        #使用者輸入的字串會存在tk.SrtingVar()裡面
        self.username = tk.StringVar() 
        ttk.Entry(bottomFrame,textvariable=self.username).grid(column=1,row=0,padx=(0,5),pady=10)
        ttk.Label(bottomFrame,text="PassWord: ").grid(row=1,column=0,sticky="E")
        
        self.password = tk.StringVar()
        ttk.Entry(bottomFrame,textvariable=self.password,show="*").grid(column=1,row=1,padx=(0,5),pady=10)

        cancel_btn = ttk.Button(bottomFrame,text="取消",command=self.cancel_click)
        cancel_btn.grid(column=0,row=2,padx=10,pady=10)

        ok_btn = ttk.Button(bottomFrame,text="確定",command=self.ok_click)
        ok_btn.grid(column=1,row=2,pady=10)


        bottomFrame.pack(expand=True,fill="x",padx=5,pady=(10))
        #===============end bottomframe================

    #點擊cancel，將輸入字串改為空字串
    def cancel_click(self):
        self.username.set("")
        self.password.set("")

    #點擊ok，將輸入字串存取，並利用showinfo顯示視窗
    def ok_click(self):
        username = self.username.get()
        password = self.password.get()
        showinfo(title="使用者輸入",message=f"使用者名稱:{username}\n使用者密碼:{password}")

def main():
    window = Window(theme="arc")
    # window.username.set("請輸入姓名:")
    # window.password.set("請輸入密碼:")
    window.mainloop()



if __name__ =='__main__':
    main()