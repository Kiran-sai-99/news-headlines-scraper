
import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

def get_headlines(url):
    headlines = []
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for span in soup.find_all("span", class_="titleline"):
            link = span.find("a")
            if link:
                text = link.get_text().strip()
                if text and text not in headlines:
                    headlines.append(text)

    except Exception as e:
        print("Error while fetching headlines:", e)

    return headlines


def save_headlines(headlines, filename="headlines.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for headline in headlines:
                f.write(headline + "\n")
        print(f"Headlines saved to {filename}")
    except Exception as e:
        print("Error while saving file:", e)


def main():
    print("Fetching latest news headlines...")
    headlines = get_headlines(URL)

    if headlines:
        print(f"Found {len(headlines)} headlines!\n")
        for i, h in enumerate(headlines[:10], start=1):
            print(f"{i}. {h}")
        save_headlines(headlines)
    else:
        print("No headlines found.")


if __name__ == "__main__":
    main()
