card_num = int(input())
charges = list()
for i in range(card_num):
    charges.append([int(i) for i in input().split()])

this_guess = 0
paid = []
# 贪心，从第一位开始猜
while this_guess < card_num:
    delta_min_charge = float('inf')
    # for i in range(this_guess+1, card_num):
    #     if charges[this_guess][i] - charges[this_guess+1][i]
