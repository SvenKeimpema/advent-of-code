from reader import FileReader

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
            continue
        
        occ = {}
        for n in range(len(nums)):
            other_nums = nums[:n] + nums[n+1 :]
            c = 0
            for o_num in other_nums:
                if nums[n] in rules and o_num in rules[nums[n]]:
                    c += 1
            occ[nums[n]] = c

        sort_occ = list({k: v for k, v in sorted(occ.items(), key=lambda item: item[1])}.keys())
        res += sort_occ[len(sort_occ)//2]
    print(res)
