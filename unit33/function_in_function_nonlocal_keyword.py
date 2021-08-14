def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            nonlocal x  # 20
            nonlocal y  # 100
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()


A()
