import random
import turtle
import pygame

pygame.init()

BGMsound = pygame.mixer.Sound("sound/BGM.mp3")
BGMsound.play(-1)

#기본설정
win = turtle.Screen()
win.setup(1200,1000)
win.addshape("pokerbg1.gif")
win.bgpic("pokerbg1.gif")
win.addshape("card_back.gif")
money=ptwomoney=pthreemoney=pfourmoney=ponemoney =50000000000
betmoney=4000000
formerbet =0
costmoney=ponecostmoney=ptwocostmoney=pthreecostmoney=pfourcostmoney =0
minimum =1000000

QT=0
myCard = []
player1card = []
player2card = []
player3card = []
player4card = []
t = turtle.Turtle()
t.shape("card_back.gif")
#사용자 거북이
t1 =turtle.Turtle()
t2 =turtle.Turtle()
t3 =turtle.Turtle()
t4 =turtle.Turtle()
t5 =turtle.Turtle()
t6 =turtle.Turtle()
t7 =turtle.Turtle()
t8 =turtle.Turtle()
t8.ht()
t8.penup()
t1.shape("card_back.gif")
t2.shape("card_back.gif")
t3.shape("card_back.gif")
t4.shape("card_back.gif")
t5.shape("card_back.gif")
t6.shape("card_back.gif")
t7.shape("card_back.gif")


#plyer1거북이
p1t1 =turtle.Turtle()
p1t2 =turtle.Turtle()
p1t3 =turtle.Turtle()
p1t4 =turtle.Turtle()
p1t5 =turtle.Turtle()
p1t6 =turtle.Turtle()
p1t7 =turtle.Turtle()
p1t8 =turtle.Turtle()
p1t1.shape("card_back.gif")
p1t2.shape("card_back.gif")
p1t3.shape("card_back.gif")
p1t4.shape("card_back.gif")
p1t5.shape("card_back.gif")
p1t6.shape("card_back.gif")
p1t7.shape("card_back.gif")
p1t8.ht()
p1t8.penup()
#plyer2거북이
p2t1 =turtle.Turtle()
p2t2 =turtle.Turtle()
p2t3 =turtle.Turtle()
p2t4 =turtle.Turtle()
p2t5 =turtle.Turtle()
p2t6 =turtle.Turtle()
p2t7 =turtle.Turtle()
p2t1.shape("card_back.gif")
p2t2.shape("card_back.gif")
p2t3.shape("card_back.gif")
p2t4.shape("card_back.gif")
p2t5.shape("card_back.gif")
p2t6.shape("card_back.gif")
p2t7.shape("card_back.gif")
p2t8 =turtle.Turtle()
p2t8.ht()
p2t8.penup()
#plyer3거북이
p3t1 =turtle.Turtle()
p3t2 =turtle.Turtle()
p3t3 =turtle.Turtle()
p3t4 =turtle.Turtle()
p3t5 =turtle.Turtle()
p3t6 =turtle.Turtle()
p3t7 =turtle.Turtle()
p3t1.shape("card_back.gif")
p3t2.shape("card_back.gif")
p3t3.shape("card_back.gif")
p3t4.shape("card_back.gif")
p3t5.shape("card_back.gif")
p3t6.shape("card_back.gif")
p3t7.shape("card_back.gif")
p3t8 =turtle.Turtle()
p3t8.ht()
p3t8.penup()
#plyer4거북이
p4t1 =turtle.Turtle()
p4t2 =turtle.Turtle()
p4t3 =turtle.Turtle()
p4t4 =turtle.Turtle()
p4t5 =turtle.Turtle()
p4t6 =turtle.Turtle()
p4t7 =turtle.Turtle()
p4t1.shape("card_back.gif")
p4t2.shape("card_back.gif")
p4t3.shape("card_back.gif")
p4t4.shape("card_back.gif")
p4t5.shape("card_back.gif")
p4t6.shape("card_back.gif")
p4t7.shape("card_back.gif")
p4t8 =turtle.Turtle()
p4t8.ht()
p4t8.penup()
p1t8.speed(10)
p2t8.speed(10)
p3t8.speed(10)
p4t8.speed(10)
p1t8.goto(-350,-100)
p2t8.goto(-350,250)
p3t8.goto(350,250)
p4t8.goto(350,-100)
#고양이 뒷면으로 바꾸는 함수
def draw():
    global money
    global QT
    if money>40000000000:
        money=money-20000000000
        QT=1
        print("구매가완료되었습니다.")
    else:
        print("돈이모자랍니다")


    
