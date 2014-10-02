from vyperlogix.decorators import DecoTrace

class minimum_x(object):
    '''
    - returns a decorator that can be used to decorate another function
    - verifies argument of the function it decorates <= the given value
    - raises a ValueError on failure.

    Example...

    >>> @minimum_x(6)
    ... def test(arg):
    ...   print arg
    ...
    '''
    def __init__(self,arg):
        self.arg = arg
    def __call__(self, original_func):
        decorator_self = self
        def wrapper( *args, **kwargs):
            if (args[0] < decorator_self.arg):
                raise ValueError
            original_func(*args,**kwargs)
        return wrapper

if (__name__ == '__main__'):
    @minimum_x(6)
    def test(arg):
        print arg

    test(6)
    test(5)
