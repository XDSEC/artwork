import math


def cal(x1, r, R):
    y1 = R + math.sqrt(r ** 2 - (x1 - R) ** 2)
    y2 = R - math.sqrt(r ** 2 - (x1 - R) ** 2)
    res = min(y1, y2)
    tl = 2 * r * math.asin((2 * (R - x1)) / 2 / r)
    return res, tl


def xdu(x1, r, R):
    # 上面一行字的起始点位于半径为r的劣弧上，指定x坐标为x1
    # 计算弧起始点和终止点的坐标，并计算弧长
    # R 为 1/2 view width，logo圆心坐标(R, R)
    res, tl = cal(x1, r, R)
    print(f'd="M {x1} {res:.2f} A {r} {r} 0 0 1 {2*R-x1},{res:.2f}"')
    print(f'textLength="{tl:.2f}"')


def isc(x1, r, R):
    # 上面一行字的起始点位于半径为r的优弧上，指定x坐标为x1
    # 计算弧起始点和终止点的坐标，并计算弧长
    # R 为 1/2 view width，logo圆心坐标(R, R)
    res, tl = cal(x1, r, R)
    tl = 2 * math.pi * r - tl
    print(f'd="M {x1} {res:.2f} A {r} {r} 0 1 0 {2*R-x1},{res:.2f}"')
    print(f'textLength="{tl:.2f}"')


xdu(93, 320, 400)
isc(45, 362, 400)
