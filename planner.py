class Planner:

    def plan(self, query):

        query = query.lower()

        if "time" in query:
            return {
                "tool": "time"
            }

        elif "calculate" in query:

            expression = query.replace("calculate", "").strip()

            return {
                "tool": "calculator",
                "expression": expression
            }

        else:

            return {
                "tool": "chat",
                "query": query
            }