def laps_to_miles(user_laps):
    return user_laps / 4  

if __name__ == '__main__':
   user_laps = float(input())
   miles = laps_to_miles(user_laps)
   print(f'{miles:.2f}')
   