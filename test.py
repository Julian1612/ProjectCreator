import requests
import json

def get_random_coding_joke():
    # URL for the JokeAPI to fetch a random coding joke
    url = "https://v2.jokeapi.dev/joke/programming?type=single"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = json.loads(response.text)
            return joke_data.get("joke")
        else:
            return "Failed to fetch joke. Status code: {}".format(response.status_code)
    except Exception as e:
        return "An error occurred: {}".format(str(e))

def main():
    joke = get_random_coding_joke()
    print("Random Coding Joke:")
    print(joke)

if __name__ == "__main__":
    main()
