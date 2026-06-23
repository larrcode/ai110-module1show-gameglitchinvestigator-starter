from logic_utils import check_guess, update_score

def test_check_guess_too_high():
    outcome, message = check_guess(43, 35)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_check_guess_too_low():
    outcome, message = check_guess(20, 35)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_update_score_wrong_guess():
    new_score = update_score(100, "Too High", 1)
    assert new_score == 99
