#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, person in enumerate(attendees, start=1):
        filled_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key)
            if not value:
                value = "N/A"
            filled_template = filled_template.replace(f"{{{key}}}", value)

        output_filename = f"output_{idx}.txt"

        if os.path.exists(output_filename):
            print(f"File '{output_filename}' already exists.")
            continue

        try:
            with open(output_filename, "w") as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
