# Vignette-group-14

Final Poetry Generation vignette project

# Description

Vignette on using markov chains to create a poetry generator based on particular poetry genres/styles; Model trained using Edgar Allen Poe poetry; created as a class project for PSTAT197A in Fall 2022.

# Vignette abstract

The topic of this vignette is related to using NLPs to train a poetry generator based on the type of particular authors. To do this, we used a markov chain model on a subset of data from the Project Gutenberg database, which is a digital database of written works categorized by genre, author, etc. Our subset of the data are poems from the author Edgar Allen Poe. This vignette consists of a pre-curated poetry corpus that our group made, as well as instructions on how to train a poem generator on this corpus and output a new poem. We have generated a sample poem in Edgar Allen Poe's style of poetry. 

# Repository contents

The repository contains our README file with a description of our project, poetry corpus as a JSON file (data/gutenberg-poetry-v001.ndjson.gz), the Edgar Allen Poe poetry corpus dataset (data/poetry_poe.ndjson), and our final vignette (Primary Vignette.ipynb).

The code used to subset lines of poetry written by Edgar Allen Poe is stored in scratchwork/Poe_Corpus.ipynb. To create a corpus of work from a different poet, one can oepn this script and write the name of a different author in it to generate poetry in the style of another poet.

# References

<https://github.com/aparrish/gutenberg-poetry-corpus/blob/master/quick-experiments.ipynb> - Allison Parrish's tutorial, with interacting with and basic analysis of the poetry corpus. Implemented Markov Chain Model Process from here.

<https://www.educative.io/blog/deep-learning-text-generation-markov-chains> - Alternative article on Markov Chain text generation
