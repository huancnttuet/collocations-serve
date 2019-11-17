### CQRS Base Design and Main Rules


#### Main Rules

* No Update in Write Process.
* Smallest table for insert.



* Generally, no need to specific version of history message, because : 

***it is not critical with data like that 
and not have many concurrent update for one item from one user at a time.***

* For specific case, if need to build with version number of history message,
we can build a specific version by:

a) A private server with provide version-number for each message (maybe IAM, Nginx Load balancing, Kafka)

b) Generate it by using unix time immediately before process request.


We can do like that because its come from request.

#### WRITE PROCESS

* Step 1 : Create transaction to

a) Insert the request to DB logs (MySQL table - it will be clean everyday, by moving past data to achieve log tables) 

with UUID primary key.

b) Get the primary key and insert to `retry_table` this UUID.



* Step 2 : When success with Transaction , put the process with this primary key to queue.

The queue must success with delete this uuid on `retry_table`.

**TODO** : setup a cronjob which run to handle those uuids 

which still not be delete after period of time in `retry_table`.


The queue process will better insert to separate tables for serve read query.

For example `Product A, User B, Client C, Rating 5` => Insert to Table `product_rating_5` `VALUES('A')`


**REMEMBER** no select or update query in step 1 & 2.

#### READ PROCESS

Base on requirements, the read process may do nothing (tables build by queue process is enough) 

or maybe a `cronjob` for rebuild specific records for read API.

For example in `PRODUCT RATING`:

* we have table for read is `product_rating` with 2 columns : 

`product_id` (PRIMARY_KEY) and `rating_average`.

* Write query to rebuild average for each `product_id` base on `product_rating_1`.. `product_rating_5`