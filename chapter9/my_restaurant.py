from restaurant import Restaurant as res, IceCreamStand as ics

restaurant = res("fasfas", "fasfasf")
restaurant.describe_restaurant()
restaurant.set_number_served(45)
restaurant.increment_number_served(5)


iceCream = ics("fasfas", "fasfasf")
iceCream.describe_restaurant()
iceCream.display_flavors()