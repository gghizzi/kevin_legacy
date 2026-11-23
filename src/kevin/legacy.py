"""
legacy.py

Some things can't really be measured in code.
"""


def calculate_impact(kevin, people):

    impact = 0

    for person in people:

        impact += person.things_learned
        impact += person.opportunities_received
        impact += person.confidence_gained
        impact += person.memories_created

    return impact


def what_kevin_leaves():

    return [
        "better engineers",
        "better leaders",
        "better teammates",
        "good memories",
        "questionable jokes",
        "people who will pass it on"
    ]


def leave_company(kevin):

    team = kevin.team

    kevin.move_to_next_adventure()

    # The person leaves.
    assert kevin not in team

    # The impact doesn't.
    assert kevin.impact in team

    return True
