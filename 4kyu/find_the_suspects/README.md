# [**Detective, ¡find the suspects!**](https://www.codewars.com/kata/63ae2ee16ef00700315462cd)

You are a famous detective who has been hired by the prince of a nation. The prince's biggest treasure has been stolen and while the police have identified the thief, they are not believed to be the mastermind behind the crime. The prince suspects one of his friends to be the real culprit, and has obtained information from the police about the friendships of his friends and the thief, and their respective friends. Your task is to investigate and determine whether any of the prince's friends are suspects in the robbery.

## **Data**
The data are given as an array of pairs where each pair (a,b) represents a bidirectional friendship between the person a and person b (so a is friend of b and b is friend of a). In other words, (a,b)=(b,a). Because of data privacy of the nation, the prince was only able to give you ID numbers that represent each person. However, he tells you his ID and the ID of the thief.

## **Definitions and assumptions**
Let's start by defining some terms and making some assumptions:

1. There are three types of relationships between two people: friends, acquaintances, and strangers. If two people are friends, they are also considered acquaintances. However, if two people are acquaintances, they are not necessarily friends.

2. A "friendship path" between person a and person b is a list of pairs of people who are friends that connect a and b. If there is a friendship path between two people, then they are considered acquaintances. If the friendship path contains only one pair, then the two people are friends. If there is no friendship path, then the two people are strangers. Please note that there can be more than one friendship path between two people.

Let's use an example to understand this better. Suppose we have the following data: [(a,b),(a,c),(b,c),(b,d),(e,f)]. Here's what we can learn from it:

- Two possible friendship paths between a and b are: [(a,b)] and [(a,c),(b,c)]. The first path means that a and b are friends, while the second path means they are only acquaintances.
- There is a friendship path between a and d: [(a,b),(b,d)]. Therefore, a and d are acquaintances. 
- There is no friendship path between a and f. This means that a and f are strangers.

## **¿What makes a friend of the prince a suspect?**
A friend of the prince is only considered a "suspect" if two conditions are met. First, they must be acquainted with the thief. Second, there must be no other potential suspect (i.e., friend of the prince) in any of the friendships paths between the thief and the friend of the prince.

To explain this mathematically, denote F
F as the set of friends of the prince. Let f∈F be the friend of the prince and t the thief of the treasure. Now, denote Pt={p1,...,pn} as the set of all the people in a friendships path between t and f excluding them. f is a suspect if and only if there is a path between t and f:

t→p1→p2→⋯→pn→f such that for all p∈Pft,p∉F

So, if the thief and a friend of the prince are strangers, then the friend is not a suspect. If they are friends, then the friend is a suspect. If they are only acquaintances, then the friend is only a suspect if the above condition is true.

## **Input**
data: (list) A list of tuples where each tuple contains the friendship of two people (ID integers). Be aware the data provided could have hundreds or thousands of different people.

prince_id: (int) The ID of the prince.

thief_id: (int) The ID of the thief.

## **Output**
(lst) An ordered list (ascending) with the IDs (integers) of all the possible suspects. If the data didn't contain enough information to get some suspects, return an empty array [].

## **Example**
Let the data be[(0,1), (0,2), (0,3), (1,2), (1,3), (2,3), (4,2)] and the prince id is 0 and thief id is 4. There is a friendships path between 3(friend of a prince) and 4(thief) but the path contains 2, who is really a potential suspect(friend of the prince). The same happens with 1. Therefore, the only suspect is, actually, the friend with id 2.