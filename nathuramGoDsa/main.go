package main;

import (
  "fmt"
  // "nathuramGoDsa/isValidParentheses"
  // "nathuramGoDsa/stack"
  // "nathuramGoDsa/queue"
  "nathuramGoDsa/dll"
)


func main() {
  // s := stack.Stack{}
  //
  // s.Push(5)
  // s.Push(6)
  // s.Push(7)
  //
  // fmt.Println(s.Pop())
  // fmt.Println(s.Pop())
  // fmt.Println(s.Pop())
  // fmt.Println(s.Pop())
  // fmt.Println(s.Pop())
  // fmt.Println(s.Pop())
  // fmt.Println(s.Pop())
  // EXPECTED OUTPUT :: 
  // 7
  // 6
  // 5
  // <nil>
  // <nil>
  // <nil>
  // <nil>
  // <nil>

  // fmt.Println(isValidParentheses.IsValidParentheses("[fjsgh{(oi)}d())[f]j]")); // false
  // fmt.Println(isValidParentheses.IsValidParentheses("[fjsgh{(oi)}d()[f]j]")); // true

  // IMPLEMENT QUEUE using stack

  // q := qUsingStacks.Queue{}
  // q.Enqueue(1);
  // q.Enqueue(2);
  // q.Enqueue(3);
  // q.Enqueue(4);
  //
  // fmt.Println(q.Dequeue());
  // fmt.Println(q.Dequeue());
  // fmt.Println(q.Dequeue());
  // fmt.Println(q.Dequeue());
  // fmt.Println(q.Dequeue());
  // fmt.Println(q.Dequeue());


  l := lruCache.MakeLru(5);

  // fmt.Println(l.Get(99)); // should give -1
  // l.Display()


  l.Set("delhi", "india")
  l.Display()
  fmt.Println("geto of delhi: ")
  fmt.Println(l.Get("delhi")); // should give india
  
  l.Set("washington", "usa")
  l.Set("london", "uk")
  l.Set("beijing", "china")
  // fmt.Println("after setting")
  // l.Display()

  fmt.Println("\nupdating..")
  l.Set("beijing", "prc")
  l.Display()

  fmt.Println("\nupdating..")
  l.Set("london", "england")
  l.Display()


  fmt.Println("\nget of beijing: ")
  fmt.Println(l.Get("beijing")); // should give prc

  fmt.Println("\noverflowing..")
  l.Set("madrid", "spain")
  l.Set("paris", "france")
  l.Display()

  fmt.Println("\nget of delhi after overflow:")
  fmt.Println(l.Get("delhi")) // should give -1
}
