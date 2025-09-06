Q5. Trapping Rain Water (Medium)

Problem: Given elevation map [0,1,0,2,1,0,1,3,2,1,2,1], compute trapped rain.
Concepts: Two-pointer, Prefix/Suffix arrays.
Why: Common “Amazon-style” interview Q.
Hint: Water at index = min(max_left, max_right) - height[i].