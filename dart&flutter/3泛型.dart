abstract class ObjectCache{
  Object getByKey(String key);
  void setByKey(String key, Object value);
}

abstract class StringCache{
  String getByKey(String key);
  void setByKey(String key, String value);
}

// .....

abstract class Cache<T>{
  T getByKey(String key);
  void setByKey(String key, T value);
}

class Person{
  String firstName;

  Person.fromJson(Map data){
    print('in Person');
  }
}

class Employee extends Person{
  Employee.fromJson(Map data): super.fromJson(data){
    print('in Employee');
  }
}

class Foo<T extends Person>{
  String toString()=>"instance of 'Foo<$T>'";
}

T first<T>(List<T> ts){
  T tmp =ts[0];
  return tmp;
}

void main(){
  var names = List<String>();
  names.addAll(['a','b']);
  // names.add(42);

  names = <String>['a','b','c'];
  var pages = <String, String>{
      'a':'b',
  };

  var nameSet = Set<String>.from(names);

  var views = Map<int,String>();

  print(names is List<String>);

  var personFoo = Foo<Person>();
  var employeeFoo = Foo<Employee>();

  var foo = Foo();
  print(foo);
}