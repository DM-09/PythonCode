import wx
import time
import keyboard
import pyautogui

# frame basic
app = wx.App()
frame = wx.Frame(None, title="Simple Auto Clicker", pos=(100, 0), size=(500, 300), name="frameName", id=wx.ID_ANY,
                 style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP)
frame.Show(True)

# element
btn = wx.Button(frame, label="시작")
label = wx.StaticText(frame, label="클릭 간격(초)")
sec = wx.TextCtrl(frame, value="0")

# pos
label.SetPosition(wx.Point(195, 40))
btn.SetPosition(wx.Point(180, 120))
sec.SetPosition(wx.Point(155, 80))


# function
def click(s):
    while True:
        if keyboard.is_pressed('`'):
            break
        pyautogui.click()
        time.sleep(s)


def start(event):
    click(int(sec.GetValue()))


# end
app.Bind(wx.EVT_BUTTON, start)
app.MainLoop()


# Author: DM-09
# Created Date: 02/03/2023(KST)
