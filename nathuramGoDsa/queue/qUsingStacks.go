package qUsingStacks

import (
  "nathuramGoDsa/stack"
  // "fmt"
)

type Queue struct {
  val stack.Stack
}

func (q *Queue) Enqueue(el any) {
  tempStack := stack.Stack{}
  qlen := q.val.Length()
  for i := 0; i < qlen; i ++ {
    tempStack.Push(q.val.Pop())
  }
  tempStack.Push(el)

  // fmt.Println("upended the queue into temp, and added an element:")
  // tempStack.Print()

  qlen= tempStack.Length()
  for i := 0; i < qlen; i ++ {
    q.val.Push(tempStack.Pop())
  }

  // fmt.Println("new q val")
  // q.val.Print()
}

func (q *Queue) Dequeue() any {
  return q.val.Pop()
}
