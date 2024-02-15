#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html

URL= "https://opentdb.com/api.php?amount=3&category=21&difficulty=easy&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    # Extract question & answer
    for result in data['results']:
        question = html.unescape(result['question'])
        answers = [html.unescape(answer) for answer in result['incorrect_answers']]
        correct_answer = html.unescape(result['correct_answer'])

        # Print the question & answer
        print("Question:", question)
        print("Answer:" , answers + [correct_answer])
        print("\n")

if __name__ == "__main__":
    main()

