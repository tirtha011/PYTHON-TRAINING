### PROBLEM STATEMENT

'''
Gary is an avid hiker. He tracks his hikes meticulously, paying
close attention to small details like topography. During his last hike,
he took exactly n steps. For every step he took, he noted if it was
an uphill or a downhill step. Gary’s hikes start and end at sea level.
We define the following terms:
A mountain is a non-empty sequence of consecutive steps above
sea level, starting with a step up from sea level and ending with a
step down to sea level.
A valley is a non-empty sequence of consecutive steps below sea
level, starting with a step down from sea level and ending with a
step up to sea level.
Given Gary’s sequence of up and down steps during his last hike,
find and print the number of valleys he walked through.
Input Format
The first line contains an integer, , denoting the number of steps in
Gary’s hike.
The second line contains a single string of characters. Each
character belongs to {U, D} (where U indicates a step up and D
indicates a step down), and the i(th) cin the string describes Gary’s
i(th) step during the hike.
Constraints

5

2 &lt;= N &lt;= 10^6
Output Format
Print a single integer denoting the number of valleys Gary walked
through during his hike.
Sample Input
8
UDDDUDUU
Sample Output
1
Explanation
If we represent _ as sea level, a step up as / , and a step down as \
, Gary’s hike can be drawn as:
_/\ _
\ /
\/\/
It’s clear that there is only one valley there, so we print on a new
line.

'''