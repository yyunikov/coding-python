"""
PROBLEM

A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.



Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
"""
from typing import List


# TODO the problem is not solved exactly right, see the commented test
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # how many stops do we need to get to N
        dp = [0] * target

        if target - startFuel <= 0:
            return 0

        if not stations:
            return 0 if target - startFuel <= 0 else - 1

        current_fuel = startFuel
        next_station_index = 0
        # one mile at a time
        for i in range(0, target):
            # if it's a station
            if next_station_index <= len(stations) - 1 and i == stations[next_station_index][0]:
                current_station_index = next_station_index
                next_station_index = current_station_index + 1
                # if we have enough fuel for the next stations and
                # we'll get less fuel on this station than on the next one
                if len(stations) - 1 >= next_station_index and \
                        current_fuel >= stations[next_station_index][0] - current_fuel:
                    # no, if we have enough fuel for next stop
                    # we skip station
                    dp[i] = dp[i - 1] if i != 0 else 0
                # if we don't have enough fuel for the next stations and
                # we'll get more fuel on this station than on the next one
                elif len(stations) - 1 >= next_station_index and \
                        current_fuel < stations[next_station_index][0] - current_fuel:
                    # we stop for fuel
                    dp[i] = dp[i - 1] + 1 if i != 0 else 0
                    current_fuel += stations[current_station_index][1]
                # if this is the last station
                elif len(stations) - 1 <= next_station_index:
                    # this is the last station
                    if target - i - current_fuel <= 0:
                        # we skip station
                        dp[i] = dp[i - 1] if i != 0 else 0
                    else:
                        # we stop for fuel
                        dp[i] = dp[i - 1] + 1 if i != 0 else 1
                        current_fuel += stations[current_station_index][1]
            else:
                dp[i] = dp[i - 1]

            # decision
            if current_fuel < 0:
                return -1

            # drive next mile
            current_fuel -= 1

        return dp[target - 1]
