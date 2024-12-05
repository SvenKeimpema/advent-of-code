from reader import FileReader
import math

if __name__ == "__main__":
    data = FileReader.read("day5/data.txt")
    next_idx = 0
    rules: dict[int, list[int]] = {}

    for idx, line in enumerate(data.split("\n")):
        if len(line) == 0:
            next_idx = idx+1
            break

        num1, num2 = list(map(int, line.split("|")))
        if num1 in rules:
            rules[num1].append(num2)
        else:
            rules[num1] = [num2]

    res = 0
    for idx, line in enumerate(data.split("\n")[next_idx:]):
        nums = list(map(int, line.split(",")))
        success = True
        for j in range(1, len(nums)):
            if nums[j-1] not in rules or nums[j] not in rules[nums[j-1]]:
                success = False
                break

        if success:
            res += nums[len(nums)//2]
    print(res)