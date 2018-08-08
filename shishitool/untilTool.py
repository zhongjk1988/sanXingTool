# -*- coding: utf-8 -*- 

class Tool ():

    list_0 = [0,3,6,9]
    list_1 = [1,4,7]
    list_2 = [2,5,8]

    def __init__(self):
        pass

    def Get_CheckBoxValue(self,getLabel):
        if getLabel == "0":
            return 0
        if getLabel == "1":
            return 1
        if getLabel == "2":
            return 2
        if getLabel == "3":
            return 3
        if getLabel == "4":
            return 4
        if getLabel == "5":
            return 5
        if getLabel == "6":
            return 6
        if getLabel == "7":
            return 7
        if getLabel == "8":
            return 8
        if getLabel == "9":
            return 9
    def Get_HouErHeWeiBool(self,list,killHouEr):
        if killHouEr in list:
            return False
        else:
            return True

    ####################################################################################
    # kill 2 码 直接杀二码
    def Kill_ErMa_m(self,list,bai,shi,ge):
        erma1 = 0
        if str(bai) in list:
            erma1 = erma1 + 1
        if str(shi) in list:
            erma1 = erma1 + 1
        if str(ge) in list:
            erma1 = erma1 + 1
        return erma1
        
    #kill 2 码 保留头尾
    def Kill_ErMa_NoTou_m(self,list,bai,shi,ge):
        erma1 = 0
        if str(bai) in list and str(shi) in list:
            erma1 = erma1 + 1
        if str(shi) in list and str(ge) in list:
            erma1 = erma1 + 1
        return erma1

        
    #kill 2 码 不包含对子和头尾二码相连
    def Kill_ErMa_NoTouSuan_m(self,list,bai,shi,ge):
        erma1 = 0
        if str(bai) in list and str(shi) in list and bai != shi:
            erma1 = erma1 + 1
        if str(shi) in list and str(ge) in list and shi != ge:
            erma1 = erma1 + 1
        return erma1

    #kill 2 码
    def Kill_ErMa_Bool(self,list,bai,shi,ge,baoLiuTouWei_s,baoLiuTouWei):
        if baoLiuTouWei_s:
            if list:
                for data_list in list:
                    num = self.Kill_ErMa_NoTouSuan_m(data_list,bai,shi,ge)
                    if num >= 1:
                        return False
        elif baoLiuTouWei:
            if list:
                for data_list in list:
                    num = self.Kill_ErMa_NoTou_m(data_list,bai,shi,ge)
                    if num >= 1:
                        return False
        else:
            if list:
                for data_list in list:
                    num = self.Kill_ErMa_m(data_list,bai,shi,ge)
                    if num >= 2:
                        return False
        return True
    #####################################################################################

    def get_012(self,num):
        if num in self.list_0:
            return 0
        if num in self.list_1:
            return 1
        if num in self.list_2:
            return 2

    #kill 012
    def Kill_012_Bool(self,kill_012_Dict, bai, shi, ge):
        bai_012 = self.get_012(bai)
        shi_012 = self.get_012(shi)
        ge_012 = self.get_012(ge)
        data_012 = str(bai_012) + str(shi_012) + str(ge_012)
        if data_012 in kill_012_Dict:
            return False
        else:
            return True
    ######################################################################
    def DaDiPinJie_Bool(self,daDiPinJie_Dict,shi,ge):
        
        if daDiPinJie_Dict:
            for data in daDiPinJie_Dict:
                if data[0] == str(shi) and data[1] == str(ge):
                    return True
            return False
        else:
            return True
    #####################################################################
    def DanMa_Bool(self,danMa_list,liangDan,bai,shi,ge):
        if len(danMa_list) == 0:
            return True
        if liangDan:
            num = 0
            if bai in danMa_list:
                num = num + 1
            if shi in danMa_list:
                num = num + 1
            if ge in danMa_list:
                num = num + 1
            if num >=2:
                return True
            else:
                return False
            pass
        else:
            if bai in danMa_list or shi in danMa_list or ge in danMa_list:
                return True
            else:
                return False