import pandas as pd
import os


def load_file():
    file_name = input("Enter CSV file path: ")

    if not os.path.exists(file_name):
        print("File not found.")
        return None

    try:
        df = pd.read_csv(file_name)
        print("\nCSV file loaded successfully!")
        return df
    except Exception as e:
        print("Error:", e)
        return None


def basic_information(df):
    print("\n--- DATA INFORMATION ---")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nColumn Names:")
    for column in df.columns:
        print("-", column)

    print("\nData Types:")
    print(df.dtypes)


def show_data(df):
    print("\n--- DATA ---")
    print(df.to_string())


def first_rows(df):
    number = int(input("How many rows? "))

    print("\n--- FIRST ROWS ---")
    print(df.head(number))


def last_rows(df):
    number = int(input("How many rows? "))

    print("\n--- LAST ROWS ---")
    print(df.tail(number))


def missing_values(df):
    print("\n--- MISSING VALUES ---")

    missing = df.isnull().sum()

    print(missing)

    total = missing.sum()

    print("\nTotal Missing Values:", total)


def statistics(df):
    print("\n--- STATISTICS ---")
    print(df.describe())


def numeric_analysis(df):
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) == 0:
        print("No numeric columns found.")
        return

    print("\n--- NUMERIC ANALYSIS ---")

    for column in numeric_columns:

        print(f"\nColumn: {column}")

        print("Total:", df[column].sum())
        print("Average:", df[column].mean())
        print("Maximum:", df[column].max())
        print("Minimum:", df[column].min())


def unique_values(df):
    print("\n--- UNIQUE VALUES ---")

    for column in df.columns:
        print(
            f"{column}: "
            f"{df[column].nunique()} unique values"
        )


def duplicate_analysis(df):
    duplicates = df.duplicated().sum()

    print("\n--- DUPLICATE ANALYSIS ---")
    print("Duplicate Rows:", duplicates)


def remove_missing(df):
    print("\n--- REMOVE MISSING VALUES ---")

    before = len(df)

    df.dropna(inplace=True)

    after = len(df)

    print("Rows before:", before)
    print("Rows after:", after)
    print("Rows removed:", before - after)

    return df


def remove_duplicates(df):
    print("\n--- REMOVE DUPLICATES ---")

    before = len(df)

    df.drop_duplicates(inplace=True)

    after = len(df)

    print("Rows before:", before)
    print("Rows after:", after)
    print("Duplicates removed:", before - after)

    return df


def save_file(df):
    file_name = input(
        "Enter output CSV file name: "
    )

    df.to_csv(
        file_name,
        index=False
    )

    print("File saved successfully!")


def search_data(df):
    column = input("Enter column name: ")

    if column not in df.columns:
        print("Column not found.")
        return

    value = input("Enter search value: ")

    result = df[
        df[column].astype(str).str.contains(
            value,
            case=False,
            na=False
        )
    ]

    print("\n--- SEARCH RESULT ---")

    if result.empty:
        print("No matching records found.")
    else:
        print(result.to_string())


def main():

    print("==============================")
    print("       CSV DATA ANALYZER")
    print("==============================")

    df = load_file()

    if df is None:
        return

    while True:

        print("\n==============================")
        print("          MENU")
        print("==============================")

        print("1. Show Data")
        print("2. Data Information")
        print("3. First Rows")
        print("4. Last Rows")
        print("5. Missing Values")
        print("6. Statistics")
        print("7. Numeric Analysis")
        print("8. Unique Values")
        print("9. Duplicate Analysis")
        print("10. Remove Missing Values")
        print("11. Remove Duplicates")
        print("12. Search Data")
        print("13. Save CSV")
        print("14. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            show_data(df)

        elif choice == "2":
            basic_information(df)

        elif choice == "3":
            first_rows(df)

        elif choice == "4":
            last_rows(df)

        elif choice == "5":
            missing_values(df)

        elif choice == "6":
            statistics(df)

        elif choice == "7":
            numeric_analysis(df)

        elif choice == "8":
            unique_values(df)

        elif choice == "9":
            duplicate_analysis(df)

        elif choice == "10":
            df = remove_missing(df)

        elif choice == "11":
            df = remove_duplicates(df)

        elif choice == "12":
            search_data(df)

        elif choice == "13":
            save_file(df)

        elif choice == "14":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()