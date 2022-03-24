'''利用pygame写一个小游戏'''
'''1.主类  2.我方飞机类  2.5 敌方飞机类  3.子弹类   4.爆炸效果类   5.音效类   6.墙壁类'''
from posixpath import splitext
from random import random, randrange
import time
from turtle import left
import pygame
from tkinter import * 

#基类，用来继承精灵Sprite类
class Base(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)

#主游戏窗口类
class MainGame():
    pause=False               #是否暂停
    isMenu=True               #是否菜单界面
    windows=None              #存放初始化主窗口
    myplane=None             #存放我方飞机的初始化
    otherplane=None          #存放敌方飞机的初始化
    otherplaneList=[]        #存放敌方飞机初始化后的对象
    bulletList=[]            #存放我方子弹
    otherbulletList=[]       #存放敌方子弹
    explodeList=[]           #存放爆炸
    wallList=[]              #存放墙壁
    bullet=None              #存放初始化子弹对象
    menu=None                #存放初始化菜单对象
    mouse=None               #存放初始化鼠标对象
    width=900                #窗口宽度
    height=500               #窗口高度
    otherPlaneConut=6        #敌方飞机数量
    liveCount=3             #我方飞机生命值
      
    
    def __init__(self):
     
      self.fontsize=20              #文字大小
      self.font='kaiti'             #文字字体
      self.fontcolor=(255,0,0)      #文字颜色
      self.mespos=(10,10)           #左上角文字的显示位置
      self.textpos=(600,10)
          
      pygame.display.init()                                            #初始化显示模块   
      clock=pygame.time.Clock()                                              #创建时钟                         
      MainGame.windows= pygame.display.set_mode((MainGame.width,MainGame.height))  #主模块
      pygame.display.set_caption('飞机大战 V0.01')                           #设置主模块窗口标题
      #初始化菜单
      MainGame.menu=Menu()   
      MainGame.myplane=MyPlane(self.width/2,self.height/2+100)            #初始化我方飞机
      OtherPlane.GetOtherPlane(self)                                     #创建敌方飞机
      Wall.GetWall(self)
      #初始化我方子弹
      MainGame.bullet=Bullet(MainGame.myplane)
    
      while True:
          MainGame.windows.fill((0,0,0))       #一直填充窗口背景色
          clock.tick(80)
          self.eventManger()                   #一直调用事件管理器
          if(MainGame.isMenu==False):
            if(MainGame.myplane.isshow):       
                MainGame.myplane.showMyPlane()              #长久显示我方飞机
            self.CreateOtherPlane()                         #长久显示敌方飞机模块
            MainGame.myplane.moveMyPlane()                  #移动我方飞机
            MainGame.myplane.check_myplane_wall_hit()       #检测我方飞机与墙壁碰撞
            self.CreateMyBullet()                           #创建，显示（发射）我方子弹
            self.CreateOtherBullet()                        #创建，显示敌方子弹
            self.CreateExplode()                            #创建爆炸效果
            self.CreateWall()                               #创建爆炸效果
            MainGame.Textbox(self)                          #创建文字
            #判断是否游戏成功/失败而显示不同的
            if(MainGame.menu.end):
              MainGame.menu.LoseGame()
            if(MainGame.menu.success):
              MainGame.menu.WinGame()
          else:    
            MainGame.menu.__init__()
            MainGame.menu.StartMenu()      
            MainGame.menu.ExitMenu()     
          #长久显示主窗口模块   
          pygame.display.update()             
    
    #开始游戏
    def Textbox(self):
          pygame.font.init()     #初始化字体模块    
          self.myfont=pygame.font.SysFont(self.font,self.fontsize)         #主字体
          #渲染，左上角文字内容
          message=self.myfont.render('敌方战机剩余：'+str(MainGame.otherPlaneConut), True, self.fontcolor)
          liveText=self.myfont.render('我方生命剩余：'+str(MainGame.liveCount), True, self.fontcolor)
          MainGame.windows.blit(message,self.mespos)        #把左上角文字插入到窗口指定位置 
          MainGame.windows.blit(liveText,self.textpos)        #把右上角文字插入到窗口指定位置 
        
    #关闭游戏
    def LoseGame():
        pygame.display.quit()
        
    #显示敌方飞机、移动和发射子弹
    def CreateOtherPlane(self):
           for plane in MainGame.otherplaneList:
                if(plane.isshow==True):
                    plane.otherImage=plane.images[plane.OtherFangxiang]
                    MainGame.windows.blit(plane.otherImage,plane.rect) 
                    plane.moveOtherPlane()
                    plane.check_otherplane_wall_hit()
                    #发射子弹
                    otherplanebullet=plane.GetBullet()
                    if(otherplanebullet!=None):
                        MainGame.otherbulletList.append(otherplanebullet)
                else:
                    MainGame.otherplaneList.remove(plane)
                         
    #循环生成我方子弹并进行移动显示
    def CreateMyBullet(self):
        for bullet in MainGame.bulletList:
            #判断是否显示，不显示则把他从列表中删除
            if(bullet.isshow==True):
                bullet.showBullet() 
                bullet.moveBullet()
                bullet.Check_bullet_other_hit()
                bullet.Check_Bullet_Wall_Hit()
                
                music=Music('hit')
                music.shoMusic()
                
            else:
                MainGame.bulletList.remove(bullet)
                
     #循环生成敌方子弹并进行移动显示
    def CreateOtherBullet(self):
        for otherbullet in MainGame.otherbulletList:
            #判断是否显示，不显示则把他从列表中删除
            if(otherbullet.isshow==True):
                otherbullet.showBullet() 
                otherbullet.moveBullet()
                otherbullet.Check_Other_Wall_Hit()
                if(MainGame.myplane):
                    otherbullet.Check_Otherbullet_my_hit()
            else:
                MainGame.otherbulletList.remove(otherbullet)
            
    #循环生成爆炸
    def CreateExplode(self):
        for explode in MainGame.explodeList:
            if(explode.isshow):
                explode.showExplode()
                explode.isshow=False
            else:
                MainGame.explodeList.remove(explode)
                
    #循环生成墙壁
    def CreateWall(self):
       for wall in MainGame.wallList:
           if(wall.isshow):
               wall.showWall()
           else:
               MainGame.wallList.remove(wall)
        
    #事件处理
    def eventManger(self):
        eventlist=pygame.event.get()
        for event in eventlist:
            if (event.type==pygame.QUIT):  # 退出
                exit()   
            elif(event.type==pygame.KEYDOWN): #按下键盘
                    if (event.key==pygame.K_DOWN):  # 向下
                        MainGame.myplane.ifStop=False
                        MainGame.myplane.fangxiang='D'
                    if (event.key==pygame.K_UP):  # 向上
                        MainGame.myplane.ifStop=False
                        MainGame.myplane.fangxiang='U'
                    if (event.key==pygame.K_LEFT):  # 向左
                        MainGame.myplane.ifStop=False
                        MainGame.myplane.fangxiang='L'
                    if (event.key==pygame.K_RIGHT):  # 向右
                        MainGame.myplane.ifStop=False
                        MainGame.myplane.fangxiang='R'
                    #按空格发射子弹
                    if(event.key==pygame.K_SPACE and MainGame.myplane.isshow==True):   
                #存储子弹,并一次性只生成一颗子弹
                        if(len(MainGame.bulletList)<3):
                                bullet=Bullet(MainGame.myplane)
                                MainGame.bulletList.append(bullet)
                    #按Tab复活
                    if(event.key==pygame.K_TAB and MainGame.myplane.isshow==False):
                        MainGame.myplane.isshow=True
                        MainGame.myplane=MyPlane(self.width/2,self.height/2+100)   
                    #shift暂停/继续游戏
                    if(event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT):
                        MainGame.pause= not MainGame.pause
                    #按S重新开始游戏
                    if((event.key==pygame.K_s and MainGame.menu.success) or (event.key==pygame.K_s and MainGame.menu.end)):
                        MainGame.menu.success=False
                        MainGame.menu.end=False
                        MainGame.pause=False
                        MainGame.otherPlaneConut=6
                        MainGame.liveCount=3
                        MainGame.myplane=MyPlane(self.width/2,self.height/2+100)   
                        OtherPlane.GetOtherPlane(self)
                      
                        
                        
                        
             #松开键盘     
            elif(event.type==pygame.KEYUP):   
                if(event.key==pygame.K_LEFT or event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_RIGHT):
                    MainGame.myplane.ifStop=True 
            elif(event.type==pygame.MOUSEBUTTONDOWN):#按下鼠标
                   Mouse(event)
            else:pass

         
