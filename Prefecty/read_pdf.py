
import prefect



import prefect
from prefect import task, Flow

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")
    x = [x**2 for x in range(1_000)]
    logger.info('Finished squaring!!')

    y = 5 + '4'



with Flow("hello-flow") as flow:
    hello_task()

flow.run()




print('done')
