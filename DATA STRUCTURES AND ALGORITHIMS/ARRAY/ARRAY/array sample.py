"""there is no static array in python, instead, python has a built-in list data structure which is dynamic array. 
It automatically adjust its capicity as elements are added or removed. this makes list flexible and convenient
to work with, as their size can change dynamically based on the operations peformed on them."""

planets = ["Venus", "Pluto", "Earth"]

planets.insert(0, "Mercury")
# ['Mercury', 'Venus', 'Pluto', 'Earth']

planets.append("Jupiter")
# ['Mercury', 'Venus', 'Pluto', 'Earth', 'Jupiter']

planets.remove("Pluto")
# ['Mercury', 'Venus', 'Earth', 'Jupiter']

print(planets)
