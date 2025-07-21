def test_hello():
    from mod import module_1

    assert module_1.hello() == "Hello from module_1"
