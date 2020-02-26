import 'dart:math';

class Point{
  num x,y;
  num distanceFromOrigin;

  Point(this.x, this.y): distanceFromOrigin = sqrt(x*x+y*y);

  Point.origin():this(0,0);

  Point.fromJson(Map<String,num> json):this(json['x'],json['y']);

  Point.withAssert(this.x, this.y):assert(x>=0),distanceFromOrigin=sqrt(x*x+y*y);

  num distanceTo(Point other){
    var dx = x -other.x;
    var dy = y -other.y;
    return sqrt(dx*dx+dy*dy);
  }

  @override
  String toString() => 'Point($x, $y)';
}

class ImmutablePoint{
  final num x,y;
  const ImmutablePoint(this.x,this.y);
  static final origin=const ImmutablePoint(0,0);
}

class Person{
  String firstName;
  Person.fromJson(Map data){
    print('in Person');
  }
}

class Employee extends Person{
  Employee.fromJson(Map data):super.fromJson(data){
    print('in Employee');
  }
}

class Logger{
  final String name;
  bool mute = false; 

  static final _cache = <String, Logger>{};

  factory Logger(String name){
    if (_cache.containsKey(name)){
      return _cache[name];
    }else{
      final logger = Logger._internel(name);
      _cache[name] = logger;
      return logger;
    }
  }


  // 命名构造函数
  Logger._internel(this.name);

  void log(String msg){
    if(!mute)print(msg);
  }
}

class Rectangle{
  num left, top, width, height;

  Rectangle(this.left, this.top, this.width, this.height);
  
  num get right => left+width;
  set right(num value)=>left=value-width;
  num get bottom =>top+height;
  set bottom(num value)=>top = value-height;
}

abstract class Doer{
  void doSomething();
}

class EffectiveDoer extends Doer{
  void doSomething(){
    print('do something');
  }
}

class Person1{
  final _name;
  Person1(this._name);
  String greet(String who)=>'Hello,$who. I am $_name';
}

class Impostor implements Person1{
  get _name=>'';
  String greet(String who)=>'Hi $who.Do you know who I am?';
}

String greetBob(Person1 person)=>person.greet('Bob');

class Television{
  void turnOn(){
    print('tv on');
  }
}

class SmartTelevision extends Television{
  @override
  void turnOn(){
    super.turnOn();
    print('upgrade app');
  }
}


class Vector{
  final int x,y;
  Vector(this.x,this.y);

  Vector operator +(Vector v) =>Vector(x+v.x,y+v.y);
  Vector operator -(Vector v) =>Vector(x-v.x,y-v.y);

  @override
  int get hashCode{
    int result=17;
    result=37*result+x.hashCode;
    result = 37*result+y.hashCode;
    return result;
  }

  @override
  bool operator ==(dynamic other){
    if (other is! Vector)return false;
    Vector vector = other;
    return (vector.x ==x&&vector.y==y);
  }
}

class A {
  @override
  void noSuchMethod(Invocation invocation){
    print('you tried to use a non-existent member'+'${invocation.memberName}');
  }
}


class CallableClass{
  call(String a) => '$a';
}


void main(){
    var p = Point(2,2);
    p.y = 3;
     
    assert(p.y==3);

    num distance = p.distanceTo(Point(4,4));

    // p不为null时
    p?.y =4;

    var p1 =Point(2,2);
    var p2 = Point.fromJson({'x':1,'y':2});
    print(p2);

    var ip = const ImmutablePoint(2, 2);

    var a=const ImmutablePoint(1, 1);
    var b = const ImmutablePoint(1, 1);
    assert(identical(a, b));

    const pointAndLine = {
      'point': [ImmutablePoint(0, 0)],
      'line': [ImmutablePoint(1, 10),ImmutablePoint(-2, 11)],
    };

    a = const ImmutablePoint(1, 1);
    b = ImmutablePoint(1, 1);
    assert(!identical(a, b));

    print('the type of a is ${a.runtimeType}');

    var emp = Employee.fromJson({});

    if (emp is Person){
      emp.firstName='Bob';
    }
    (emp as Person).firstName = 'Bob';

    var logger = Logger('UI');
    logger.log('button clicked');

    var rect = Rectangle(3,4,20,15);
    assert(rect.left==3);
    rect.right = 12;
    assert(rect.left==-8);

    print(greetBob(Person1('kathy')));
    print(greetBob(Impostor()));

    final v = Vector(2,3);
    final w = Vector(2,2);
    assert(v+w==Vector(4,5));
    assert(v-w ==Vector(0,1));

    dynamic a1=A();
    a1.xxx();

}