Every day, as part of her walk around the farm, Bessie the cow visits her favorite pasture, which has N flowers (all
colorful daisies) labeled 1…N lined up in a row (1≤N≤100). Flower i has pi petals (1≤pi≤1000).
As a budding photographer, Bessie decides to take several photos of these flowers. In particular, for every pair of
flowers (i,j) satisfying 1≤i≤j≤N, Bessie takes a photo of all flowers from flower i to flower j (including i and j).

Bessie later looks at these photos and notices that some of these photos have an "average flower" --
 a flower that has P petals, where P is the exact average number of petals among all flowers in the photo.

How many of Bessie's photos have an average flower?

INPUT FORMAT (input arrives from the terminal / stdin):
The first line of input contains N. The second line contains N space-separated integers p1…pN.
OUTPUT FORMAT (print output to the terminal / stdout):
Please print out the number of photos that have an average flower.
SAMPLE INPUT:
4
1 1 2 3
SAMPLE OUTPUT:
6
Every picture containing just a single flower contributes to the count (there are four of these in the example).
 Also, the (i,j) ranges (1,2) and (2,4) in this example correspond to pictures that have an average flower.

Problem credits: Nick Wu
4
1 1 2 3

First photo:
only take first flower
number of flowers: 1
number of petals in the photo: 1
average number of petals in the photo: 1/1 = 1

Question: does any flower in the photo have average number of petals?
    average number of petals: 1
    flower one has 1 petal
        so first photo has a flower which has average number of petals.

second photo:
only take second flower.
    number of flower 1
    number of petals 1
    average number of petals: 1
    does any flower has averager number of petals:
            YES


four flowers
flowerA, flowerB, flowerC, flowerD
1 1 2 3

classic combination will give us total number of photos:
2 ^ 4 = 16

flowerA has 1 petal
flowerB has 1 petal
flowerC has 2 petals
flowerD has 3 petals.

Now photos.

photo 1 only has flowerA
    it contains a flower which has petal count matches the average count of flower petals. True

photo 2 only has flowerB
    1 1 True
photo 3 only has flowerC
    2 2 True
photo 4 only has flowerD
    3 3 True
photo 5 has flowerA and flowerB
    number of total petals in photo: 1 + 1 = 2
    number of flowers in photo 5: 2
    avereger number of petals in photo: 2/2 = 1
        it contains a flower which has petal count matches the average count of flower petals. True


photo 6 has flowerB and flowerC
    1 2
    number of total petals in photo 6: 1 + 2 = 3
    number of flowers in photo 6: 2
    avereger number of petals in photo: 3/2 = 1.5
            it contains a flower which has petal count matches the average count of flower petals. False


photo 7 has flowerC and flowerD
    2 3
    number of total petals in photo 7: 2 + 3 = 5
    number of flowers in photo 7: 2
    avereger number of petals in photo 7: 5/2 = 2.5
            it contains a flower which has petal count matches the average count of flower petals. False

# we can not have a photo  with only flowerA and flowerC, because flowerB can not be skipped.
photo 8 has flowerA and flowerB and flowerC
    1 1 2
    total petal = 1 + 1 + 2 = 4
    number of flowers in photo 8: 3
    avereger number of petals in photo 8: 4/3 = 1.333
            it contains a flower which has petal count matches the average count of flower petals. False

photo 9 has flowerB and flowerC and flowerD
    1 2 3
    total petal = 1 + 2 + 3 = 6
    number of flowers in photo 9: 3
    avereger number of petals in photo 9: 6/3 = 2
            it contains a flower which has petal count matches the average count of flower petals. True


photo 10 has flower A and flowerB and flowerC and flowerD
   1 1 2 3
    total petal = 1 + 1 + 2 + 3 = 7
    number of flowers in photo 10: 4
    avereger number of petals in photo 10: 7/4 = 1.75
            it contains a flower which has petal count matches the average count of flower petals. False


