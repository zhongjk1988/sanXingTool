# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from untilTool import Tool
import wx.xrc
import clipboard

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    #定义工具类
    tool = Tool()
    #定义kill胆码列表
    killBaiWei_list = []
    killShiWei_list = []
    killGeWei_list = []
    #kill后三和尾列表
    kill_HouSanHeWei_list = []
    #kill后二和尾列表
    kill_HouErHeWei_list = []
    #胆码列表
    danMa_list = []
    #kill 二码
    kill_ErMa_Dict = []
    #kill 012
    kill_012_Dict = []
    #大底拼接
    daDiPinJie_Dict = []
    
    #至少两胆
    liangDan = False
    #保留头尾
    baoLiuTouWei = False
    #保留头尾双
    baoLiuTouWei_s = False

    #结果值
    result_list = []
    def __init__(self, parent):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 573,791 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        gb_DanMaBai = wx.GridBagSizer( 0, 0 )
        gb_DanMaBai.SetFlexibleDirection( wx.BOTH )
        gb_DanMaBai.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
        
        gb_DanMaBai.SetMinSize( wx.Size( -1,40 ) ) 
        self.m_DanMaBai = wx.StaticText( self, wx.ID_ANY, u"杀百位", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.m_DanMaBai.Wrap( -1 )
        self.m_DanMaBai.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        gb_DanMaBai.Add( self.m_DanMaBai, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_0, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_2, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_3, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_4, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_5, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_6, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_7, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_8, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_bai_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_9, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer2.Add( gb_DanMaBai, 0, wx.EXPAND, 5 )
        
        gb_DanMaShi = wx.GridBagSizer( 0, 0 )
        gb_DanMaShi.SetFlexibleDirection( wx.BOTH )
        gb_DanMaShi.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        gb_DanMaShi.SetMinSize( wx.Size( -1,40 ) ) 
        self.m_DanMaShi = wx.StaticText( self, wx.ID_ANY, u"杀十位", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.m_DanMaShi.Wrap( -1 )
        self.m_DanMaShi.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        gb_DanMaShi.Add( self.m_DanMaShi, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_0, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_2, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_3, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_4, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_5, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_6, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_7, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_8, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_shi_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_9, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer2.Add( gb_DanMaShi, 0, wx.EXPAND, 5 )
        
        gb_DanMaGe = wx.GridBagSizer( 0, 0 )
        gb_DanMaGe.SetFlexibleDirection( wx.BOTH )
        gb_DanMaGe.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        gb_DanMaGe.SetMinSize( wx.Size( -1,40 ) ) 
        self.m_DanMaGe = wx.StaticText( self, wx.ID_ANY, u"杀个位", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.m_DanMaGe.Wrap( -1 )
        self.m_DanMaGe.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        gb_DanMaGe.Add( self.m_DanMaGe, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_0, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_2, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_3, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_4, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_5, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_6, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_7, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_8, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ge_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_9, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer2.Add( gb_DanMaGe, 0, wx.EXPAND, 5 )
        
        b_line = wx.BoxSizer( wx.VERTICAL )
        
        b_line.SetMinSize( wx.Size( 500,-1 ) ) 
        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
        self.m_staticline2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline2.SetMinSize( wx.Size( -1,10 ) )
        self.m_staticline2.SetMaxSize( wx.Size( 560,-1 ) )
        
        b_line.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer2.Add( b_line, 0, wx.EXPAND, 5 )
        
        gb_HouSanHeWei = wx.GridBagSizer( 0, 0 )
        gb_HouSanHeWei.SetFlexibleDirection( wx.BOTH )
        gb_HouSanHeWei.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        gb_HouSanHeWei.SetMinSize( wx.Size( -1,40 ) ) 
        self.m_HouSanHeWei = wx.StaticText( self, wx.ID_ANY, u"后三杀和尾", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_HouSanHeWei.Wrap( -1 )
        self.m_HouSanHeWei.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        gb_HouSanHeWei.Add( self.m_HouSanHeWei, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_0, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_2, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_3, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_4, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_5, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_6, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_7, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_8, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_9, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer2.Add( gb_HouSanHeWei, 0, wx.EXPAND, 5 )
        
        b_HouErHeiWei = wx.BoxSizer( wx.HORIZONTAL )
        
        b_HouErHeiWei.SetMinSize( wx.Size( 40,-1 ) ) 
        self.m_HouErHeWei = wx.StaticText( self, wx.ID_ANY, u"后二杀和尾", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_HouErHeWei.Wrap( -1 )
        self.m_HouErHeWei.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_HouErHeiWei.Add( self.m_HouErHeWei, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_9, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( b_HouErHeiWei, 0, wx.EXPAND, 5 )
        
        b_line2 = wx.BoxSizer( wx.VERTICAL )
        
        b_line2.SetMinSize( wx.Size( 500,-1 ) ) 
        self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
        self.m_staticline21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline21.SetMinSize( wx.Size( -1,10 ) )
        self.m_staticline21.SetMaxSize( wx.Size( 560,-1 ) )
        
        b_line2.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer2.Add( b_line2, 0, wx.EXPAND, 5 )
        
        b_DanMa = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_DanMa = wx.StaticText( self, wx.ID_ANY, u"胆码", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.m_DanMa.Wrap( -1 )
        self.m_DanMa.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_DanMa.Add( self.m_DanMa, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_9, 0, wx.ALL, 5 )
        
        self.m_ZhiShaoLianMa_checkBox = wx.CheckBox( self, wx.ID_ANY, u"至少两码", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_ZhiShaoLianMa_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( b_DanMa, 0, wx.EXPAND, 5 )
        
        b_line3 = wx.BoxSizer( wx.VERTICAL )
        
        b_line3.SetMinSize( wx.Size( 500,-1 ) ) 
        self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
        self.m_staticline22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline22.SetMinSize( wx.Size( -1,10 ) )
        self.m_staticline22.SetMaxSize( wx.Size( 560,-1 ) )
        
        b_line3.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer2.Add( b_line3, 0, wx.EXPAND, 5 )
        
        b_kill_ErMa1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_BaoLiuTouWei_checkBox = wx.CheckBox( self, wx.ID_ANY, u"保留头尾", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_BaoLiuTouWei_checkBox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        b_kill_ErMa1.Add( self.m_BaoLiuTouWei_checkBox, 0, wx.ALL, 5 )
        
        self.m_BaoLiuTouWeiSuan_checkBox = wx.CheckBox( self, wx.ID_ANY, u"保留头尾双", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_BaoLiuTouWeiSuan_checkBox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        b_kill_ErMa1.Add( self.m_BaoLiuTouWeiSuan_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( b_kill_ErMa1, 0, wx.EXPAND, 5 )
        
        b_kill_ErMa2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_Kill_ErMa = wx.StaticText( self, wx.ID_ANY, u"杀二码", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.m_Kill_ErMa.Wrap( -1 )
        self.m_Kill_ErMa.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_kill_ErMa2.Add( self.m_Kill_ErMa, 0, wx.ALL, 5 )
        
        self.m_Kill_ErMa_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Kill_ErMa_textCtrl.SetMinSize( wx.Size( 400,-1 ) )
        
        b_kill_ErMa2.Add( self.m_Kill_ErMa_textCtrl, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( b_kill_ErMa2, 0, wx.EXPAND, 5 )
        
        b_kill_012 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_Kill_012_Text = wx.StaticText( self, wx.ID_ANY, u"杀012", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.m_Kill_012_Text.Wrap( -1 )
        self.m_Kill_012_Text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_kill_012.Add( self.m_Kill_012_Text, 0, wx.ALL, 5 )
        
        self.m_Kill_012_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Kill_012_textCtrl.SetMinSize( wx.Size( 400,-1 ) )
        
        b_kill_012.Add( self.m_Kill_012_textCtrl, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( b_kill_012, 0, wx.EXPAND, 5 )
        
        b_line4 = wx.BoxSizer( wx.VERTICAL )
        
        b_line4.SetMinSize( wx.Size( 500,-1 ) ) 
        self.m_staticline23 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
        self.m_staticline23.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline23.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticline23.SetMinSize( wx.Size( -1,10 ) )
        self.m_staticline23.SetMaxSize( wx.Size( 560,-1 ) )
        
        b_line4.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer2.Add( b_line4, 0, wx.EXPAND, 5 )
        
        b_DaDiPinJie = wx.BoxSizer( wx.VERTICAL )
        
        self.m_DaDiPinJie_Text = wx.StaticText( self, wx.ID_ANY, u"大底拼接", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.m_DaDiPinJie_Text.Wrap( -1 )
        self.m_DaDiPinJie_Text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_DaDiPinJie.Add( self.m_DaDiPinJie_Text, 0, wx.ALL, 5 )
        self.m_DaDiPinJie_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_DaDiPinJie_textCtrl.SetMinSize( wx.Size( 500,100 ) )
        
        b_DaDiPinJie.Add( self.m_DaDiPinJie_textCtrl, 1, wx.ALL, 5 )
        
        
        bSizer2.Add( b_DaDiPinJie, 0, wx.EXPAND, 5 )
        
        gb_BUTTON = wx.GridBagSizer( 0, 0 )
        gb_BUTTON.SetFlexibleDirection( wx.BOTH )
        gb_BUTTON.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
        
        self.gb_SuoShui_BUTTON = wx.Button( self, wx.ID_ANY, u"缩水", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.gb_SuoShui_BUTTON, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_cp_button = wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.m_cp_button, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_clean_button = wx.Button( self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.m_clean_button, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )
        
        self.m_ZhuShuText10 = wx.StaticText( self, wx.ID_ANY, u"注数:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_ZhuShuText10.Wrap( -1 )
        gb_BUTTON.Add( self.m_ZhuShuText10, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_ZhuShuDatatextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.m_ZhuShuDatatextCtrl, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer2.Add( gb_BUTTON, 0, 0, 5 )
        
        b_Result = wx.BoxSizer( wx.VERTICAL )
        
        self.m_result_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_result_textCtrl.SetMaxLength( 1000 ) 
        self.m_result_textCtrl.SetMinSize( wx.Size( 500,400 ) )
        
        b_Result.Add( self.m_result_textCtrl, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( b_Result, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_bai_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        
        self.m_shi_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        
        self.m_ge_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        
        self.m_HouSanWei_checkBox_0.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_1.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_2.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_3.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_4.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_5.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_6.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_7.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_8.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_9.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        
        self.m_HouErWei_checkBox_0.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_1.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_2.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_3.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_4.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_5.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_6.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_7.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_8.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_9.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        
        self.m_DanMa_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        
        self.m_ZhiShaoLianMa_checkBox.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_BaoLiuTouWei_checkBox.Bind( wx.EVT_CHECKBOX, self.Kill_BaoLiu_OnCheckBox )
        self.m_BaoLiuTouWeiSuan_checkBox.Bind( wx.EVT_CHECKBOX, self.Kill_BaoLiu_OnCheckBox )
        self.gb_SuoShui_BUTTON.Bind( wx.EVT_BUTTON, self.OnButtonClick )
        self.m_cp_button.Bind( wx.EVT_BUTTON, self.OnButtonClick )
        self.m_clean_button.Bind( wx.EVT_BUTTON, self.OnButtonClick )
        #########################################################################################
    def __del__( self ):
        pass
    
    def clearData(self):
        #清空所有数据
        self.killBaiWei_list.clear()
        self.killShiWei_list.clear()
        self.killGeWei_list.clear()
        #清空后三和尾列表
        self.kill_HouSanHeWei_list.clear()
        #清空后二和尾列表
        self.kill_HouErHeWei_list.clear()
        #清空胆码列表
        self.danMa_list.clear()
        #清空kill 二码
        self.kill_ErMa_Dict.clear()
        #清空kill 012
        self.kill_012_Dict.clear()
        #清空大底拼接
        self.daDiPinJie_Dict.clear()
        #清空至少两胆
        self.liangDan = False
        #清空保留头尾
        self.baoLiuTouWei = False
        #清空保留头尾双
        self.baoLiuTouWei_s = False
        #清空结果值
        self.result_list.clear()


    def Get_Result(self):
        #缩水前先清空数据
        for bai in range(0,10):
            #杀百位
            if bai not in self.killBaiWei_list:
                for shi in range(0,10):
                    #杀十位
                    if shi not in self.killShiWei_list:
                        for ge in range(0,10):
                            #杀个位
                            if ge not in self.killGeWei_list:
                                #杀后二和尾
                                killHouEr = (shi + ge) % 10
                                #杀后三和尾
                                killHouSan = (bai + shi + ge) % 10;

                                killHouEr_bool = self.tool.Get_HouErHeWeiBool(self.kill_HouErHeWei_list,killHouEr)
                                killHouSan_bool = self.tool.Get_HouErHeWeiBool(self.kill_HouSanHeWei_list,killHouSan)
                                #杀二码
                                killErMa_bool = self.tool.Kill_ErMa_Bool(self.kill_ErMa_Dict, bai, shi, ge,self.baoLiuTouWei_s,self.baoLiuTouWei)
                                #杀012
                                kill_012_bool = self.tool.Kill_012_Bool(self.kill_012_Dict, bai, shi, ge)
                                #大底拼接
                                daDiPinJie_bool = self.tool.DaDiPinJie_Bool(self.daDiPinJie_Dict,shi,ge)
                                #胆码
                                danMa_bool = self.tool.DanMa_Bool(self.danMa_list,self.liangDan,bai,shi,ge)
                                if killHouEr_bool and killHouSan_bool and killErMa_bool and kill_012_bool and daDiPinJie_bool and danMa_bool:
                                    s = str(bai) + str(shi) + str(ge)
                                    self.result_list.append(s)


    # Virtual event handlers, overide them in your derived class
    def DanMaBai_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.killBaiWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.killBaiWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def DanMaShi_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.killShiWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.killShiWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def DanMaGe_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.killGeWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.killGeWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def Kill_HouSanHeWei_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.kill_HouSanHeWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.kill_HouSanHeWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def Kill_HouErHeWei_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.kill_HouErHeWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.kill_HouErHeWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    
    def DanMa_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"至少两码"):
            if cb.GetValue() == True:
                self.liangDan = True
            else:
                self.liangDan = False
        else:
            if cb.GetValue() == True:
                self.danMa_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
            if cb.GetValue() == False:
                self.danMa_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))

        event.Skip()
    
    def Kill_BaoLiu_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"保留头尾"):
            if cb.GetValue() == True:
                self.baoLiuTouWei = True
            else:
                self.baoLiuTouWei = False
        if(cb.GetLabel() == r"保留头尾双"):
            if cb.GetValue() == True:
                self.baoLiuTouWei_s = True
            else:
                self.baoLiuTouWei_s = False
        event.Skip()
    
    
    def OnButtonClick( self, event ):
        cb = event.GetEventObject() 
        if cb.GetLabel() == r"缩水":
            '''
            print("杀百位:"+str(self.killBaiWei_list)+r"\n")
            print("杀十位:"+str(self.killShiWei_list)+r"\n")
            print("杀个位:"+str(self.killGeWei_list)+r"\n")
            print("杀后三和尾:"+str(self.kill_HouSanHeWei_list)+r"\n")
            print("杀后二和尾:"+str(self.kill_HouErHeWei_list)+r"\n")
            print("胆码:"+str(self.danMa_list)+r"\n")
            print("至少两胆:"+str(self.liangDan)+r"\n")
            print("保留头尾:"+str(self.baoLiuTouWei)+r"\n")
            print("保留头尾双:"+str(self.baoLiuTouWei_s)+r"\n")
            print("杀二码:"+str(self.m_Kill_ErMa_textCtrl.GetValue()))
            print("杀012:"+str(self.m_Kill_012_textCtrl.GetValue()))
            print("大底拼接:"+str(self.m_DaDiPinJie_textCtrl.GetValue()))
            '''
            #缩水前先获取输入的值
            self.kill_ErMa_Dict = str(self.m_Kill_ErMa_textCtrl.GetValue()).split(" ")
            self.kill_012_Dict = str(self.m_Kill_012_textCtrl.GetValue()).split(" ")
            #获取大底的数据并赋值给列表，去除换行符
            num = 0
            add_data = ""
            for data in str(self.m_DaDiPinJie_textCtrl.GetValue()):
                if data.isdigit():
                    num = num +1
                    add_data = add_data + data
                    #
                    if num == 2:
                        num = 0
                        self.daDiPinJie_Dict.append(add_data)
                        add_data = ""
            #####################################################################
           
            #缩水前先清空结果
            self.result_list.clear()
            self.Get_Result()
            self.m_result_textCtrl.SetValue(str(self.result_list).replace(r'[',"").replace(r']',"").replace("'",""))
            self.m_ZhuShuDatatextCtrl.SetValue(str(len(self.result_list)))
            
        if cb.GetLabel() == r"清空":
            #清空杀百位
            self.m_bai_checkBox_0.SetValue(False)
            self.m_bai_checkBox_1.SetValue(False)
            self.m_bai_checkBox_2.SetValue(False)
            self.m_bai_checkBox_3.SetValue(False)
            self.m_bai_checkBox_4.SetValue(False)
            self.m_bai_checkBox_5.SetValue(False)
            self.m_bai_checkBox_6.SetValue(False)
            self.m_bai_checkBox_7.SetValue(False)
            self.m_bai_checkBox_8.SetValue(False)
            self.m_bai_checkBox_9.SetValue(False)
            #清空杀十位
            self.m_shi_checkBox_0.SetValue(False)
            self.m_shi_checkBox_1.SetValue(False)
            self.m_shi_checkBox_2.SetValue(False)
            self.m_shi_checkBox_3.SetValue(False)
            self.m_shi_checkBox_4.SetValue(False)
            self.m_shi_checkBox_5.SetValue(False)
            self.m_shi_checkBox_6.SetValue(False)
            self.m_shi_checkBox_7.SetValue(False)
            self.m_shi_checkBox_8.SetValue(False)
            self.m_shi_checkBox_9.SetValue(False)
            #清空杀个位
            self.m_ge_checkBox_0.SetValue(False)
            self.m_ge_checkBox_1.SetValue(False)
            self.m_ge_checkBox_2.SetValue(False)
            self.m_ge_checkBox_3.SetValue(False)
            self.m_ge_checkBox_4.SetValue(False)
            self.m_ge_checkBox_5.SetValue(False)
            self.m_ge_checkBox_6.SetValue(False)
            self.m_ge_checkBox_7.SetValue(False)
            self.m_ge_checkBox_8.SetValue(False)
            self.m_ge_checkBox_9.SetValue(False)
            #清空胆码
            self.m_DanMa_checkBox_0.SetValue(False)
            self.m_DanMa_checkBox_1.SetValue(False)
            self.m_DanMa_checkBox_2.SetValue(False)
            self.m_DanMa_checkBox_3.SetValue(False)
            self.m_DanMa_checkBox_4.SetValue(False)
            self.m_DanMa_checkBox_5.SetValue(False)
            self.m_DanMa_checkBox_6.SetValue(False)
            self.m_DanMa_checkBox_7.SetValue(False)
            self.m_DanMa_checkBox_8.SetValue(False)
            self.m_DanMa_checkBox_9.SetValue(False)
            #清空后三和尾
            self.m_HouSanWei_checkBox_0.SetValue(False)
            self.m_HouSanWei_checkBox_1.SetValue(False)
            self.m_HouSanWei_checkBox_2.SetValue(False)
            self.m_HouSanWei_checkBox_3.SetValue(False)
            self.m_HouSanWei_checkBox_4.SetValue(False)
            self.m_HouSanWei_checkBox_5.SetValue(False)
            self.m_HouSanWei_checkBox_6.SetValue(False)
            self.m_HouSanWei_checkBox_7.SetValue(False)
            self.m_HouSanWei_checkBox_8.SetValue(False)
            self.m_HouSanWei_checkBox_9.SetValue(False)
            #清空后二和尾
            self.m_HouErWei_checkBox_0.SetValue(False)
            self.m_HouErWei_checkBox_1.SetValue(False)
            self.m_HouErWei_checkBox_2.SetValue(False)
            self.m_HouErWei_checkBox_3.SetValue(False)
            self.m_HouErWei_checkBox_4.SetValue(False)
            self.m_HouErWei_checkBox_5.SetValue(False)
            self.m_HouErWei_checkBox_6.SetValue(False)
            self.m_HouErWei_checkBox_7.SetValue(False)
            self.m_HouErWei_checkBox_8.SetValue(False)
            self.m_HouErWei_checkBox_9.SetValue(False)
            #清空至少两码
            self.m_ZhiShaoLianMa_checkBox.SetValue(False)
            #清空保留头尾
            self.m_BaoLiuTouWei_checkBox.SetValue(False)
            #清空保留头尾双
            self.m_BaoLiuTouWeiSuan_checkBox.SetValue(False)
            #清空杀二码
            self.m_Kill_ErMa_textCtrl.Clear()
            #清空012
            self.m_Kill_012_textCtrl.Clear()
            #清空大底拼接
            self.m_DaDiPinJie_textCtrl.Clear()
            #清空结果
            self.m_result_textCtrl.Clear()
            #清空注数
            self.m_ZhuShuDatatextCtrl.Clear()
            #清空数据
            self.clearData()
        if cb.GetLabel() == r"复制":
            clipboard.copy(str(self.result_list).replace(r'[',"").replace(r']',"").replace("'",""))
        event.Skip()
   

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()

#使用wxPython获取系统剪贴板中的数据的教程
'''
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
'''