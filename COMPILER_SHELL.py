import main

f = open("test_file.txt", "r")
for line in f:
    text = line
    result, error = main.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        print(result)
