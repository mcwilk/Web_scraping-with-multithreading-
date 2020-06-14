from bs4 import BeautifulSoup
import watki


def html_tags():
    """
        Function asks user for HTML tags in which to conduct searching for
        phrase.
    """

    choice_tags = input('Please type comma separated html tags or push Enter: ')
    
    if len(choice_tags) != 0:
        tags = choice_tags.replace(' ', '').split(',')
    else:
        tags = ['p']

    return tags


def scraper(page, phrase, choice, *args):
    """
        Function looks for user's phrase in each HTML. If phrase is found 
        it prints sentence containing that phrase. If not - 'phrase not 
        found' statement is printed.
    """

    name = page.find('title')
    name = name.text

    for tag in args:
        content = page.find_all(tag)

        for c in content:
            text = c.text
            sentences = text.split('.')

            for sentence in sentences:

                if phrase in sentence:
                    sentence = sentence.strip()

                    if choice == 'y':
                        encoding = page.find('meta').get('charset').lower()
                        sentence = sentence.encode(encoding)
                        return name, sentence

                    return name, sentence
                
    sentence = "phrase not found"
    return name, sentence


def final_result(pages_content, phrase, choice, *args):
    """
        Function prints final result of the program.
    """

    for page in pages_content:
        name, sentence = scraper(page, phrase, choice, *args)
        print(f'\nname:\t {name}\nphrase:\t {phrase}\nresult:\t {sentence}')


def main():
    """
        Function executes all functions (main program).
    """

    pages_content = watki.main()
    tags = html_tags()
    phrase = input("Please type a phrase (e.g. Python): ")
    choice = input("Do you want to use website's encoding (y/n)? ").lower()

    final_result(pages_content, phrase, choice, *tags)


if __name__ == '__main__':
    main()
