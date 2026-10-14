# Student Club Checker
from pyscript import display, document

def student_club(e):
    document.getElementById('result').innerHTML = ' '
    student_firstname  = document.getElementById('student_first').value
    student_lastname  = document.getElementById('student_last').value
    cocc_members_first = ['zoe', 'zarina', 'maryam', 'nathan', 'hans']
    cocc_members_last = ['reyes', 'perez', 'ledesma', 'bautista', 'baquiran']
    member_checker = student_firstname in cocc_members_first
    member_checker = student_lastname in cocc_members_last


    display_message = (f'Sorry you name is not on the list', f'Congratulations {student_firstname}  {student_lastname}! You are now part of COCC.')

    display(display_message[member_checker], target='result')
