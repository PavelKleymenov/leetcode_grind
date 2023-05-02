"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. 

Answers within 10-5 of the actual answer will be accepted.
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        
        # Remove maximum salary
        salary.remove(max(salary))

        # Remove minimum salary
        salary.remove(min(salary))

        """Calculate the average salary by dividing the total value to be paid 
                            by the number of people sharing it""" 
        return sum(salary)/len(salary)