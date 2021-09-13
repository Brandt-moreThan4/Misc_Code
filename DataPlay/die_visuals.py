from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


#six sided die
die_1 = Die()
die_2 = Die()

roll_results = []

for roll_num in range(100000):
    roll_results.append(die_1.roll() + die_2.roll())

freq = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    freq.append(roll_results.count(value))

x_vals = list(range(2,max_result+1))
data = [Bar(x=x_vals,y=freq)]

x_ax_config = {'title': 'Result','dtick':1}
y_ax_config = {'title': 'Freuency of Result'}
my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis= x_ax_config,yaxis = y_ax_config)

offline.plot({'data':data, 'layout': my_layout}, filename = 'd6_d6.html')