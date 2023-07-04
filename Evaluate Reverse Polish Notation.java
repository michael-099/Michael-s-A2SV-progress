
class Solution {
 public
  int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();
     int x, y, z,a,b;
    int o = 0;
    for (int i = 0; i < tokens.length; i++) {
      if (!tokens[i].equals("+") && !tokens[i].equals("-") &&
          !tokens[i].equals("*") && !tokens[i].equals("/")) {
        stack.push(Integer.parseInt(tokens[i]));
      }
   
    
      if (tokens[i].equals ("+")) {
     
          a = stack.peek();
        stack.pop();
        b = stack.peek();
        stack.pop();
        o = a + b;
        stack.push(o);
      }
      if (tokens[i].equals("-")) {
        a = stack.peek();
        stack.pop();
        b = stack.peek();
        stack.pop();
        o = b - a;
        stack.push(o);
      }
      if (tokens[i].equals( "*")) {
        a = stack.peek();
        stack.pop();
        b = stack.peek();
        stack.pop();
        o = a * b;
        stack.push(o);
      }
      if (tokens[i].equals ("/")) {
        a = stack.peek();
        stack.pop();
        b = stack.peek();
        stack.pop();
        o = b / a;
        stack.push(o);
      }
    }
   
    return stack.peek();
  }
}
     
     
