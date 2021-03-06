
#Algorithm

#Following the above intuition, it seems intuitive to implement the solution with recursion.

#We define a recursive function called _wordBreak_topdown(s) which generates the results for the input string. Here are a few steps to implement our recursive function.

#First of all, as the base case of the recursion, when the input string is empty, the recursion would terminate. Note that we return a list of empty list as the result, rather than just an empty list.

#As the main body of the function, we run an iteration over all the prefixes of the input string. If the corresponding prefix happens to match a word in the dictionary, we then invoke recursively the function on the postfix.

#At the end of the iteration, we keep the results in the hashmap named memo with each valid postfix string as its key and the list of words that compose the prefix of as the value. For instance, for the postfix dogo, its corresponding entry in the hashmap would be memo["dogo"] = ["do", "go"].

#Finally, as the result, we return the entry of memo with the input string as the key. (The string itself is a postfix of the string itself.)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo=defaultdict(list)
        
       
        
        def cansplit(s):
          
            if not s:
                return [[]]
            
            if s in memo:
                return memo[s]
            
            for i in range(1,len(s)+1):
                pre = s[:i]
                if pre in wordDict:
                    suf = s[i:]
                    for w in cansplit(suf):
                        memo[s].append([pre]+ w)

            return memo[s]
        cansplit(s)
        return [" ".join(words) for words in memo[s]]
        
            
        