'''
Approach #1: Set [Accepted]
Intuition and Algorithm

To check whether words1[i] and words2[i] 
are similar, either they are the same word,
 or (words1[i], words2[i]) or (words2[i], words1[i]) appear in pairs.

To check whether (words1[i], words2[i]) appears in pairs quickly, 
we could put all such pairs into a Set structure.


Complexity Analysis:

Time Complexity: O(N+P), where NN is the maximum length of words1 and words2, 
and PP is the length of pairs.

Space Complexity: O(P), the size of pairs. 
Intermediate objects created in evaluating whether a pair of words 
are similar are created one at a time, so they don't take additional space.


'''




class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        
        for w1,w2 in zip(sentence1,sentence2):
            if w1==w2:
                continue
            if ([w1,w2] not in  similarPairs and [w2,w1] not in similarPairs):
                print('print([w1,w2])',[w1,w2])
                print('[w2,w1]',[w2,w1])
                return False
        
        return True