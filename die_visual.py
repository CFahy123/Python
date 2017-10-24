from die import Die
import pygal

#create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print results,'\n'

# analyse the results
frequencies = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print frequencies

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D6 1000 times"
hist.x_labels = [x for x in range(1, die.num_sides+1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
