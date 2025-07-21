def test_main():
    from main import main

    assert main(1, 2) == 5


def test_hello():
    from mod import module_1

    assert module_1.hello() == "Hello from module_1"
