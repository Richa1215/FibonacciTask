import asyncio
import random


# Recursive Fibonacci function without delay
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Call Fibonacci function with random delay
async def async_fib(n):
    # Random delay up to 1 second
    delay = round(random.random(), 2)
    await asyncio.sleep(delay)
    return fib(n)


def is_positive_number(number):
    try:
        number = int(number)
    except ValueError:
        return False
    return number > 0


async def main():
    # Read positive (>0) number
    n = input("Enter a positive number n: ")
    if not is_positive_number(n):
        print("This is not a positive number!")
        return

    # Create two asynchronous tasks
    n = int(n)
    task1 = asyncio.create_task(async_fib(n), name="Task 1")
    task2 = asyncio.create_task(async_fib(n), name="Task 2")
    tasks = (task1, task2)

    # Wait for the first task to complete
    await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED)

    if task1.done():
        first_to_finish = "Task 1"
        task_result = task1.result()
    else:
        first_to_finish = "Task 2"
        task_result = task2.result()

    # Wait for all the tasks to complete
    await asyncio.wait(
        tasks,
        return_when=asyncio.ALL_COMPLETED)

    print(f"Fib({n}) result : {task_result} & First finished task : {first_to_finish}")


if __name__ == "__main__":
    asyncio.run(main())
