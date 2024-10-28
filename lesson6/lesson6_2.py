import datasource

from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo


class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
    #==============style===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
    #============end style===============
        
    #==============top Frame===============
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='空氣品質指標(AQI)(歷史資料)',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
    #==============end topFrame===============

    #==============bottomFrame===============
        bottomFrame = ttk.Frame(self)
    #------Combobox------
        #建立取得站點名稱清單 (sitenames)
        sitenames = datasource.get_sitename()
        #儲存和追蹤使用者的選擇值
        self.selected_site = tk.StringVar()
        #創建下拉選單 
        sitenames_cb = ttk.Combobox(bottomFrame, textvariable=self.selected_site,values=sitenames)
        #設定初始選項
        self.selected_site.set('請選擇站點')
        #利用bind設定點擊後回傳的動作
        sitenames_cb.bind('<<ComboboxSelected>>', self.sitename_selected)
        #顯示下拉選單
        sitenames_cb.pack(side="left",expand=True,anchor="n")
    #------end Combobox------
        
    #--------Treeview--------用於展示帶有標題（欄位名稱）的多行資料
        #設定欄位名稱（列標題）
        columns = ('date', 'county', 'aqi',"pm25",'status',"lat","lon")
        #建立 Treeview
        self.tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')
        #設定欄位寬度
        self.tree.column('date',width=150,anchor="center")
        self.tree.column('county',width=80,anchor="center")
        self.tree.column('aqi',width=50,anchor="center")
        self.tree.column('pm25',width=50,anchor="center")
        self.tree.column('status',width=50,anchor="center")
        self.tree.column('lat',width=100,anchor="center")
        self.tree.column('lon',width=100,anchor="center")
        #定義欄位顯示的標題
        self.tree.heading('date', text='日期')
        self.tree.heading('county', text='縣市')
        self.tree.heading('aqi', text='AQI')
        self.tree.heading('pm25', text='PM25')
        self.tree.heading('status', text='狀態')
        self.tree.heading('lat', text='緯度')
        self.tree.heading('lon', text='經度')
        # #插入資料
        # self.tree.insert("", "end", values=('2024-10-28 09:00','屏東縣',17,6.5,'良好',22.260899,120.651472))
        # #生成範例資料
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
        # #將資料添加到 Treeview
        # for contact in contacts:
        # self.tree.insert('', tk.END, values=contact)
        
        self.tree.pack(side='right')
    #------end Treeview------

        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============
    
    #設定點擊後回傳的動作
    def sitename_selected(self,event):
        selected= self.selected_site.get()
        selected_data = datasource.get_selected_data(selected)
        for record in selected_data:
            self.tree.insert("",'end',values=record)
        

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()