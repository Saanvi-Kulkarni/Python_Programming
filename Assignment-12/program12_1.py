def ChkVowel(Alphabet):
    Vowels = 0

    Vowels = ['a','e','i','o','u']

    if Alphabet in Vowels:
        return True
    else:
        return False

def main():
    Value = {'\0'}
    Ret = False

    Value = input("Enter character : ")

    Ret = ChkVowel(Value)

    if(Ret == True):
        print("It is a vowel")
    else:
        print("It is not a vowel")

if __name__ == "__main__":
    main()