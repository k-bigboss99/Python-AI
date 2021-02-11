"""
Myturn = True             # 輪到玩家出牌
Get_btn["state"] = NORMAL # 摸牌有效

playersCard               # 牌手的牌
playersOutCard            # 出過的牌
m_aCards                  # 牌清單
k                         # 紀錄發牌個數
"""

def canPeng(a, card): #(List a, Card card)
    n = 0
    for i in range(0, len(a)):
        c = a[i]
        if(c.imageID == card.imageID):
            n = n+1
    if(n>=2):
        return True
    print("can not peng", card.imageID)
    return False

def canChi(a, card):
    n = 0
    if (card.m_nType == 4):
        return False
    # 1**
    for i in range(0, len(a)-1):
        c1 = a[i]
        c2 = a[i+1]
        if(c1.m_nNum == card.m_nNum+1 and c1.m_nType == card.m_nType)
            and c2.m_nNum == card.m_nNum+2 and c2.m_nType == card.m_nType):
            return True
    # *1*
    for i in range(0, len(a)-1):
        c1 = a[i]
        c2 = a[i+1]
        if(c1.m_nNum == card.m_nNum-1 and c1.m_nType == card.m_nType
            and c2.m_nNum == card.m_nNum+1 and c2.m_nType == card.m_nType):
            return True
    # **1
    for i in range(0, len(a)-1):
        c1 = a[i]
        c2 = a[i+1]
        if(c1.m_nNum == card.m_nNum-2 and c1.m_nType == card.m_nType
            and c2.m_nNum == card.m_nNum-1 and c2.m_nType == card.m_nType):
            return True
    print("can not chi", card.imageID)
    return False