def point(letter,number):#점수확인
    number=int(number)
    if letter == "StraigtFlush":
        return 100+ number*0.001
    if letter == "FourCard":
           return 99 + number*0.001
    if letter == "FullHouse":
        return 98+ number*0.001
    if letter == "Flush":
        return 87+number*0.001
    if letter == "Straight":
        return 86+number*0.001
    if letter =="Trips":
        return 85+number*0.001
    if letter =="TwoPair":
        return 84+number*0.001
    if letter =="OnePair":
        return 83+number*0.001
    if letter =="HighCard":
        return 82+number*0.001
def winnerresult(ppoint,p1point,p2point,p3point,p4point):#승자결정
    global money
    global betmoney
    points=[ppoint,p1point,p2point,p3point,p4point]
    winner =max(points)
    if winner==points[0]:
        print("당신이 이겼습니다!.")
        money=money+betmoney
        print("당신의 머니:",change(money))
    if winner==points[1]:
        print("Player1 이 이겼습니다!.")
    if winner==points[2]:
        print("Player2 가 이겼습니다!.")
    if winner==points[3]:
        print("Player3 이겼습니다!.")
    if winner==points[4]:
        print("Player4 가 이겼습니다!.")
        

def turtlereset():#거북이들을 초기상태로 리셋
    resetsound = pygame.mixer.Sound("sound/cardFan1.mp3")
    resetsound.play()
    t1.reset()
    t2.reset()
    t3.reset()
    t4.reset()
    t5.reset()
    t6.reset()
    t7.reset()

    p1t1.reset()
    p1t2.reset()
    p1t3.reset()
    p1t4.reset()
    p1t5.reset()
    p1t6.reset()
    p1t7.reset()

    p2t1.reset()
    p2t2.reset()
    p2t3.reset()
    p2t4.reset()
    p2t5.reset()
    p2t6.reset()
    p2t7.reset()


    p3t1.reset()
    p3t2.reset()
    p3t3.reset()
    p3t4.reset()
    p3t5.reset()
    p3t6.reset()
    p3t7.reset()

    p4t1.reset()
    p4t2.reset()
    p4t3.reset()
    p4t4.reset()
    p4t5.reset()
    p4t6.reset()
    p4t7.reset()

def turtleShape(order, turtle, card):# 카드를 앞면으로 뒤집는 함
    turtle.shape(str(card[order-1]+str(".gif")))

def playerCardMove(order, turtle, card):#플레이어 카드 움직임
    cardMoveSound1 = pygame.mixer.Sound("sound/cardPlace1.mp3")
    cardMoveSound1.play()
    turtle.speed(6)
    turtle.penup()
    turtle.goto(-150+50*order, -350)
    turtle.shape(str(card[order-1]+str(".gif")))

def player1CardMove(order, turtle):#컴퓨터 카드 움직임
    cardMoveSound2 = pygame.mixer.Sound("sound/cardPlace2.mp3")
    cardMoveSound2.play()
    turtle.speed(6)
    turtle.penup()
    turtle.goto(-500+50*order, 0)

def player2CardMove(order, turtle):#컴퓨터 카드 움직임
    cardMoveSound2 = pygame.mixer.Sound("sound/cardPlace2.mp3")
    cardMoveSound2.play()
    turtle.speed(6)
    turtle.penup()
    turtle.goto(-500+50*order, 350)

def player3CardMove(order, turtle):#컴퓨터카드 움직임
    cardMoveSound3 = pygame.mixer.Sound("sound/cardPlace3.mp3")
    cardMoveSound3.play()
    turtle.speed(6)
    turtle.penup()
    turtle.goto(150+50*order, 0)

def player4CardMove(order, turtle):#컴퓨터 카드 움직임
    cardMoveSound2 = pygame.mixer.Sound("sound/cardPlace2.mp3")
    cardMoveSound2.play()
    turtle.speed(6)
    turtle.penup()
    turtle.goto(150+50*order, 350)

