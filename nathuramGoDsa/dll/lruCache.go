package lruCache;

import "fmt"

type Node struct {
  Key any;
  Next  *Node;
  Prev  *Node;
}

type Lru struct {
  Head *Node;
  Tail *Node;
  Cache map[any]any;
  Limit int;
}

func MakeLru(limit int) (*Lru) {
  head := Node{}
  tail := Node{Prev: &head}
  head.Next= &tail
  
  return &Lru{
    Head: &head,
    Tail: &tail,
    Cache: map[any]any{},
    Limit: limit,
  }
}

func (l *Lru) Get(key any) (any) {
  // the cache must have fix size, evicts if overflown
  // lru: put values to those keys
  // (updated / inserted) and evict the last node, replacing with the newest
  // at the head

  if val, ok := l.Cache[key]; ok {
    // key is there in cache
    return val;
  }

  // not found case
  return -1;
}

func (l *Lru) Set(key any, val any) {
  // see if the head is null

  if l.Head.Key == nil {
    node := Node{Key: key}
    l.Head = &node
    l.Tail = &node
    l.Cache[key] = val
    return;
  }

  if _, ok := l.Cache[key]; ok {

    // already there, update the value, refresh and return.
    l.Cache[key] = val;
    l.refresh(key);
  } else {

    // wasnt there, check if overflowing, put it afresh
    l.Cache[key] = val;
    if len(l.Cache) > l.Limit {
      // overflow! pop the oldest, and push to front
      fmt.Println("overfloww!!")
      l.evict()
    }
    l.add(key)
  }

  // fmt.Println("setting done:")
  // temp := l.Head
  // for temp != nil && temp.Key != nil {
  //   fmt.Println(temp)
  //   temp = temp.Next
  // }
}

func (l *Lru) refresh(key any) (int) {
  // find the key and put it at front
  temp := l.Head
  for temp.Key != key && temp.Key != nil {
    temp = temp.Next;
  }

  if temp.Key == key {
    // found it, refreshing...

    if temp.Prev != nil {
      // the refreshee is not at the start
      temp.Prev.Next = temp.Next
    } else {
      // no need of refreshing if its already at the start
      return 0;
    }

    if temp.Next != nil {
      // the refreshee is not at the end either
      temp.Next.Prev = temp.Prev
    }


    temp.Next = l.Head
    l.Head.Prev = temp
    l.Head = temp
    l.Head.Prev = nil

    return 0;
  } else {
    return 1;
  }

}

func (l *Lru) add(key any) (int) {
  node := Node{Key: key}

  node.Next = l.Head
  l.Head.Prev = &node
  l.Head = &node

  return 0;
}

func (l Lru) Display() {
  temp := l.Head
  for temp != nil && temp.Key != nil {
    fmt.Print(temp.Key, "-> ")
    fmt.Println(l.Cache[temp.Key])
    temp = temp.Next
  }
}

func (l *Lru) evict() (int) {
  delete(l.Cache, l.Tail.Key)
  l.Tail.Prev.Next = nil;
  l.Tail.Prev = nil
  l.Tail = l.Tail.Prev

  return 0;
}
