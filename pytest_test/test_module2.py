from utils.utilConfigParser import getPetApiUrl

base_url_path = getPetApiUrl()  

def test_checkUlr():
    assert 'petstore' in base_url_path