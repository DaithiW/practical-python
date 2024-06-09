# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(file, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if isinstance(file, str):
        with open(file, "rt") as f:
            return parse_csv(f, select=select, types=types, has_headers=has_headers, delimiter=delimiter, silence_errors=silence_errors)

    if select and not has_headers:
        raise RuntimeError("select argument requires columns headers")

    # with open(filename) as f:
    rows = csv.reader(file, delimiter=delimiter)
    records = []
    # Read the file headers
    if has_headers:
        headers = next(rows)

        # If a column selector was given, find indices of the specified headers
        # Also narrow the set of headers used for output dict
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        for i, row in enumerate(rows):
            if not row:
                continue
            # Apply type conversion (optionally)
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                # Filter the row if specific columns selected
                if indices:
                    row = [row[index] for index in indices]

                # Make dictionary
                record = dict(zip(headers, row))
                records.append(record)
            except ValueError as e:
                if silence_errors == False:
                    print(f"Row: {i+1} Reason", e)

    else:
        for i, row in enumerate(rows):
            if not row:
                continue
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                record = tuple(row)
                records.append(record)
            except ValueError as e:
                if silence_errors == False:
                    print(f"Row: {i+1} Reason", e)

    return records
