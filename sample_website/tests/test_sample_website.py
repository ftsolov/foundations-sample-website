from sample_website.website import hello_world # pylint: disable=import-error


def test_sample_website():
    assert hello_world() == '<h1>Hello, Felsi!</h1>'
