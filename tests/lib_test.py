from mytoolbox.lib import cleaning

def test_clean():
    res = cleaning()
    assert ',' in res

def test_clean2():
    res = cleaning()
    assert 'á' in res

def test_clean3():
    res = cleaning()
    assert 'ç' in res

def test_clean4():
    res = cleaning()
    assert res.Capitalize in res
