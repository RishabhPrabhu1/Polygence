# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:00:56 2022

@author: Gameboy
"""

import csv
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
winratenum ={}
winrateden ={}
winrate={}
with open('pokedata1.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
      #print(lines)
      if (len(lines) == 17):
         if (lines[0] == (lines[16])):
             for i in range(2,7):
                 curr = (lines[i].replace(", M","").replace(", F","").replace("-Rapid-Strike","").replace("-Bug", "").replace("-Dark", "").replace("-Dragon", "").replace("-Electric", "").replace("-Fairy", "").replace("-Fighting", "").replace("-Fire", "").replace("-Flying", "").replace("-Ghost", "").replace("-Grass", "").replace("-Ground", "").replace("-Ice", "").replace("-Poison", "").replace("-Psychic", "").replace("-Rock", "").replace("-Steel", "").replace("-Water", "").replace("-Crowned", "").replace("-Ice", "").replace("-Shadow", "").replace("-Burn", "").replace("-Chill", "").replace("-Douse", "").replace("-Shock", "").replace("-Original", "").replace("-Origin", "").replace("-Dawn-Wings", "").replace("-Dusk-Mane", "").replace("-Complete", "").replace("-Dada", "").replace("-Blue-Striped", "").replace("-Large", "").replace("-Small", "").replace("-Super", "").replace("-Hoenn", "").replace("-Kalos", "").replace("-Partner", "").replace("-Sinnoh", "").replace("-Unova", "").replace("-World", "").replace(", shiny",""))
                 if curr in winratenum.keys():
                     winratenum[curr] = winratenum[curr]+1
                     winrateden[curr] = winrateden[curr]+1
                 else:
                     winratenum.update({curr:0})
                     winrateden.update({curr:1})
             for i in range(8,13):
                 curr = (lines[i].replace(", M","").replace(", F","").replace("-Rapid-Strike","").replace("-Bug", "").replace("-Dark", "").replace("-Dragon", "").replace("-Electric", "").replace("-Fairy", "").replace("-Fighting", "").replace("-Fire", "").replace("-Flying", "").replace("-Ghost", "").replace("-Grass", "").replace("-Ground", "").replace("-Ice", "").replace("-Poison", "").replace("-Psychic", "").replace("-Rock", "").replace("-Steel", "").replace("-Water", "").replace("-Crowned", "").replace("-Ice", "").replace("-Shadow", "").replace("-Burn", "").replace("-Chill", "").replace("-Douse", "").replace("-Shock", "").replace("-Original", "").replace("-Origin", "").replace("-Dawn-Wings", "").replace("-Dusk-Mane", "").replace("-Complete", "").replace("-Dada", "").replace("-Blue-Striped", "").replace("-Large", "").replace("-Small", "").replace("-Super", "").replace("-Hoenn", "").replace("-Kalos", "").replace("-Partner", "").replace("-Sinnoh", "").replace("-Unova", "").replace("-World", "").replace(", shiny",""))
                 if curr in winratenum.keys():
                     winratenum[curr] = winratenum[curr]
                     winrateden[curr] = winrateden[curr]+1
                 else:
                     winratenum.update({curr:0})
                     winrateden.update({curr:1})
         else:
            for i in range(8,13):
                curr = (lines[i].replace(", M","").replace(", F","").replace("-Rapid-Strike","").replace("-Bug", "").replace("-Dark", "").replace("-Dragon", "").replace("-Electric", "").replace("-Fairy", "").replace("-Fighting", "").replace("-Fire", "").replace("-Flying", "").replace("-Ghost", "").replace("-Grass", "").replace("-Ground", "").replace("-Ice", "").replace("-Poison", "").replace("-Psychic", "").replace("-Rock", "").replace("-Steel", "").replace("-Water", "").replace("-Crowned", "").replace("-Ice", "").replace("-Shadow", "").replace("-Burn", "").replace("-Chill", "").replace("-Douse", "").replace("-Shock", "").replace("-Original", "").replace("-Origin", "").replace("-Dawn-Wings", "").replace("-Dusk-Mane", "").replace("-Complete", "").replace("-Dada", "").replace("-Blue-Striped", "").replace("-Large", "").replace("-Small", "").replace("-Super", "").replace("-Hoenn", "").replace("-Kalos", "").replace("-Partner", "").replace("-Sinnoh", "").replace("-Unova", "").replace("-World", "").replace(", shiny",""))
                if curr in winratenum.keys():
                    winratenum[curr] = winratenum[curr]+1
                    winrateden[curr] = winrateden[curr]+1
                else:
                    winratenum.update({curr:0})
                    winrateden.update({curr:1})
            for i in range(2,7):
                curr = (lines[i].replace(", M","").replace(", F","").replace("-Rapid-Strike","").replace("-Bug", "").replace("-Dark", "").replace("-Dragon", "").replace("-Electric", "").replace("-Fairy", "").replace("-Fighting", "").replace("-Fire", "").replace("-Flying", "").replace("-Ghost", "").replace("-Grass", "").replace("-Ground", "").replace("-Ice", "").replace("-Poison", "").replace("-Psychic", "").replace("-Rock", "").replace("-Steel", "").replace("-Water", "").replace("-Crowned", "").replace("-Ice", "").replace("-Shadow", "").replace("-Burn", "").replace("-Chill", "").replace("-Douse", "").replace("-Shock", "").replace("-Original", "").replace("-Origin", "").replace("-Dawn-Wings", "").replace("-Dusk-Mane", "").replace("-Complete", "").replace("-Dada", "").replace("-Blue-Striped", "").replace("-Large", "").replace("-Small", "").replace("-Super", "").replace("-Hoenn", "").replace("-Kalos", "").replace("-Partner", "").replace("-Sinnoh", "").replace("-Unova", "").replace("-World", "").replace(", shiny",""))
                if curr in winratenum.keys():
                    winratenum[curr] = winratenum[curr]
                    winrateden[curr] = winrateden[curr]+1
                else:
                    winratenum.update({curr:0})
                    winrateden.update({curr:1})
  for i in winratenum.keys():
      winrate.update({i:winratenum[i]/winrateden[i]})
  pd = pandas.DataFrame([winrate,winratenum,winrateden])
  pd = pd.transpose()
  pd = pd.sort_values(2,ascending=False)
  
#  sns.barplot(x=pd[2][0:10],y=pd[0][0:10])
  winrateusageslr = LinearRegression(fit_intercept=True)
  #x=pd.iloc[0:100,[2]]
  #y=pd.iloc[0:100,[0]]
  x=pd[[2]]
  y=pd[[0]]
  winratetousage = plt.scatter(x,y)
  winrateusageslr.fit(x,y)
  LinearRegression()
  ypredictwinrateusageslr = winrateusageslr.predict(x)
  print(mean_squared_error(y,ypredictwinrateusageslr))
  print(winrateusageslr.coef_)
  print(winrateusageslr.intercept_)
  plt.plot([0,14000],[winrateusageslr.intercept_,winrateusageslr.intercept_+14000*winrateusageslr.coef_],linewidth=2,color='red')
