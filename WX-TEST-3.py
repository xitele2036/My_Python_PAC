import sys

import wx
import wx.py.images as images

class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar() #1 创建状态栏
        toolbar = self.CreateToolBar()     #2 创建工具栏
        toolbar.AddTool(toolId = wx.NewIdRef(),bitmap = images.getPyBitmap(),label = "New",kind = wx.ITEM_NORMAL) #3 给工具栏增加一个工具
        toolbar.Realize() #4 准备显示工具栏
        menuBar = wx.MenuBar() # 创建菜单栏
    # 创建两个菜单
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
    #6 创建菜单的项目
        copys = menu2.Append(wx.NewIdRef(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewIdRef(), "C&ut", "")
        paste = menu2.Append(wx.NewIdRef(), "Paste", "")
        menu2.AppendSeparator()
        option = menu2.Append(wx.NewIdRef(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit") # 在菜单栏上附上菜单
        self.SetMenuBar(menuBar)  # 在框架上附上菜单栏

        self.Bind(wx.EVT_MENU, self.mas,copys)
        self.Bind(wx.EVT_MENU, self.mass, paste)
        self.Bind(wx.EVT_MENU, self.masss, option)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def mas(self,event):
        dlg = wx.MessageDialog(None, 'Is this the coolest thing ever!',
                               'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            print("OK")
        else:
            print("no")
        dlg.Destroy()

    def mass(self,event):
        dlg = wx.TextEntryDialog(None, "Who is buried in Grant’s tomb?",'A Question', 'Cary Grant')
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            print(response)

    def masss(self,event):
        dlg = wx.SingleChoiceDialog(None,'What version of Python are you using?','Single Choice',
        ['1.5.2', '2.0', '2.1.3', '2.2', '2.3.1'])
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetStringSelection()

    def OnCloseWindow(self, event):
        self.Destroy()
class App(wx.App):

    def __init__(self, redirect=True, filename=None):
        print ("App__init__")
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print ("OnInit")  # 输出到stdout
        self.frame = ToolbarFrame(parent=None, id=-1)  # 创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print("A pretend error message",file=sys.stderr)  # 输出到stderr
        return True


if __name__ == '__main__':
    app = App(False,'logcat.log')
    # frame = ToolbarFrame(parent=None, id=-1)
    # app.Show()
    app.MainLoop()
