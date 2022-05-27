
import random
from tkinter import ttk
import tkinter as tk
from functools import partial


class Enemy: 
    def __init__(self, name, deskripsi, totalhp, damage, speed, Defense, exp_gain, gold_gain, level):
        self.hp = totalhp
        self.maxhp = self.hp
        self.name = name
        self.deskripsi = deskripsi
        self.dam = damage
        self.speed = speed
        self.defense = Defense
        self.expgain = exp_gain
        self.goldgain = gold_gain
        self.level = level


class player:
    def __init__(self, name, totalhp, damage, speed, Defense, gold, exp, level, mana):
        self.hp = totalhp
        self.rhp = self.hp
        self.name = name
        self.dam = damage
        self.speed = speed
        self.defense = Defense
        self.gold = gold
        self.exp = exp
        self.level = level
        self.mana = mana

    #getter stat
    def get_hp(self):
        return self.hp 
    def get_name(self):
        return self.name
    def get_dam(self):
        return self.dam
    def get_speed(self):
        return self.speed
    def get_defense(self):
        return self.defense 
    def get_gold(self):
        return self.gold
    def get_exp(self):
        return self.exp 
    def get_level(self):
        return self.level
    
    #setter stat
    def set_hp(self,hp):
        self.hp = hp
    def set_name(self,name):
        self.name = name
    def set_dam(self,dam):
        self.dam = dam
    def set_speed(self,speed):
        self.speed = speed           
    def set_defense(self,defense):
        self.defense = defense
    def set_gold(self,gold):
        self.gold = gold
    def set_exp(self,exp):
        self.exp = exp
    def set_level(self,level):
        self.level = level

class skill:
    def __init__(self, manacost ,sname ,description):
        self.sname = sname
        self.description = description
        self.manacost = manacost
        self.window = None
    
    def info(self):
        self.window = tk.Tk()
        self.window.title(self.sname)
        ttk.Label(self.window, text=self.sname).pack()
        ttk.Label(self.window, text='Mana Cost: ' + str(self.manacost)).pack()
        ttk.Label(self.window, text=self.description).pack()
        ttk.Button(self.window, text="Exit", command=self.exit).pack()

    def exit(self):
        self.window.destroy()

               

class Weapon:
    def __init__(self, name, damage, description):
        self.name = name
        self.dam = damage
        self.desc = description
        self.window = None
    def info(self):
        """membuat window baru info senjata"""
        self.window = tk.Tk()
        self.window.title(self.name)
        ttk.Label(self.window, text=self.name).pack()
        ttk.Label(self.window, text="Damage: " + str(self.dam)).pack()
        ttk.Label(self.window, text=self.desc).pack()
        ttk.Button(self.window, text="Exit", command=self.exit).pack()
    def exit(self):
        self.window.destroy()
    

class Armor:
    def __init__(self, name, defense, description):
        self.name = name
        self.defense = defense
        self.desc = description
        self.window = None
    def info(self):
        """membuat info armor pada window baru"""
        self.window = tk.Tk()
        self.window.title(self.name)
        ttk.Label(self.window, text=self.name).pack()
        ttk.Label(self.window, text="Armor Value: " + str(self.defense)).pack()
        ttk.Label(self.window, text=self.desc).pack()
        ttk.Button(self.window, text="Exit", command=self.exit).pack()
    def exit(self):
        self.window.destroy()

