package hashMap;

import (
  "fmt"
  "strings"
  "strconv"
)


func display(myHash map[rune]string) {
  for k, v := range myHash {
    fmt.Printf("%c -> %s, ", k, v)
  }
  fmt.Println()
}

func displayArr(myHash map[string][]string) {
  for k, strArr := range myHash {
    fmt.Printf("%s -> [", k)
    for _, s := range strArr {
      fmt.Printf("%s, ", s)
    }
    fmt.Printf("], ")
  }
  fmt.Println()
}

// Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
func Group(strs []string) (map[string][]string) {
  // fmt.Println(strs);
  groupHash := make(map[rune]string)
  anaHash := make(map[string][]string)
  gc := 0
  for _, s := range strs {
    // fmt.Println(s);
    // curLen := s.Length()
    diff := false
    group := "0"
    var prevgc string
    for iss, ss := range s {
      // if in same group, for each char, put in hash with the group number
      if gotCount, ok := groupHash[ss]; ok {
        // fmt.Println("ss is already there in groupHash")
        group = gotCount
        if iss == 0 {
          prevgc = group
        }


        // fmt.Println("prevgc, group: ", prevgc, group)
        if group == prevgc {
          // fmt.Println("the current char has been in other groups.")
          prevgc = group
          continue
        } else if strings.Contains(group, ";") {

          // check if the current group which were hoping for in the entire word,
          // is present in the groups arr
          groupsTheCharHasBeenIn := strings.Split(group, ";")
          lookup := make(map[string]struct{})
          for _, val := range groupsTheCharHasBeenIn {
            lookup[val] = struct{}{}
          }
          
          if strings.Contains(prevgc, ";") {
            // example: searching for 2;4 inside 1;2;3;4
            // look for the shorter groups arr, and look for that in other

            prevGcArr := strings.Split(prevgc, ";")

            // bool to check if, say, previous chars groups were 2;3;4
            // and current is 3;5
            // if current are 2;4 we narrow down the prevgc to 2;4
            consistentGroups := true
            if len(prevGcArr) > len(groupsTheCharHasBeenIn) {
              // search for groups in prevs
              prevLookup := make(map[string]struct{})
              for _, val := range prevGcArr {
                prevLookup[val] = struct{}{}
              }
              for _, tbs := range groupsTheCharHasBeenIn {
                if _, exists := prevLookup[tbs]; exists {

                } else {
                  consistentGroups = false
                }
              }
            } else {
              // search for prevs in groups
              for _, tbs := range prevGcArr {
                if _, exists := lookup[tbs]; exists {

                } else {
                  consistentGroups = false
                }
              }
            }
            if consistentGroups {
              // narrow down to lesser groups one
              if len(prevGcArr) > len(groupsTheCharHasBeenIn) {
                prevgc = group
              }
              continue 
            }
          } else if _, exists := lookup[prevgc]; exists {
            continue
          }
        } else if strings.Contains(prevgc, ";") {
          // the case where current char isnt in many groups but prev is distributed
          prevGcArr := strings.Split(prevgc, ";")
          prevLookup := make(map[string]struct{})
          for _, val := range prevGcArr {
            prevLookup[val] = struct{}{}
          }
          if _, exists := prevLookup[group]; exists {
            prevgc = group
            continue
          }
        }
      }

      diff = true;
      break
      
    }

    if diff {
      // fmt.Println("diff")
      gc++
      // fmt.Println("gc: ", gc)
      gcs := strconv.Itoa(gc)
      anaHash[gcs] = []string{s}
      for _, ss := range s {
        if _, ok := groupHash[ss]; ok {
          // curGroup, err := groupHash[ss]
          // curGroup++
          // groupHash[ss] = curGroup
          groupHash[ss] = groupHash[ss] + ";" + gcs
        } else {
          groupHash[ss] = gcs
        }
      }
    } else {
      if strings.Contains(prevgc, ";") {
        // if the entire word was found in two groups, check whose group-length is same
        finalGc := strings.Split(prevgc, ";")
        for _, g := range finalGc {
          if len(s) == len(anaHash[g][0]) {
            // found the group to which s belongs in!
            anaHash[g] = append(anaHash[g], s)
          }
        }
      } else {
        anaHash[prevgc] = append(anaHash[prevgc], s)
      }
    }

    // fmt.Printf("groupHash: ")
    // display(groupHash)
    // fmt.Printf("anaHash: ")
    // displayArr(anaHash)
  }
  return anaHash;
}

