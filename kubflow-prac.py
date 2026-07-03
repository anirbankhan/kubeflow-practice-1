from kfp import dsl
from kfp import compiler
@dsl.component
def say_hello(name: str) -> str:
    return f'Hello {name}'
@dsl.pipeline
def hello_pipeline(recepient: str) -> str:
    hello_task = say_hello(name=recepient)
    return hello_task.output

compiler.Compiler().compile(hello_pipeline, 'pipeline.yaml')