#我方飞机类    
class MyPlane():
    def __init__(self,left,top):
        self.name='MyPlane'
        self.fangxiang='U'  #默认方向为上
        self.speed=10       #控制飞机速度
        self.ifStop=True    #判断是否应该停止行动 
        self.isshow=True    #是否显示
        self.images={
            'U':pygame.image.load('FightGame/FightGame/img/up.gif'),
            'D':pygame.image.load('FightGame/FightGame/img/down.gif'),
            'L':pygame.image.load('FightGame/FightGame/img/left.gif'),
            'R':pygame.image.load('FightGame/FightGame/img/right.gif')
        }
        self.image=self.images[self.fangxiang]  #设置默认方向
        self.rect=self.image.get_rect()    #获得当前图片的区域
        #修改图片的区域值
        self.rect.left=left
        self.rect.top=top
        
        #碰到墙壁不能移动的实现方法是：让坐标不变，即碰到墙壁后让坐标返回到碰撞前
        self.oldleft=self.rect.left
        self.oldtop=self.rect.top
        
        music=Music('start')
        music.shoMusic()
    
    #显示我方飞机
    def showMyPlane(self):    
        self.image=self.images[self.fangxiang]  #设置默认方向
        MainGame.windows.blit(self.image,self.rect)
    
    #移动我方飞机    
    def moveMyPlane(self):
        if(MainGame.pause==False):
            time.sleep(0.02)   #延缓一下飞机的速度
            self.oldleft=self.rect.left
            self.oldtop=self.rect.top
            if(self.fangxiang=='U' and self.rect.top>0 and self.ifStop==False):
                self.rect.top=self.rect.top-self.speed
            elif(self.fangxiang=='D' and self.rect.top+self.rect.height<MainGame.height and self.ifStop==False):
                self.rect.top=self.rect.top+self.speed
            elif(self.fangxiang=='L' and self.rect.left>5 and self.ifStop==False) : 
                self.rect.left=self.rect.left-self.speed
            elif(self.fangxiang=='R' and self.rect.left+self.rect.height<MainGame.width and self.ifStop==False): 
                self.rect.left=self.rect.left+self.speed
            else:pass
    
            
    #检测我方飞机和墙壁的碰撞
    def check_myplane_wall_hit(self):
        for wall in MainGame.wallList:
            check=pygame.sprite.collide_rect(wall,self)
            if(check):
               self.rect.left=self.oldleft 
               self.rect.top=self.oldtop
        
