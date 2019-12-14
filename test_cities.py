import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

def test_compute_total_distance2():

    roadmapX=[("state1", "capi1", -4, 6)]
   # assert compute_total_distance(road_mapX)== #ERROR, SHOULD BE MORE THAN 1 CITY/STATE
   


def test_compute_total_distance3():

    roadmapX=None
    #assert compute_total_distance(road_mapX)== #ERROR THERE IS NO ROADMAP LOADED



def test_swap_cities():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    assert swap_cities(roadmapA, 0, 1)== [("state2", "capi2", 123, 323),("state1", "capi1", 22, 33),("state3", "capi13", 42, 11)]
   


def test_swap_cities2():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    #assert swap_cities(roadmapA, 0, 0)== #ERROR SWAP INDEXES SHOULD BE DIFFERENT


def test_swap_cities3():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    #assert swap_cities(roadmapA, "a", 1)== #ERROR INDEXES HAVE TO BE INTEGERS

    
def test_swap_cities4():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    #assert swap_cities(roadmapA, 2.4, 1)== #ERROR INDEXES HAVE TO BE INTEGERS

    
def test_swap_cities5():

    roadmapA=None
    
    #assert swap_cities(roadmapA, 0, 1)== #ERROR THERE IS NO DATABASE



def test_shift_cities():
    
    roadmapB=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]   

    assert shift_cities(roadmapB)==[("state3", "capi13", 42, 11), ("state1", "capi1", 22, 33),("state2", "capi2", 123, 323)]


def test_shift_cities2():
    
    roadmapB=None 

    #assert shift_cities(roadmapB)== #ERROR THERE IS NO DATABASE

def test_shift_cities3():
    
    roadmapB=[("state1", "capi1", -4, 6)] 

   # assert shift_cities(roadmapB)== #ERROR THERE IS ONLY ONE STATE/CITY

    

