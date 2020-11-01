from elasticsearch import Elasticsearch

es = Elasticsearch()
q = \
{
    'size':20000,
    'aggs':{
        'dd':{
            'cardinality':{'field':'live_sido'}
        }
    }
}

# idx_nm = ''
# r = es.search(index='', body=q)
print(es.indices.get_mapping())