#敌方飞机类   
class OtherPlane(Base):
    def __init__(self) :
        self.images={
            'U':pygame.image.load('FightGame/FightGame/img/OtherU.gif'),
            'D':pygame.image.load('FightGame/FightGame/img/OtherD.gif'),
            'L':pygame.image.load('FightGame/FightGame/img/OtherL.gif'),
            'R':pygame.image.load('FightGame/FightGame/img/OtherR.gif')
        }
        self.OtherSpeeds=10;  #敌方飞机移动速度
        self.step=5
        self.name='OtherPlane'
        self.isshow=True
        
        #获得随机飞机方向,并导入我方照片    
        self.OtherFangxiang=self.RandomFangxiang()
        self.otherImage=self.images[self.OtherFangxiang]
        #获得当前矩形区域并赋值left和top
        self.rect=self.otherImage.get_rect()
        self.rect.left=self.RandomLeft()
        self.rect.top=50
        #定义一个变量，把每一次上次的位置给它
        self.oldleft=self.rect.left
        self.oldtop=self.rect.top
    
    #初始化敌方飞机,得到飞机列表
    def GetOtherPlane(self):
        for x in range(0,MainGame.otherPlaneConut):
           MainGame.otherplane=OtherPlane() #初始化敌方飞机
           MainGame.otherplaneList.append(MainGame.otherplane)
    
    #获得随机的飞机朝向方向   
    def RandomFangxiang(self):
        randomCount=randrange(1,5,1)      #从1-4中随机生成数，间隔差距为1
        if(randomCount==1): randomCount='U'
        if(randomCount==2): randomCount='D'
        if(randomCount==3): randomCount='L'
        if(randomCount==4): randomCount='R'
        return randomCount;
    
    #获得随机left定位方向
    def RandomLeft(self):
        return randrange(1,MainGame.width-100,30)+30
    
    #敌方获取子弹返回
    def GetBullet(self):
        randomint=randrange(1,100,1)
        if(randomint<40):
            return OtherBullet(self)
                
    #随机移动敌方飞机
    def moveOtherPlane(self):
       if(MainGame.pause==False):
        #定义一个变量，把每一次上次的位置给它
        self.oldleft=self.rect.left
        self.oldtop=self.rect.top
        if(self.step<0):
            self.OtherFangxiang=self.RandomFangxiang();
            self.step=200
        else:    
            if(self.OtherFangxiang=='U' and self.rect.top>0 ):   
                self.rect.top=self.rect.top-self.OtherSpeeds  
            if(self.OtherFangxiang=='D' and self.rect.top+self.rect.height<MainGame.height ):
                self.rect.top=self.rect.top+self.OtherSpeeds          
            if(self.OtherFangxiang=='L' and self.rect.left>0 ) : 
                self.rect.left=self.rect.left-self.OtherSpeeds
            if(self.OtherFangxiang=='R' and  self.rect.left+ self.rect.height<MainGame.width ): 
                self.rect.left=self.rect.left+self.OtherSpeeds
            self.step=self.step-2    
    
     #检测敌方飞机和墙壁的碰撞
    def check_otherplane_wall_hit(self):
        for wall in MainGame.wallList:
            check=pygame.sprite.collide_rect(wall,self)
            if(check):
               self.rect.left=self.oldleft 
               self.rect.top=self.oldtop
         

