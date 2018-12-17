def tour_plan(destination, head_count=4, mode='air', origin='Ranchi', hotel='makemytrip'):
    """Plan a tour using any mode of transport from origin to destination with
    a group of n people. You have option to book accommodation through makemytrip.
    Default origin is Ranchi, default mode of transport is
    air, default head count is 4, default accommodation is through makemytrip.
    1. Plan a trip to kerala, from ranchi, for 4, by air, on makemytrip
    2. Plan a trip to Thailand, from ranchi, for 10.
    3. Plan a trip to Nepal, from ranchi, by car, for 2, through 'airbnb' instead of makemystrip.
     """
    print("We will leave", origin, end='')
    print(" to", destination, end='')
    print(" by", mode, end='')
    print(" and book accommodation with", hotel, end='')
    print(" for", head_count)


if __name__=='__main__':
    tour_plan("Kerala")
    # error
    #tour_plan()
    #tour_plan(head_count=20, "kerala")
    #tour_plan("Singapore", destination="Thailand")
    tour_plan("Thailand", head_count=10)
    tour_plan("Nepal", mode='car', hotel='airbnb', head_count=2)

