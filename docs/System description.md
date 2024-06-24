# The system 
This is how I imagine the system should work. There are so many different ways of doing this that it can be difficult to settle on one specific and to deside which would be the best for Lego pieces. 

## Loading the system
The bricks will need to be separated before loading them into the system. When this is done I imagine they could be loaded in bulk into a reservoir that would slowly empty into the system. This would be a large conveyor ending in a much smaller line. The important thing is that they are single lined. I assume Lego has already a lot of experience in this. 

## Splitting the bricks into single line of bricks
This can be done with conveyors of different speed.

It might be an idea to split the bricks into different sizes as well. This could be by height. 

## The PLC
The PLC should keep track of the different pieces once separated and give every piece a running number. With belt speed or buckets the PLC can keep track of the items and add properties like weight or image classification results onto the bucket. 

## The sets
I imagine a round conveyor with buckets that can be emptied into many different sets. This could also be done with pick-and-place robots to save space. Once a brick is outside a set that is missing that brick the robot will take it and the list of missing bricks for the set will be updated in the PLC or the database.

## The database
The brick is put into the database following the running number with its weight and classification, which set it was delivered to and from which station ect.

This means that we would have a series of tables in the database. Something like this:

|  Production | type     |
|------------:|:---------|
|          id | int      |
|    brick_id | int (FK) |
| set_prod_id | int (FK) |
|       image | jpg      |

| SetProduction | type     |
|--------------:|:---------|
|            id | int      |
|        set_id | int (FK) |

|    Brick | type     |
|---------:|:---------|
|       id | int      |
|     name | str      |
|   weight | float    |
| color_id | int (FK) |
|      CAD | str      |

|     Color | type     |
|----------:|:---------|
|        id | int      |
|      name | str      |
| color_hex | str      |

|              Set | type |
|-----------------:|:-----|
|               id | int  |
|             name | str  |
|      description | str  |
| validation_image | jpg  |

| SetContent | type     |
|-----------:|:---------|
|     set_id | int (FK) |
|   brick_id | int (FK) |


