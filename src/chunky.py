"""
Helper functions for amazon-cnn.py
"""

def chunky(input, chunk_size=50, delim=','):
    """
    Function to break text file into chunks of managable size

    Arguments
    ---------
    input -- textfile that is newline separated
    chunk_size -- number of lines to yield; default 50
    delim -- line delimiter; default ','
    """
    with open(input, 'r') as f:
        rows = []
        counter = 1
        for line in f:
            rows.append(line.strip().split(delim))
            if counter % chunk_size == 0:
                yield rows
                rows = []
            
            counter += 1
        if rows != []:
            yield rows

if __name__ == "__main__":
    batch = chunky('test.txt', chunk_size=4)
    print(next(batch))
    print(next(batch)) 
