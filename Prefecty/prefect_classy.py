import prefect
from prefect import task, Flow
import numpy as np



def my_dec(fun):
    def wrapper(*args,**kwargs):
        print('Wrap Start')
        print(fun)
        fun_ret = fun(*args,**kwargs)
        print('Wrap End')
        return fun_ret
    return wrapper


@my_dec
def fact(n:int) -> float:
    return np.prod(range(1,n+1))


# print(fact(5))




class Person:

    # @my_dec
    def __init__(self) -> None:
        print('OMG!')
        self.num = np.random.random()

    @task
    def hello_task(self):
        logger = prefect.context.get("logger")
        logger.info("Hello world!")
        x = [x**2 for x in range(1_000)]
        print(self.num)
        logger.info('Finished squaring!!')

        # y = 5 + '4'


p = Person()
# p.hello_task()

with Flow("hello-flow") as flow:
    p.hello_task(p)



flow.run()

print(p.num)

