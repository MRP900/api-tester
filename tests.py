from apiTest import testApi

if __name__ == "__main__":
    print("\nTesting in progress")
    myApiString = "http://api.open-notify.org/astros.json"

    print("\nTest 1 - Default Args")
    test1 = testApi(myApiString)
    print(f"test1: {test1}")
    print("*************************************")

    print("\nTest 2 - False, False")
    test2 = testApi(myApiString, False, False)
    print(f"Test2: {test2}")
    print("*************************************")

    print("\nTest 3 - True, False")
    test3 = testApi(myApiString, True, False)
    print(f"test3: {test3}")
    print("*************************************")

    print("\nTest 4 - False, True")
    test4 = testApi(myApiString, False, True)
    print(f"test4: {test4}")
    print("*************************************")

    print("\nTest 5 - Bad String, True, True")
    myApiString = "http://api.open-notify.org/astros.j"
    test5 = testApi(myApiString)
    print(f"test5: {test5}")
    print("*************************************")

    print("\nTest 6 - Bad String, False, False")
    myApiString = "http://api.open-notify.org/astros.j"
    test6 = testApi(myApiString, False, False)
    print(f"test6: {test6}")
    print("*************************************")
