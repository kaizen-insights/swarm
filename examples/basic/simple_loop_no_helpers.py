from swarm import Swarm, Agent
from swarm.swarm.repl.repl import run_demo_loop

client = Swarm()

my_agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)


def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")


if __name__ == "__main__":
    run_demo_loop(my_agent, debug=True)
