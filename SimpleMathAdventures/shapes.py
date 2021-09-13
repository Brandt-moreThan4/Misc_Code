from matplotlib import pyplot as plt
from matplotlib import animation


def create_circle():
    """Creates a circle"""
    circle = plt.Circle((0, 0), .5)
    return circle


def update_radius(i, circle):
    circle.radius = i * .5
    return circle


def create_animation():
    """Make a growing circle. This is pretty cool."""
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_radius, fargs=(circle,), frames=30, interval=75)
    plt.title('Bet Circle')
    plt.show()


if __name__ == '__main__':
    create_animation()
