"""
Given a string senate representing each senator's party belonging. 
The character 'R' and 'D' represent the Radiant party and the Dire party. 
Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. 
                    This procedure will last until the end of voting. 
All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. 
Predict which party will finally announce the victory and change the Dota2 game. 
The output should be "Radiant" or "Dire".

"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQ = deque()
        dQ = deque()
        
        for i,c in enumerate(senate):
            if c == "R":
                rQ.append(i)
            else:
                dQ.append(i)
        while dQ and rQ:
            d,r = dQ.popleft(), rQ.popleft()
            
            if d < r:
                dQ.append(d+len(senate))
            else:
                rQ.append(r+len(senate))
        return "Radiant" if rQ else "Dire"