#我方子弹类   
class Bullet(Base):
    def __init__(self,plane) :
        self.images={
                'U':pygame.image.load('FightGame/FightGame/img/bulletup.gif'),
                'D':pygame.image.load('FightGame/FightGame/img/bulletdown.gif'),
                'L':pygame.image.load('FightGame/FightGame/img/bulletleft.gif'),
                'R':pygame.image.load('FightGame/FightGame/img/bulletright.gif')
                 }
        self.fangxiang=plane.fangxiang
        self.bulletSpeeds=6
        self.isshow=True
       
        self.image=self.images[self.fangxiang]
        self.rect=self.image.get_rect()
        
        if(self.fangxiang=='U'):
            self.rect.left=plane.rect.left+plane.rect.width/2-self.rect.width/2
            self.rect.top=plane.rect.top-self.rect.height
        if(self.fangxiang=='D'):
            self.rect.left=plane.rect.left+plane.rect.width/2-self.rect.width/2
            self.rect.top=plane.rect.top+plane.rect.height 
        if(self.fangxiang=='L'):
            self.rect.left=plane.rect.left-self.rect.width/2-self.rect.width/2
            self.rect.top=plane.rect.top+plane.rect.width/2-self.rect.width/2
        if(self.fangxiang=='R'):
            self.rect.left=plane.rect.left+plane.rect.width
            self.rect.top=plane.rect.top+plane.rect.width/2-self.rect.width/2         
            
    #显示我方子弹        
    def showBullet(self):
          self.image=self.images[self.fangxiang]
          MainGame.windows.blit(self.image,self.rect)
          
    #移动我方子弹        
    def moveBullet(self):
        if(MainGame.pause==False): #当暂停之后全都不准移动
            if(self.fangxiang=='U'):   
                if(self.rect.top>0):
                    self.rect.top=self.rect.top-self.bulletSpeeds  
                else: 
                    self.isshow=False
            elif(self.fangxiang=='D'):
                if(self.rect.top+self.rect.height<MainGame.height):
                    self.rect.top=self.rect.top+self.bulletSpeeds      
                else: 
                    self.isshow=False
            elif(self.fangxiang=='L'): 
                if(self.rect.left>0):
                    self.rect.left=self.rect.left-self.bulletSpeeds
                else: 
                    self.isshow=False
            elif(self.fangxiang=='R'):
                if(self.rect.left+ self.rect.height<MainGame.width):
                    self.rect.left=self.rect.left+self.bulletSpeeds
                else: 
                    self.isshow=False
            else:pass
            
    #检测我方子弹与敌方飞机的碰撞
    def Check_bullet_other_hit(self):
        for other in MainGame.otherplaneList:
            check=pygame.sprite.collide_rect(other,self)
            if(check):
                other.isshow=False
                self.isshow=False
                MainGame.otherPlaneConut=MainGame.otherPlaneConut-1   #左上角飞机数量减一
                #加载爆炸图片
                explode=Explode(other)
                MainGame.explodeList.append(explode)
                if(MainGame.otherPlaneConut==0):
                    MainGame.menu.WinGame()
    
    #检测我方子弹与墙壁的碰撞
    def Check_Bullet_Wall_Hit(self):
        for wall in MainGame.wallList:
           check=pygame.sprite.collide_rect(wall,self)
           if(check):
               self.isshow=False
               if(wall.live>0):
                wall.live=wall.live-1
               else:
                   wall.isshow=False
                

