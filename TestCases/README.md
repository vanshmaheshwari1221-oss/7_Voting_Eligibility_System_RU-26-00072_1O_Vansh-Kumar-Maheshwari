# PS 7 - Voting Eligibility System: Test Cases

* Test Case 1: Normal Input
Input: Name: Aman, Age: 25, Indian citizen (y/n): y
Output: Aman is eligible to vote.

* Test Case 2: Boundary / Minimum Input
Input: (a) Name: Neha, Age: 18, Citizen: y, Check another voter? y
       (b) Name: Ravi, Age: 17, Citizen: y
Output: (a) Neha is eligible to vote.
        (b) Ravi is not eligible to vote.
            Years left to become eligible: 1

* Test Case 3: Invalid Input
Input: Name: Amit, Age: abc, then -5, then 30, Citizen: y
Output: Invalid input. Enter a whole number.
        Invalid age. Age must be between 0 and 120.
        Amit is eligible to vote.

* Test Case 4: Different Valid Scenario
Input: Name: Riya, Age: 30, Indian citizen (y/n): n
Output: Riya is not eligible to vote.
        Reason: Not an Indian citizen.
        Voters checked: 5 | Eligible: 3 | Not eligible: 2

