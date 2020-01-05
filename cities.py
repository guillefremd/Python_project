import copy
import math
from tkinter import *
from random import randint
from tkinter import font


    
def read_cities(file_name):
    try:
        infile = open(file_name, "r")
        global road_map
        road_map=[]
        line=infile.readline()
     
        while line !="":
            line=str(line)
            line=line.rstrip()
            city=line.split("\t")
            road_map.append(city)
            line=infile.readline()

        for i in range (0,len(road_map)):
            road_map[i][2]=float(road_map[i][2])
            road_map[i][3]=float(road_map[i][3])

        for i in range (0,len(road_map)):
            for i2 in range(0,len(road_map)):
                if i!=i2:
                
                    a= road_map[i][2]
                    b=road_map[i2][2]
                    c=road_map[i][3]
                    d=road_map[i2][3]
                    if a==b and c==d:
                        print("There is a problem with your file: two cities cannot have the exact same latitude and longitude. \nPlease try again with a new file")
                        return False
            
        return (road_map)

    except FileNotFoundError:
        print("The file you entered does not exist. Please try again.")
        return False
    except ValueError:
        print("Make sure the coordinates (longitude and latitude) in the chosen file are numerical values.\nPlease try again with a new file.")
        road_map=[]
        return False

          

def print_cities(road_map):
    try:
        if len(road_map)<3:
            print ("The road map is empty or has less than three cities, please load a new file")
            return False
        else:
            for i in road_map:
                print(i[1], round((i[2]),1), round((i[3]),1))
    except:
        print(str(road_map) + " is not a valid road map. Please try again")
        return False

def compute_total_distance(road_map):
    try:
        if len(road_map)<3:
            print ("There are less than three cities in the road map, please load a new file")
            return False
        else:
            total_distance=0
            for i in range (0,len(road_map)):
                a= road_map[i][2]
                b=road_map[((i+1)%len(road_map))][2]
                c=road_map[i][3]
                d=road_map[((i+1)%len(road_map))][3]
                nextdistance=math.sqrt(((a-b)**2)+((c-d)**2))
                total_distance+=nextdistance
            return total_distance
    except ValueError:
        print("Please make sure your cities data file is correct.\nPlease usa a new map")
        return False

def swap_cities(road_map, index1, index2):

    try:
        if index1==index2:
            print("Please choose two different indexes to swap")
            return False
        elif len(road_map)<=2:
            print ("The road map is empty or has less than two cities, please use another file")
            return False
        else:
            oldindex2=road_map[index2]
            road_map[index2]=road_map[index1]
            road_map[index1]=oldindex2
            newtuple=(road_map,compute_total_distance(road_map))
            return newtuple
               
    except IndexError:
        print("Please make sure the indexes you chose are correct.\nRemember your road map has " + str(len(road_map)) + " cities. Try again.")
        return False

    except TypeError:
        print("Please make sure the indexes you chose are integer numbers.Try again.")
        return False


def shift_cities(road_map):

    if len(road_map)<=2:
        print ("The road map is empty or has less than two cities, please use another file")
        return False
    else:
        first=[()]
        deep=copy.deepcopy(road_map)
        first[0]=deep[-1]
        first.extend(deep[:-1])
        for i in range (0,len(road_map)):
            road_map[i]=first[i]
        return road_map
    
def find_best_cycle(road_map):
    if road_map==[]:
        print("Please load a new road map, the current one is empty")
        return False
    
    bestmap=copy.deepcopy(road_map)
    bestdist=compute_total_distance(road_map)
     
    for i in range (0, 10000):
        ran1=randint(0,(len(road_map)-1))
        ran2=randint(0,(len(road_map)-1))
        while ran1==ran2:
            ran2=randint(0,(len(road_map)-1))

        swap_cities(road_map, ran1, ran2)
        shift_cities(road_map)

        if bestdist>compute_total_distance(road_map):
            bestdist=compute_total_distance(road_map)
            bestmap=copy.deepcopy(road_map)
                    
        else:
            for i in range (0,len(road_map)):
                road_map[i]=bestmap[i]

    return road_map
    

