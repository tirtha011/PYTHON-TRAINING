'''
 Extract Players
You work at a sports club. The following sets contain the names of players registered to
play different sports:
football_players = ["Eve", "Tom", "Richard", "Peter"]
volleyball_players = ["Jack", "Hugh", "Peter", "Sam"]
basketball_players = ["Eve", "Richard", "Jessica ",
"Sam", "Michael"]
How can you obtain a set that includes the players that are only registered to play
basketball (i.e. not registered for football or volleyball)?

'''
football_players = ["Eve", "Tom", "Richard", "Peter"]
volleyball_players = ["Jack", "Hugh", "Peter", "Sam"]
basketball_players = ["Eve", "Richard", "Jessica ", "Sam", "Michael"]
 
basketball_only_players = basketball_players - (football_players | volleyball_players)
 
print("Basketball-only players:", basketball_only_players)