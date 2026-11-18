x = 512
y = 750
v_sx = 80
i_ = v_sx * 2 ** 13 / x / y
v_or = v_sx * 165 / 100
i = v_or * 2 ** 13 / x / y
print(i, i_)