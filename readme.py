# ================================= Question 1 =================================
sentences = [
    "Hello World",
    "Hello World Hello World",
    "Hello World Hello World Hello World",
]
# should return 6 since the longest sentence has 6 words

# ================================= Question 2 =================================
nums = [1, 2, 3, 4, 5]
# should return False since there is no duplicate in the given array
nums = [1, 2, 3, 4, 5, 5]
# should return True since there is a duplicate in the given array

# ================================= Question 3 =================================
# find a way to check the index of x value inside the given array
arr = [2, 3, 4, 10, 40]
x = 10

# =================================  =================================
nums = [2, 7, 11, 15], target = 9
output = [0,1]

nums = [1,4,7,9], target = 11
# create a function to do this job

# ================================= Question 5 =================================
Region               Month                     Sales
-----------------------  ---------------- ---------------------  
Canada                Jan                       10
Canada                Feb                       5
Canada                Mar                       3
Canada                June                      10
Canada                July                      13
# result
Region               Month                   SalesYTD
-----------------------  ---------------- ---------------------  
Canada                Jan                       10
Canada                Feb                       15
Canada                Mar                       18
Canada                Apr                       18
Canada                May                       18
Canada                June                      28
Canada                July                      41


# ================================= Question 6 =================================
Region               Month                     Sales            UpdateAt
-----------------------  ---------------- ---------------------  
Canada                Jan                       10              2024-08-01
Canada                Jan                       10              2024-08-03
Canada                Feb                       5               2024-08-03
Canada                Mar                       3               2024-08-03
Canada                Mar                       3               2024-08-01
Canada                June                      10              2024-08-03
Canada                July                      13              2024-08-03

Region               Month                     Sales            UpdateAt
-----------------------  ---------------- ---------------------  
Canada                Jan                       10              2024-08-03
Canada                Feb                       5               2024-08-03
Canada                Mar                       3               2024-08-03
Canada                June                      10              2024-08-03
Canada                July                      13              2024-08-03

# ================================= Question 7 =================================
# table a
Coupon      Value
01TOPS123     1
02TOPS124     2
03CFR1250     3

# table b
CouponGroup         ExpireDate
TOPS                2024-01-01
CFR                 2025-01-01

# expected result
Coupon      ExpireDate
01TOPS123     2024-01-01
02TOPS124     2024-01-01
03CFR125      2025-01-01