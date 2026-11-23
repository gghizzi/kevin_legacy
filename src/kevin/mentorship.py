"""
mentorship.py

Dependency installed automatically when working with Kevin.

Side effects may include career growth.
"""


def ask_kevin(question):

    answer = Kevin.answer(question)

    # Kevin rarely just gives you the answer.
    if answer == "What do YOU think?":
        return unexpectedly_learn_something()

    return answer


def career_advice(person):

    potential = person.potential

    # Kevin usually detects this before the person does.
    if potential > person.confidence:
        person.confidence = potential

    return person


def comfort_zone(person):

    while person.is_comfortable():
        opportunity = Kevin.find_slightly_scary_opportunity()

        Kevin.say("I think you should do this.")

        person.accept(opportunity)

    return person.upgrade()


def mentoring_session():

    scheduled_duration = 30  # minutes

    topics = [
        "work",
        "career",
        "leadership",
        "life",
        "why_are_we_talking_about_this_now"
    ]

    actual_duration = "¯\\_(ツ)_/¯"

    return actual_duration
