
#Algorithm

#Do the pre-processing on the given wordList and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.

#Push a tuple containing the beginWord and 1 in a queue. The 1 represents the level number of a node. We have to return the level of the endNode as that would represent the shortest sequence/distance from the beginWord.

#To prevent cycles, use a visited dictionary.

#While the queue has elements, get the front element of the queue. Let's call this word as current_word.

#Find all the generic transformations of the current_word and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the all_combo_dict.

#The list of words we get from all_combo_dict are all the words which have a common intermediate state with the current_word. These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.

#Hence, for each word in this list of intermediate words, append (word, level + 1) into the queue where level is the level for the current_word.

#Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.

from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not endWord or endWord not in wordList:
            return 0
        
    
        wordcollection = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                wordcollection[word[:j]+"*"+word[j+1:]].append(word)
        #print(wordcollection)        
        q = deque()
        q.append([beginWord,1])
       
        vist={beginWord:True}
        while q:
            word,level = q.popleft()
            for i in range(len(word)):
                matchword = word[:i]+"*"+word[i+1:]
               # print(matchword)
                for resword in wordcollection[matchword]:
                    if resword==endWord:
                        return level+1
                    if resword not in vist:
                        vist[word]=True
                        q.append([resword,level+1])
                #clear the wordcollection we have already met
                wordcollection[matchword]=[]
        return 0
                
                
            
        
        
       