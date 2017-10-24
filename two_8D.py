from die import Die
import pygal

#create a D6
die1= Die(8)
die2= Die(8)

# Make some rolls, and store results in a list.
results = []

for roll_num in range(30000):
    result = die1.roll() + die2.roll()
    results.append(result)

print results,'\n'

# analyse the results
frequencies = []
max_result = die1.num_sides + die2.num_sides

for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print frequencies

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of two D8 1000 times"
hist.x_labels = [x for x in range(2, max_result+1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'

hist.add('two D8',frequencies)
hist.render_to_file('die_visual_2D8.svg')
