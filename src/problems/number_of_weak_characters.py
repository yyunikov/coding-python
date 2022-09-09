from typing import List

"""
PROBLEM

You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        sorted_properties = list(
            sorted(properties, key=lambda i: i[0]))
        weak_characters = 0

        for i, i_prop in enumerate(sorted_properties):
            attack = i_prop[0]
            defense = i_prop[1]

            for j_prop in sorted_properties[i + 1:]:
                current_attack = j_prop[0]
                current_defense = j_prop[1]

                if current_attack > attack and current_defense > defense:
                    weak_characters += 1
                    break

        return weak_characters
