import math


def cal(x1, r, R):
    # 计算弧起始点的纵坐标，并计算劣弧弧长
    # 1_
    # ( )
    # 2- 两个纵坐标
    # R 为 1/2 view width，logo圆心坐标(R, R)
    y1 = R + math.sqrt(r ** 2 - (x1 - R) ** 2)
    y2 = R - math.sqrt(r ** 2 - (x1 - R) ** 2)
    tl = 2 * r * math.asin((2 * (R - x1)) / 2 / r)
    return y1, y2, tl


def xdu(x1, r, R):
    # 上面一行字的起始点位于半径为r的劣弧上，指定x坐标为x1
    y1, y2, tl = cal(x1, r, R)
    res = min(y1, y2)
    print(f'd="M {x1} {res:.2f} A {r} {r} 0 0 1 {2*R-x1},{res:.2f}"')
    print(f'textLength="{tl:.2f}"')


def isc(x1, r, R, is_minor_arc=False):
    # 下面一行字的起始点位于半径为r的优弧上，指定x坐标为x1
    y1, y2, tl = cal(x1, r, R)
    if not is_minor_arc:
        tl = 2 * math.pi * r - tl
        res = min(y1, y2)
    else:
        res = max(y1, y2)
    print(f'd="M {x1} {res:.2f} A {r} {r} 0 1 0 {2*R-x1},{res:.2f}"')
    print(f'textLength="{tl:.2f}"')


xdu(93, 320, 400)
isc(45, 362, 400)
xdu(154, 280, 400)
isc(62, 354, 400)
