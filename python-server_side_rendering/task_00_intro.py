import os
import sys
import logging

def generate_invitations(template, attendees):
    """
        function to generate a similar message but message are customised to the attendees.

        arg:
            template: A string message for all the attendies.
            attendees:  customising each users message.
    """

    # Check if template is a string
    if not isinstance(template, str):
        logging.error('Invalid template.')
        sys.exit()

    # Check if attendees is a list of a dictionary
    if not all(isinstance(x, dict) for x in attendees):
        logging.error('Invalid list.')
        sys.exit()
    
    # Arguments cannot be emoty
    if template is None:
        logging.error('Template is empty, no output files generated.')
        sys.exit
    
    if attendees is None:
        logging.error('No data provided, no output files generated.')
        sys.exit

    # Iterate in attendees
    for index, attendee in enumerate(attendees, start=1):
        invitation = template[:]

        # Where its's replace with N/A
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            invitation = invitation.replace(f"{{{key}}}", value)

        # Print message for all attendees using template and save in file
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)



