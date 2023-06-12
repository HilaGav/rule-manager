class Rule:
    def __init__(self, id, app, rule_name, condition, countries, action):
        self.id = id
        self.app = app
        self.rule_name = rule_name
        self.condition = condition
        self.countries = countries
        self.action = action