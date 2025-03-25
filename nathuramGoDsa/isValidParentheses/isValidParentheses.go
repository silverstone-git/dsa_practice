package isValidParentheses

func IsValidParentheses(str1 string) bool {

  openStack := []int {};
  parens := map[string]string {
    "[": "]",
    "{": "}", 
    "(": ")",
  };
  parensClose := map[string]bool {
    "]": true,
    "}": true,
    ")": true,
  } 

  for i, strByte := range str1 {

    str := string(strByte);

    // fmt.Printf("%d -> %c\n", i, strByte);

    if _, ok:= parens[str]; ok {
      // the character is an opener
      openStack= append(openStack, i)
      continue;
    }


    if _, ok := parensClose[str]; ok {
      // the char is a closer
      stackPointer := len(openStack);
      // check if stack peek 's complement is the char
      if parens[string(str1[openStack[stackPointer - 1]])] == str {

        // clean closing
        openStack= openStack[:stackPointer-1]

      } else {

        // what are you trying to close here?
        break;

      }
    }
    // fmt.Println(openStack);
  }

  if len(openStack) == 0 {
    return true;
  } else {
    return false;
  }
}

// func main() {
// }
