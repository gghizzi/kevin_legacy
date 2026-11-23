"""
trust.py

Security notice:
Kevin appears to grant elevated permissions
with surprisingly little bureaucracy.
"""


def assign_important_project(person):

    try:
        person.assign(
            responsibility="HIGH",
            instructions="MINIMAL",
            visibility="ALARMINGLY_HIGH"
        )

        Kevin.say("You'll figure it out.")

        return person

    except PersonSaysTheyAreNotReady:

        Kevin.say("I think you are.")

        return assign_important_project(person)


def request_approval(decision):

    if decision.is_sensible():
        return "Why are you asking me?"

    if decision.is_reversible():
        return "Just try it."

    return Kevin.help_think_it_through(decision)


def micromanage(team):

    raise NotImplementedError(
        "This functionality was never implemented."
    )
