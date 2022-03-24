import wx
import sys


class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print ("Frame__init__")
        wx.Frame.__init__(self, parent, id, title)

    def OnExit(self):
        print ("OnExit")

class App(wx.App):

    def __init__(self, redirect=True, filename=None):
        print ("App__init__")
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print ("OnInit")  # 输出到stdout
        self.frame = Frame(parent=None, id=-1, title='Startup')  # 创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print("A pretend error message",file=sys.stderr)  # 输出到stderr
        return True

    def OnExit(self):
        print ("OnExit")


if __name__ == '__main__':
    app = App(True,"output")  # 1 文本重定向从这开始
    print ("before MainLoop")
    app.MainLoop()  # 2 进入主事件循环
    print ("after MainLoop")