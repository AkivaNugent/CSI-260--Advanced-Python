import time
from datetime import datetime as dt
from datetime import timedelta as td


def fact(iterations):
    try:
        iterations = int(iterations)
        if iterations < 0:
            raise ValueError
        return 1 if iterations == 0 else iterations * fact(iterations - 1)
    except ValueError as ve:
        print("cannot do ", iterations)
    except Exception as e:
        print(e, " broke :/")
        pass

#print(fact(5))
#print(fact(0))
#print(fact(-5))
#print(fact("h"))

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        base_fn(*args, **kwargs)
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds.")
        print(*args, **kwargs)
    return enhanced_fn

@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} tea.")
    time.sleep(steep_time)
    print("tea is ready")

@timer_dec
def make_matcha():
    print("Making matcha...")
    time.sleep(2)
    print("Matcha is ready")
    return f"Drink matcha by {dt.now() + td(minutes=30)}"


brew_tea("Lipton", 5)
print(make_matcha())