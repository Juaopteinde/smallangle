import click
import numpy as np
import pandas as pd
from numpy import pi


# create smallangle command
@click.group()
def smallangle():
    pass


# create subcommand sin of smallangle
@smallangle.command()
@click.option("-n", "--number", default=10)
def sin(number):
    """Calculate sin(x) and small angle approximation of sin(x)

    \b
    Args:
        number (int): amount of equally spaced numbers 0 < n < 2pi to calculate for
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


# create subcommand tan of smallangle
@smallangle.command()
@click.option("-n", "--number", default=10)
def tan(number):
    """Calculate tan(x) and small angle approximation of tan(x)

    \b
    Args:
        number (int): amount of equally spaced numbers 0 < n < 2pi to calculate for
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


# create approx command
@click.command()
@click.option("-e", "--epsilon", default=0.1)
@click.option("-t", "--tan", is_flag=True, default=False)
@click.option("-s", "--sin", is_flag=True, default=False)
def approx(epsilon, tan, sin):
    """Print the maximum angle for which the small angle of sin(x) and/or tan(x) holds within given accuracy.

    \b
    Args:
        epsilon (str): accuracy whithin which approx must hold
        tan (bool): choose if you want to calculate only for tan(x)
        sin (bool): choose if you want to calculate only for sin(x)
    """

    # print max small angle approx for sin(x)
    if sin:
        max_angle_sin = 0
        while np.abs(max_angle_sin - np.sin(max_angle_sin)) <= float(epsilon):
            max_angle_sin += 0.001
        print(
            f"For an accuracy of {epsilon}, the small-angle approximation for sin(x) holds \n up to x = {round(max_angle_sin, 3)}"
        )

    # print max small angle approx for tan(x)
    if tan:
        max_angle_tan = 0
        while np.abs(max_angle_tan - np.tan(max_angle_tan)) <= float(epsilon):
            max_angle_tan += 0.001

        print(
            f"For an accuracy of {epsilon}, the small-angle approximation for tan(x) holds \n up to x = {round(max_angle_tan, 3)}"
        )

    # print small angle approx for sin(x) and tan(x)
    if not sin and not tan:

        max_angle_sin = 0
        while np.abs(max_angle_sin - np.sin(max_angle_sin)) <= float(epsilon):
            max_angle_sin += 0.001
        max_angle_tan = 0
        while np.abs(max_angle_tan - np.tan(max_angle_tan)) <= float(epsilon):
            max_angle_tan += 0.001

        print(
            f"For an accuracy of {epsilon}, the small-angle approximation for sin(x) holds \n up to x = {round(max_angle_sin, 3)}"
        )
        print(
            f"For an accuracy of {epsilon}, the small-angle approximation for tan(x) holds \n up to x = {round(max_angle_tan, 3)}"
        )


if __name__ == "__main__":
    smallangle()
    approx()
