<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.document.CandidateSet" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_document"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="get_all_documents"/>
<meta itemprop="property" content="get_documents"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="remove_document"/>
<meta itemprop="property" content="size"/>
</div>

# recsim.document.CandidateSet

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

## Class `CandidateSet`

<!-- Start diff -->
Class to represent a collection of AbstractDocuments.

<!-- Placeholder for "Used in" -->

The candidate set is represented as a hashmap (dictionary), with documents
indexed by their document ID.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
__init__()
```

Initializes a document candidate set with 0 documents.

## Methods

<h3 id="add_document"><code>add_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
add_document(document)
```

Adds a document to the candidate set.

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
create_observation()
```

Returns a dictionary of observable features of documents.

<h3 id="get_all_documents"><code>get_all_documents</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
get_all_documents()
```

Returns all documents.

<h3 id="get_documents"><code>get_documents</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
get_documents(document_ids)
```

Gets the documents associated with the specified document IDs.

#### Args:

*   <b>`document_ids`</b>: an array representing indices into the candidate set.
    Indices can be integers or string-encoded integers.

#### Returns:

(documents) an ordered list of AbstractDocuments associated with the document
ids.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
observation_space()
```

<h3 id="remove_document"><code>remove_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
remove_document(document)
```

Removes a document from the set (to simulate a changing corpus).

<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
size()
```

Returns an integer, the number of documents in this candidate set.
