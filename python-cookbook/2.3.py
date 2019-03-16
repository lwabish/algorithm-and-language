from fnmatch import fnmatch, fnmatchcase
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

# fnmatch大小写规则与操作系统一致，fnmatchcase大小写与参数一致
print([file for file in names if fnmatch(file, 'Dat*.csv')])
