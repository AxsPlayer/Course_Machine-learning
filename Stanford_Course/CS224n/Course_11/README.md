# Note of Course 11.

## GRU pros.
- Problem: The simple RNN has the problem that vanishing gradient is super-problematic. (When vanishing gradient, we cannot tell whether no dependency between t and t+n in data, or wrong configuration of parameters(the vanishing gradient condition)). The main cause is the naive transition function.
- The improvement of GRU: It implies that the error must back propagate through all the intermediate nodes. Perhaps we can create shortcut connections between each pair of nodes. Thus use update gate, and use reset gate to forget some unnecessary info.
- Why: The reason is that the relation between ht and ht-1 is linear, thus the gradient flows perfectly through time line.