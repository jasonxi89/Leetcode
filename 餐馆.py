from bisect import bisect

class Solution:
    """
    @param stores: The location of each store.
    @param houses: The location of each house.
    @return: The location of the nearest store to each house.
    """
    def findNearestStore(self, stores, houses):
        stores.sort()
        
        print(stores)
        
        closest = []
        for house in houses:
            i = bisect(stores, house)
            
            # print(house, i)
            
            if i >= len(stores):
                closest.append(stores[-1])
            elif stores[i] == house:
                closest.append(stores[i])
            elif i > 0 and house - stores[i-1] <= stores[i] - house:
                closest.append(stores[i-1])
            else:
                closest.append(stores[i])
        
        return closest
        
