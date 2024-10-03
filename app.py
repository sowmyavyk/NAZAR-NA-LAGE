from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Questions and their corresponding point values
questions = [
    {
        "question": "Do you ever feel like a CCTV camera is following you whenever you get a new job or promotion?",
        "options": [
            ("Yes, and it feels like ‘Congratulations’ has a creepy echo.", 2),
            ("Only if it’s the aunty next door… binoculars in hand.", 1),
        ]
    },
    {
        "question": "Do you *know* people who are secretly hoping you'll fail, just so they can feel better about their own lives?",
        "options": [
            ("Oh, absolutely. They’re like human bad vibes machines.", 2),
            ("Yeah, but they give me premium content for *nazaron ka bhoot* stories.", 1),
        ]
    },
    {
        "question": "Does your neighbor aunty have an unhealthy obsession with your life, especially when her kid isn't topping the class?",
        "options": [
            ("Her jealousy could fuel my bike, honestly.", 2),
            ("She turns greener than my mom’s chutney.", 1),
        ]
    },
    {
        "question": "How often do you feel 'mysteriously' sick in a month and immediately blame someone's evil eye?",
        "options": [
            ("Every other Monday—right after someone praises my new shoes.", 2),
            ("Once, after a relative saw me with my new phone… it hasn’t worked properly since.", 1),
        ]
    },
    {
        "question": "Do you think your relatives have low-key black magic skills?",
        "options": [
            ("Definitely. Their eyes practically glow when I mention an achievement.", 2),
            ("They can't figure out how to use WhatsApp properly, but sure, they know *jadoo tona*.", 1),
        ]
    },
    {
        "question": "On a scale of 1 to 10, how would you rate your relatives' black magic?",
        "options": [
            ("11. I’m convinced they’ve been to Hogwarts.", 2),
            ("5. They try, but my *nazar blockers* are stronger.", 1),
        ]
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i in range(1, 7):  # 6 questions
            answer = request.form.get(f'question-{i}')
            if answer:
                score += int(answer)

        # Generate a fun description based on the score
        if score >= 10:
            description = "You've got a whole squad of nazar watching you! Keep those lemons handy!"
            remedies = ["Always keep a lemon in your pocket.", "Start a Nazar Defense Team with your friends!"]
        elif score >= 5:
            description = "Some nazar is lurking around, but you’re mostly safe. Just stay alert!"
            remedies = ["Wear mismatched socks for extra protection.", "Do the full nazar utarna ritual after every birthday!"]
        else:
            description = "Chill! You’re mostly nazar-free, enjoy your life!"
            remedies = ["Keep it casual; good vibes only!", "Touch wood after every accomplishment!"]

        return render_template('results.html', score=score, description=description, remedies=remedies)

    # Randomly select 6 questions for the quiz
    selected_questions = random.sample(questions, 6)
    return render_template('quiz.html', questions=selected_questions)

if __name__ == '__main__':
    app.run(debug=True)