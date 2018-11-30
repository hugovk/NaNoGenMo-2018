"""
Generate a catalogue of pharmaceutical drug names
https://github.com/NaNoGenMo/2018/issues/27

'Brain' coins 42,000 Words in 2 Hours - Would Take a Human 269,000 Years

Pfizer seems to find it easier to rout disease that to create names for their new
products. In the past the firm employed a philoligist or two who scanned the names of
the contents of a drug. Selecting a syllable here and there from the principle
components, they patched together a few pronouncable, spellable, descriptive names and
submitted them for adoption and trademark.

But the task grows increasingly complicated as new drugs appear, not only Pfizer's but
those of a number of renowned pharmaceutical firms. The public has not needed to learn
all the jaw-breaking words, as many of them are sold by prescription only. But doctors
are stymied at loading their minds with ever more complicated names whose sounds tax
their spelling, and whose roots go back to forgotten pharmacology terms. With human
brains groping for new word-sound combinations, the forementioned pharmaceutical firm
appealed to a business machine corporation for help. It has just arrived in the form of
a rare book published by IBM, and of which there are only three in existence.

The 198-page volume was written for Charles Pfizer & Co., Inc., of Brooklyn,
pharmaceutical and chemical manufacturer, whose researchers have been having trouble
finding new names for its products.

IBM's "electronic data processing machine" was fed an outline of the problem on a
magnetic tape: combine 30 groups of word endings like "il," "in," "ite," "ide," and
"ane" with various combinations of one and two syllable words. Then, come up with words
easy to spell, remember and translate into medical terms.

The IBM machine also was taught to be discreet. It was fixed to automatically eliminate
four-letter combinations that wouldn't be proper in a family medicine chest.
"""
import datetime

import tracery


print("# A CATALOGUE OF PHARMACEUTICAL DRUG NAMES")
print()

when = datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p")
print(f"Generated on {when} by {__file__}")
print()
print()

with open("startings.txt") as f:
    startings = f.read().splitlines()

with open("endings.txt") as f:
    endings = f.read().splitlines()

with open("4letterwords.txt") as f:
    impropers = f.read().splitlines()

kept = []
for starting in startings:
    keep = True
    for bad in impropers:
        if bad in starting:
            keep = False
    if keep:
        kept.append(starting)

rules = {"origin": "#starting##ending#", "starting": startings, "ending": endings}

grammar = tracery.Grammar(rules)

good = set()
bad = set()
while len(good) + len(bad) < 50000:
    drug = grammar.flatten("#origin#")
    ok = True
    for improper in impropers:
        if improper in drug:
            # print(drug, "\t", improper)
            ok = False
            bad.add(drug)
            break
    # print(drug)
    if ok:
        good.add(drug)

print("## NEW DRUG NAMES")
print()

for word in good:
    print(word)

print()
print()
print("## IMPROPER FOR A FAMILY MEDICINE CHEST")
print()

for word in bad:
    print(word)
