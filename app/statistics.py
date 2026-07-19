from collections import Counter

request_counter = Counter()

def record_request(
    int1: int,
    int2: int,
    limit: int,
    str1: str,
    str2: str,
):
    key = (int1, int2, limit, str1, str2)
    request_counter[key] += 1

def get_most_frequent():
    if not request_counter:
        return None 

    key, count = request_counter.most_common(1)[0]

    return {
        "int1": key[0],
        "int2": key[1],
        "limit": key[2],
        "str1": key[3],
        "str2": key[4],
        "hits": count,
    }

