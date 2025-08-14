import matplotlib.pyplot as plt 

# First plot - Bar chart
fig, ax = plt.subplots()

fruits = ['apple', 'banana', 'cherry', 'date']
counts = [40, 100, 30, 55]
bar_colors = ['tab:red', 'tab:orange', 'pink', 'saddlebrown']  # valid colors

bars = ax.bar(fruits, counts, color=bar_colors)

ax.set_ylabel('Fruits supply')
ax.set_title('Fruit Supply by Kind and Color')
ax.legend(bars, ['red', 'yellow', 'pink', 'brown'], title='Fruit Color')

plt.savefig('bars.png', bbox_inches='tight')

# Second plot - Line chart
cat = ['bored', 'happy', 'happy', 'happy', 'happy', 'bored']
dog = ['happy', 'happy', 'happy', 'happy', 'bored', 'bored']
activity = ['combing', 'drinking', 'feeding', 'napping', 'playing', 'washing']

fig, ax = plt.subplots()
ax.plot(activity, dog, label='dog')
ax.plot(activity, cat, label='cat')
ax.legend()

plt.savefig('lines.png', bbox_inches='tight')
