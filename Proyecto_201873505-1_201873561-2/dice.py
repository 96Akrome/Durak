from random import randrange

def ROLL(dice){
	if dice == "d4":
        return randrange(1, 4)
    
    if dice == "d6":
        return randrange(1, 6)
    
    if dice == "d8":
        return randrange(1, 8)
    
    if dice == "d10":
        return randrange(1, 10)
    
    if dice == "d12":
        return randrange(1, 12)
    
    if dice == "d20":
        return randrange(1, 20)
    
    if dice == "d100":
        return randrange(1, 100)
}