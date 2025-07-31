from src import *

def test_mapping_flat():
    assert mars_rover((0, 0), "N", 7,
                      [],
                      "") == (0, 0)

def test_mapping_one_obstacle():
    assert mars_rover((0, 0), "N", 7,
                      [(2, 3)],
                      "") == (0, 0)

def test_mapping_two_obstacles():
    assert mars_rover((0, 0), "N", 7,
                      [(2, 3), (5, 6)],
                      "") == (0, 0)

def test_mapping_a_to_b():
    assert mars_rover((0, 0), "E", 7,
                      [(2, 3), (5, 6)],
                      "▲ ▶ ▲ ▲") == (1, 2)

def test_mapping_oob():
    assert mars_rover((0, 0), "E", 4,
                      [(2, 3)],
                      "▲ ▲ ▲ ▲") == (3, 0)

def test_mapping_obstacle_crash():
    assert mars_rover((0, 0), "E", 4,
                      [(2, 0)],
                      "▲ ▲ ▲ ▲") == (1, 0)

def test_mapping_final():
    assert mars_rover((0, 0), "S", 15,
                      [(2, 0), (4, 5), (4, 6), (4, 7), (7, 11), (8, 11), (9, 11), (10, 11)],
                      "▲ ◀ ▲ ▶ ▲ ▲ ◀ ▲ ▲ ▶ ▲ ▲ ◀ ▲ ▶ ▲ ▲ ▲ ▲ ▲ ▲ ◀ ▲ ▲ ▲ ▲ ▲ ▶ ▲ ◀ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲") == (14, 12)