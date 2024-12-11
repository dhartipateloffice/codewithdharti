import time


def calculatetime(func):
    def wrapper_excute(*args,**kwargs):
        starttime = time.time()
        result = func(*args,**kwargs)
        endtime = time.time()
        consumetime = endtime - starttime
        print(f"Function has taken {consumetime} seconds")
        return result  # Return the original function's result
    return wrapper_excute

@calculatetime
def interview_prepare():
    for i in range (90):
        pass
interview_prepare()