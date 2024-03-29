import wx

class Frame(wx.Frame):
    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title='Hello,WxPython'):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)


class APP(wx.App):
    def OnInit(self):
        image = wx.Image('Maine.jpg',wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = APP()
    app.MainLoop()