def print_map(road_map):
    try:
        if len(road_map)<3:
            print ("There are less than three cities in the road map, please load a new file")
            return False
        else:
            total_distance=0
            for i in range (0,len(road_map)):
                a= road_map[i][2] 
                b=road_map[((i+1)%len(road_map))][2]
                c=road_map[i][3]
                d=road_map[((i+1)%len(road_map))][3]
                nextdistance=math.sqrt(((a-b)**2)+((c-d)**2))

                print ("Distance from " + road_map[i][1] + " to " + (road_map[((i+1)%len(road_map))][1]) +": "+ str(nextdistance))
                total_distance+=nextdistance
            print("----------End of the road map----------")
            print("The total distance of the current road map is " + str(total_distance))

    except ValueError:
        print("Please make sure your cities data file is correct.\n Please usa a new map")
        return False
    
def visualise(road_map):

    if road_map==[]:
        print ("Your road map is empty. Please load a new one")
        return False
    elif len(road_map)<3:
        print ("Your road map hsa less than three cities. Please load a new one")
        return False
    
    min_distance=compute_total_distance(road_map)

    for i in range (0,len(road_map)):
        for i2 in range(0,len(road_map)):
            if i!=i2:
                
                a= road_map[i][2]
                b=road_map[i2][2]
                c=road_map[i][3]
                d=road_map[i2][3]
                this_distance=math.sqrt(((a-b)**2)+((c-d)**2))
                if this_distance<min_distance:min_distance=this_distance
                

    mapa=Tk()
    mapa.title("Road Map")
    canvas=Canvas(mapa,width=800,height=800)
    canvas.config(scrollregion=canvas.bbox(mapa))
    scrollbar = Scrollbar(mapa)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar2 = Scrollbar(mapa,orient=HORIZONTAL)
    scrollbar2.pack(side=BOTTOM, fill=X)

    min_lat=90
    max_lat=-90
    min_lon=180
    max_lon=-180    

    for i in range (0,len(road_map)):
        a=road_map[i][2]
        b=road_map[i][3]

        if a<min_lat:min_lat=a
        if a>max_lat:max_lat=a
        if b>max_lon:max_lon=b
        if b<min_lon:min_lon=b

    dist_lat=max_lat-min_lat
    dist_lon=max_lon-min_lon

    width_map=(dist_lon/min_distance)
    height_map=(dist_lat/min_distance)

    if height_map<50:with_map=50
    if width_map<100:width_map=100

    scale=30/min_distance
    if scale<30:scale=30


    myfontbold = font.Font(family='freemono', size=9, weight="bold")

    for i in range(int(max_lat)+2, int(min_lat)-2,-1):
        canvas.create_line((int(min_lon)-2)*scale, height_map-i*scale, int((max_lon)+1)*scale,height_map-i*scale,fill="grey", dash=(1,1))
        canvas.create_text((int(min_lon)-2)*scale, height_map-i*scale,anchor=NE,font=myfontbold,text=str(i))
    for i in range(int(max_lon)+1,int(min_lon)-3,-1):
        canvas.create_line(i*scale, height_map-int((min_lat)-1)*scale,i*scale, height_map-int((max_lat)+2)*scale,fill="grey", dash=(1,1))
        canvas.create_text(i*scale, height_map-int((max_lat)+2)*scale,anchor=S,font=myfontbold,text=str(i))

    myfont = font.Font(family='freemono', size=8)

    for i in range (0,len(road_map)):
        a= road_map[i][2] 
        b=road_map[((i+1)%len(road_map))][2]
        c=road_map[i][3]
        d=road_map[((i+1)%len(road_map))][3]
        nextdistance=math.sqrt(((a-b)**2)+((c-d)**2))

        lontomap=((c)*scale)
        lattomap=height_map-(((a)*scale))
        lontomapnext=((d)*scale)
        lattomapnext=height_map-(((b)*scale))

        canvas.create_oval(lontomap-3, lattomap-3,lontomap+3, lattomap+3,fill="salmon")
        canvas.create_text(lontomap,lattomap,anchor=W, font=myfont,text=str(i+1)+"\n" + road_map[i][1])
        canvas.create_line(lontomap, lattomap, lontomapnext,lattomapnext,fill="steel blue")
        
        canvas.pack(fill="both", expand=True)
        
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.config(xscrollcommand=scrollbar2.set)

    scrollbar.config(command=canvas.yview)
    scrollbar2.config(command=canvas.xview)

    canvas.configure(scrollregion=canvas.bbox("all"))

    mapa.mainloop()


def main():

    if read_cities("city-data.txt")==False:
        return False
    print("This is the original city data:")
    print_cities(road_map)
    find_best_cycle(road_map)
    print("This is the best cycle we identifed:")
    print_cities(road_map)
    visualise(road_map)

if __name__ == "__main__": #keep this in
    main()

