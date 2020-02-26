// 同步生成器
Iterable<int> naturalsTo(int n) sync*{
  int k = 0;
  while(k<n)yield k++;
}

// 异步生成器
Stream<int> asyncNaturalsTo(int n)async*{
  int k=0;
  while(k<n)yield k++;
}

Iterable<int> naturalsDownFrom(int n)sync*{
  if(n>0){
    yield n;
    yield* naturalsDownFrom(n-1);
  }
}


void main()async{
  for (var v in naturalsTo(3)){
    print(v);
  }

  await for(var v in asyncNaturalsTo(3)){
    print(v);
  }
}