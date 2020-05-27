COINS           = [1, 2, 5, 10, 20, 50, 100, 200]
COIN_INDEX      = len(COINS) - 1

def GetNumberOfWaysToCreateCoin(coin_index, coins):
    desired_coin = coins[coin_index]
    ways = [0] * (desired_coin + 1)
    ways[0] = 1
    for coin in coins:
        for s in xrange(coin, desired_coin + 1, 1):
            ways[s] += ways[s - coin]
    return ways[desired_coin]
               
# Main
def main():	
    # 73682
    print GetNumberOfWaysToCreateCoin(COIN_INDEX, COINS)
   
if __name__ == "__main__":
    main()
