num_cents = int(input( "How much change? :"))

quarters_in_change = num_cents//25
dime_in_change = num_cents % 25 //10
nickels_in_change = num_cents % 25//10//5
pennies_in_change = num_cents % 25//10//5//1

print "You have" + {num_cents//quarters_in_change} + "quarters," + {num_cents//dime_in_change} + "dimes," + {num_cents//nickels_in_change} + "nickels, and"  + {num_cents//pennies_in_change} + "pennies."
