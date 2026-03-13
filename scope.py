
int_value = None
str_value = None

def set_globals(some_int, some_str):
    int_value, str_value
    int_value = some_int
    str_value = some_str

def get_globals():
    return (int_value, str_value)

if __name__ == "__main__":
    print(get_globals())      
    set_globals(10, "Hello")
    print(get_globals())       


    
