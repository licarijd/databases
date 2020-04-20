# Find the players whose weight is less than the average.
# 
# The function below performs two database queries in order to find the right players.
# Refactor this code so that it performs only one query.

# This example uses subqueris to join the columns of interest with an average. Then,
# we select from that join the players who's weight is less than average.

def lightweights(cursor):
    """Returns a list of the players in the db whose weight is less than the average."""
    cursor.execute("select name, weight from (players join (select avg(weight) as av from players)) where weight < av;")
    return cursor.fetchall()
