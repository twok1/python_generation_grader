def hash_function(obj):
    obj = str(obj)
    temp1 = temp2 = 0
    for i in range(0, len(obj) // 2):
        temp1 += ord(obj[i]) * ord(obj[-i - 1])
    if len(obj) % 2:
        temp1 += ord(obj[i + 1])
    for k, v in enumerate(obj, start=1):
        if not k % 2:
            z = -1
        else:
            z = 1
        temp2 += ord(v) * k * z
    return (temp1 * temp2) % 123456791
    