class game:
    def __init__(self,name):
        self.window = tk.Tk()
        self.healWindow = None
        self.menuWindow = None
        self.eHealthBar = None
        self.window.title('RPG')
        self.window.geometry('600x560+150+150')
        exitButton = ttk.Button(self.window, text="Close Game", command=self.window.destroy)
        exitButton.place(x=500, y=20, width=75, height=50)
        self.current = ttk.Label(self.window, text="")
        self.current.place(x=0, y=0)
        self.statusConsole = ttk.Label(self.window, text="")
        self.statusConsole.place(x=245, y=300)
        self.statusConsole.config(font=("Courier", 8)) 
        self.sidebar = ttk.Labelframe(self.window, width=375, height=300, text='Sidebar') #items and stats and stuff
        self.sidebar.place(x=0, y=310)
        self.info = ttk.Notebook(self.sidebar)
        self.info.grid(row=0, column=0)
        #--------------------------player stats---------------------------------------------
        self.winv = []
        self.ainv = []
        self.skill = []
        self.stat = player(name, 20, 6, 5, 4, 150, 0, 1, 10)        
        self.rhealth = self.stat.hp #sisa Hp
        self.rmana = self.stat.mana
        self.expCap = 1
        self.weapon = Weapon("Wood Sword", 1, "A simple wooden sword")#Senjata
        self.stat.set_dam(self.stat.dam + self.weapon.dam)
        self.armor = Armor("Wood armor", 2 , "A simple wood armor")#Armor
        self.stat.set_defense(self.stat.defense + self.armor.defense)

        #----------------------------------------ENEMIES-------------------------------------
        #name, deskripsi, totalhp, damage, speed, Defense, exp_gain, gold_gain, level 
        self.goblin = Enemy("Goblin","your normal fantasy goblin", 5, 7, 5, 4, 20, 50, 1)
        self.spider = Enemy("Spider","small spider", 4, 8, 9, 2, 25, 60, 2)
        self.hobgoblin = Enemy("Hob Goblin","slightly bigger than goblin", 10, 12, 6, 6, 55, 90, 3)
        self.wolf = Enemy("Wolf","A Mighty beast with sharp claw", 6, 14, 10, 4, 50, 95, 3)
        self.alphawolf = Enemy("Alpha Wolf","The leader of the wolfs", 10, 16, 12, 5, 100, 100, 5)
        self.lesserdemon = Enemy("Lesser Demon","The lowest rank of demon race", 20, 17, 10, 8, 300, 300, 7)
        self.greaterdemon = Enemy("Greater Demon","More powerful than lesser demon", 25, 20, 12, 10, 500, 500, 9)
        self.Demonking = Enemy("Demon king", "the king of demon race",100,30,15,17,2000,4000,10)

        self.enemies = [self.goblin,self.spider,self.hobgoblin,self.wolf,self.alphawolf,self.lesserdemon,self.greaterdemon]
        #------NOTEBOOK TABS-----------------------------------------------------------------
        self.stats = ttk.Frame(self.info)
        self.wep = ttk.Frame(self.info) #weapons
        self.am = ttk.Frame(self.info) #armor
        self.sk = ttk.Frame(self.info)
        self.info.add(self.stats, text='Stats')
        self.info.add(self.wep, text='Weapons')
        self.info.add(self.am, text='Armor')
        self.info.add(self.sk, text='skill')
        #--------NOTEBOOK LABELS-----------------------------------------------------------------
        self.nameLabel = ttk.Label(self.stats, text='name : ' + str(self.stat.name))
        self.nameLabel.grid(row=0, column=0, sticky=tk.W) 
        self.nameLabel.config(font=("Courier", 10))
        healthLabelLabel = ttk.Label(self.stats, text='Health:')
        healthLabelLabel.grid(row=1, column=0, sticky=tk.W) 
        healthLabelLabel.config(font=("Courier", 10))
        self.healthLabel = ttk.Label(self.stats, text=str(self.rhealth) + '/' + str(self.stat.hp))
        self.healthLabel.config(font=("Courier", 10))
        self.healthLabel.grid(row=1, column=1, sticky=tk.W)
        manaLabelLabel = ttk.Label(self.stats, text='Mana:')
        manaLabelLabel.grid(row=2, column=0, sticky=tk.W) 
        manaLabelLabel.config(font=("Courier", 10))
        self.manaLabel = ttk.Label(self.stats, text=str(self.rmana) + '/' + str(self.stat.mana))
        self.manaLabel.config(font=("Courier", 10))
        self.manaLabel.grid(row=2, column=1, sticky=tk.W)
        expLabelLabel = ttk.Label(self.stats, text='Experience:')
        expLabelLabel.config(font=("Courier",10))
        expLabelLabel.grid(row=3, column=0, sticky=tk.W)
        self.expLabel = ttk.Label(self.stats, text=str(self.stat.exp) + '/' + str(self.expCap))
        self.expLabel.config(font=("Courier",10))
        self.expLabel.grid(row=3, column=1)
        self.damLabel = ttk.Label(self.stats, text='Damage: ' + str(self.stat.dam))
        self.damLabel.config(font=("Courier",10))
        self.damLabel.grid(row=4, column=0, sticky=tk.W)
        self.defenseLabel = ttk.Label(self.stats, text='Defense: ' + str(self.stat.defense))
        self.defenseLabel.config(font=("Courier",10))
        self.defenseLabel.grid(row=5, column=0, sticky=tk.W)
        self.speedLabel = ttk.Label(self.stats, text='Speed: ' + str(self.stat.speed))
        self.speedLabel.config(font=("Courier",10))
        self.speedLabel.grid(row=6, column=0, sticky=tk.W)
        self.levelLabel = ttk.Label(self.stats, text='Level: ' + str(self.stat.level))
        self.levelLabel.config(font=("Courier",10))
        self.levelLabel.grid(row=7, column=0, sticky=tk.W)
        self.goldLabel = ttk.Label(self.stats, text="Gold: " + str(self.stat.gold))
        self.goldLabel.config(font=("Courier",10))
        self.goldLabel.grid(row=8, column=0, sticky=tk.W)
        self.currentWeapon = ttk.Button(self.stats, text="Current Weapon", command=self.weapon.info)
        self.currentWeapon.grid(row=9, column=0)
        self.currentArmor = ttk.Button(self.stats, text="Current Armor", command=self.armor.info)
        self.currentArmor.grid(row=9, column=1)
        #------------NOTEBOOK BUTTONS-----------------------------


        self.winvCol = 0
        self.winvRow = 0
        self.ainvCol = 0
        self.ainvRow = 0
        self.skillCol = 0
        self.skillRow = 0
        
        self.winvButtons = []
        self.ainvButtons = []
        self.skillButtons = []
        self.town()

    def town(self):
        """berfungsi untuk membuat layar utama menjadi kota"""
        self.current.destroy()
        self.current = ttk.Labelframe(self.window, width=475, height=300, text='TOWN')
        self.current.place(x=0, y=0)
        townShop = ttk.Labelframe(self.current, width=225, height=175, text="SHOP")
        townShop.place(x=10, y=100)
        playerActions = ttk.Labelframe(self.current, width=100, height=175, text="SELF")
        playerActions.place(x=340, y=100)
        equipWeapon = ttk.Button(playerActions, text="Equip Weapon", command=self.wEquip)
        equipWeapon.pack()
        equipArmor = ttk.Button(playerActions, text="Equip Armor", command=self.aEquip)
        equipArmor.pack()
        discardInvItem = ttk.Button(playerActions, text="Discard", command=self.discard)
        discardInvItem.pack()
        heal = ttk.Button(playerActions, text="Heal", command=self.heal)
        heal.pack()
        ttk.Button(playerActions, text="dungeon", command=lambda:self.combat(random.randint(1,4),False)).pack()
        if self.stat.level >= 8:
            Boss = ttk.Labelframe(self.current, width= 100, height=50, text="Boss" )
            Boss.place(x=240, y=100)
            Demonking = ttk.Button(Boss, text="Demon King", command=lambda:self.combat(1,True,self.Demonking))
            Demonking.pack()  
        self.log("Welcome to town!")
        itemRow = 0
        itemCol = 0
        item1 = ttk.Button(townShop, text="Old Knife 200G", command=lambda:self.buyWeapon(Weapon("Old Knife", 3, "An old chef's knife"), 250))
        item1.grid(row=itemRow, column=itemCol)
        itemRow +=1
        item2 = ttk.Button(townShop, text="Leather Mail 250G", command=lambda:self.buyArmor(Armor("Tatered Cloth", 4 , "more efficent than wood"), 250))
        item2.grid(row=itemRow, column=itemCol)
        itemRow += 1
        if self.stat.level > 3:
            item3 = ttk.Button(townShop, text="Iron Sword 500G", command=lambda:self.buyWeapon(Weapon("Iron Sword", 5, "A Sword that made from iron"), 500))
            item3.grid(row=itemRow, column=itemCol)
            itemRow += 1
        if self.stat.level > 4:
            item4 = ttk.Button(townShop, text="Iron Mail 750G", command=lambda:self.buyArmor(Armor("Iron Mail", 9, "Classic Knight armor"), 750))
            item4.grid(row=itemRow, column=itemCol)
            itemRow += 1
        if self.stat.level > 5:
            item5 = ttk.Button(townShop, text="Diamond Sword 900G", command=lambda:self.buyWeapon(Weapon("Diamond Sword", 10, "A Sword that made from iron"), 900))
            item5.grid(row=itemRow, column=itemCol)
            itemRow += 1
        if self.stat.level > 6:
            item6 = ttk.Button(townShop, text="Diamond Armor 1000G", command=lambda:self.buyArmor(Armor("Diamon Armor", 14, "Made with storngest metal in The world"), 1000))
            item6.grid(row=itemRow, column=itemCol)
            itemRow += 1    
           

    #------------EQUIPPING------------------
    def wEquip(self):
        """Membuka menu senjata"""
        self.healWindow = tk.Tk()
        self.healWindow.title("Equipment")
        weaponIndex = tk.IntVar()
        weaponIndex.set(0)
        for val, obj in list(enumerate(self.winv)): 
            tk.Radiobutton(self.healWindow, text=obj.name, variable=weaponIndex, value=val).pack()
        ttk.Button(self.healWindow, text="Submit", command=lambda:self.wChange(self.winv[weaponIndex.get()])).pack()
        ttk.Button(self.healWindow, text="Exit", command=self.healWindow.destroy).pack()
    def wChange(self, weapon):
        """Mengganti Senjata"""
        index = self.winv.index(weapon)
        self.stat.set_dam(self.stat.dam - self.weapon.dam)
        self.gainWeapon(self.weapon)
        self.weapon = weapon
        self.stat.set_dam(self.stat.dam + self.weapon.dam)
        self.winv.pop(index)
        self.winvButtons[index].destroy()
        self.winvButtons.pop(index)
        self.log("You equipped the " + self.weapon.name)
        self.currentWeapon["command"] = self.weapon.info
        self.updateDam()
        self.healWindow.destroy()
    def aEquip(self):
        """Membukan menu ganti armor"""
        self.healWindow = tk.Tk()
        self.healWindow.title("Equipment")
        armorIndex = tk.IntVar()
        armorIndex.set(0)
        for val, obj in list(enumerate(self.ainv)): #THIS HAS SOLVED SO MUCH WHY DID I NOT KNOW ABOUT THIS EARLIER
            tk.Radiobutton(self.healWindow, text=obj.name, variable=armorIndex, value=val).pack()
        ttk.Button(self.healWindow, text="Submit", command=lambda:self.aChange(self.ainv[armorIndex.get()])).pack()
        ttk.Button(self.healWindow, text="Exit", command=self.healWindow.destroy).pack()
    def aChange(self, armor):
        """mengganti armor"""
        index = self.ainv.index(armor)
        self.stat.set_defense(self.stat.defense - self.armor.defense)
        self.gainArmor(self.armor)
        self.armor = armor
        self.stat.set_defense(self.stat.defense + self.armor.defense)
        self.ainv.pop(index)
        self.ainvButtons[index].destroy()
        self.ainvButtons.pop(index)
        self.log("You equipped the " + self.armor.name)
        self.currentArmor["command"] = self.armor.info
        self.updateDefense()
        self.healWindow.destroy()
    #----------------------Item Gain-----------------------
    def gainWeapon(self, weapon):
        """Adds the entered weapon to the weapon inventory"""
        if len(self.winv) < 16:
            self.winv.append(weapon)
            self.winvButtons.append(ttk.Button(self.wep, text=weapon.name, command=weapon.info))
            self.winvButtons[-1].grid(row=self.winvRow, column=self.winvCol)
            self.winvRow += 1
            if self.winvRow > 7:
                self.winvRow = 0
                self.winvCol += 1
        else:
            self.log("Not enough space for the " + weapon.name)        
    def gainArmor(self, armor):
        """Adds the entered armor to the armor inventory"""
        if len(self.ainv) < 16:
            self.ainv.append(armor)
            self.ainvButtons.append(ttk.Button(self.am, text=armor.name, command=armor.info))
            self.ainvButtons[-1].grid(row=self.ainvRow, column=self.ainvCol)
            self.ainvRow += 1
            if self.ainvRow > 3:
                self.ainvRow = 0
                self.ainvCol += 1
        else:
            self.log("Not enough space for the " + armor.name)
    
    #---------------------Healing----------------------
    def heal(self):
        if (self.rhealth < self.stat.hp) or (self.rmana < self.stat.mana):
            self.rhealth = self.stat.hp
            self.rmana = self.stat.mana
            self.updateHealth()
            self.updateMana()
            self.log("you have fully healed")
        else:
            self.log("your are already healthy")
    
    #--------------Text Updates---------------
    def updateHealth(self):
        """Updates health notebook label"""
        self.healthLabel['text'] = str(self.rhealth) + '/' + str(self.stat.hp)
    def updateExp(self):
        """updates notebook exp label"""
        self.expLabel['text'] = str(self.stat.exp) + '/' + str(self.expCap)
    def updateLevel(self):
        """updates notebook level label"""
        self.levelLabel['text'] = "Level: " + str(self.stat.level)
    def updateGold(self):
        """updates notebook gold label """
        self.goldLabel["text"] = "Gold: " + str(self.stat.gold)
    def updateDam(self):
        """updates notebook damage label """
        self.damLabel["text"] = "Damage: " + str(self.stat.dam)
    def updateDefense(self):
        """updates notebook defense label """
        self.defenseLabel["text"] = "defense: " + str(self.stat.defense)
    def updateSpeed(self):
        """updates notebook Speed label """
        self.speedLabel["text"] = "speed: " + str(self.stat.speed)
    def updateMana(self):
        """updates notebook Mana label """
        self.manaLabel["text"] = str(self.rmana) + '/' + str(self.stat.mana)
    
      
    def log(self, text): #menulis ke console
        """menulis string label ke console, maksimal 70 character"""
        tempText = self.statusConsole["text"]
        text += "\n"
        tempText += text
        if len(tempText) > 360:
            tempText = text
        self.statusConsole["text"] = tempText
    #-------------Buying Items-----------------
    def buyWeapon(self, weapon, cost):
      """Beli senjata"""
      if self.stat.gold - cost >= 0 and len(self.winv) < 16:
        self.log("You have bought the " + weapon.name + " for " + str(cost) + " gold.")
        self.gainWeapon(weapon)
        self.stat.gold -= cost
        self.updateGold()
      elif self.stat.gold - cost < 0:
        self.log("Not enough gold.")
      else:
        self.log("Not enough space.")
    def buyArmor(self, armor, cost):
      """Beli armor"""
      if self.stat.gold - cost >= 0 and len(self.ainv) < 16:
        self.log("You have bought the " + armor.name + " for " + str(cost) + " gold.")
        self.gainArmor(armor)
        self.stat.gold -= cost
        self.updateGold()
      elif self.stat.gold - cost < 0:
        self.log("Not enough gold.")
      else:
        self.log("Not enough space.")

    #-----------------DISCARDING ITEMS--------
    def discard(self):
      """Opens a menu to select what type of inventory object to destroy"""
      self.healWindow = tk.Tk()
      self.healWindow.title("Discard")
      ttk.Label(self.healWindow, text="Choose an item type to discard:").pack()
      ttk.Button(self.healWindow, text="Weapon", command=self.discardWeapon).pack()
      ttk.Button(self.healWindow, text="Armor", command=self.discardArmor).pack()
      ttk.Button(self.healWindow, text="Exit", command=self.healWindow.destroy).pack()
    def destroyThing(self, config, index):
      """takes in a string value of type of item deleted, and them index in respective list of item"""
      if config == "weapon":
        self.winv.pop(index)
        self.winvButtons[index].destroy()
        self.winvButtons.pop(index)
        self.winvRow -= 1
        if self.winvRow < 0:
          self.winvRow = 0
          self.winvCol += 1
      elif config == "armor":
        self.ainv.pop(index)
        self.ainvButtons[index].destroy()
        self.ainvButtons.pop(index)
        self.ainvRow -= 1
        if self.ainvRow < 0:
          self.ainvRow = 0
          self.ainvCol += 1
      self.menuWindow.destroy()
    def discardWeapon(self):
      """Opens a menu to select a weapon to destroy"""
      self.healWindow.destroy()
      self.menuWindow = tk.Tk()
      self.menuWindow.title("Inventory")
      weaponIndex = tk.IntVar()
      weaponIndex.set(0)
      for val, obj in list(enumerate(self.winv)): #THIS HAS SOLVED SO MUCH WHY DID I NOT KNOW ABOUT THIS EARLIER
        tk.Radiobutton(self.menuWindow, text=obj.name, variable=weaponIndex, value=val).pack()
      ttk.Button(self.menuWindow, text="Submit", command=lambda:self.destroyThing("weapon", weaponIndex.get())).pack()
      ttk.Button(self.menuWindow, text="Exit", command=self.menuWindow.destroy).pack()
    def discardArmor(self):
      """Opens a menu to select armor to destroy"""
      self.healWindow.destroy()
      self.menuWindow = tk.Tk()
      self.menuWindow.title("Inventory")
      armorIndex = tk.IntVar()
      armorIndex.set(0)
      for val, obj in list(enumerate(self.ainv)): #THIS HAS SOLVED SO MUCH WHY DID I NOT KNOW ABOUT THIS EARLIER
        tk.Radiobutton(self.menuWindow, text=obj.name, variable=armorIndex, value=val).pack()
      ttk.Button(self.menuWindow, text="Submit", command=lambda:self.destroyThing("armor", armorIndex.get())).pack()
      ttk.Button(self.menuWindow, text="Exit", command=self.menuWindow.destroy).pack()
    #------------------------------Skill gain--------------------------------------
    def getSkill(self,skill):
        self.skill.append(skill)
        self.skillButtons.append(ttk.Button(self.sk, text=skill.sname, command=skill.info))
        self.skillButtons[-1].grid(row=self.skillRow, column=self.skillCol)
        self.skillRow += 1
        if self.skillRow > 4:
            self.skillRow = 0
            self.skillCol += 1
        self.log("you've gained " + skill.sname + " !")
    #------------------------------level up-----------------------------------    
    def handleExp(self):
        """level up handler"""
        if self.stat.exp >= self.expCap:
            while self.stat.exp >= self.expCap:
                self.stat.level += 1
                self.log("You leveled up to level " + str(self.stat.level) + "!")
                self.stat.exp = self.stat.exp - self.expCap
                self.expCap = 3 * (self.stat.level * self.stat.level * self.stat.level)
                self.stat.hp += 2
                self.stat.mana += 1
                self.rhealth = self.stat.hp
                self.rmana = self.stat.mana
                if self.stat.level % 1 == 0:
                    self.stat.dam += 1
                    self.stat.speed += 2
                    self.stat.defense += 1
                if self.stat.level == 2:
                    self.getSkill(skill(5,"omnislash","deal 2 times damage to your enemy"))
                if self.stat.level == 5:
                    self.getSkill(skill(7,"vital slash","deal damage that ignore enemy defense"))
                if self.stat.level == 7:
                    self.getSkill(skill(9,"leech slash","gain HP equal 70 % " + "of your damage"))
            self.updateLevel()
            self.updateDam()
            self.updateDefense()
            self.updateSpeed()                
            self.updateHealth()
            self.updateMana()
            self.updateExp()
    
    #---------------combat screen-------------------------
    def combat(self,round,bossstate, enemy = None):
        """Combat state"""
        self.current.destroy()
        self.current = ttk.LabelFrame(self.window, width=475, height=300, text="COMBAT")
        self.current.place(x=0, y=0)
        if bossstate:
            foe = enemy
            self.log("You started battle with the" + foe.name)
        else:
            tempList = self.enemies[:]
            foe = enemy
            loop = True
            if foe != None:
                loop = False
            while loop == True: 
                foe = random.choice(tempList)
                if foe.level > self.stat.level - 2 and foe.level < self.stat.level + 2:
                    loop = False
                else:
                    tempList.remove(foe) 
                    if len(tempList) == 0:
                        self.window.destroy()
            self.log("You encounter a " + foe.name)
        enemyStats = ttk.LabelFrame(self.current, width=150, height = 200, text=foe.name.upper())
        enemyStats.place(x=5, y=10)
        self.eHealthBar = ttk.Label(enemyStats, text="Health: " + str(foe.hp) + "/" + str(foe.maxhp))
        self.eHealthBar.pack()
        ttk.Label(enemyStats, text="Level: " + str(foe.level)).pack()
        ttk.Label(enemyStats, text="Armor: " + str(foe.defense)).pack()
        ttk.Label(enemyStats, text="Damage: " + str(foe.dam)).pack()
        ttk.Label(enemyStats, text="Speed: " + str(foe.speed)).pack()
        attackButton = ttk.Button(self.current, text="Attack", command=lambda:self.attack(bossstate,foe,round))
        attackButton.place(x=150, y=100, width=100, height=75)
        skillButton = ttk.Button(self.current, text="Skill", command=lambda:self.SkillList(bossstate,foe,round))
        skillButton.place(x=150, y=200, width=100, height=75)
        runButton = ttk.Button(self.current, text="Run", command=lambda:self.run(bossstate,foe))
        runButton.place(x=300, y=200, width=100, height=75)
        defenseButton = ttk.Button(self.current, text="Defense", command=lambda:self.Defense(foe))
        defenseButton.place(x=300, y=100, width=100, height=75)
    #----------------------Attack-------------------------
    def attack(self,bossstate,enemy,round):
        """Attack satu sama lain"""
        turn = self.speedcheck(enemy)
        if turn:
            self.attackenemy(enemy)
            if enemy.hp < 1:
                self.DeathEnemy(bossstate,enemy,round)
            else:
                self.attackplayer(enemy)
                if self.rhealth < 1:
                    self.window.destroy()
        else:
            self.attackplayer(enemy)
            if self.rhealth < 1:
                self.window.destroy()
            else:   
                self.attackenemy(enemy)
                if enemy.hp < 1:
                    self.DeathEnemy(bossstate,enemy,round)
    
    def attackenemy(self,enemy):
        dealt = self.stat.dam - enemy.defense
        if dealt < 1:
            dealt = 1
        enemy.hp -= dealt
        self.log("You dealt " + str(dealt) + " damage.")
        self.eHealthBar["text"] = "Health: " + str(enemy.hp) + "/" + str(enemy.maxhp)
        self.cRestoreMana(0.2)
    
    def attackplayer(self,enemy):
        dealt1 = enemy.dam - self.stat.defense
        if dealt1 < 1:
            dealt1 = 1
        self.rhealth = self.rhealth - dealt1
        self.updateHealth()
        self.log("You took " + str(dealt1) + " damage")

    def DeathEnemy (self,bossstate,enemy,round):
        self.log("You defeated the " + enemy.name)
        enemy.hp = enemy.maxhp
        self.stat.gold += enemy.goldgain
        self.stat.exp += enemy.expgain
        self.handleExp()
        self.updateExp()
        self.updateGold()
        if round > 1:
            round -= 1
            self.combat(round,bossstate)
        else:
            if bossstate:
                self.current.destroy()
                self.current = ttk.Labelframe(self.window, width=475, height=300)
                self.current.place(x=0, y=0)
                win = tk.Label(self.current, text="You win!")
                win.place(x=200, y=135)
                win.config(font=15)
                
            else:
                self.town()
    #---------------------speed Check--------------------------
    def speedcheck (self,enemy):
        if self.stat.speed >= enemy.speed:
            return True
        else:
            return False

    #------------------RUN-----------------------
    def run(self,bossstate,enemy):
        if bossstate:
            self.log("you can't run from boss battle")
        else:
            turn = self.speedcheck(enemy)
            if turn:
                enemy.hp = enemy.maxhp
                self.log("you have run succesfully !")
                self.town()
            else:
                runchance = random.randint(0,10) 
                runchancemod = enemy.hp - self.stat.speed
                if runchance > runchancemod:
                    enemy.hp = enemy.maxhp
                    self.log("you have run succesfully !")
                    self.town()
                else:
                    self.log("You can't outrun your enemy !")
                    self.attackplayer(enemy)
                    if self.rhealth < 1:
                        self.window.destroy()
    #---------------------Skill----------------------
    def SkillList(self,bossstate,enemy,round):
        self.healWindow = tk.Tk()
        self.healWindow.title("Skill")
        for obj in self.skill: 
            ttk.Button(self.healWindow, text=obj.sname, command=partial(self.command,bossstate,obj.sname,obj.manacost,enemy,round)).pack()
    
    def skilllog(self,sname,enemy,dealt):
        self.log("you Use " + sname + " !")
        self.log("You dealt " + str(dealt) + " damage.")
        self.eHealthBar["text"] = "Health: " + str(enemy.hp) + "/" + str(enemy.maxhp)
    
    def omnislash(self,enemy,manacost,sname):
        dealt = (2 * self.stat.dam) - enemy.hp
        enemy.hp -= dealt
        if dealt < 1:
            dealt = 1
        self.rmana -= manacost
        self.updateMana()
        self.skilllog(sname,enemy,dealt)

    def vitalslash(self,enemy,manacost,sname):
        dealt = self.stat.dam
        enemy.hp -= dealt
        if dealt < 1:
            dealt = 1
        self.rmana -=manacost
        self.updateMana()
        self.skilllog(sname,enemy,dealt)
        
    
    def leechslash(self,enemy,manacost,sname):
        dealt = self.stat.dam - enemy.defense
        enemy.hp -= dealt
        restoredHP = round(0.5*self.stat.dam)
        self.rhealth = self.rhealth + restoredHP
        if self.rhealth > self.stat.hp:
           self.rhealth = self.stat.hp         
        if dealt < 1:
           dealt = 1
        self.rmana -=manacost
        self.updateMana()
        self.skilllog(sname,enemy,dealt)
        self.log("You gain " + str(restoredHP) + " hp")
        self.updateHealth()
    
    def command(self,bossstate,sname,manacost,enemy,round):
        turn = self.speedcheck(enemy)
        if self.rmana >= manacost:
            if turn:
                if sname == "omnislash":
                    self.omnislash(enemy,manacost,sname)
                    if enemy.hp < 1:
                        self.DeathEnemy(bossstate,enemy,round)
                    else:
                        self.attackplayer(enemy)
                        if self.rhealth < 1:
                            self.window.destroy()
                elif sname == "vital slash":
                    self.vitalslash(enemy,manacost,sname)
                    if enemy.hp < 1:
                        self.DeathEnemy(bossstate,enemy,round)
                    else:
                        self.attackplayer(enemy)
                        if self.rhealth < 1:
                            self.window.destroy()
                elif sname == "leech slash":
                    self.leechslash(enemy,manacost,sname)
                    if enemy.hp < 1:
                        self.DeathEnemy(bossstate,enemy,round)
                    else:
                        self.attackplayer(enemy)
                        if self.rhealth < 1:
                            self.window.destroy()
            else:
                if sname == "omnislash":
                    self.attackplayer(enemy)
                    if self.rhealth < 1:
                        self.window.destroy()
                    else:
                        self.omnislash(enemy,manacost,sname)
                        if enemy.hp < 1:
                            self.DeathEnemy(bossstate,enemy,round)

                elif sname == "vital slash":
                    self.attackplayer(enemy)
                    if self.rhealth < 1:
                        self.window.destroy()
                    else:
                        self.vitalslash(enemy,manacost,sname)
                        if enemy.hp < 1:
                            self.DeathEnemy(bossstate,enemy,round)
                elif sname == "leech slash":
                    self.attackplayer(enemy)
                    if self.rhealth < 1:
                        self.window.destroy()
                    else:
                        self.leechslash(enemy,manacost,sname)
                        if enemy.hp < 1:
                            self.DeathEnemy(bossstate,enemy,round)
            self.healWindow.destroy()
        else:
            self.log("your mana is not enough")
    #-----------------------restore mana----------------------
    def cRestoreMana(self,mod):
        if self.rmana < self.stat.mana:
            restoredmana = round(mod * self.stat.mana )
            self.rmana = self.rmana + restoredmana
            if self.rmana > self.stat.mana:
                restoredmana = restoredmana - (self.rmana - self.stat.mana)
                self.rmana = self.stat.mana     
            self.log('you restored ' + str(restoredmana) + ' mana.')
            self.updateMana()
    #-----------------------Defense---------------------------
    def Defense(self,enemy):
        self.stat.defense = 2 * self.stat.defense
        self.log('you tighten your defense !')
        self.attackplayer(enemy)
        self.stat.defense = round(self.stat.defense / 2)
        self.cRestoreMana(0.3)
        

                
                    

        


