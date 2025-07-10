import time
import asyncio

async def say_hi(name, delay):
  await asyncio.sleep(delay)
  print(f"hi {name} after {delay} seconds!")
  
async def main():
  await asyncio.gather(
    say_hi("apple", 1),
    say_hi("axe", 2),
    say_hi("morphling", 3),
    say_hi("clarity", 4),
    say_hi("tango", 5),
    say_hi("iron", 1),
    say_hi("pen", 2),
    say_hi("assassin", 3),
    say_hi("watermellon", 4),
    say_hi("change", 5),)
    
# asyncio.run(main())
# words = [
#   'apple',
#   'axe',
#   'morphling',
#   'clarity',
#   'tango',
#   'iron',
#   'pen',
#   'assassin',
#   'watermellon',
#   'change']

# x = -1

# while x < 10:
#   x += 1
#   time.sleep(1)
#   print(words[x])
