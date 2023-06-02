def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        max_speed = 0 # S(1) T(1)
        redShirtSpeeds.sort() # S(1) T(nlogn)
        blueShirtSpeeds.sort(reverse=True) # S(1) T(nlogn)
        for blue, red in zip(blueShirtSpeeds, redShirtSpeeds): # S(2) T(nlogn)
            max_speed += max(blue, red) # S(1) T(1)
        return max_speed
    else:
        min_speed = 0
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        for blue, red in zip(blueShirtSpeeds, redShirtSpeeds):
            min_speed += max(blue, red)
        return min_speed
