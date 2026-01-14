#  monitor file access patterns and suggest cache strategy.

access_count = {}
recent_files = []

def access_file(name):
    print("Accessing:", name)
    access_count[name] = access_count.get(name,0) + 1
    recent_files.append(name)

def suggest_strategy():
    lfu_file = max(access_count, key=access_count.get)
    lru_file = recent_files[-1]
    print("Most Frequent file:", lfu_file, "->Use LFU")
    print("Most Recent file:", lru_file, "->Use LRU")

    if recent_files == sorted(recent_files):
        print("Sequential Access")
    else:
        print("No Sequential Pattern")

access_file("A")
access_file("C")
access_file("B")
access_file("C")

suggest_strategy()


