from toto.lib import who_am_i


def test_who_am_i():

    result = who_am_i()
    assert len(result) > 0
    assert type(result) == int
    assert "Yannis" in result
