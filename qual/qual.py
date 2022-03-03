class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.available = True

    def __repr__(self):
        return 'Contributor {0}, skills: {1}'.format(self.name, self.skills)


class Project:
    def __init__(self, name, days, score, deadline, roles):
        self.name = name
        self.days = int(days)
        self.score = int(score)
        self.deadline = int(deadline)
        self.roles = roles

    # def find_skilled_contributors(self, contributors):
    #     contr = []
    #     for role, level in self.roles.items():
    #

    def __repr__(self):
        return 'Project {0}, days: {1}, score {2}, deadline {3}, roles {4}'.format(
            self.name, self.days, self.score, self.deadline, self.roles)


C, P = input().split(' ')

contributors = []
for i in range(int(C)):
    name, number_of_skills = input().split(' ')
    skills = {}
    for j in range(int(number_of_skills)):
        sk, level = input().split(' ')
        skills[sk] = int(level)
    contributors.append(Contributor(name, skills))

projects = []
for i in range(int(P)):
    name, days, score, deadline, number_of_roles = input().split(' ')
    roles = []
    for j in range(int(number_of_roles)):
        project_name, level = input().split(' ')
        roles.append([project_name, int(level)])
    projects.append(Project(name, days, score, deadline, roles))

# print(contributors)
# print(projects)

contributors_pool = contributors.copy()


def get_skilled_contributor(skill, level):
    for contributor in contributors_pool:
        if skill in contributor.skills and contributor.skills[skill] >= level:
            contributors_pool.remove(contributor)
            return contributor
    return None


projects = sorted(projects, key=lambda x: x.days)

assignments = {}
for project in projects:
    contr_assigned = []
    contrs_found = True
    for role in project.roles:
        contr = get_skilled_contributor(role[0], role[1])
        if contr is None:
            contrs_found = False
            break
        if contr is not None and contr not in contr_assigned:
            contr_assigned.append(contr)
    if contrs_found and len(contr_assigned) != 0:
        assignments[project.name] = contr_assigned

for project in projects:
    if project.name in assignments:
        len_roles = len(project.roles)
        len_assigned = len(assignments[project.name])
        assert len_roles == len_assigned

# Print output
# print(assignments)

print(len(assignments))
for project_name in assignments:
    print(project_name)
    contrs = [contr.name for contr in assignments[project_name]]
    print(' '.join(contrs))
