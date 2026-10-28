What I will need to know about child in db and activities that child did

child 
 - first & last name
 - date of birth
 - team
 - child_id (probably) [PK]
 - age group (A, B, C, D, F)
 - gender

activities
 - activity_id [PK]
 - activity_type [time / points]
 - name of that activity
 - date & time / order  [day 1.; at 10:10 or 2nd September; 1st activity]
 - max points
 - time intervals they are starting from each other (time disciplines)

score
 - activity_id & child_id 
 - score_id [PK]
 - status [`OK`: Finished, `DNS`: Did not start, `DNF`: Did not finish, `DSQ`: disqualified]
 - how much they scored
 - how long they run (starting time - finishing time)
 - starting time & finishing time
 - for time activities manual starting time override
