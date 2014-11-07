#! /usr/bin/env python

howMany = int(raw_input("How many numbers should I create?"))
nums = [1,1]

print(1)
print(1)

for i in range(2,howMany):
	nextFib = nums[-1] + nums[-2]
	nums.append(nextFib)
	print(nextFib)