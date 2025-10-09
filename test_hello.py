from hello import say_hello

def test_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