for cardShape in range(1,5): #카드 이미지 불러오기
    for cardNum in range(1,14):
        if cardShape == 1:
            cardShape = "Spade"
        elif cardShape == 2:
            cardShape = "Clover"
        elif cardShape == 3:
            cardShape = "Heart"
        elif cardShape == 4:
            cardShape = "Diamond"

        if cardNum == 1:
            cardNum = "Ace"
        elif cardNum == 11:
            cardNum = "Jack"
        elif cardNum == 12:
            cardNum = "Queen"
        elif cardNum == 13:
            cardNum = "King"
        win.addshape(str(cardShape)+str("_")+str(cardNum)+str(".gif"))

def card(): #카드 생성 및 섞기
    cardList = []
    for cardShape in range(1,5):
        for cardNum in range(1,14):
            if cardShape == 1:
                cardShape = "Spade"
            elif cardShape == 2:
                cardShape = "Clover"
            elif cardShape == 3:
                cardShape = "Heart"
            elif cardShape == 4:
                cardShape = "Diamond"

            if cardNum == 1:
                cardNum = "Ace"
            elif cardNum == 11:
                cardNum = "Jack"
            elif cardNum == 12:
                cardNum = "Queen"
            elif cardNum == 13:
                cardNum = "King"
            cardList.append(str(cardShape)+str("_")+str(cardNum))
    random.shuffle(cardList)
    return cardList

def getCard(cardList,playerCard, count): #원하는 장수의 카드 나누어주기
    for i in range(count):
        playerCard.append(cardList.pop())
    return playerCard


    

def change(num): #돈 단위
    str_result = "" 
    str_sign   = "" 
    num_change = num 

    if num_change == 0: 
        str_result = "0"
    elif num_change < 0: 
        str_sign = "-" 
        num_change = abs(num_change)
    if num_change >= 1000000000000: 
        str_result += f"{int(num_change // 1000000000000):,}조"
        num_change = num_change % 1000000000000

    if num_change >= 100000000: 
        str_result += f"{int(num_change // 100000000):,}억"
        num_change = num_change % 100000000
    if num_change >= 10000: 
        str_result += f" {int(num_change // 10000):,}만"
        num_change = num_change % 10000
    if num_change >= 1: 
        str_result += f" {int(num_change):,}"       
    if len(str_result) >= 1:
        return str_sign + str_result + "원"
    else:
        return str_result

def findKey(dict, val): #key값으로 첫 번째 value값 찾기
    for key, value in dict.items():
        if value == val:
            return key

def findKey2(dict, val): #key값으로 두 번째 vlaue값 찾기
    i = 0
    for key, value in dict.items():
        if (value == val) and (i == 1):
            return key
        if value == val:
            i += 1
            pass
        
def highCard(numDic): #highcard 반환 함수
    for cardNum in range(13, 0, -1):
        if cardNum == 1:
            cardNum = "Ace"
        elif cardNum == 11:
            cardNum = "Jack"
        elif cardNum == 12:
            cardNum = "Queen"
        elif cardNum == 13:
            cardNum = "King"

        if numDic[str(cardNum)] == 1:
            return str(cardNum)

def isStraight(numDic):#스트레이트
    valueList = list(numDic.values())
    straight = 0
    for i in valueList:
        if i >= 1:
            straight += 1
        else:
            straight = 0
        
        if straight == 5:
            return 1
    return 0

def reslutStraigt(numDic):
    valueList = list(numDic.values())
    keyList = list(numDic.keys())
    straight = 0
    count = 0
    for i in valueList:
        count += 1
        if i >= 1:
            straight += 1
        else:
            straight = 0

        if straight == 5:
            return str(keyList[count-1])

def letterToNum(letter): #앞에있는 숫자 변환 함수
    if letter == "Ace":
        return 14
    elif letter == "Jack":
        return 11
    elif letter == "Queen":
        return 12
    elif letter == "King":
        return 13
    else:
        return int(letter)
        
