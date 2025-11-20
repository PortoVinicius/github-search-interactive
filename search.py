import requests

print("GitHub Search Simulator Started. Type 'exit' to quit.\n")

while True:
    query = input("Enter search term: ").strip()

    if query.lower() == "exit":
        print("Exiting simulator...")
        break

    if not query:
        print("Please type something.\n")
        continue

    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"

    print(f"\nSearching GitHub for: '{query}' ...\n")

    try:
        response = requests.get(url).json()

        items = response.get("items", [])

        if not items:
            print("No results.\n")
            continue

        for repo in items[:5]:
            print(f"📌 {repo['name']}")
            print(f"⭐ Stars: {repo['stargazers_count']}")
            print(f"🔗 URL: {repo['html_url']}")
            print(f"📝 Description: {repo['description']}\n")

    except Exception as e:
        print("Error:", e)
        print()
