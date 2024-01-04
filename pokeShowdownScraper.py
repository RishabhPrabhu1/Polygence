# -*- coding: utf-8 -*-
"""
Created on Fri May 20 07:56:33 2022

@author: Gameboy
"""
import requests
import csv
import re





def matchParser (gamecode):
    try:
        real = True
        f = requests.get(gamecode).text
        if (f.find("|rated|Tournament battle") == -1):
            f = requests.get(gamecode).text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            fields = ['p1', 'p2', 'p1p1', 'p1p2', 'p1p3', 'p1p4', 'p1p5', 'p1p6', 'p2p1', 'p2p2', 'p2p3', 'p2p4', 'p2p5', 'p2p6', 'p1lead', 'p2lead', 'winner'] 
            filename = "pokedata1.csv"
            mydict = {'p1':re.findall(r'"p1":"([^"]+)',f)[0],'p2':re.findall(r'"p2":"([^"]+)',f)[0], 'p1p1':(re.findall(r'\|poke\|p1\|([^\|]*)',f)[0].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p1p2':(re.findall(r'\|poke\|p1\|([^\|]*)',f)[1].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p1p3':(re.findall(r'\|poke\|p1\|([^\|]*)',f)[2].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p1p4':(re.findall(r'\|poke\|p1\|([^\|]*)',f)[3].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p1p5':(re.findall(r'\|poke\|p1\|([^\|]*)',f)[4].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p1p6':(re.findall(r'\|poke\|p1\|([^\|]*)',f)[5].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p2p1':(re.findall(r'\|poke\|p2\|([^\|]*)',f)[0].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p2p2':(re.findall(r'\|poke\|p2\|([^\|]*)',f)[1].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p2p3':(re.findall(r'\|poke\|p2\|([^\|]*)',f)[2].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p2p4':(re.findall(r'\|poke\|p2\|([^\|]*)',f)[3].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p2p5':(re.findall(r'\|poke\|p2\|([^\|]*)',f)[4].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p2p6':(re.findall(r'\|poke\|p2\|([^\|]*)',f)[5].replace(", F","").replace("-*","").replace("-Original", "").replace("-Rapid-Strike","").replace("-Dada", "")), 'p1lead':( re.findall(r'\|switch\|p1a: [^\|]*\|([^\|]*)',f)[0].replace(", M","").replace(", F","").replace("-Rapid-Strike","").replace("-Bug", "").replace("-Dark", "").replace("-Dragon", "").replace("-Electric", "").replace("-Fairy", "").replace("-Fighting", "").replace("-Fire", "").replace("-Flying", "").replace("-Ghost", "").replace("-Grass", "").replace("-Ground", "").replace("-Ice", "").replace("-Poison", "").replace("-Psychic", "").replace("-Rock", "").replace("-Steel", "").replace("-Water", "").replace("-Crowned", "").replace("-Ice", "").replace("-Shadow", "").replace("-Burn", "").replace("-Chill", "").replace("-Douse", "").replace("-Shock", "").replace("-Original", "").replace("-Origin", "").replace("-Dawn-Wings", "").replace("-Dusk-Mane", "").replace("-Complete", "").replace("-Dada", "").replace("-Blue-Striped", "").replace("-Large", "").replace("-Small", "").replace("-Super", "").replace("-Hoenn", "").replace("-Kalos", "").replace("-Partner", "").replace("-Sinnoh", "").replace("-Unova", "").replace("-World", "").replace(", shiny","")), 'p2lead':(re.findall(r'\|switch\|p2a: [^\|]*\|([^\|]*)',f)[0].replace(", M","").replace(", F","").replace("-Rapid-Strike","").replace("-Bug", "").replace("-Dark", "").replace("-Dragon", "").replace("-Electric", "").replace("-Fairy", "").replace("-Fighting", "").replace("-Fire", "").replace("-Flying", "").replace("-Ghost", "").replace("-Grass", "").replace("-Ground", "").replace("-Ice", "").replace("-Poison", "").replace("-Psychic", "").replace("-Rock", "").replace("-Steel", "").replace("-Water", "").replace("-Crowned", "").replace("-Ice", "").replace("-Shadow", "").replace("-Burn", "").replace("-Chill", "").replace("-Douse", "").replace("-Shock", "").replace("-Original", "").replace("-Origin", "").replace("-Dawn-Wings", "").replace("-Dusk-Mane", "").replace("-Complete", "").replace("-Dada", "").replace("-Blue-Striped", "").replace("-Large", "").replace("-Small", "").replace("-Super", "").replace("-Hoenn", "").replace("-Kalos", "").replace("-Partner", "").replace("-Sinnoh", "").replace("-Unova", "").replace("-World", "").replace(", shiny","")), 'winner':re.findall(r'\|win\|([^\\]*)',f)[0]}
            #with open(filename, 'a') as csvfile: 
               # writer = csv.DictWriter(csvfile, fieldnames = fields) 
               # writer.writerow(mydict) 
        else:
            real = False
        return  real
    except (UnicodeEncodeError, IndexError) as e:
        return False









real =0
fake =0
#main method over here
l = requests.get("https://pokemonshowdown.com/ladder/gen8ou.json").text
listLines = l.split("}");
for i in listLines:
    currplayerid = i[i.find("userid")+9:i.find(",",i.find("userid")+2)-1]
    for k in range(1,25):
        currurl = "https://replay.pokemonshowdown.com/search.json?user="+currplayerid+"&page="+str(k)+"&format=gen8ou"
        currpagedata = requests.get(currurl).text
        currindex=currpagedata.find("gen8ou-");
        while (currindex != -1):
            
            currmatchid = currpagedata[currindex+7:currindex+17]
            if (currmatchid.find(",") == -1):
                currurl2 = "https://replay.pokemonshowdown.com/gen8ou-"+currmatchid+".json"
                print(currurl2+" "+str(k))
                if (matchParser(currurl2)):
                    real=real+1
                else:
                    fake=fake+1
                print("\n\n\n\n\n\n")
                print(str(real)+" "+str(fake))
            currindex = currpagedata.find("gen8ou-1",currindex+1)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
