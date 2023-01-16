import sys
# names = ['明', '红', '白', '新', '李', '张']
# cf = {'00'+str(i+1): '小'+names[i] for i in range(6)}
cf = {'001': '小明', '002': '小红', '003': '小白',
      '004': '小新', '005': '小李', '006': '小张'}


for line in sys.stdin:
    a = line.split()[0]
    print(cf[a])
