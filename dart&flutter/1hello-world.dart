main() {
  // hello world
  print('hello world');

  // 变量定义 var类型推断或类型预定义
  var s = 'string1';
  String s1 = 'string2';
  int i1 = 123;
  double f1 = 1.23;
  print(s + s1);
  print(i1);
  print(f1);

  // 常量
  const PI1 = 3.14;
  final PI2 = 3.14;
  print(PI1 + PI2);

  // const此时不能用（惰性赋值）
  final C1 = new DateTime.now();
  print(C1);
}
