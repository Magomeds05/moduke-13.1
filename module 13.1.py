import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    await asyncio.sleep(power)
    print(f'Силач {name} поднял {power} шар')
    print(f'Силач {name} закончил соревнования.')


async def  start_tournament():
    task1 = asyncio.create_task(start_strongman())
    task2 = asyncio.create_task(start_strongman())
    task3 = asyncio.create_task(start_strongman())
    await task1
    await task2
    await task3


asyncio.run(start_strongman('Pasha', 3))
asyncio.run(start_strongman('Denis', 4))
asyncio.run(start_strongman('Apollon', 5))