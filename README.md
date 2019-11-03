# DBLP-collaboration-dataset
The raw data is downloaded in DBLP (https://dblp.uni-trier.de/xml/). It's a big xml file recording all papers' information on DBLP. The file named 'parse.py' can parse the xml file, giving each author an id. The mapping of id-author is saved in 'author.txt'. 

'parse.py' can also extract collaboration relations between all authors. Each collaboration is represented as a pair of number. For instance,  '1 2' represent the author whose id is 1 and the author whose id is 2 have collaborated at least once. All these information is saved in 'collaboration.txt'.

I compressed the file because of the size's limitation of github. 
