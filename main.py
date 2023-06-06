import wx
from typing import Any


class CalculatorFrame(wx.Frame):
    def __init__(self, parent: Any, title: str) -> None:
        super().__init__(parent, title=title, size=(300, 300))
        panel: wx.Panel = wx.Panel(self)
        main_box: wx.BoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.text_field: wx.TextCtrl = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        main_box.Add(self.text_field, 1, flag=wx.EXPAND | wx.ALL, border=5)
        button_box: wx.BoxSizer = wx.BoxSizer(wx.VERTICAL)
        button_labels = [
            "7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0",
            ".", "=", "+"
        ]
        button_grid: wx.GridSizer = wx.GridSizer(5, 4, 10, 10)
        for label in button_labels:
            button: wx.Button = wx.Button(panel, label=label)
            button_grid.Add(button, 0, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.on_button_click)
        clear_button: wx.Button = wx.Button(panel, label="Clear")
        clear_button.Bind(wx.EVT_BUTTON, self.on_clear_click)
        button_grid.Add(clear_button, 0, wx.EXPAND)
        button_box.Add(button_grid, proportion=1, flag=wx.EXPAND | wx.ALL,
                       border=5)
        main_box.Add(button_box, proportion=1, flag=wx.EXPAND | wx.ALL,
                     border=5)
        panel.SetSizerAndFit(main_box)
        self.Centre()
        self.Show()
        self.text_field.SetFocus()

    def on_button_click(self, event: wx.Event) -> None:
        label: str = event.GetEventObject().GetLabel()
        current_input: str = self.text_field.GetValue()
        new_input: str = current_input + label
        if "=" in new_input:
            if new_input.count("=") > 1 or new_input[-1] != "=":
                return
            try:
                expression: str = new_input.rstrip("=")
                result: str = str(eval(expression))
                self.text_field.SetValue(result)
            except Exception as ex:
                wx.MessageBox("Invalid input", "Error", wx.OK | wx.ICON_ERROR)
        else:
            self.text_field.SetValue(new_input)

    def on_clear_click(self, event: wx.Event) -> None:
        self.text_field.SetValue("")


app: wx.App = wx.App()
CalculatorFrame(None, "Calculator")
app.MainLoop()