def rule(playerCard): #족보 구현
    cardShapeDic = {"Spade":0, "Clover":0, "Heart":0, "Diamond":0}
    cardNumDic = {}
    for i in range(1, 14):
        if i == 1:
            i = "Ace"
        elif i == 11:
            i = "Jack"
        elif i == 12:
            i = "Queen"
        elif i == 13:
            i = "King"
        cardNumDic[str(i)] = 0
    for card in playerCard:
        cardShapeDic[card[:card.index("_")]] += 1
        cardNumDic[card[card.index("_")+1:]] += 1

    if (isStraight(cardNumDic) == 1) and (list(cardShapeDic.values()).count(5) == 1):
        return reslutStraigt(cardNumDic)+findKey(cardShapeDic, 5)+"_StraigtFlush"
    if list(cardNumDic.values()).count(4) == 1:
        return findKey(cardNumDic, 4)+"_FourCard"
    elif (list(cardNumDic.values()).count(2) == 1) and list(cardNumDic.values()).count(3) == 1:
        return findKey(cardNumDic, 3)+" "+findKey(cardNumDic, 2)+"_FullHouse"
    elif list(cardShapeDic.values()).count(5) == 1:
        return findKey(cardShapeDic, 5)+"_Flush"
    elif (isStraight(cardNumDic) == 1):
        return reslutStraigt(cardNumDic)+"_Straight"
    elif list(cardNumDic.values()).count(3) == 1:
        return findKey(cardNumDic, 3)+"_Trips"
    elif list(cardNumDic.values()).count(2) == 2:
        return findKey(cardNumDic, 2)+" "+findKey2(cardNumDic, 2)+"_TwoPair"
    elif list(cardNumDic.values()).count(2) == 1:
        return findKey(cardNumDic, 2)+"_OnePair"
    else:
        return highCard(cardNumDic)+"_HighCard"

def returnNum(result): #숫자 반환
    resultback = result[result.index("_")+1:]
    if resultback == "HighCard":
        return letterToNum(result[:result.index("_")])
    elif resultback == "OnePair":
        return letterToNum(result[:result.index("_")])
    elif resultback == "TwoPair":
        return letterToNum(result[result.index(" ")+1:result.index("_")])
    elif resultback == "Trips":
        return letterToNum(result[:result.index("_")])
    elif resultback == "Straight":
        return letterToNum(result[:result.index("_")])
    elif resultback == "Flush":
        if result[:result.index("_")] == "Clover":
            return 100
        elif result[:result.index("_")] == "Heart":
            return 200
        elif result[:result.index("_")] == "Diamond":
            return 300
        elif result[:result.index("_")] == "Spade":
            return 400
    elif resultback == "FullHouse":
        return letterToNum(result[:result.index(" ")])
    elif resultback == "FourCard":
        return letterToNum(result[:result.index("_")])
    elif resultback == "StraightFlush":
        if result[:result.index("_")] == "Clover":
            return 100
        elif result[:result.index("_")] == "Heart":
            return 200
        elif result[:result.index("_")] == "Diamond":
            return 300
        elif result[:result.index("_")] == "Spade":
            return 400

def returnRule(result): #족보 반환
    return result[result.index("_")+1:]
    


def betting(myCard):#유저 배팅 함수
    global money
    global betmoney
    global formerbet
    global costmoney
    global minimum
    print("================================================================================")
    betmoney=round(betmoney,0)
    money=round(money,0)
    me = rule(myCard)
    t8.goto(-100, -470)
    t8.write(me,font=("",30))
    print("my card:", myCard, me)
    print("1.하프 2.쿼터 3.체크 4.삥 5.다이    배팅 머니:",change(betmoney),  "  보유머니:",change(money))
    choice=int(input("원하시는 배팅을 선택하세요:"))

    if choice == 1:   
        costmoney = formerbet + betmoney/2
        if money - costmoney<0:
            print("배팅 할 머니가 부족합니다 다시 선택해주세요")
            betting(myCard)
        else:
            betmoney = betmoney + costmoney
            money = money - costmoney
            formerbet =costmoney
            costmoney= 0           
    if choice == 2:    
        costmoney = formerbet + betmoney/4
        if money - costmoney<0:
            print("배팅 할 머니가 부족합니다 다시 선택해주세요")
            betting(myCard)   
        else:
            betmoney = betmoney + costmoney
            money = money - costmoney
            formerbet =costmoney
            costmoney= 0
    if choice == 4:
        costmoney = minimum
 
        if money - costmoney<0:
            print("배팅 할 머니가 부족합니다 다시 선택해주세요")
            betting(myCard)
        else:
            betmoney = betmoney + costmoney
            money = money - costmoney
            formerbet =costmoney
            costmoney= 0
    if choice == 3:
        print("턴을 넘깁니다.")
    if choice == 5:
        print("게임을 종료합니다.")
        turtlereset()
        t8.reset()
        p1t8.reset()
        p2t8.reset()
        p3t8.reset()
        p4t8.reset()
        t8.ht()
        t8.penup()
        p1t8.ht()
        p1t8.penup()
        p2t8.ht()
        p2t8.penup()
        p3t8.ht()
        p3t8.penup()
        p4t8.ht()
        p4t8.penup()
        p1t8.speed(10)
        p2t8.speed(10)
        p3t8.speed(10)
        p4t8.speed(10)
        p1t8.goto(-350,-100)
        p2t8.goto(-350,250)
        p3t8.goto(350,250)
        p4t8.goto(350,-100)
        betmoney=4000000       
        t8.clear()
        main()
    elif choice>5 or choice<1:
        print("1~5번중에 선택해주세요.")
        betting(myCard)
    t8.clear()

