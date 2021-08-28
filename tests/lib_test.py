from mytoolbox.lib import cleaning

def test_clean():
    res = cleaning('hello, my name')
    assert not ',' in res

def test_clean2():
    res = cleaning('$ pesos')
    assert not '$' in res

def test_clean3():
    res = cleaning('française')
    assert not 'ç' in res

def test_clean4():
    string=  'My Name Is'
    res = cleaning(string)
    assert res == res.lower()

