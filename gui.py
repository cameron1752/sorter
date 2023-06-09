import wx

class MyFrame(wx.Frame):
    def make_lines(self):
        panel = wx.Panel(self)
        self.ln = wx.StaticLine(panel, -1, style=wx.LI_VERTICAL)
        self.ln.SetPosition((804, 450))
        self.ln.SetSize((4,50))

    def __init__(self):
        super().__init__(parent=None, title='Sorter', size=(1600,900))
        panel = wx.Panel(self)

        my_sizer = wx.BoxSizer(wx.VERTICAL)        

        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)  

        my_btn = wx.Button(panel, label='Press Me')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)       

        # self.ln = wx.StaticLine(panel, -1, style=wx.LI_VERTICAL)
        # self.ln.SetPosition((800, 450))
        # self.ln.SetSize((4,30))

        # self.make_lines(panel)

        panel.SetSizer(my_sizer) 
        self.Show()
    

    
    
    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()