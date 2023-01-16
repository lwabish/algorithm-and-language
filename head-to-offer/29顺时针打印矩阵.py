from my_data_structure import generate_matrix, print_matrix
import string

tc = [
    # 由25个字母组成的5行5列矩阵
    generate_matrix(string.ascii_lowercase[:25], 5, 5),
    # 单行矩阵
    generate_matrix('abcde', 1, 5),
    # 单列矩阵
    generate_matrix('abcde', 5, 1),
    # 单元素矩阵
    generate_matrix('1', 1, 1)
]


# 书上思路：分析循环规律，由外到内一圈一圈打印
# 我的实现思路：走迷宫。生成一个可行矩阵，根据每个点的可行集合，结合优先级，决定下一步走到哪个点。知道可行矩阵不再有可行的点。
def main(matrix):
    x = len(matrix)
    y = len(matrix[0])
    print_matrix(matrix)

    def generate_avai_matrix(x, y):
        """
        根据要打印矩阵的行数列数，生成可行矩阵。\n
        0代表不能进入的点，1代表可以进入的点。
        """
        avai_matrix = []
        for i in range(x + 2):
            avai_matrix.append([])
            for j in range(y + 2):
                if i in (0, x+1) or j in (0, y+1):
                    avai_matrix[i].append(0)
                else:
                    avai_matrix[i].append(1)
        return avai_matrix
    avai_matrix = generate_avai_matrix(x, y)

    def check_avai_steps(x, y):
        """
        输入当前点的坐标，检查在该点可以进入的下一个点有哪些可能\n
        ;返回一个四元素list：[]，顺序为上下左右，1代表可进入，0代表不可进入\n
        """
        # 由于可行矩阵在原矩阵的四周加了一圈，所以坐标需要转换
        # 原矩阵的坐标xy分别加一即为可行矩阵里的坐标
        res = [0]*4
        avai_x, avai_y = x + 1, y + 1
        # 检查上方是否可行
        if avai_matrix[avai_x - 1][avai_y]:
            res[0] = 1
        # 下
        if avai_matrix[avai_x + 1][avai_y]:
            res[1] = 1
        # 左
        if avai_matrix[avai_x][avai_y-1]:
            res[2] = 1
        # 右
        if avai_matrix[avai_x][avai_y+1]:
            res[3] = 1
        return res
    # print(check_avai_steps(0, 0))

    # 初始化当前点以及是否还有下一个点可以走的标志
    this_x, this_y = 0, 0
    is_end = False

    # 开始走
    while not is_end:
        # 主要任务，打印出当前点
        print(matrix[this_x][this_y], end=',')

        # 维护当前点在可行矩阵里的值为0
        avai_matrix[this_x + 1][this_y + 1] = 0

        # 得到当前点的可行集合，四元素分别代表上下左右
        avails = check_avai_steps(this_x, this_y)

        # 有两个1说明有两个方向可走，说明当前点不在矩阵的角点。根据顺时针的要求
        # 当有两个方向可以走的时候，自然就可以确定下一步往哪个方向走。
        if sum(avails) == 2:
            # 下右选右
            if avails[1] and avails[3]:
                this_y += 1
            # 下左选下
            elif avails[1] and avails[2]:
                this_x += 1
            # 上左选左
            elif avails[0] and avails[2]:
                this_y -= 1
            # 上右选上
            elif avails[0] and avails[3]:
                this_x -= 1
        # 只有一个方向可走，说明现在是在四个角
        elif sum(avails) == 1:
            if avails[0]:
                this_x -= 1
            elif avails[1]:
                this_x += 1
            elif avails[2]:
                this_y -= 1
            elif avails[3]:
                this_y += 1
        # 可行集合为空，说明已经打印完成，退出。
        else:
            is_end = True
    # print_matrix(avai_matrix)


if __name__ == '__main__':
    for i in tc:
        main(i)
