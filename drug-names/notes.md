https://github.com/NaNoGenMo/2018/issues/27


42,000 new words /  30 endings = 1,400 words
42,000 new words / 111 endings = 378.378378 words

# Get word endings

> 30 groups of word endings like "il,", "in," "ite," "ide," and "ane"

## Get drug names and stems

wget https://raw.githubusercontent.com/dariusk/corpora/master/data/medicine/drugs.json
wget https://raw.githubusercontent.com/dariusk/corpora/master/data/medicine/drugNameStems.json

Copy to text files and convert from JSON to plain word lists

# Keep those beginning "-abc", drop those also ending "-abc-"
grep "^-" drugNameStems.txt > drugNameStems2.txt
grep "[a-z]$" drugNameStems2.txt > drugNameStems.txt

-> 406 endings

## Find endings from drugNameStems.txt

vowel-consonant-[vowel]

vowel: [aeiouy]
consonant: [b-df-hj-np-tv-z]

BBEdit replace in drugNameStems.txt:
.*([aeiouy][b-df-hj-np-tv-z][aeiouy]?)$
with:
\1

And delete any leftovers, replace:
-.*\n
with nothing

-> 372 endings

Sort unique

-> 53 endings

## Find endings from drugs.txt

-> 1000 endings

BBEdit replace in drugNameStems.txt:
.*([aeiouy][b-df-hj-np-tv-z][aeiouy]?)$
with:
\1

And delete any leftovers, replace (case-sensitive):
[A-Z].*\n
with nothing

-> 803 endings

Sort unique

-> 105 endings

## Combine endings

cat drugNameStems.txt drugs.txt | sort | uniq > endings.txt

-> 111 endings

# Get some one or two syllable words

wget https://raw.githubusercontent.com/elasticdog/yawl/master/yawl-0.3.2.03/word.list

p 1or2syllables.py >startings.txt

$ wc -l startings.txt endings.txt
   28724 startings.txt
     111 endings.txt
   28835 total

# Get some bad words

wget https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en -O LDNOOBW.txt

wget https://raw.githubusercontent.com/dariusk/wordfilter/master/lib/badwords.json

Combine and select which ones to keep in 4letterwords.txt

# Generate

python drugs.py > catalogue.md

Copy catalogue.md into Word and create PDF
