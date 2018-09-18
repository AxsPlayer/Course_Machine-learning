# Note of Course 15.

## The definition of coreference resolution.
- Identify all noun phrases (mentions) that refer to the same real world entity.

## Applications.
- Full text understanding.
- Machine translation.
- Text summarization.
- Information extraction and question answering. 

## Coreference Evaluation.
- The method people used in clustering also applied into coreference evaluation. 
- B-cubed algorithm for evaluation: precision and recall for entities in a reference chain. 

## Kinds of Reference.
- Referring expressions.
- Free variables.  
- Bound variables. (nearby)
- Not all NPs are referring.

## Kinds of coreference models
- Mention Pair Models: Treat coreference chains as a collection of pairwise links. Train a supervised classifier to classify mention pair-wise, using human-made feature.
- Mention ranking models: Explicitly rank all candidate antecedents for a mention.
- Entity-Mention Models: A cleaner, but less studied, approach.

## Neural coreference models.
- Just four papers.

## Neural Mention-Pair Model.
- Use word vector as well as some handcraft features for word vector can only capture some similarity of words but no other kind of relationships. No RNN.

## Coreference Resolution with Reinforcement Learning.
- B3 metrics evaluation matric.
- Reward-Rescaling: Add the reward into the max-margin loss function. 


