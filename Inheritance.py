class One:
    def display(self):
        print("this is the parent class")
class two(One):
    def show(self):
        print("this is the child class")
        print("this is another file")
obj=two()
obj.display()
obj.show()
