"""
  Build a robot to fight other robots!
  Commands:
    rgrun yourcode.py yourothercode.py # Pits codes against each other
      Optional Parameters:
        -m, specifies a map file
        -H, headlines, runs without the UI
        -c, specifies a number of games to run concurrently
 
 From http://robotgame.net
"""

import rg

class Robot:
    
    ### List of spawning locations
    
    def act(self, game):
        """ For each turn, you can move, guard, attack, or suicide """
        
        ### Print all the robots in your team
        for loc, robot in game.robots.items():
            if robot.player_id == self.player_id:
                print "Robot # ", " X ", " is at ", loc

        ### Guard if you are in the middle
        if self.location == rg.CENTER_POINT:
            return ['guard']
        
        ### If there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id: # Check if enemy robot
                if rg.dist(loc, self.location) <= 1: # Within attacking distance
                    if (self.hp<11):
                        return ['suicide']
                    return ['attack', loc]
        
        ### Go towards center of the Map
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]