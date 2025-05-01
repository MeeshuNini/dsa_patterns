
# 📘 Sliding Window & Two Pointers — Final DSA Notes

---

## 1️⃣ Fixed Size Sliding Window

**Problem**: Max sum of subarray of size `k`

### 🔹 Approach

- Use two pointers to define a window of size `k`
- Calculate the sum of the first window
- Slide the window by one index at a time
- Update max sum on each slide

### ✅ Code

```python
def maxSum(arr, k):
    i = 0
    j = 0
    summ = 0
    maxi = float('-inf')
    
    while j < len(arr):
        summ += arr[j]
        
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            maxi = max(maxi, summ)
            summ -= arr[i]
            i += 1
            j += 1
    
    return maxi
```

---

## 2️⃣ Variable Size Sliding Window

**Problem**: Longest subarray with sum ≤ `k`

### 🔹 Approach2

- Use two pointers to create a dynamic window
- Expand `j` until the sum exceeds `k`
- Shrink window from `i` to reduce sum
- Track the max window length

### ✅ Code2

```python
def longestSubarraySumK(arr, k):
    i = 0
    j = 0
    summ = 0
    max_len = 0
    
    while j < len(arr):
        summ += arr[j]
        
        while summ > k:
            summ -= arr[i]
            i += 1
        
        if summ <= k:
            max_len = max(max_len, j - i + 1)
        
        j += 1
    
    return max_len
```

---

## 3️⃣ Two Pointers – Opposite Ends

**Problem**: Pair sum in sorted array

### 🔹 Approach3

- Initialize pointers at start and end
- Move inward based on current sum
- Return True if target found

### ✅ Code3

```python
def hasPairSum(arr, target):
    i = 0
    j = len(arr) - 1
    
    while i < j:
        summ = arr[i] + arr[j]
        if summ == target:
            return True
        elif summ < target:
            i += 1
        else:
            j -= 1
    
    return False
```

---

## 4️⃣ Two Pointers – Same Direction

**Problem**: Count subarrays with at most `k` distinct elements

### 🔹 Approach4

- Use a hashmap to track frequency
- Shrink window when distinct elements > `k`
- Count all valid subarrays ending at `j`

### ✅ Code4

```python
from collections import defaultdict

def countAtMostK(arr, k):
    i = 0
    j = 0
    freq = defaultdict(int)
    count = 0
    
    while j < len(arr):
        freq[arr[j]] += 1
        
        while len(freq) > k:
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                del freq[arr[i]]
            i += 1
        
        count += j - i + 1
        j += 1
    
    return count
```

**💡 Tip**: To find subarrays with **exactly `k` distinct elements**:

```python
countExactlyK = countAtMostK(arr, k) - countAtMostK(arr, k - 1)
```

---
