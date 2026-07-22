# DSA-From-Scratch

Classic data structures built from a blank file in Python. No AI writes the code here. The point is fluency, not output: every method gets traced by hand, every bug gets found by reasoning, and every operation gets a complexity justification before moving on.

## Implemented

- **Dynamic Array** (`dynamic_array.py`) — array-backed list with doubling resize.
  Append is amortized O(1), worst case O(n) on resize. Index access is O(1) via contiguous memory. Pop from the end is O(1); pop from the front would be O(n) since everything shifts.

## Up Next

- Singly linked list
- Hash map with chaining
- Array vs linked list tradeoffs writeup

## Why

I'm a CS student at Clemson preparing for cloud engineering internships. I knew what these structures were conceptually but couldn't build them or defend the tradeoffs out loud. This repo is me fixing that, one structure at a time.
