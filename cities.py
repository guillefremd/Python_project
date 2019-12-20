import copy
import math
from random import randint


def go():
    read_cities("city-data.txt")
    swap_cities(road_map, 5, 3)
    
def read_cities(file_name):
           
     """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
     try:
          infile = open(file_name, "r")
          global road_map
          road_map=[]
          cities_data=[]
          line=infile.readline()
     
          while line !="":
               line=str(line)
               line=line.rstrip()
               city=line.split("\t")
               road_map.append(city)
               line=infile.readline()

     except FileNotFoundError:
         print("The file you entered does not exist. Please try again.")
          

    
"""
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
      [(state, city, latitude, longitude), ...] 
    Use this as your initial `road_map`, that is, the cycle 
      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """

def print_cities(road_map):
     try:
          if len(road_map)<3:
               print ("The road map is empty or has less than three cities, please load a new file")
               return False
          else:
               for i in road_map:
                    print(i[1], round(float(i[2]),1), round(float(i[3]),1))
     except:
          print(str(road_map) + " is not a valid road map. Please try again")
          return False

    
"""
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    

def compute_total_distance(road_map):
    try:
        if len(road_map)<3:
            print ("There are less than three cities in the road map, please load a new file")
            return False
        else:
            total_distance=0
            for i in range (0,len(road_map)):
                a= float(road_map[i][2])
                b=float(road_map[((i+1)%len(road_map))][2])
                c=float(road_map[i][3])
                d=float(road_map[((i+1)%len(road_map))][3])
                nextdistance=math.sqrt(((a-b)**2)+((c-d)**2))
                total_distance+=nextdistance
            return total_distance
    except ValueError:
        print("Please make sure your cities data file is correct.\n Please usa a new map")
        return False
    
"""
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
"""


def swap_cities(road_map, index1, index2):

     try:
          if index1==index2:
               print("Please choose two different indexes to swap")
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


"""
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 
        (new_road_map, new_total_distance)
    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def shift_cities(road_map):

    if len(road_map)<2:
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
    

          
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """

def find_best_cycle(road_map):
    
     bestmap=road_map
     bestdist=compute_total_distance(road_map)
     
     for i in range (0, 1000):
          ran1=randint(0,(len(road_map)-1))
          ran2=randint(0,(len(road_map)-1))
          while ran1==ran2:
               ran2=randint(0,(len(road_map)-1))

          swap_cities(road_map, ran1, ran2)
          shift_cities(road_map)

          if bestdist>compute_total_distance(road_map):
              bestdist=compute_total_distance(road_map)
              bestmap=copy.deepcopy(road_map)
                    

     for i in range (0,len(road_map)):
          road_map[i]=bestmap[i]


     return road_map
    
"""
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    read_cities("city-data.txt")
    print("This is the original city data:")
    print_cities(road_map)
    find_best_cycle(road_map)
    print("This is the best cycle we identifed:")
    print_cities(road_map)

if __name__ == "__main__": #keep this in
    main()
