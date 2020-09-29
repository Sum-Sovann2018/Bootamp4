import datetime

def timestamp_to_str(timestamps):

    try:

        timestamps = int(timestamps)
        read = datetime.datetime.fromtimestamp(timestamps)

        print(f"timestamp_to_str({timestamps})\n{read}")

    except ValueError:

        print("Your timestamp is not valid.")


timestamp_to_str("1623646780")