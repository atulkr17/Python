def santity_chake(data_type):
    def outer_warpper(funct):
        def inner_wrapper(*args):

            if args[0]==data_type:
                funct(*args)
            else:
                raise TypeError('ye data type nhii chalega')    
            
        return inner_wrapper
    return outer_warpper

@santity_chake(int)

def Square(num):
    return num**2

Square(6)