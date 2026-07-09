Reborn Combat Simulator

A Monte Carlo simulation of a Hearthstone Battleground interaction between Golden Timewarped Embalmer (SP) and insta kill minions (Kill) (leeory or venomous minions)

The simulation plays out repeated attacks:


Even steps: minion at index 0 attacks.

Odd steps: a random minion is attacked.


When a minion with Reborn is hit:


If any other SP minion still has a charge left, that charge is spent to keep the hit minion alive (Reborn is preserved).
If no SP minion has any charges left, the hit minion loses Reborn permanently.


When a minion without Reborn is hit, it dies and is removed from the list. The simulation for that game ends once the list is empty.

This is the default for 100,000 simulations. For each game, the script records:


Total token summons plus original before all minions disappear
How many times the "Kill" minion was involved in an attack (as attacker or target)


How to run it:

in bash

python3 main.py

By default, it runs 100,000 simulations, which is a lot — each game usually resolves in well under 200 steps, so total runtime is mostly a function of how many trials you set at the top of the script:

pythonfor i in range(100000):  # <- number of simulated games

Lower this while testing/debugging.

Output

The script produces two histograms:


Total Tokens — distribution of how many tokens will be summoned, including the starting original number 

Total Kills — distribution of how many times the Kill minion hit or is hit per simulation
