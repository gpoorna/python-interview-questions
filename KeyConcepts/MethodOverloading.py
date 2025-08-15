class Demo:
    def disp1(self):
        print("Inside disp1")

    def disp1(self,a):
        print("Inside disp with argument", a)

    def disp1(self,a,b):
        print("Inside disp with 2 arguments", a, b)

d =Demo()
d.disp1()
d.disp1(10)
d.disp1(10,20)
