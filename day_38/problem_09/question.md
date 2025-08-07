Filter Unopened Snaps
Find snaps that are still unopened.

Problem:
Given a list of snaps (each with opened: True/False), return the unopened ones.
snaps = [
  {"from": "zoe", "opened": True},
  {"from": "arya", "opened": False},
  {"from": "luke", "opened": False}
]

Function: get_unopened_snaps(snaps)
Output: ['arya', 'luke']