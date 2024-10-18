# #tkinter庫這是一個用來創建 GUI（圖形用戶界面）應用的標準庫。
# #tkinter為package，tk為暱稱
# import tkinter as tk
# #Tk()是tkinter的一個類，root為TK的實體
# #所有的GUI元件（如按鈕、標籤等）都會被放在這個root主窗口中。
# root=tk.Tk()
# #mainloop()為實體方法，執行後會持續運行
# root.mainloop()

# ---------------------------------------------------------------

# import tkinter as tk
# root = tk.Tk()
# #修改視窗名字
# root.title('這是我的第一個視窗!')
# #設定視窗大小(寬*高)
# root.geometry('800x300')

# #label標籤可以用來顯示文本或圖像。
# #將label的引數值設為字串，放入root(主窗口)內，並指定給message
# message=tk.Label(root,text="Hello~~這是我的第一個視窗!")
# #pack會將message加入到主窗口中並根據控件的大小和順序自動進行排列。
# message.pack()
# root.mainloop()


# ---------------------------------------------------------------
#利用main( )呼叫程式
# import tkinter as tk

# def main():
#     root = tk.Tk()
#     print(type(root))
#     root.title('這是我的第一個視窗!')
#     root.geometry('800x300')
#     message = tk.Label(root,text='Hello! 這是我的第一個視窗!')
#     message.pack()
#     root.mainloop()

# if __name__ == '__main__':
#     main()


# ---------------------------------------------------------------    
import tkinter as tk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('這是我的第一個視窗!')
        self.geometry('800x300')
        message = tk.Label(self,text='Hello! 這是我的第一個視窗!')
        message.pack()



def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()