def test_main():
    from src.main import main

    assert main(1, 2) == 2


def test_hello():
    from mod import module_1

    assert module_1.hello() == "Hello from module_1"
