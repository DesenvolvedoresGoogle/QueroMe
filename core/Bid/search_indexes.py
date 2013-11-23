# bid.search_indexes
import search
from search.core import porter_stemmer
from core.models import Bid

# index used to retrieve posts using the title, content or the
# category.
search.register(Bid, ('product',),
    indexer=porter_stemmer)