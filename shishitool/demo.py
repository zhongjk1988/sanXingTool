# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 970,608 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"胆码十", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        gbSizer2.Add( self.m_staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox15 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox15, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox16 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox16, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox17 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox17, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox18 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox18, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox19 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox19, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox20 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox20, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox21 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox21, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox22 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox22, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox23 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox23, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_checkBox24 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_checkBox24, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.m_textCtrl1, wx.GBPosition( 0, 12 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_CHECKBOX, self.OnChar)
        self.m_textCtrl1.Bind( wx.EVT_TEXT, self.OnText )
	
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnChar( self, event ):
        print("dd")
        cb = event.GetEventObject() 
        print (cb.GetLabel(),' is clicked',cb.GetValue())
        event.Skip()

	
    def OnText( self, event ):
        cb = event.GetEventObject()
        print(self.m_textCtrl1.GetValue())
        #SetValue(value)
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()

#使用wxPython获取系统剪贴板中的数据的教程
