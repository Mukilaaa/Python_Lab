from collections import deque

def is_palindrome(word):
    n = len(word)
    dq = deque()

    # Step 3: Push first half into deque
    for i in range(n // 2):
        dq.append(word[i])

    # Step 4: If odd length, skip the middle character
    if n % 2 != 0:
        mid = (n // 2) + 1
    else:
        mid = n // 2

    # Step 5–7: Compare remaining characters with deque (stack behavior)
    for i in range(mid, n):
        if dq.pop() != word[i]:
            return False
    return True


# -------- Driver Code --------
word = input("Enter a word/phrase: ").replace(" ", "").lower() # ignoring spaces & case
if is_palindrome(word):
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")
