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
label2 = wx.StaticText(frame, label="")
sec = wx.TextCtrl(frame, value="0")

# pos
label.SetPosition(wx.Point(195, 40))
btn.SetPosition(wx.Point(180, 120))
sec.SetPosition(wx.Point(155, 80))
label2.SetPosition(wx.Point(5, 5))


# function

def click(s):
    label2.SetLabel('시작됨')

    while True:
        if keyboard.is_pressed('f2'): break
        pyautogui.click()
        time.sleep(s)

    label2.SetLabel('')

def use():
    value = sec.GetValue()

    if str(value).isdigit():
        click(float(sec.GetValue()))

def start(event): use()

def short_cut(event):
    if event.name == 'f1': use()

# end
keyboard.on_press(short_cut)

app.Bind(wx.EVT_BUTTON, start)
app.MainLoop()


# Author: DM-09
# Created Date: 07/27/2023(KST)
