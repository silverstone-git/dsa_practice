package stack

import "fmt"

type Stack struct {
  values []any
}

func (s *Stack) Push(val any) {
  s.values= append(s.values, val)
}

func (s *Stack) Pop() any {
  last := s.Length() - 1
  // fmt.Printf("last is: %d\n", last)
  if last < 0 {
    return nil;
  }
  tbr := s.values[last]
  s.values= s.values[:last]
  return tbr
}

func (s Stack) Length() int {
  return len(s.values)
}

func (s Stack) Print() {
  fmt.Println("{")
  for _, s := range s.values {
    fmt.Printf("\t")
    fmt.Println(s)
  }
  fmt.Println("}\n")
}
