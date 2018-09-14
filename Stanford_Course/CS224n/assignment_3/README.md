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

(d) (ii) The first disadvantage is the window-based model would lose the information out of the window. The second one is that the window-based model does’t consider the sequence of the words in window.

2. Recurrent neural nets for NER.
(a) (i) The number of parameters is (V ×D + H×H + D×H + H + H×C + C)

(b) (i) Because the target of Neural Network is to predict token’s label correctly, it will decrease the F1 score for named entity.
    (ii) The first reason is that the F1 is not differentiate. The second reason is that the F1 is global measure, thus it’s difficulty to batch and parallelize.

