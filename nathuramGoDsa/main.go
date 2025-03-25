package main;

import (
  "fmt"
  // "nathuramGoDsa/isValidParentheses"
  // "nathuramGoDsa/stack"
  "nathuramGoDsa/queue"
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

  q := qUsingStacks.Queue{}
  q.Enqueue(1);
  q.Enqueue(2);
  q.Enqueue(3);
  q.Enqueue(4);

  fmt.Println(q.Dequeue());
  fmt.Println(q.Dequeue());
  fmt.Println(q.Dequeue());
  fmt.Println(q.Dequeue());
  fmt.Println(q.Dequeue());
  fmt.Println(q.Dequeue());
}
