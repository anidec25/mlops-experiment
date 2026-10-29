def calculate_total_apples(baskets, apples_per_basket):
    return baskets + apples_per_basket  # Intentional bug


if __name__ == "__main__":
    print("Total apples:", calculate_total_apples(5, 10))