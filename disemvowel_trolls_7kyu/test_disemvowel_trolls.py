import pytest


def test_disemvowel():
    """Tests that vowels are being removed."""
    from disemvowel_trolls import disemvowel
    string = "This website is for losers LOL!"
    assert disemvowel(string) == "Ths wbst s fr lsrs LL!"


def test_disemvowel2():
    """Tests that vowels are being removed."""
    from disemvowel_trolls import disemvowel
    string = "REGEX for the win!"
    assert disemvowel(string) == "RGX fr th wn!"


def test_disemvowel3():
    """Tests that vowels are being removed."""
    from disemvowel_trolls import disemvowel
    string = "We are the knights who say 'Ni'!"
    assert disemvowel(string) == "W r th knghts wh sy 'N'!"


def test_disemvowel4():
    """Tests that vowels are being removed."""
    from disemvowel_trolls import disemvowel
    string = "Raindrops keep falling on my head"
    assert disemvowel(string) == "Rndrps kp fllng n my hd"


def test_disemvowel5():
    """Tests that vowels are being removed."""
    from disemvowel_trolls import disemvowel
    string = "All your base are belong to us"
    assert disemvowel(string) == "ll yr bs r blng t s"
