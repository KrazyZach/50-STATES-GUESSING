import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.listen()


data = pandas.read_csv('50_states.csv')
fish = open("review.txt" , "w")

def get_mouse(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse)

score = 0

blame = turtle.Turtle()
blame.penup()
blame.color("Black")
blame.hideturtle()
blame.speed(0)

used_sates = []

game = True

while game:
    awnser = screen.textinput(title=f"Guess the State {score} / 50", prompt="What's another state's name?")
    for i in range(0, 49):
        if (awnser.lower() == data.state[i].lower() and awnser.lower() not in used_sates):
            used_sates.append(awnser.lower())
            blame.goto(data.x[i], data.y[i])
            blame.write(data.state[i], font=('Arial', 8, 'bold'))
            score += 1
    if score == 50:
        game = False

for x in range(0, 50):
    if data.state[x].lower() not in used_sates:
        fish.write(f"{data.state[x]}\n")


turtle.mainloop()
