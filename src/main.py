# A simple program on the Collatz Conjecture.

import argparse
import time

def calc(num: int):
   if num % 2 == 0:
       return (num // 2)
   elif num % 2 == 1:
       return (num * 3 + 1)
   else:
        return num
        
def is_even(num):
    if num % 2 == 0:
        return True 
    elif num % 2 == 1:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            # prog="Collatz Conjecture", 
            description="A simple program on the Collatz Conjecture.",
            epilog="Author: python128")
    parser.add_argument('num', type=int, help="An integer to start with.")
    parser.add_argument('-q',"--quiet", help="Stop showing numbers.", action="store_true")
    args = parser.parse_args()
    
    
    max_val = []
    num = args.num
    print(f"{num}")
    ans = calc(num)
    if not args.quiet:
        if is_even(ans): print(f"Even: {ans}")
        else: print(f"Odd: \033[1m{ans}\033[0m")
    step = 1
    while int(ans) != 1:
        ans = calc(ans)
        max_val.append(ans)
        
        if not args.quiet:
            parity = is_even(ans)
            if parity:
                print(f"Even: {ans}")
            else:
                print(f"Odd: \033[1m{ans}\033[0m")
        
            if step <= 5:
                time.sleep(1)
            elif step <= 10:
                time.sleep(0.5)
            elif step <= 15:
                time.sleep(0.2)
            elif step <= 20:
                time.sleep(0.1)
            elif step <= 25:
                time.sleep(0.05)
            elif step <= 30:
                time.sleep(0.02)
            else:
                time.sleep(0.01)
        step += 1
        
    print(f"\nStarting Number: {num}")
    print(f"Total Steps taken: {step}")
    print(f"Maximum Value in the sequence is: {max(max_val)}")
    
