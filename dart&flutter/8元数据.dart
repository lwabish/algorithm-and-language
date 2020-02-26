class Tele{
  @deprecated
  void activate(){
    turnOn();
  }
  void turnOn(){
    print('turn on');
  }
}


class Todo{
  final String who;
  final String what;

  const Todo(this.who,this.what);
}

/// Todo is meta
/// this is a document comment
/// 文档注释会被编译器保留
@Todo('seth','make this do something')
void doSomething(){
  print('do');
}


