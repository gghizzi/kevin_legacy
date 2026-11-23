"""
humour.py

Production stability: questionable.
Entertainment value: high.
"""


def kevin_joke(meeting):

    seriousness = meeting.seriousness

    if seriousness > 80:
        Kevin.say_something_completely_unexpected()

        meeting.seriousness -= 35

    return meeting


def dad_joke():

    joke = Kevin.generate_joke()

    reactions = [
        "😂",
        "😐",
        "Kevin...",
        "please stop",
        "I'm leaving this meeting"
    ]

    # Kevin considers all of these successful outcomes.

    return joke, reactions


def mute_button():

    Kevin.start_talking()

    if Kevin.is_on_mute:
        team.wait(5)

        someone.say("Kevin, you're on mute.")

    return Kevin.say(
        "Sorry guys..."
    )
