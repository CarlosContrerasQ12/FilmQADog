#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Sat Nov 14 15:06:22 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class DialogoMapaDosis(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SelectorCalibracion = wx.Button(self, wx.ID_ANY, "Navegar")
        self.CajaTextoCalibracion=wx.TextCtrl(self,value="",style=wx.TE_READONLY)
        self.SelectorImagen = wx.Button(self, wx.ID_ANY, "Navegar")
        self.CajaTextoImagen=wx.TextCtrl(self,value="",style=wx.TE_READONLY)
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, "Background")
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, "Filtrar")
        self.button_2 = wx.Button(self, wx.ID_ANY, "Aceptar")
        self.button_3 = wx.Button(self, wx.ID_ANY, "Cancelar")
        
        self.resultado='cancelar'
        self.rutaImagen=''
        self.rutaCalibracion=''
        self.filtrar=False
        self.corrBackground=False

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.Bind(wx.EVT_BUTTON, self.aceptar, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.cancelar, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.buscarIm, self.SelectorImagen)
        self.Bind(wx.EVT_BUTTON, self.buscarCal, self.SelectorCalibracion)

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(u"Seleccion mapa dosis")
        self.SelectorImagen.SetMinSize((400, 50))
        self.SelectorCalibracion.SetMinSize((400, 50))
        self.SetSize((900, 438))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        grid_sizer_1 = wx.GridSizer(4, 2, 0, 0)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Ruta calibracion", style=wx.ALIGN_CENTER)
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)
        sizerNav=wx.BoxSizer(wx.HORIZONTAL)
        sizerNav.Add(self.CajaTextoCalibracion,  1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 10)
        sizerNav.Add(self.SelectorCalibracion, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 20)
        grid_sizer_1.Add(sizerNav, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Ruta Imagen")
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER, 0)
        sizerNav2=wx.BoxSizer(wx.HORIZONTAL)
        sizerNav2.Add(self.CajaTextoImagen,  1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 10)
        sizerNav2.Add(self.SelectorImagen, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.FIXED_MINSIZE, 20)
        grid_sizer_1.Add(sizerNav2, 1, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Correcciones")
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        sizer_3.Add(self.checkbox_1, 0, 0, 0)
        sizer_3.Add(self.checkbox_2, 0, 0, 0)
        grid_sizer_1.Add(sizer_3, 1, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.button_3, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
    def buscarCal(self,event):
        dial=wx.FileDialog(self,name="Seleccione archivo",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dial.ShowModal()==wx.ID_OK:
            self.rutaCalibracion=dial.GetPath()
            self.CajaTextoCalibracion.SetValue(self.rutaCalibracion)
    def buscarIm(self,event): 
        dial=wx.FileDialog(self,name="Seleccione archivo",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dial.ShowModal()==wx.ID_OK:
            self.rutaImagen=dial.GetPath()
            self.CajaTextoImagen.SetValue(self.rutaImagen)
        
    def aceptar(self,event):
        self.filtrar=self.checkbox_2.GetValue()
        self.corrBackground=self.checkbox_1.GetValue()
        self.resultado='aceptar'
        event.Skip()
        self.Close()
    def cancelar(self,event):
        self.Close()
        event.Skip()

# end of class MyDialog

class MyApp(wx.App):
    def OnInit(self):
        self.dialog = DialogoMapaDosis(None, wx.ID_ANY, "")
        self.SetTopWindow(self.dialog)
        self.dialog.ShowModal()
        self.dialog.Destroy()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
