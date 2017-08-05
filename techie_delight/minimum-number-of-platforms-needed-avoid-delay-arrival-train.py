#!/usr/bin/python


def main():
    trains_arriving = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
    trains_departing = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]
        
    trains_arriving.sort()
    trains_departing.sort()
    
    
    print trains_arriving
    print trains_departing
    
    max_platforms = 0
    platforms = 0
    arrival_idx = 0
    departure_idx = 0
    while arrival_idx < len(trains_arriving):
        next_arrival_time = trains_arriving[arrival_idx]
        if departure_idx < len(trains_departing):
            next_departure_time = trains_departing[departure_idx]
        if departure_idx >= len(trains_departing) or next_arrival_time < next_departure_time:
            platforms = platforms + 1
            arrival_idx = arrival_idx + 1
            print "train arriving at " + str(next_arrival_time)
            if platforms > max_platforms:
                max_platforms = platforms
        else:
            if platforms > 0:
                platforms = platforms - 1
            departure_idx = departure_idx + 1
            print "train departing at " + str(next_departure_time)
    print "platforms needed=" + str(max_platforms)
            
if __name__ == "__main__":
    main()
    
    