# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(300, 300))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        box.Add(self.text, 1, flag=wx.EXPAND | wx.ALL, border=5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        stbox = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        gs = wx.GridSizer(5, 4, 10, 10)

        for i in stbox:
            btn = wx.Button(panel, label=i)
            gs.Add(btn, 0, wx.EXPAND)
            btn.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        clear = wx.Button(panel, label="Clear")
        clear.Bind(wx.EVT_BUTTON, self.OnClearClicked)
        gs.Add(clear, 0, wx.EXPAND)

        vbox.Add(gs, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        box.Add(vbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        panel.SetSizerAndFit(box)
        self.Centre()
        self.Show()
        self.text.SetFocus()

    def OnButtonClicked(self, e):
        label = e.GetEventObject().GetLabel()
        current_input = self.text.GetValue()
        new_input = current_input + label
        if '=' in new_input:
            if new_input.count('=') > 1 or new_input[-1] != '=':
                return
            try:
                compute = new_input.rstrip('=')
                # compute the expression
                result = str(eval(compute))
                self.text.SetValue(result)
            except Exception as ex:
                wx.MessageBox('Invalid input', 'Error', wx.OK | wx.ICON_ERROR)
        else:
            self.text.SetValue(new_input)

    def OnClearClicked(self, e):
        self.text.SetValue("")


app = wx.App()
Mywin(None, "Calculator")
app.MainLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
