from tables import create_tables
from services import *


#Create Table
create_tables()

### Create Data
# create_user("suyog", "suyog@johomail.com")
# create_user("Suraj", "suraj@johomail.com")
# create_user("Anand", "ananad@gmail.com")
# create_user("Prashant", "prashant@gmail.com")
# create_post(1,"Hellow World", "This is suyog first post")
# create_post(2,"Hellow World", "This is Suraj first post")
# create_post(3,"Hi Hello", "This is Networking lelated posts")
# create_post(4,"Hi prashant post", "Hi i am prshant p")
# create_post(5,"Hi prashant post", "Hi i am prshant p")




## Read Data
# get_user_by_id(1)
# print(get_user_by_id(1))
# print(get_all_users())
# print(get_posts_by_user(2))



## Update Data
# update_user_email(1,'suyogbhere@gmail.com')



# Delete Data
# delete_post(2)



## Get Users data Order by
# print(get_users_ordered_by_name())
# print(get_latest_post_first())
# print(get_post_count_per_user())


## Using Join 
print(get_posts_with_author())
