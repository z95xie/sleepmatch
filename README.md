# SleepMatch

## What does this project do?
SleepMatch calculates a recommended sleep duration based on a user's age and activity level.

## Inputs
- Age (integer)
- Activity level: low / medium / high

## Output
- Recommended sleep hours
- Explanation of how the result is calculated

## How does it work?
1. The program asks the user for their age.
2. The program asks the user for their activity level.
3. It calculates a base sleep time based on age.
4. It adjusts the sleep time based on activity level.
5. The final recommendation and explanation are printed.

## How to run
```bash
python3 sleep_target.py

## What I learned
- How to use functions to organize code
- How to validate user input safely
- How to explain program logic in plain language



## Example

Input:
- Age: 20
- Activity level: high

Output:
- Recommended sleep hours: 8.5  
- Reason: Base sleep for age 20 is 8.0h. High activity adds 0.5h.

