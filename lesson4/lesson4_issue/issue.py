from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)        
        topFrame = ttk.Frame(self,borderwidth=1,relief='solid')
        
        btn1 = ttk.Button(topFrame,text="按鈕1")
        btn1.pack(side='left',expand=True,fill='x',padx=10)

        btn2 = ttk.Button(topFrame,text="按鈕2")
        btn2.pack(side='left',expand=True,fill='x')

        btn3 = ttk.Button(topFrame,text="按鈕3")
        btn3.pack(side='left',expand=True,fill='x',padx=10)

        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')

        bottomFrame = ttk.Frame(self,width=500,height=300,borderwidth=1,relief='solid')

        leftFrame =ttk.Frame(bottomFrame,width=100,height=300,borderwidth=8,relief='solid')
        leftFrame.pack(padx=10,pady=10,side="left")

        centerFrame =ttk.Frame(bottomFrame,width=100,height=300,borderwidth=6,relief='solid')
        centerFrame.pack(padx=10,pady=10,side="left")

        rightFrame =ttk.Frame(bottomFrame,width=100,height=300,borderwidth=3,relief='solid')
        rightFrame.pack(padx=10,pady=10,side="right")

        bottomFrame.pack(padx=10,pady=10)

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()