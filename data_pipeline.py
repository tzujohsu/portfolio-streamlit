import logging
from utils.document_loader import *
from utils.retriever import Retriever

#%% setup config
today_date = datetime.now()
basepath = 'data/data-news/'

#%%
# step 1
docloader = DocumentLoader()
print('step 1: load the vector database done')
print('\t# docs in the current database: ', len(docloader.vector_store.get()['documents']))


# # step 2: 
documents = docloader.load_documents_from_scraping(start_date=today_date , latest=True)
# documents = docloader.load_documents_from_scraping(start_date=(datetime.now() - timedelta(days=4)), end_date= (datetime.now() - timedelta(days=35)), latest=False)
print('step 2: scrape the latest news done')

# # step 3:
docloader.load_documents_into_database(documents)
print('step 3: load the documents into db done')
print('\t# docs in the current database: ', len(docloader.vector_store.get()['documents']))

# # step 4
# docloader.remove_documents(cutoff_threshold=60)
# print('step 4: remove the oldest transcripts done')
# print('\t# docs in the current database: ', len(docloader.vector_store.get()['documents']))