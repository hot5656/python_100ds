import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # print("people:", reader)
        for row in reader:
            # lib
            # print(row)
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

        # print("\n people", len(people),people)
        print("\n names", len(names), names)

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # print("people:", reader)
        for row in reader:
            # print(row)
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }
        # print("\nmovies", len(movies),movies)

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # print("stars:", reader)
        for row in reader:
            # print(row)
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass
        print("\n people", len(people),people)
        print("\n movies", len(movies),movies)


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        print("connected.")
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        print("path:", path)
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


class Connect():
    def __init__(self, source, traget):
        # print("\n name source, traget", type(source), traget)
        # print(names)
        # print("\n id source, traget", names[source], names[traget])
        self.start = source
        self.goal = traget
        print("start, goal :", source, traget)

    # def movies(self, people_id):
    #     result = []
    #     for row in people[people_id]['movies']:
    #         result.append((row, people_id))
    #     return result


    def solve(self):
        # count
        self.num_explored = 0

        # put start
        start = Node(state=self.start, parent=None, action=None)
        start.print()
        # stack
        frontier = StackFrontier()
        frontier.add(start)

        # explored set
        self.explored = set()

        while True:
            # chedk no next ,no solution
            if frontier.empty():
                raise Exception("no solution")

            # remove the state and count
            node = frontier.remove()
            self.num_explored += 1

            print("current:", node.state)
            # save route result
            if node.state == self.goal:
                path = []
                actions = []
                cells = []
                while node.parent is not None:
                    # print("\n node.parent", node.parent)
                    actions.append(node.action)
                    cells.append(node.state)
                    path = [(node.action, node.state)] + path
                    print("run path:", path)
                    node = node.parent
                    node.print()

                actions.reverse()
                cells.reverse()
                self.path = path
                self.solution = (actions, cells)
                print("self.solution:", self.solution)
                print("self.path:", self.path)
                return self.path

            # add step
            self.explored.add(node.state)


            for movie in people[node.state]['movies']:
                # if id not in  frontier.contains_state and explored, add to frontier
                # print("\n movie: ", movie)
                print(" movie:", movie)
                for next_id in movies[movie]['stars']:
                    if not frontier.contains_state(next_id) and next_id not in self.explored:
                        print("  add movie,id", node.state, movie, next_id)
                        child = Node(state=next_id, parent=node, action=movie)
                        child.print()
                        frontier.add(child)

            # frontier.print()
            # break
        return None

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # TODO
    # raise NotImplementedError

    result = Connect(source, target)
    return result.solve()




def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()

# Kevin Bacon
# Robin Wright