Django Environment Setup Reflection
Setting up the Django environment was trickier than I expected. At first, I had trouble with my virtual environment because I kept forgetting to activate it, so Django wasn't installing in the right place. I kept getting confused about whether I was in my virtual environment or not until I learned to look for the (venv) in my terminal prompt.

The hardest part was probably getting the Django server to actually run without errors. I kept getting migration warnings that made me think something was broken, but it turns out I just needed to run python manage.py migrate first. Once I did that, everything worked fine and I could see the Django welcome page.

Git was also kind of annoying to set up. I created my repository on GitHub but then spent like 20 minutes trying to figure out why my pushes weren't working. Turns out I had the wrong remote URL copied. After I fixed that with git remote set-url origin <correct-url>, everything worked.

Overall, I learned that following the steps in order really matters. When I tried to skip ahead or do things out of sequence, I ran into problems. Now I know to always check my Python version, activate my virtual environment, install Django, run migrations, and then set up Git properly. Having a checklist definitely helps so I don't forget any steps next time.

