from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)

        style.configure('Main.TButton',font=("Arial",15,"bold"),background="lightblue",foreground="blue")

        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        btn1 = ttk.Button(topFrame,text="按鈕1",style='Main.TButton')
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text="按鈕2",style='Main.TButton')
        btn2.pack(side='left',expand=True,fill='x')
        btn3 = ttk.Button(topFrame,text="按鈕3",style='Main.TButton')
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')

        bottomFrame = ttk.Frame(self,height=300,borderwidth=1,relief='groove')
        bottomFrame.pack(padx=10,pady=10)

        leftFrame =ttk.Frame(bottomFrame,width=100,height=300,borderwidth=2,relief='groove')
        btn1 = ttk.Button(leftFrame,text="按鈕1",style='Main.TButton')
        btn1.pack(expand=True,fill='x',padx=10,pady=5,ipady=50)
        btn2 = ttk.Button(leftFrame,text="按鈕2")
        btn2.pack(expand=True,fill='x',padx=10,pady=5,ipady=25)
        btn3 = ttk.Button(leftFrame,text="按鈕3")
        btn3.pack(expand=True,fill='x',padx=10,pady=5,ipady=25)
        leftFrame.pack(padx=10,pady=10,side="left")

        centerFrame =ttk.Frame(bottomFrame,width=100,height=300,borderwidth=2,relief='groove')
        btn1 = ttk.Button(centerFrame,text="按鈕1",style='Main.TButton')
        btn1.pack(expand=True,fill='x',padx=10,pady=5,ipady=40)
        btn2 = ttk.Button(centerFrame,text="按鈕2")
        btn2.pack(expand=True,fill='x',padx=10,pady=5,ipady=20)
        btn3 = ttk.Button(centerFrame,text="按鈕3",style='Main.TButton')
        btn3.pack(expand=True,fill='x',padx=10,pady=5,ipady=40)
        centerFrame.pack(padx=10,pady=10,side="left")

        rightFrame =ttk.Frame(bottomFrame,width=100,height=300,borderwidth=2,relief='groove')
        btn1 = ttk.Button(rightFrame,text="按鈕1")
        btn1.pack(expand=True,fill='x',padx=10,pady=5,ipady=33)
        btn2 = ttk.Button(rightFrame,text="按鈕2")
        btn2.pack(expand=True,fill='x',padx=10,pady=5,ipady=33)
        btn3 = ttk.Button(rightFrame,text="按鈕3")
        btn3.pack(expand=True,fill='x',padx=10,pady=5,ipady=34)
        rightFrame.pack(padx=10,pady=10,side="right")

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()