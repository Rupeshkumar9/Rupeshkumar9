# Simulate resource allocation and scheduling using Docker.

import docker
import time
# Create Docker client
client = docker.from_env()
# List of "tasks" to run (each task is a container)
tasks = [
 {"name": "task1", "image": "alpine", "command": "echo Task 1 running; sleep 2", "cpus": 0.5,
 "mem_limit": "50m"},
  {"name": "task2", "image": "alpine", "command": "echo Task 2 running; sleep 3", "cpus": 0.5,
  "mem_limit": "50m"},
   {"name": "task3", "image": "alpine", "command": "echo Task 3 running; sleep 1", "cpus": 0.5,
   "mem_limit": "50m"}
   ]
   # Simulate scheduling and resource allocatio

for task in tasks:
        print(f"Starting {task['name']}...")
        container = client.containers.run(
          image=task["image"],
          command=task["command"],
           name=task["name"],
           detach=True,
            cpu_quota=int(task["cpus"] * 100000),
             mem_limit=task["mem_limit"]
           )
        container.wait() # Wait for container to finish
        logs = container.logs().decode("utf-8")
        print(logs)
        container.remove() # Clean up container
        print(f"{task['name']} finished.\n")

print("All tasks completed!")










