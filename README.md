This is the repository for the second assignment of the Computational Creativity course at Leiden University. The assignment tasks us with building a poem generator using approaches covered in class. After careful consideration, we decided to go for Markov Chains, where there is a probability of transition to the next word.

Part of the assignment was gathering an inspiring dataset. This was achieved by merging and cleaning a few book poems found on Project Gutenberg such as *Tender buttons* by Gertrude Stein, *Selected poems* by Robert Frost and *The waste land* by T.S. Elliott. Note that these poems vary in style and length, but are all in English.

The poem generator is was experimented on  the file `poem_generator.ipynb` and the requirements are to be on the latest version of Python3 (note that it doesn't run on Python2) and install the required packages listed in the `requirements.txt`file. This can be easily done by running the following command in the terminal pointing to this directory:

```
pip install -r requirements.txt
```

Lastly, to run the poem generator, run the following command:

```
python3 poem_generator.py
```
Inside the `poem_generator.py` file, there are initial configurations that can be tuned, such as the maximum syllables per line, poem length and the dataset used to train. Capitalization is still not perfected.

It is worth saying that this poem generator can still be improved. There already are implementations out there that include a rhyming function, and even one that uses a recurrent neural network that generate significantly more believable poems. Nonetheless, we are content with the novelty and results of our approach given the time restrains we had.
