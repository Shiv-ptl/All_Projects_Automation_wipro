def make_it_equal(A, B):
    # write your logic here
    if "%" not in A:
        if A==B:
            return ""
        else:
            return -1

    precent_index = A.index("%")
    prefix = A[:precent_index]
    suffix =A[precent_index+1:]

    if len(B)<len(prefix)+len(suffix):
        return -1

    if not B.startswith(prefix):
        return -1

    if not B.endswith(suffix):
        return -1

    start = len(prefix)
    end = len(B) - len(suffix)

    return B[start:end]

# non editable starts here
if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    print(make_it_equal(A, B))
# non editable ends here