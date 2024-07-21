from manager import ManagerAgent, main

objective = """I am trying to run `pip install blahhh` and I got `ERROR: Could not find a version that satisfies the requirement blahhh (from versions: none)
ERROR: No matching distribution found for blahhh`, how do I solve this?"""
manager_agent = ManagerAgent()
main(manager_agent, objective)
