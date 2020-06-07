class Test:
    # name = 'hi'

    def __init__(self):
        self.name: str = 'hi' 

test = Test()

print(getattr(test, 'name'))

setattr(test, 'name', 'yo')

print(getattr(test, 'name'))

print(test.__dict__)