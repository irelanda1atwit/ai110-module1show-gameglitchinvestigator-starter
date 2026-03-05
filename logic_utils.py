def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


# ---------------------------------------------------------------------------
# Tests for win logic — run with: pytest logic_utils.py -v
# ---------------------------------------------------------------------------

# check_guess — win detection

def test_win_exact_match():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_win_at_lower_boundary():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_win_at_upper_boundary():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"


# check_guess — hint direction (regression for the string-cast bug)
#
# The mid-game type-coercion bug caused lexicographic comparison on even
# attempts, e.g. str(6) > str(50) → True, producing a "Too High" hint when
# the guess was actually lower than the secret.

def test_hint_too_high_when_guess_above_secret():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_too_low_when_guess_below_secret():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_regression_string_cast_single_digit_vs_two_digit():
    # Before the fix: str(6) > str(50) evaluates True lexicographically,
    # so check_guess(6, 50) would wrongly return "Too High".
    # After the fix it must return "Too Low".
    outcome, message = check_guess(6, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_regression_string_cast_high_guess_vs_low_secret():
    # Symmetric case: str(20) > str(9) → False lexicographically (wrong).
    # Confirm numeric comparison is used.
    outcome, message = check_guess(20, 9)
    assert outcome == "Too High"
    assert "LOWER" in message


# update_score — win scoring

def test_win_score_first_attempt():
    # attempt_number=2 (incremented before check): 100 - 10*(2+1) = 70
    score = update_score(0, "Win", 2)
    assert score == 70

def test_win_score_adds_to_existing_score():
    score = update_score(50, "Win", 2)
    assert score == 120

def test_win_score_floors_at_10():
    # attempt_number=9: 100 - 10*10 = 0 → clamped to 10
    score = update_score(0, "Win", 9)
    assert score == 10

def test_win_score_exactly_at_floor_boundary():
    # attempt_number=8: 100 - 90 = 10 → exactly at floor, no clamping needed
    score = update_score(0, "Win", 8)
    assert score == 10

def test_non_win_outcome_does_not_add_win_points():
    score = update_score(100, "Too High", 2)
    assert score != 100 + 70  # should not apply win formula


# ---------------------------------------------------------------------------
# parse_guess — invalid input handling
# ---------------------------------------------------------------------------

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_plain_letters():
    ok, value, _ = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_guess_special_characters():
    ok, value, _ = parse_guess("!@#$")
    assert ok is False
    assert value is None

def test_parse_guess_mixed_alphanum():
    ok, value, _ = parse_guess("12abc")
    assert ok is False
    assert value is None

def test_parse_guess_emoji():
    ok, value, _ = parse_guess("🎉")
    assert ok is False
    assert value is None

def test_parse_guess_whitespace_only():
    ok, value, _ = parse_guess("   ")
    assert ok is False
    assert value is None

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    # Floats are accepted but truncated to int
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_guess_negative_number():
    # Negative numbers parse successfully — range validation is separate
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
