# Note of Course 6.

## Language analysis.
There are two ways to analyze the structure of natural languages.
- Constituency context-free grammar(Phrase structure grammar) viewpoint: The first way is to conclude the grammar for each kind of language.
- Dependency grammar viewpoint: The second way is to analyze every sentences’ dependency tree structure. The disadvantages are that this method takes a lot of labor and seems slower than prior. But the advantages are that it’s reusable for the upstreaming works, it shows the frequencies and distributional information, and it’s also a good way to evaluate systems for the labeled ones could be ground truth.
In syntactic representations, the dependency grammar wins.

## Dependency tree structure.
Often add pseudo-word ROOT as the head of the whole sentence for the formal advantages. And another advantage of dependency grammar is that it’s useful to almost all kinds of languages in which the grammar is free, such as chinese, not like the fixed grammar language, such as english.

## How to get the information of dependency?
- Bilexical affinities
- Dependency distance: mostly with nearby word.
- Intervening materials: the information in the intervening.
- Valency of heads: the dependent is always in the left or right side of head.

## Constraint on dependency parsing.
- Only one word is dependent of ROOT.
- Don’t want cycles.
- Whether arrows can cross makes dependency tree is projective(not) or non-projective(can be).

## The problem on training a neural dependency parser using traditional feature representations.
- The first problem is that the features are sparse.
- The second problem is that it’s incomplete.
- The third problem is that it takes expensive computation to compute the feature number, as well as to find the suitable weights for features.
- The solution is to represent the features with dense representations.
- Attention: The improved neural dependency parser is good enough in terms of accuracy of UAS and LAS, compared to graph-based method. And it’s faster than graph-based method. Thus, if your data is small, you can choose graph-based method, but if your task is to parse the website, you should choose the neural dependency parser for its efficiency.

## The metric of parser.
- UAS: Unlabeled attachment score, using head.
- LAS: Labeled attachment score, using head and label.

## Transition based parser.
- The transition based parser has stack and buffer, as well as having three kinds of actions, shift, left-arc and right-arc. It’s based on transition actions of each word.


