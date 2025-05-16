from utils.loader import load_data

def main():
    data = load_data()

    for line in data:
        try:
            column_value = float(line[20])  # Coluna U
            if column_value >= 1:
                print(line[0])  # Coluna A
        except (IndexError, ValueError, TypeError):
            continue

if __name__ == "__main__":
    main()
