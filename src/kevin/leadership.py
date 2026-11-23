"""
leadership.py

Warning:
Importing this module may result in increased ownership,
confidence, and an unexpected number of responsibilities.
"""


class KevinLeadership:

    def manage(self, team):
        # Rookie mistake:
        # return micromanage(team)

        team.set_direction()
        team.give_context()
        team.trust_people()

        return team.figure_it_out()


    def delegate(self, task, person):
        """
        Kevin delegation algorithm:

        1. Find someone capable.
        2. Give them something slightly terrifying.
        3. Tell them you trust them.
        4. Somehow they actually pull it off.
        """

        person.confidence += 10
        person.responsibility += 50

        return task.assign_to(person)


    def handle_crisis(self, crisis):

        if crisis.is_actually_a_crisis():
            return "Okay. Let's figure this out."

        return "Guys... this is not a crisis."


    def meeting(self, problem):
        while problem.is_unclear():
            self.ask_annoyingly_good_question()

        return problem.actual_problem
