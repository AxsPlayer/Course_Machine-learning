# Note of Course 14.(Deep Reinforcement Learning)

## Reinforcement Learning.
- Problems involving an agent interacting with an environment, which provides numeric reward signals. 
- Goal: Learn how to take actions in order to maximize reward.
- agent: give action to environment, and receive reward from environment.
- environment: give state to agent

## Markov Decision Process.
- Mathematical formulation of the RL problem.
- Markov property: Current state completely characterises the state of the world.
- Definitions: Value function and Q-value function.
- How good is a state?
	- The value function at state s, is the expected cumulative rward from following the policy from state s
- How good is a state-action pair?
	- The Q-value function at state s and action a, is the expected cumulative reward from taking action a in state s and then following the policy.
	- Q* (optimal) satisfies the following Bellman equation.

## Q-learning.
- Q-learning: Use a function approximator to estimate the action-value function.
- If the function approximator is a deep neural nework -> deep 1-learning.
- experience replay: to solve the related samples problem.

## Policy Gradients.
- Problem: The Q-function can be very complicated, But the policy can be much simpler.

## Reinforce algorithm.
- does not depend on transition probability.


