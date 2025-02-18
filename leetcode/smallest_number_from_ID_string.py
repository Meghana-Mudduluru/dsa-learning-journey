def smallestNumber(pattern: str) -> str:
    result = []  # Stores the final result
    numStack = []  # Stack to hold numbers temporarily

    for i in range(len(pattern) + 1):
        numStack.append(i + 1)  # Always push the next number onto the stack

        # When we see 'I' or reach the end, pop all elements from the stack
        if i == len(pattern) or pattern[i] == 'I':
            while numStack:
                result.append(str(numStack.pop()))

    return "".join(result)


# Example usage
pattern = "IDID"
print(smallestNumber(pattern))  # Output: "13254"