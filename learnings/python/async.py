import asyncio

async def task1():
    await asyncio.sleep(3)
    print("Task1 is done")
    
async def task2():
    await asyncio.sleep(1)
    print("Task2 is done")

async def task3():
    await asyncio.sleep(2)
    print("Task3 is done")
    
async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    t3 = asyncio.create_task(task3())
    await t1
    await t2
    await t3
    
asyncio.run(main())
        
    