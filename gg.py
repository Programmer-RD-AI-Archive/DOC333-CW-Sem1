def calculate_price(adult: int, child: int, a_price: int, c_price: int) -> int:
    return (adult * a_price) + (child * c_price)


price_of_adult_local = 110
adult_saarc_price = 800
child_saarc_price = 400
adult_non_saarc_price = 3000
child_non_saarc_price = 1500
while True:
    print("Welcome To The Dehiwala Zoo")
    print("1. Local")
    print("2. Foreign")

    str = int(input("\nEnter your choice : "))

    if str == 1:
        num_of_adults = int(input("\nEnter the no. of adults : "))
        print(
            f"\nPrice of tickets: Rs. {calculate_price(adult=num_of_adults, a_price=price_of_adult_local)}",
        )

    elif str == 2:
        s_or_n = (
            input("\nEnter the type of foreigner (SAARC - s, Not SAARC - n) : ")
            .lower()
            .replace(" ", "")
        )

        if s_or_n == "s":
            adults = int(input("\nEnter the no. of Foreign Adult visitors: "))
            children = int(input("Enter the no. of Foreign child visitors: "))
            print(
                f"\nPrice of tickets: Rs. {calculate_price(adults, children, adult_saarc_price, child_saarc_price)}",
            )

        elif s_or_n == "n":
            adults = int(input("\nEnter the no. of Foreign Adult visitors: "))
            children = int(input("Enter the no. of Foreign child visitors: "))
            print(
                f"\nPrice of tickets: Rs. {calculate_price(adults,children,adult_non_saarc_price,child_non_saarc_price)}"
            )

        else:
            print("Invalid Input")

    else:
        print("Error")

    res = input(
        "\nDo you want to perform another cal - if yes enter Y - if no enter N:"
    )
    if res.lower() != "y":
        print("\nThank you")
        break
