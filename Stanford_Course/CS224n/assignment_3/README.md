# Assignment 3.

## The solution to assignment_3.
1. A window into NER.
(a) (i) Waston.
(ii) Because if just use center word, it has ambiguous possibility.
(iii) One feature is the word is capital or not, another feature is whether the word is the start of sentence or not.

(b) (i) [1, (2w+1)*h(t)] - e(t)
	[(2w+1)*h(t), H] - W
	[H, C] - U
    (ii) O(T*((2w+1)*h(t)*H+(2w+1)*V*H)+H*C)
    