from src import bowling_score

def test_shitty_player():
        assert bowling_score('-- -- -- -- -- -- -- -- -- --') == 0

def test_godly_player():
        assert bowling_score('X X X X X X X X X X X X') == 300

def test_average_player():
        assert bowling_score('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5') == 150

def test_fourth_player():
        assert bowling_score('-2 53 61 27 7- 18 -- 71 44 9-') == 67

def test_final_player():
        assert bowling_score('-2 4/ 61 X 7- 1/ -- 71 X 9-') == 95