#敌方子弹类
class OtherBullet(Bullet):
     def __init__(self,plane):
        self.images={
                'U':pygame.image.load('FightGame/FightGame/img/obulletup.gif'),
                'D':pygame.image.load('FightGame/FightGame/img/obulletdown.gif'),
                'L':pygame.image.load('FightGame/FightGame/img/obulletleft.gif'),
                'R':pygame.image.load('FightGame/FightGame/img/obulletright.gif')
                 }
        self.fangxiang=plane.OtherFangxiang
        self.bulletSpeeds=10
        self.isshow=True
        self.image=self.images[self.fangxiang]
        self.rect=self.image.get_rect()
      
        if(self.fangxiang=='U'):
                self.rect.left=plane.rect.left+plane.rect.width/2-self.rect.width/2
                self.rect.top=plane.rect.top-self.rect.height+2+1
        if(self.fangxiang=='D'):
                self.rect.left=plane.rect.left+plane.rect.width/2-self.rect.width/2
                self.rect.top=plane.rect.top+plane.rect.height+5
        if(self.fangxiang=='L'):
                self.rect.left=plane.rect.left-self.rect.width/2-self.rect.width/2
                self.rect.top=plane.rect.top+plane.rect.width/2-self.rect.width/2-2
        if(self.fangxiang=='R'):
                self.rect.left=plane.rect.left+plane.rect.width+9
                self.rect.top=plane.rect.top+plane.rect.width/2-self.rect.width/2 +4
            
     #展示敌方子弹   
     def showBullet(self):
         self.image=self.images[self.fangxiang]
         MainGame.windows.blit(self.image,self.rect)
     #移动敌方子弹    
     def moveBullet(self):
         Bullet.moveBullet(self)
         
    #检测敌方子弹与我方飞机的碰撞
     def Check_Otherbullet_my_hit(self):
            for other in MainGame.otherbulletList:
                check=pygame.sprite.collide_rect(MainGame.myplane,self)
                if(check and MainGame.myplane.isshow):
                    self.isshow=False
                    explode=Explode(MainGame.myplane)
                    MainGame.explodeList.append(explode)
                    MainGame.myplane.isshow=False
                    #爆炸后我方生命减一
                    if(MainGame.liveCount<=3 and MainGame.liveCount>0):
                      MainGame.liveCount=MainGame.liveCount-1
                    if(MainGame.liveCount==0):
                       MainGame.menu.LoseGame()
                    #展示音效
                    music=Music('hit')
                    music.shoMusic()
    
     #检测敌方子弹与墙壁的碰撞
     def Check_Other_Wall_Hit(self):
        for wall in MainGame.wallList:
           check=pygame.sprite.collide_rect(wall,self)
           if(check):
               self.isshow=False
               if(wall.live>0):
                wall.live=wall.live-1
               else:
                   wall.isshow=False
                  
                
#爆炸类   
class Explode():
     def __init__(self,plane) :
            self.isshow=True
            self.image=pygame.image.load('FightGame/FightGame/img/explode.gif')
            self.rect=plane.rect
    
    #显示爆炸效果
     def showExplode(self):
         self.image=self.image=pygame.image.load('FightGame/FightGame/img/explode.gif')
         MainGame.windows.blit(self.image,self.rect)
     
#音效类   
class Music():
     def __init__(self,event) :
            #初始化混音对象
            pygame.mixer.init()
            if(event=='start'):
              pygame.mixer.music.load('FightGame/FightGame/img/start.wav')
            if(event=='hit'):
              pygame.mixer.music.load('FightGame/FightGame/img/hit.wav')
            if(event=='win'):
              pygame.mixer.music.load('FightGame/FightGame/img/win.wav')
            if(event=='lose'):
              pygame.mixer.music.load('FightGame/FightGame/img/lose.wav')
    
    #播放音乐
     def shoMusic(self):
         pygame.mixer.music.play()
         
#墙壁类   
class Wall():
     def __init__(self,left,top) :
        self.isshow=True
        self.live=100  #墙壁生命值
        self.image=pygame.image.load('FightGame/FightGame/img/wall.gif')
        self.rect=self.image.get_rect()
        self.rect.top=top
        self.rect.left=left
    
     #展示墙壁 
     def showWall(self):
         MainGame.windows.blit(self.image,self.rect)
         
     #随机获取墙壁对象数值并给列表中     
     def GetWall(self):
         for x in range(0,6):
             wall=Wall(x*100+x*110,MainGame.height/2-50)
             MainGame.wallList.append(wall)
  
     
#菜单类
class Menu():
    #初始化并创建标题
    def __init__(self):
        self.fontsize=25              #文字大小
        self.font='kaiti'             #文字字体
        self.fontcolor=(200,20,20)      #文字颜色
        self.success=False
        self.end=False
        pygame.font.init()     #初始化字体模块    
        self.myfont=pygame.font.SysFont('kaiti',40)         #主字体
        self.menu=self.myfont.render('飞机大战 V0.01', True, self.fontcolor)
        self.menurect=self.menu.get_rect()
        self.menurect.left=280
        self.menurect.top=100
        MainGame.windows.blit(self.menu,self.menurect)
        
        #显示开始
    def StartMenu(self): 
        self.myfont=pygame.font.SysFont(self.font,self.fontsize)         #主字体   
        self.start=self.myfont.render('开始游戏', True, self.fontcolor)
        self.startrect=self.start.get_rect()
        self.startrect.left=370
        self.startrect.top=200
        MainGame.windows.blit(self.start,self.startrect)
    
     #显示退出游戏
    def ExitMenu(self):
        self.myfont=pygame.font.SysFont(self.font,self.fontsize)
        self.exit=self.myfont.render('退出游戏', True, self.fontcolor)
        self.exitrect=self.exit.get_rect()
        self.exitrect.left=370
        self.exitrect.top=300
        MainGame.windows.blit(self.exit,self.exitrect)
    
    #显示游戏失败
    def LoseGame(self):
        self.myfont=pygame.font.SysFont(self.font,60)
        self.lose=self.myfont.render('游戏结束！按S键重新开始游戏', True, self.fontcolor)
        self.loserect=self.exit.get_rect()
        self.loserect.left=50
        self.loserect.top=300
        MainGame.windows.blit(self.lose,self.loserect)
        MainGame.pause=True
        self.end=True
        #添加失败音效
        music=Music('lose')
        music.shoMusic()
        
    #显示游戏成功
    def WinGame(self):
        self.myfont=pygame.font.SysFont(self.font,50)
        self.win=self.myfont.render('你赢啦！按S键重新开始游戏吧！', True, self.fontcolor)
        self.winrect=self.exit.get_rect()
        self.winrect.left=50
        self.winrect.top=100
        MainGame.windows.blit(self.win,self.winrect)
        MainGame.pause=True
        self.success=True
        #添加成功音效
        music=Music('win')
        music.shoMusic()

#鼠标类
class Mouse():
    def __init__(self,event):
        #点击开始游戏
        if(MainGame.menu.startrect.collidepoint(event.pos)):
            MainGame.isMenu=False
        #点击退出游戏
        if(MainGame.menu.exitrect.collidepoint(event.pos)):
            exit()
     
#开始调用
MainGame()
