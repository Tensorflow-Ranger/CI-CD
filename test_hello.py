from hello import say_hello, verify_number

def test_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out

def test_verify_number():
    assert verify_number("123") is True
    assert verify_number("45.67") is True
    assert verify_number("-0.5") is True
    assert verify_number("abc") is False
    assert verify_number("") is False
