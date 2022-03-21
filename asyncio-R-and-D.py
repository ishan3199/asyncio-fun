import asyncio
import time

async def coro():
    print("This is the first message from coro")
    await asyncio.sleep(2)
    print("This is the second message from coro")

    pass



async def coro2():
    print("This is the first message from coro2")
    await asyncio.sleep(2)
    print("This is the second message from coro2")

    pass


#we have used asyncio.gather to serve the two coroutines concurrently.

async def main():
    await asyncio.gather(coro(),coro2())

# You can use this below
#1)

#a=asyncio.get_event_loop()
#a.run_until_complete(main())

# OR you can use below simple
#2)

asyncio.run(main())



