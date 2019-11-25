import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

def test_compute_total_distance2():

    roadmapX=[("state1", "capi1", -4, 6),("state2", "capi2", 20, 2),("state3", "capi13", 88, -18)]
    assert compute_total_distance(road_mapX)= pytest.approx(24.331+70.880+95.078, 0.01)


def test_swap_cities():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    assert swap_cities(roadmapA, 0, 1)== [("state2", "capi2", 123, 323),("state1", "capi1", 22, 33),("state3", "capi13", 42, 11)]
   


def test_shift_cities():
    
    roadmapB=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]   

    assert shift_cities(roadmapB)==[("state3", "capi13", 42, 11), ("state1", "capi1", 22, 33),("state2", "capi2", 123, 323)] 