def computerbetting():#컴퓨터 배팅 함수
    p1t8.clear()
    p2t8.clear()
    p3t8.clear()
    p4t8.clear()
    global ponemoney,ptwomoney,pthreemoney,pfourmoney
    global ponecostmoney,ptwocostmoney,pthreecostmoney,pfourcostmoney
    global minimum
    global formerbet
    global betmoney
    money=costmoney =0
    for i in range(1,5):
        if i == 1:
            money= ponemoney
            costmoney=ponecostmoney
        if i == 2:
            money = ptwomoney
            costmoney=ptwocostmoney
        if i == 3:
            money = pthreemoney
            costmoney=pthreecostmoney
        if i == 4:
            money = pfourmoney
            costmoney=pfourcostmoney
        choice = random.randint(1,4)

        if choice == 1:    
            costmoney = formerbet + betmoney/2
            if money - costmoney<0:
                choice = 2
            else:
                betmoney = betmoney + costmoney
                money = money - costmoney
                formerbet =costmoney
                costmoney= 0
        if choice == 3:    
            costmoney = formerbet + betmoney/4
            if money - costmoney<0:
                choice = 4
            else:
                betmoney = betmoney + costmoney
                money = money - costmoney
                formerbet =costmoney
                costmoney= 0
        if choice == 4:
            costmoney = minimum
            if money - costmoney<0:
                betmoney= betmoney+money
                money=0
            else:
                betmoney = betmoney + costmoney
                money = money - costmoney
                formerbet =costmoney
                costmoney= 0
        if choice == 3:
            betmoney++0
            
        if choice ==1:
            rufwjd ="하프"
        if choice ==2:
            rufwjd ="체크"
        if choice ==3:
            rufwjd ="쿼터"

        if choice ==4:
            rufwjd ="삥"
        if i ==1:
            p1t8.write(rufwjd,font=120)
        if i ==2:
            p2t8.write(rufwjd,font=120)
        if i ==3:
            p3t8.write(rufwjd,font=120)
        if i ==4:
            p4t8.write(rufwjd,font=120)
            



def cardchange(cardList,myCard):#처음4장받고 1장바꿀떄쓰는 함

    i=int(input("바꾸시길원하는카드의 번호를 선택하세요(1~4):"))
    if 0<i or 5>i:
            if i== 1:
                cardList.insert(0,myCard[0])
                del myCard[0]
                t1.goto(0,0)
                a=cardList.pop()
                myCard.insert(0,cardList.pop())
                playerCardMove(1, t1, myCard)
            if i== 2:
                cardList.insert(0,myCard[1])
                del myCard[1]
                t2.goto(0,0)
                a=cardList.pop()
                myCard.insert(1,cardList.pop())
                playerCardMove(2, t2, myCard)
            if i== 3:
                cardList.insert(0,myCard[2])
                del myCard[0]
                t3.goto(0,0)
                a=cardList.pop()
                myCard.insert(2,cardList.pop())
                playerCardMove(3, t3, myCard)
            if i== 4:
                cardList.insert(0,myCard[3])
                del myCard[3]
                t4.goto(0,0)
                a=cardList.pop()
                myCard.insert(3,cardList.pop())
                playerCardMove(4, t4, myCard)
           


    if 0>=i or 5<=i:
        print("1~4번중에 선택해주세요!")
        cardchange(cardList,myCard)



