import 'dart:async';

Future<String> lookUpVersion() async=>  '1.0.0';

Future checkVersion() async{
  var version = await lookUpVersion();
  print(version);
}

void main() async{
  var version;
  try{
    version = await checkVersion();
  }catch(e){
    print(e);
    return ;
  }
  print(version);

  var s = Stream.fromIterable([1,2,3]);
  await for (var v in s){
    print(v);
  }

}