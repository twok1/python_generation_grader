def limited_hash(left, right, hash_function=hash):
    def wrap(obj):
        result = hash_function(obj)
        if result > right:
            result = left + (result - right - 1) % (right - left + 1)
        if result < left:
            result = right - (left - result - 1) % (right - left + 1)
        return result
    return wrap
