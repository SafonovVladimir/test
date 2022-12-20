import sys


def comp(array1, array2) -> bool:
    new_array1 = []
    # print(array1, file=sys.stdout)
    # print(array2, file=sys.stdout)
    for i in array1:
        if i < 0:
            new_array1.append(i * (-1))
    if array1 == [] and array2 == []:
        return True
    if array1 is None or array2 is None:
        return False
    if len(array1) == 0 or len(array2) == 0:
        return False
    if len(array1) != len(array2):
        return False
    ar1 = sorted(new_array1)
    ar2 = sorted(array2)
    for i in range(len(ar1)):
        if ar1[i] ** ar1[i] != ar2[i]:
        # if pow(ar1[i], ar1[i]) != ar2[i]:
            return False
    else:
        return True
    # else:
    #     return False


# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# a1 = []
# a2 = []
a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a1, a2))
