from merge import merge

print merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]) 
#[2, 8, 16, 8, 4, 4, 8, 4, 2, 8, 0, 0, 0, 0, 0]
print merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]))
#[2, 8, 16, 8, 8, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0]
print merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4])))
#[2, 8, 16, 16, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0]
print merge(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]))))
#[2, 8, 32, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0]
print merge(merge(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4])))))
#[2, 8, 32, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0]