#main 함수 구현
def game(): #게임 진행
    global betmoney
    global formerbet
    global costmoney
    global ponecostmoney
    global ptwocostmoney
    global pthreecostmoney
    global pfourcostmoney
    global minimum
    betmoney=4000000
    formerbet =0
    costmoney=ponecostmoney=ptwocostmoney=pthreecostmoney=pfourcostmoney =0
    turtlereset()
    t2.shape("card_back.gif")
    t3.shape("card_back.gif")
    t4.shape("card_back.gif")
    t5.shape("card_back.gif")
    t6.shape("card_back.gif")
    t7.shape("card_back.gif")
    p1t1.shape("card_back.gif")
    p1t2.shape("card_back.gif")
    p1t3.shape("card_back.gif")
    p1t4.shape("card_back.gif")
    p1t5.shape("card_back.gif")
    p1t6.shape("card_back.gif")
    p1t7.shape("card_back.gif")
    p2t1.shape("card_back.gif")
    p2t2.shape("card_back.gif")
    p2t3.shape("card_back.gif")
    p2t4.shape("card_back.gif")
    p2t5.shape("card_back.gif")
    p2t6.shape("card_back.gif")
    p2t7.shape("card_back.gif")
    p3t1.shape("card_back.gif")
    p3t2.shape("card_back.gif")
    p3t3.shape("card_back.gif")
    p3t4.shape("card_back.gif")
    p3t5.shape("card_back.gif")
    p3t6.shape("card_back.gif")
    p3t7.shape("card_back.gif")
    p4t1.shape("card_back.gif")
    p4t2.shape("card_back.gif")
    p4t3.shape("card_back.gif")
    p4t4.shape("card_back.gif")
    p4t5.shape("card_back.gif")
    p4t6.shape("card_back.gif")
    p4t7.shape("card_back.gif")
    if QT ==1:
        i=random.randint(1,7)
        a=str("cat")+str(i)+str(".gif")
        i=random.randint(1,7)
        b=str("cat")+str(i)+str(".gif")
        i=random.randint(1,7)
        c=str("cat")+str(i)+str(".gif")
        i=random.randint(1,7)
        d=str("cat")+str(i)+str(".gif")
        i=random.randint(1,7)
        e=str("cat")+str(i)+str(".gif")
        win.addshape(a)
        win.addshape(b)
        win.addshape(c)
        win.addshape(d)
        win.addshape(e)
        p4t1.shape(a)
        p4t2.shape(b)
        p4t3.shape(c)
        p4t4.shape(d)
        p4t5.shape(e)
        p4t6.shape(a)
        p4t7.shape(b)
        p3t1.shape(c)
        p3t2.shape(d)
        p3t3.shape(e)
        p3t4.shape(a)
        p3t5.shape(b)
        p3t6.shape(c)
        p3t7.shape(d)
        p2t1.shape(e)
        p2t2.shape(a)
        p2t3.shape(b)
        p2t4.shape(c)
        p2t5.shape(d)
        p2t6.shape(e)
        p2t7.shape(a)
        p1t1.shape(b)
        p1t2.shape(c)
        p1t3.shape(d)
        p1t4.shape(e)
        p1t5.shape(a)
        p1t6.shape(b)
        p1t7.shape(c)
    t8.ht()
    t8.penup()
    p1t8.ht()
    p1t8.penup()
    p2t8.ht()
    p2t8.penup()
    p3t8.ht()
    p3t8.penup()
    p4t8.ht()
    p4t8.penup()
    p1t8.speed(10)
    p2t8.speed(10)
    p3t8.speed(10)
    p4t8.speed(10)
    p1t8.goto(-350,-100)
    p2t8.goto(-350,250)
    p3t8.goto(350,250)
    p4t8.goto(350,-100)
    cardList = card()

    myCard = []
    player1card = []
    player2card = []
    player3card = []
    player4card = []
    
    myCard = getCard(cardList, myCard,4)#카드4번나눠
    player1card = getCard(cardList,player1card,4)
    player2card = getCard(cardList,player2card,4)
    player3card = getCard(cardList,player3card,4)
    player4card = getCard(cardList,player4card,4)
    playerCardMove(1, t1, myCard)
    player1CardMove(1, p1t1)
    player2CardMove(1, p2t1)
    player3CardMove(1, p3t1)
    player4CardMove(1, p4t1)

    playerCardMove(2, t2, myCard)
    player1CardMove(2, p1t2)
    player2CardMove(2, p2t2)
    player3CardMove(2, p3t2)
    player4CardMove(2, p4t2)

    playerCardMove(3, t3, myCard)
    player1CardMove(3, p1t3)
    player2CardMove(3, p2t3)
    player3CardMove(3, p3t3)
    player4CardMove(3, p4t3)
    
    playerCardMove(4, t4, myCard)
    player1CardMove(4, p1t4)
    player2CardMove(4, p2t4)
    player3CardMove(4, p3t4)
    player4CardMove(4, p4t4)
    cardchange(cardList,myCard)#플레이어 카드한장바꾸기
    for i in range(1,5):#컴퓨터 카드 1장바꾸기
        if i == 1:
            AB=random.randint(1,4)
            if AB ==1:
                p1t1.goto(0,0)
                player1CardMove(1, p1t1)
            if AB ==2:
                p1t2.goto(0,0)
                player1CardMove(2, p1t2) 
            if AB ==3:
                p1t3.goto(0,0)
                player1CardMove(3, p1t3)
            if AB ==4:
                p1t3.goto(0,0)
                player1CardMove(4, p1t4)
        if i == 2:
            AB=random.randint(1,4)
            if AB ==1:
                p2t1.goto(0,0)
                player2CardMove(1, p2t1)
            if AB ==2:
                p2t2.goto(0,0)
                player2CardMove(2, p2t2)  
            if AB ==3:
                p2t3.goto(0,0)
                player2CardMove(3, p2t3)
            if AB ==4:
                p2t4.goto(0,0)
                player2CardMove(4, p2t4)
        if i == 3:
            AB=random.randint(1,4)
            if AB ==1:
                p3t1.goto(0,0)
                player3CardMove(1, p3t1)
            if AB ==2:
                p3t2.goto(0,0)
                player3CardMove(2, p3t2)  
            if AB ==3:
                p3t3.goto(0,0)
                player3CardMove(3, p3t3)
            if AB ==4:
                p3t4.goto(0,0)
                player3CardMove(4, p3t4)
        if i == 4:
            AB=random.randint(1,4)
            if AB ==1:
                p4t1.goto(0,0)
                player4CardMove(1, p4t1)
            if AB ==2:
                p4t2.goto(0,0)
                player4CardMove(2, p4t2)  
            if AB ==3:
                p4t3.goto(0,0)
                player4CardMove(3, p4t3)
            if AB ==4:
                p4t4.goto(0,0)
                player4CardMove(4, p4t4)
    turtleShape(3, p1t3, player1card)#여기부터
    turtleShape(4, p1t4, player1card)
    turtleShape(3, p2t3, player2card)
    turtleShape(4, p2t4, player2card)
    turtleShape(3, p3t3, player3card)
    turtleShape(4, p3t4, player3card)
    turtleShape(3, p4t3, player4card)
    turtleShape(4, p4t4, player4card)#여기까지 이제 4장받고 한장받아서 컴퓨터들의 3,4번쨰 카드 공개
    print(myCard)
    betting(myCard)       
    computerbetting()





    myCard = getCard(cardList,myCard,1)#카드한장나눠줌+ 배팅
    player1card = getCard(cardList,player1card,1)
    player2card = getCard(cardList,player2card,1)
    player3card = getCard(cardList,player3card,1)
    player4card = getCard(cardList,player4card,1)
    playerCardMove(5, t5, myCard)
    player1CardMove(5, p1t5)
    turtleShape(5, p1t5, player1card)
    player2CardMove(5, p2t5)
    turtleShape(5, p2t5, player2card)
    player3CardMove(5, p3t5)
    turtleShape(5, p3t5, player3card)
    player4CardMove(5, p4t5)
    turtleShape(5, p4t5, player4card)
    betting(myCard)
    computerbetting()#여기까지

    myCard = getCard(cardList,myCard,1)#또한장나눠줌
    player1card = getCard(cardList,player1card,1)
    player2card = getCard(cardList,player2card,1)
    player3card = getCard(cardList,player3card,1)
    player4card = getCard(cardList,player4card,1)
    playerCardMove(6, t6, myCard)
    player1CardMove(6, p1t6)
    turtleShape(6, p1t6, player1card)
    player2CardMove(6, p2t6)
    turtleShape(6, p2t6, player2card)
    player3CardMove(6, p3t6)
    turtleShape(6, p3t6, player3card)
    player4CardMove(6, p4t6)
    turtleShape(6, p4t6, player4card)
    betting(myCard)
    computerbetting()#여끼까지

    myCard = getCard(cardList,myCard,1)#또또 나눠줌
    player1card = getCard(cardList,player1card,1)
    player2card = getCard(cardList,player2card,1)
    player3card = getCard(cardList,player3card,1)
    player4card = getCard(cardList,player4card,1)
    playerCardMove(7, t7, myCard)
    player1CardMove(7, p1t7)

    player2CardMove(7, p2t7)

    player3CardMove(7, p3t7)

    player4CardMove(7, p4t7)

    betting(myCard)
    computerbetting()#여기까지
    print("\n최종배팅머니:",change(betmoney),"보유머니:",change(money))#결과 출력

    me = rule(myCard)#게산
    number = returnNum(me)
    letter = returnRule(me)
    p1me= rule(player1card)
    p2me= rule(player2card)
    p3me= rule(player3card)
    p4me= rule(player4card)
    p1number=returnNum(p1me)
    p2number=returnNum(p2me)
    p3number=returnNum(p3me)
    p4number=returnNum(p4me)
    p1letter = returnRule(p1me)
    p2letter = returnRule(p2me)
    p3letter = returnRule(p3me)
    p4letter = returnRule(p4me)

    ppoint=point(letter,number)
    p1point=point(p1letter,p1number)
    p2point=point(p2letter,p2number)
    p3point=point(p3letter,p3number)
    p4point=point(p4letter,p4number)#여기까지
    
    turtleShape(1, p1t1, player1card)#카드 전부공개
    turtleShape(2, p1t2, player1card)
    turtleShape(1, p2t1, player2card)
    turtleShape(2, p2t2, player2card)
    turtleShape(1, p3t1, player3card)
    turtleShape(2, p3t2, player3card)
    turtleShape(1, p4t1, player4card)
    turtleShape(2, p4t2, player4card)
    turtleShape(7, p1t7, player1card)
    turtleShape(7, p2t7, player2card)
    turtleShape(7, p3t7, player3card)
    turtleShape(7, p4t7, player4card)
    print("my card:", myCard, me)
    p1 = rule(player1card)
    print("p1 card:", player1card, p1)
    p2 = rule(player2card)
    print("p2 card:", player2card, p2)
    p3 = rule(player3card)
    print("p3 card:", player3card, p3)
    p4 = rule(player4card)
    print("p4 card", player4card, p4)
    winnerresult(ppoint,p1point,p2point,p3point,p4point)#결과산출

A=1 #초기화면
def main():
    global A
    while A == 1 or 3:
        A=int(input("1. 게임시작, 2. 종료, 3.카드뒷면바꾸기(랜덤한 고양이사진,가격200억,400억이상 보유중에만 구매가능): "))

        if A ==1:
            betmoney=4000000
            formerbet =0
            costmoney=ponecostmoney=ptwocostmoney=pthreecostmoney=pfourcostmoney =0
            minimum =1000000
            game()
            p1t8.reset()
            p2t8.reset()
            p3t8.reset()
            p4t8.reset()
            p1t8.shape("card_back.gif")
            p2t8.shape("card_back.gif")
            p3t8.shape("card_back.gif")
            p4t8.shape("card_back.gif")
        elif A == 2:
            quit()
        elif A ==3:
            draw()
        else:
            print("1~3번중 하나를 선택해주세요.")
            A = 1
main()
pygame.quit()
turtle.done()
